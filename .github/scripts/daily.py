import os
from datetime import datetime

REPORTS_DIR = 'reports'

def main():
    if not os.path.exists(REPORTS_DIR):
        os.makedirs(REPORTS_DIR)

    today = datetime.now().strftime('%Y-%m-%d')
    report_path = os.path.join(REPORTS_DIR, f'{today}.md')

    with open(report_path, 'w') as f:
        f.write(f'# Daily Report for {today}\n\n')
        f.write('This is a dummy report.\n')

    # Update index.html
    index_path = os.path.join(REPORTS_DIR, 'index.html')
    reports = sorted([f for f in os.listdir(REPORTS_DIR) if f.endswith('.md')], reverse=True)

    with open(index_path, 'w') as f:
        f.write('<!DOCTYPE html>\n<html>\n<head>\n  <title>Reports</title>\n</head>\n<body>\n  <h1>Reports</h1>\n')
        for report in reports:
            f.write(f'  <p><a href="{report}">{report.replace(".md", "")}</a></p>\n')
        f.write('</body>\n</html>\n')

if __name__ == '__main__':
    main()

