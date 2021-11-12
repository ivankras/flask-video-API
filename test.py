try:
    from main import app
    import unittest, requests
except Exception as e:
    print(f'Missing modules: {e}')

BASE = 'http://127.0.0.1:5000'

class FlaskTest(unittest.TestCase):
    def testGet(self):
        tester = app.test_client(self)
        response = tester.get(f'{BASE}/video/1')
        status_code = response.status_code
        self.assertEqual(status_code, 200)
    
    def testWrongGet(self):
        tester = app.test_client(self)
        response = tester.get(f'{BASE}/video/9999999')
        status_code = response.status_code
        self.assertEqual(status_code, 404)
    
    def testContent(self):
        tester = app.test_client(self)
        response = tester.get(f'{BASE}/video/1')
        content_type = response.content_type
        self.assertEqual(content_type, 'application/json')
    
    def testData(self):
        tester = app.test_client(self)
        response = tester.get(f'{BASE}/video/1')
        data = response.data
        self.assertTrue(b'id' in data)
        self.assertTrue(b'name' in data)
        self.assertTrue(b'views' in data)
        self.assertTrue(b'likes' in data)
    
    def testInexistentData(self):
        tester = app.test_client(self)
        response = tester.get(f'{BASE}/video/99999999')
        data = response.data
        self.assertTrue(b'message' in data)

if __name__ == '__main__':
    try:
        response = requests.post(f'{BASE}/video/1', {'name': 'myvideo2', 'views': 929, 'likes': 210})
    except Exception as e:
        print(f'Problems setting the prereq video')
    
    unittest.main()