from main import app
import json
import unittest

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        print("Health Test")
        self.testHealth()
        self.assertEqual(app.debug, False)

    def testHealth(self):
        response = self.app.get("/health")
        self.assertEqual(response.data, b'Alive')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()