import os
import sys

# Force UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

from app import create_app

def run_tests():
    app = create_app()
    app.config['TESTING'] = True
    client = app.test_client()

    print("==================================================")
    print("      RUNNING COMPREHENSIVE ROUTE BUG AUDIT       ")
    print("==================================================")

    test_urls = [
        '/',
        '/lessons/',
        '/lessons/levels',
        '/lessons/subjects',
        '/lessons/1',
        '/book/1',
        '/quiz/',
        '/quiz/?type=entrance',
        '/quiz/?type=onet',
        '/quiz/take/1',
        '/admissions/',
        '/admissions/1',
        '/thailand/',
        '/thailand/province/1',
        '/thailand/random',
        '/wiki/',
        '/wiki/1',
        '/games/',
        '/games/speed-math',
        '/games/word-match',
        '/games/geo-quiz',
        '/achievements/leaderboard',
        '/achievements/badges',
        '/search/?q=คณิต',
        '/search/?q=กรุงเทพ',
        '/auth/login',
        '/auth/register'
    ]

    passed = 0
    failed = 0
    errors = []

    for url in test_urls:
        try:
            res = client.get(url, follow_redirects=True)
            if res.status_code == 200:
                print(f" [PASS 200] {url}")
                passed += 1
            else:
                print(f" [FAIL {res.status_code}] {url}")
                failed += 1
                errors.append((url, res.status_code))
        except Exception as e:
            print(f" [EXCEPTION] {url}: {e}")
            failed += 1
            errors.append((url, str(e)))

    print("\n--------------------------------------------------")
    print(f"RESULTS: {passed} PASSED, {failed} FAILED")
    if errors:
        print("FAILURES FOUND:")
        for u, err in errors:
            print(f"  - {u} -> {err}")
    else:
        print("ALL CHECKED ROUTES RETURNED 200 OK!")
    print("==================================================")

if __name__ == '__main__':
    run_tests()
