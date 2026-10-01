import unittest
from app import create_app

class DocominTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Docomin', response.data.decode('utf-8'))
        self.assertIn('ประถมศึกษา', response.data.decode('utf-8'))
        self.assertIn('มัธยมศึกษาตอนปลาย', response.data.decode('utf-8'))

    def test_thailand_provinces_portal(self):
        response = self.client.get('/thailand/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('77 จังหวัด', response.data.decode('utf-8'))
        self.assertIn('เชียงใหม่', response.data.decode('utf-8'))

        response_prov = self.client.get('/thailand/province/1')
        self.assertEqual(response_prov.status_code, 200)
        self.assertIn('คำขวัญประจำจังหวัด', response_prov.data.decode('utf-8'))

    def test_book_reader(self):
        response = self.client.get('/book/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('สารบัญเล่ม', response.data.decode('utf-8'))

    def test_wiki_encyclopedia(self):
        response = self.client.get('/wiki/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('สารานุกรม', response.data.decode('utf-8'))

    def test_games_hub_and_speed_math(self):
        response = self.client.get('/games/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('มินิเกม', response.data.decode('utf-8'))

        response_math = self.client.get('/games/speed-math')
        self.assertEqual(response_math.status_code, 200)
        self.assertIn('คิดเลขเร็วสายฟ้าแลบ', response_math.data.decode('utf-8'))

    def test_onet_exam_bank(self):
        response = self.client.get('/quiz/?type=onet')
        self.assertEqual(response.status_code, 200)
        self.assertIn('O-NET', response.data.decode('utf-8'))

    def test_admissions_center(self):
        response = self.client.get('/admissions/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('ปฏิทินสอบ', response.data.decode('utf-8'))
        self.assertIn('โรงเรียนเตรียมอุดมศึกษา', response.data.decode('utf-8'))

        response_detail = self.client.get('/admissions/1')
        self.assertEqual(response_detail.status_code, 200)
        self.assertIn('ระเบียบการ', response_detail.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
