#!/bin/bash

# Go to repo directory
cd "$(dirname "$0")" || exit 1

echo "===== Run started at $(date) =====" >> cron.log

/usr/bin/python3 main.py >> cron.log 2>&1

echo "===== Run finished at $(date) =====" >> cron.log
echo "" >> cron.log