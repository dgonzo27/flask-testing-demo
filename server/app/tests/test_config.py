"""tests the flask app configuration app.config.py"""

import os


def test_development_config(test_app):
    test_app.config.from_object("app.config.DevelopmentConfig")
    assert test_app.config["SECRET_KEY"] == "change_me"
    assert not test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.getenv("DATABASE_URL")


def test_testing_config(test_app):
    test_app.config.from_object("app.config.TestingConfig")
    assert test_app.config["SECRET_KEY"] == "change_me"
    assert test_app.config["TESTING"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.getenv("DATABASE_TEST_URL")
