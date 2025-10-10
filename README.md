# Automation Station
[![pages-build-deployment](https://github.com/royhodge812/automation-station/actions/workflows/pages/pages-build-deployment/badge.svg?branch=main)](https://github.com/royhodge812/automation-station/actions/workflows/pages/pages-build-deployment)
<br>
[![Generate and Deploy Reports](https://github.com/royhodge812/automation-station/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/royhodge812/automation-station/actions/workflows/main.yml)
<br>

This project is an automated work-tracking system that analyzes your daily work and generates insightful reports. It's designed to help you track your progress, improve your focus, and achieve your goals.

## How it Works

1.  **Daily Work Capture:** You save your daily work into a folder named with the current date (e.g., `2025-10-10`).
2.  **Automated Analysis:** A GitHub Actions workflow runs daily, analyzing the files in your daily work folder.
3.  **Report Generation:** The script generates a daily report in HTML format, summarizing your work and categorizing your files.
4.  **Automated Deployment:** The generated reports are automatically deployed to a GitHub Pages website.

## Features

*   **Automated Daily & Weekly Reports:** Get a clear overview of your work without any manual effort.
*   **Dark Mode & Mobile-First:** The reports are designed to be easily viewable on any device, at any time.
*   **Non-Destructive:** The system is read-only and never modifies your original files.
*   **Searchable & Browsable:** The reports are published to a website, making them easy to access and review.

## Getting Started

1.  **Create a daily work folder:** At the start of your workday, create a new directory with the current date (e.g., `2025-10-10`).
2.  **Save your work:** Save all your files for that day into this folder.
3.  **Let the automation run:** The GitHub Actions workflow will automatically analyze your work and generate a report at the end of the day.
