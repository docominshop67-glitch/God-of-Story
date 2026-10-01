import sqlite3
import shutil
import os
import glob

def check_history(db_path):
    if not os.path.exists(db_path):
        return
    tmp = 'history_temp.db'
    try:
        shutil.copy2(db_path, tmp)
        conn = sqlite3.connect(tmp)
        c = conn.cursor()
        c.execute("SELECT url, title, last_visit_time FROM urls WHERE url LIKE '%github.com%' ORDER BY last_visit_time DESC LIMIT 10")
        for row in c.fetchall():
            print(f"URL: {row[0]} | Title: {row[1]}")
        conn.close()
        if os.path.exists(tmp):
            os.remove(tmp)
    except Exception as e:
        print(f"Error reading {db_path}: {e}")

# Edge
for p in glob.glob(r'C:\Users\ACER\AppData\Local\Microsoft\Edge\User Data\*\History'):
    print('Checking Edge:', p)
    check_history(p)

# Chrome
for p in glob.glob(r'C:\Users\ACER\AppData\Local\Google\Chrome\User Data\*\History'):
    print('Checking Chrome:', p)
    check_history(p)
