from tests import BaseTestCase


class TestAppConfig(BaseTestCase):

    def test_app_in_test_mode(self):

        self.assertIsNotNone(self.app)

        self.assertTrue(self.app.config["TESTING"])
