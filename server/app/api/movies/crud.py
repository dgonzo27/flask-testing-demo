from typing import List, Union

from structlog import get_logger

from app import db
from app.api.movies.models import Movie

logger = get_logger(__name__)


def get_all_movies() -> List[Movie]:
    """returns all movies"""

    logger.debug("get_all_movies")
    movies = None
    try:
        movies = Movie.query.all()
    except Exception as ex:
        logger.exception(f"exception occurred: {ex}")
        logger.error("unable to fetch all movies")
        pass
    return movies


def get_movie_by_id(id: int) -> Movie:
    """returns a single movie"""

    logger.debug("get_movie_by_id")
    movie = None
    try:
        movie = Movie.query.filter_by(id=id).first()
    except Exception as ex:
        logger.exception(f"exception occurred: {ex}")
        logger.error(f"unable to fetch movie {id}")
        pass
    return movie


def create_movie(title: str, description: str) -> Movie:
    """creates a single movie"""

    logger.debug("create_movie")
    movie = None
    try:
        movie = Movie(title=title, description=description)
        db.session.add(movie)
        db.session.commit()
    except Exception as ex:
        logger.exception(f"exception occurred: {ex}")
        logger.error(f"unable to create movie {title}")
        pass
    return movie


def update_movie(movie: Movie, title: str, description: str) -> Movie:
    """updates a single movie"""

    logger.debug("update_movie")
    try:
        movie.title = title
        movie.description = description
        db.session.commit()
    except Exception as ex:
        logger.exception(f"exception occurred: {ex}")
        logger.error(f"unable to update movie {movie.id}")
        movie = None
        pass
    return movie


def delete_movie(movie: Movie) -> Union[Movie, None]:
    """deletes a single movie"""

    logger.debug("delete_movie")
    try:
        db.session.delete(movie)
        db.session.commit()
    except Exception as ex:
        logger.exception(f"exception occurred: {ex}")
        logger.error(f"unable to delete movie {movie.id}")
        movie = None
        pass
    return movie
