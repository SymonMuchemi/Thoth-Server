import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class Config:

    pass


class DevConfig(Config):
    DEBUG = True

    @staticmethod
    def init_app(app):

        pass


class TestConfig(Config):

    TESTING = True

    @staticmethod
    def init_app(app):

        pass


class ProdConfig(Config):

    @staticmethod
    def init_app(app):

        pass


env_config = {
    "default": DevConfig,
    "dev": DevConfig,
    "test": TestConfig,
    "prod": ProdConfig
}
