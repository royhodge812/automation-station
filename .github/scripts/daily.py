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
    with open(index_path, 'a') as f:
        f.write(f'<p><a href="{today}.md">{today}</a></p>\n')

if __name__ == '__main__':
    main()

