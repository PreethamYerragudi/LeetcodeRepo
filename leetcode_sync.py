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


def get_problem_by_number(problem_number, problems):
    for problem in problems:
        if problem['stat']['frontend_question_id'] == int(problem_number):
            title = problem['stat']['question__title']
            difficulty = difficulty_map[problem['difficulty']['level']]
            return title, difficulty


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
    number = submission['question_id']
    try:
        title, difficulty = get_problem_by_number(int(number),
                                                  fetch_problem_data())
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
    else:
        print(f"Already exists: {filepath}")


def auto_commit_and_push():
    est = pytz.timezone('US/Eastern')
    now = datetime.now(est).strftime("%Y-%m-%d")
    commit_message = f"LeetCode solutions for {now}"
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
            save_solution(sub)
        except Exception as e:
            print(e)

    auto_commit_and_push()
