import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
import subprocess
import pytz

load_dotenv()  # Load values from .env into environment

LEETCODE_SESSION = os.getenv("LEETCODE_SESSION")
CSRF_TOKEN = os.getenv("CSRF_TOKEN")
EMAIL = os.getenv("EMAIL")

difficulty_map = {1: 'Easy', 2: 'Medium', 3: 'Hard'}

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://leetcode.com",
    "cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={CSRF_TOKEN}",
    "x-csrftoken": f"{CSRF_TOKEN}"
}


def get_today_timestamp_range():
    est = pytz.timezone('US/Eastern')
    now = datetime.now(est)
    start = datetime(now.year, now.month, now.day)
    end = start + timedelta(days=1)
    return int(start.timestamp()), int(end.timestamp())


def fetch_problem_data():
    url = "https://leetcode.com/api/problems/all/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['stat_status_pairs']
    else:
        print("Failed to fetch problem data.")
        exit()


def get_problem_by_number(slug, problems):
    for problem in problems:
        if problem['stat']['question__title_slug'] == slug:
            title = problem['stat']['question__title']
            difficulty = difficulty_map[problem['difficulty']['level']]
            frontend_id = problem['stat']['frontend_question_id']
            return frontend_id, title, difficulty
    raise ValueError(f"Problem not found for slug: {slug}")


def fetch_submissions():
    url = "https://leetcode.com/api/submissions/?offset=0&limit=1000"
    res = requests.get(url, headers=HEADERS)
    if res.status_code != 200:
        print("Error fetching submissions.")
        return []

    data = res.json()
    start_ts, end_ts = get_today_timestamp_range()
    today_submissions = []

    for item in data['submissions_dump']:
        if item['status_display'] == 'Accepted' and start_ts <= item[
                'timestamp'] < end_ts:
            today_submissions.append(item)

    return today_submissions


def save_solution(submission):
    code = submission['code']
    slug = submission['title_slug']
    try:
        number, title, difficulty = get_problem_by_number(slug, fetch_problem_data())
    except Exception as e:
        print(f"Problem not found: {number}")
        return
    # Format filename
    filename = f"{number}_{title.lower().replace(' ', '-')}.py"
    folder = difficulty.capitalize()

    if not os.path.exists(folder):
        os.makedirs(folder)

    filepath = os.path.join(folder, filename)
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write(f"# Problem {number}: {title}\n")
            f.write(f"# Difficulty: {difficulty}\n")
            f.write(code)
        print(f"Saved: {filepath}")
        return number
    else:
        print(f"Already exists: {filepath}")
        return None


def auto_commit_and_push(num):
    est = pytz.timezone('US/Eastern')
    now = datetime.now(est).strftime("%Y-%m-%d")
    commit_message = f"LeetCode solution for Problem #{num}"
    print(f"{commit_message}")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Changes committed and pushed to GitHub.")
    except subprocess.CalledProcessError:
        print("No changes to commit or Git error occurred.")


def sync_leetcode():
    submissions = fetch_submissions()
    for sub in submissions:
        try:
            num = save_solution(sub)
            if num:
                auto_commit_and_push(num)
        except Exception as e:
            print(e)

    
