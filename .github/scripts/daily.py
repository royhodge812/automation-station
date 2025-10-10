import os
import shutil
from datetime import datetime

REPORTS_DIR = 'reports'
DIST_DIR = 'dist'
TEMPLATES_DIR = 'templates'

def main():
    if not os.path.exists(DIST_DIR):
        os.makedirs(DIST_DIR)

    # Copy CSS to dist
    shutil.copy(os.path.join(TEMPLATES_DIR, 'style.css'), DIST_DIR)

    today = datetime.now().strftime('%Y-%m-%d')
    report_path = os.path.join(DIST_DIR, f'{today}.html')

    with open(report_path, 'w') as f:
        f.write('<!DOCTYPE html>\n<html>\n<head>\n')
        f.write(f'  <title>Daily Report for {today}</title>\n')
        f.write('  <link rel="stylesheet" href="style.css">\n')
        f.write('</head>\n<body>\n  <main>\n')
        f.write(f'    <h1>Daily Report for {today}</h1>\n')
        f.write('    <p>This is a dummy report.</p>\n')
        f.write('  </main>\n</body>\n</html>\n')

    # Update index.html
    index_path = os.path.join(DIST_DIR, 'index.html')
    reports = sorted([f for f in os.listdir(DIST_DIR) if f.endswith('.html') and f != 'index.html'], reverse=True)

    with open(index_path, 'w') as f:
        f.write('<!DOCTYPE html>\n<html>\n<head>\n')
        f.write('  <title>Reports</title>\n')
        f.write('  <link rel="stylesheet" href="style.css">\n')
        f.write('</head>\n<body>\n  <main>\n')
        f.write('    <h1>Reports</h1>\n')
        for report in reports:
            f.write(f'    <p><a href="{report}">{report.replace(".html", "")}</a></p>\n')
        f.write('  </main>\n</body>\n</html>\n')

if __name__ == '__main__':
    main()

