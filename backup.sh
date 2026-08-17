#!/bin/bash

# Go to repo directory
cd "$(dirname "$0")" || exit 1

echo "===== Run started at $(date) =====" >> cron.log

source "$(dirname "$0")/.env"

output=$("$(dirname "$0")/venv/bin/python3" main.py 2>&1)
echo "$output" >> cron.log

if echo "$output" | grep -q "Error fetching submissions"; then
    echo "Error"
    echo "$output" | mail -s "LeetCode Sync Error: Error fetching submissions" "$EMAIL"
fi

echo "===== Run finished at $(date) =====" >> cron.log
echo "" >> cron.log
