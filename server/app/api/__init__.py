from flask_restx import Api

from app.api.movies.views import movies_namespace
from app.api.ping.views import ping_namespace


api = Api(version="1.0", title="Flask API", doc="/api/v1/docs")
api.add_namespace(movies_namespace, path="/api/v1/movies")
api.add_namespace(ping_namespace, path="/api/v1/ping")
