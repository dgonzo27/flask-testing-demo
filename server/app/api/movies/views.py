from flask_restx import Namespace, Resource, fields
from structlog import get_logger

from app.api.movies.crud import (
    get_all_movies,
    get_movie_by_id,
    create_movie,
    update_movie,
    delete_movie
)
from app.api.movies.serializers import post_movie_serializer

logger = get_logger(__name__)

movies_namespace = Namespace("movies")
movie = movies_namespace.model(
    "Movie",
    {
        "id": fields.Integer(readOnly=True),
        "title": fields.String(required=True),
        "description": fields.String(required=True)
    },
)


class MovieList(Resource):
    @movies_namespace.marshal_with(movie, as_list=True)
    def get(self):
        """returns all movies"""

        logger.debug("MovieList.GET")
        return get_all_movies(), 200
    
    @movies_namespace.expect(post_movie_serializer, validate=True)
    @movies_namespace.marshal_with(movie)
    def post(self):
        """creates a single movie"""

        logger.debug("MovieList.POST")
        args = post_movie_serializer.parse_args()
        return create_movie(args["title"], args["description"]), 201


class MovieDetail(Resource):
    @movies_namespace.marshal_with(movie)
    def get(self, movie_id):
        """returns a single movie"""

        logger.debug("MovieDetail.GET")
        _movie = get_movie_by_id(movie_id)
        if not _movie:
            movies_namespace.abort(404, "movie does not exist")
        return _movie, 200
    
    @movies_namespace.expect(post_movie_serializer, validate=True)
    @movies_namespace.marshal_with(movie)
    def put(self, movie_id):
        """updates a single movie"""

        logger.debug("MovieDetail.PUT")
        args = post_movie_serializer.parse_args()
        _movie = get_movie_by_id(movie_id)
        if not _movie:
            movies_namespace.abort(404, "movie does not exist")
        return update_movie(_movie, args["title"], args["description"]), 200
    
    @movies_namespace.marshal_with(movie)
    def delete(self, movie_id):
        """deletes a single movie"""

        logger.debug("MovieDetail.DELETE")
        _movie = get_movie_by_id(movie_id)
        if not _movie:
            movies_namespace.abort(404, "movie does not exist")
        return delete_movie(_movie), 204


movies_namespace.add_resource(MovieList, "")
movies_namespace.add_resource(MovieDetail, "/<int:movie_id>")
