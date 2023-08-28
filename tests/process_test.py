import unittest
from app import app


class FlaskTestCase(unittest.TestCase):
    def test_list_process(self):
        tester = app.test_client()
        with open('static/input.json', 'rb') as f:
            response = tester.post(
                '/process',
                content_type='multipart/form-data',
                data={'file': (f, 'input.json')}
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), [
            {'FirstFrame': 'file_0000001.jpg', 'LastFrame': 'file_0000010.jpg'},
            {'FirstFrame': 'image_0000002.png', 'LastFrame': 'image_0000020.png'}
        ])

    def test_dict_process(self):
        tester = app.test_client()
        with open('static/input_dict.json', 'rb') as f:
            response = tester.post(
                '/process',
                content_type='multipart/form-data',
                data={'file': (f, 'input_dict.json')}
            )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.get_json(), {
                "FirstFrame": "/Volumes/MD_1717/CF_CATS_ARI_Test/B077R0EC/B077C002_190201_R0EC/B077C002_190201_R0EC.1235386.ari",
                "LastFrame": "/Volumes/MD_1717/CF_CATS_ARI_Test/B077R0EC/B077C002_190201_R0EC/B077C002_190201_R0EC.1240067.ari"
            }
        )


if __name__ == '__main__':
    unittest.main()