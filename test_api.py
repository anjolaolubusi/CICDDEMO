from main import app
import json
import unittest

class ApiTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        # self.testHealth()
        # self.testHome()
        # self.assertEqual(app.debug, False)

    def testHealth(self):
        # print("Health Func Test")
        response = self.app.get("/health")
        self.assertEqual(response.data, b'Alive')
        self.assertEqual(response.status_code, 200)

    def testHome(self):
        # print("desc Func Test")
        response = self.app.get("/desc")
        self.assertEqual(response.data, b'This is an api page')
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()