from flask_restx import reqparse


post_movie_serializer = reqparse.RequestParser()
post_movie_serializer.add_argument("title", required=True)
post_movie_serializer.add_argument("description", required=True)
