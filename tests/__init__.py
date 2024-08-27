from unittest import TestCase
from app import create_app


class BaseTestCase(TestCase):
    
    def setUp(self) -> None:
        
        self.app = create_app("test")

        self.app_context = self.app.app_context()

        self.app_context.push()
    
    def tearDown(self) -> None:
        
        self.app_context.pop()

        self.app = None
