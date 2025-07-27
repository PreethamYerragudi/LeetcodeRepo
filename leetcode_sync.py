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


def get_problem_by_id(problem_id, problems):
    """Get problem by question_id (from submissions) or frontend_question_id"""
    for problem in problems:
        if (problem['stat']['frontend_question_id'] == int(problem_id) or \
           (problem['stat']['question_id'] == int(problem_id)):
            title = problem['stat']['question__title']
            difficulty = difficulty_map[problem['difficulty']['level']]
            return title, difficulty, problem['stat']['frontend_question_id']
    return None, None, None


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
        if item['status_display'] == 'Accepted' and start_ts <= item['timestamp'] < end_ts:
            today_submissions.append(item)

    return today_submissions


def save_solution(submission, problems):
    code = submission['code']
    question_id = submission['question_id']  # This is the internal question_id
    title_slug = submission['title_slug']

    # Try to find the problem by either frontend_question_id or question_id
    title, difficulty, frontend_id = get_problem_by_id(question_id, problems)

    if not title:
        # If not found by ID, try to find by title slug
        for problem in problems:
            if problem['stat']['question__title_slug'] == title_slug:
                title = problem['stat']['question__title']
                difficulty = difficulty_map[problem['difficulty']['level']]
                frontend_id = problem['stat']['frontend_question_id']
                break

    if not title:
        print(f"Problem not found for submission: {submission}")
        return None

    # Format filename
    filename = f"{frontend_id}_{title.lower().replace(' ', '-')}.py"
    folder = difficulty.capitalize()

    if not os.path.exists(folder):
        os.makedirs(folder)

    filepath = os.path.join(folder, filename)
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write(f"# Problem {frontend_id}: {title}\n")
            f.write(f"# Difficulty: {difficulty}\n")
            f.write(f"# URL: https://leetcode.com/problems/{title_slug}/\n")
            f.write(code)
        print(f"Saved: {filepath}")
        return frontend_id
    else:
        print(f"Already exists: {filepath}")
        return None


def auto_commit_and_push(num):
    est = pytz.timezone('US/Eastern')
    now = datetime.now(est).strftime("%Y-%m-%d")
    commit_message = f"LeetCode Solution for Problem #{num}"
    print(f"{commit_message}")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push"], check=True)
        print("Changes committed and pushed to GitHub.")
    except subprocess.CalledProcessError:
        print("No changes to commit or Git error occurred.")


def sync_leetcode():
    problems = fetch_problem_data()  # Fetch all problems once
    submissions = fetch_submissions()

    # Process submissions in reverse chronological order
    for sub in reversed(submissions):
        try:
            num = save_solution(sub, problems)
            if num:
                auto_commit_and_push(num)
        except Exception as e:
            print(f"Error processing submission: {e}")


if __name__ == "__main__":
    sync_leetcode()