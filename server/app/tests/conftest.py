import pytest

from app import create_app, db
from app.api.movies.models import Movie


@pytest.fixture(scope="module")
def test_app():
    """fixture for testing the application"""

    app = create_app()
    app.config.from_object("app.config.TestingConfig")
    with app.app_context():
        yield app # testing happens here


@pytest.fixture(scope="module")
def test_database():
    """fixture for cleaning and leveraging test db"""

    db.create_all()
    yield db # testing happens here
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="module")
def add_movie():
    def _add_movie(title, description=""):
        movie = Movie(title=title, description=description)
        db.session.add(movie)
        db.session.commit()
        return movie
    
    return _add_movie