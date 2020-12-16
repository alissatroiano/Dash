from flask import Flask
from src.controllers import ArticleController
import src.database


def create_app(db_uri: str) -> Flask:
    app = Flask(__name__)
    app.config["MONGO_URI"] = db_uri
    src.database.mongo.init_app(app)

    # Add the articles collection if it doesn't already exist
    if not 'recipes' in src.database.mongo.db.list_collection_names():
       recipes_collection = src.database.mongo.db['recipes']

    # Register the article routes
    ...

    return app
