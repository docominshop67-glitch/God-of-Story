import sqlite3
import os
import sys

# Force UTF-8 for console output on Windows
sys.stdout.reconfigure(encoding='utf-8')

def audit_database():
    db_path = r"c:\Users\ACER\Desktop\docomin\database\docomin.db"
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    print("==================================================")
    print("           DOCOMIN SYSTEM AUDIT REPORT            ")
    print("==================================================")

    # 1. Levels and Subjects
    levels = c.execute("SELECT * FROM education_levels ORDER BY order_num").fetchall()
    subjects = c.execute("SELECT * FROM subjects ORDER BY order_num").fetchall()
    print(f"\n1. Education Levels: {len(levels)} levels")
    for l in levels:
        print(f"   [{l['code']}] {l['name']} ({l['group_name']})")
        
    print(f"\n2. Subjects: {len(subjects)} subjects")
    for s in subjects:
        print(f"   [{s['code']}] {s['name']} {s['icon']}")

    # 2. Lessons count per level and subject
    print("\n3. Lessons Breakdown:")
    total_lessons = c.execute("SELECT COUNT(*) FROM lessons").fetchone()[0]
    print(f"   Total Lessons in DB: {total_lessons}")
    
    level_lesson_counts = c.execute("""
        SELECT l.code, l.name, COUNT(ls.id) as cnt 
        FROM education_levels l 
        LEFT JOIN lessons ls ON l.id = ls.level_id 
        GROUP BY l.id ORDER BY l.order_num
    """).fetchall()
    for row in level_lesson_counts:
        print(f"   - {row['name']} ({row['code']}): {row['cnt']} lessons")

    # 3. Quizzes and Questions
    print("\n4. Quizzes & Exam Bank Breakdown:")
    total_quizzes = c.execute("SELECT COUNT(*) FROM quizzes").fetchone()[0]
    total_questions = c.execute("SELECT COUNT(*) FROM quiz_questions").fetchone()[0]
    print(f"   Total Quizzes: {total_quizzes}")
    print(f"   Total Questions: {total_questions}")

    quiz_types = c.execute("SELECT exam_type, COUNT(*) as cnt FROM quizzes GROUP BY exam_type").fetchall()
    for qt in quiz_types:
        print(f"   - Exam Type '{qt['exam_type']}': {qt['cnt']} quizzes")

    # 4. Thailand 77 Provinces
    total_provinces = c.execute("SELECT COUNT(*) FROM thai_provinces").fetchone()[0]
    print(f"\n5. Thailand Provinces: {total_provinces}/77 provinces")

    # 5. Wiki Terms
    total_wiki = c.execute("SELECT COUNT(*) FROM wiki_terms").fetchone()[0]
    print(f"\n6. Wiki Terms: {total_wiki} terms")

    # 6. School Admissions & Alerts
    total_admissions = c.execute("SELECT COUNT(*) FROM school_admissions").fetchone()[0]
    print(f"\n7. School Admissions: {total_admissions} entries")

    # 7. Check for missing book_pages or empty content
    empty_books = c.execute("SELECT COUNT(*) FROM lessons WHERE book_pages IS NULL OR book_pages = '' OR book_pages = '[]'").fetchone()[0]
    print(f"\n8. Lessons without Book Pages (E-Book format): {empty_books}")

    # 8. Check for questions without explanations
    no_explain = c.execute("SELECT COUNT(*) FROM quiz_questions WHERE explanation IS NULL OR explanation = ''").fetchone()[0]
    print(f"9. Questions without Explanations: {no_explain}")

    conn.close()

if __name__ == '__main__':
    audit_database()
