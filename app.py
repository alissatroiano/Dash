import os
import requests
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from pymongo import MongoClient
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import urllib.parse

if os.path.exists("env.py"):
    import env

from settings import *
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
username = username
password = password
mongo = MongoClient('mongodb+srv://%s:%s@myfirstcluster.shvov.mongodb.net/' % (username, password))
db = mongo['Dash']
recipes = db['recipes']
users = db['users']

@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(db.recipes.find().sort(
        "_id", -1))
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.args.get("query")
    recipes = list(db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if username  already exists in db
        existing_user = db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("This username already exists")
            return redirect(url_for("signup"))

        signup = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(signup)

        # create session cookies
        session["user"] = request.form.get("username").lower()
        flash("Success!")
        return redirect(url_for("get_recipes", username=session["user"]))
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "get_recipes", username=session["user"]))
            else:
                flash("Incorrect username and/or password")
                return redirect(url_for("login"))

        else:
            flash("Incorrect username and/or password")
            return redirect(url_for("login"))

    return render_template("login.html")

    # Fetch session username from databases
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("recipes.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove user from session cookie and redirect user to login function
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        image_path = upload_file()
        recipe = {
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "file": image_path,
            "tools_needed": request.form.get("tools_needed"),
            "recipe_instructions": request.form.get("recipe_instructions"),
            "created_by": session["user"]
        }
        db.recipes.insert_one(recipe)
        flash("Recipe successfully added")
        return redirect(url_for("get_recipes"))

    return render_template("add_recipe.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file():
    path = url_for('static', filename='uploads/dash.jpg')
    # if user does not select file, stock photo will be used
    if 'file' not in request.files:
        return path
    file = request.files['file']
    if file.filename == '':
        return path
    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
    return path

 
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    edit_path = upload_file()
    if request.method == "POST":
        edit = {
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "file": edit_path,
            "tools_needed": request.form.get("tools_needed"),
            "recipe_instructions": request.form.get("recipe_instructions")
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edit)
        flash("Recipe edited!")
        return redirect(url_for('get_recipes'))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    return render_template("edit_recipe.html", recipe=recipe)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


if __name__ == "__main__":
    app.run(debug=True)