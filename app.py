import os
import boto3
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
    import env
    print("env.py loaded successfully")

UPLOAD_FOLDER = '/static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
S3_BUCKET_NAME = os.environ.get("S3_BUCKET_NAME")
S3_KEY = os.environ.get("S3_KEY")
S3_SECRET = os.environ.get("S3_SECRET")
S3_LOCATION = os.environ.get("S3_LOCATION")
USE_LOCAL_STORAGE = os.environ.get("USE_LOCAL_STORAGE")
print(USE_LOCAL_STORAGE)
FLASK_ENV = os.environ.get("FLASK_ENV")
print(FLASK_ENV)

app = Flask(__name__, static_url_path='/static')

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")
app.config['UPLOAD_FOLDER'] = os.environ.get("UPLOAD_FOLDER", "/tmp/uploads")

# Ensure the upload directory exists
upload_folder = os.path.join(app.root_path, app.config['UPLOAD_FOLDER'])
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

s3 = boto3.client("s3", aws_access_key_id=S3_KEY,
                  aws_secret_access_key=S3_SECRET)
app.config["S3_BUCKET_NAME"] = os.environ.get("S3_BUCKET_NAME")
app.config["S3_KEY"] = os.environ.get("S3_KEY")
app.config["S3_SECRET"] = os.environ.get("S3_SECRET")
app.config["S3_LOCATION"] = os.environ.get("S3_LOCATION")

mongo = PyMongo(app)
mongo.db = mongo.cx[app.config["MONGO_DBNAME"]]
# print(mongo.db)
# print(mongo.db.list_collection_names())
print("Mongo URI:", os.environ.get("MONGO_URI"))
print("Mongo DB Name:", os.environ.get("MONGO_DBNAME"))


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find().sort("_id", -1))
    # print("Fetched recipes:", recipes)  # Add this line for debugging
    return render_template("recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.args.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # check if username  already exists in db
        existing_user = mongo.db.users.find_one(
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
        existing_user = mongo.db.users.find_one(
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
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe successfully added")
        return redirect(url_for("get_recipes"))

    return render_template("add_recipe.html")


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def upload_file():
    # Default path in case of no file or error
    path = '/static/uploads/dash.jpg'

    if 'file' not in request.files:
        print("No file part")
        return path

    file = request.files['file']

    if file.filename == '':
        print("No filename")
        return path

    # Check allowed file types
    if file and allowed_file(file.filename):
        file.filename = secure_filename(file.filename)
        print(f"Secure filename for upload: {file.filename}")
        print(f"Content type for upload: {file.content_type}")

        # Local storage mode
        if os.environ.get("USE_LOCAL_STORAGE") == "True":
            # Ensure the upload directory exists
            upload_folder = os.path.join(app.root_path, 'static', 'uploads')
            os.makedirs(upload_folder, exist_ok=True)

            file_path = os.path.join(upload_folder, file.filename)
            print(f"Saving file locally to: {file_path}")
            file.save(file_path)
            path = f"/static/uploads/{file.filename}"
            print(f"File saved successfully at {file_path}")

        # S3 upload mode
        else:
            try:
                path = upload_file_to_s3(file)
                if not path:
                    print("Error: Failed to upload file to S3.")
                    path = "/static/uploads/dash.jpg"
            except Exception as e:
                print(f"S3 Upload Error: {str(e)}")
                path = "/static/uploads/dash.jpg"

    else:
        print("Invalid file type")

    print(f"Final image path: {path}")
    return path


def upload_file_to_s3(file):
    if not file or not file.filename:
        print("Error: No file or filename provided for upload.")
        return None

    secure_filename_str = secure_filename(file.filename)
    print(f"Secure filename for upload: {secure_filename_str}")

    try:
        # Ensure ContentType is correctly set based on the file's actual type
        content_type = file.content_type if file.content_type else "application/octet-stream"
        print(f"Content type for upload: {content_type}")

        # Upload the file to S3
        s3.upload_fileobj(
            file,
            S3_BUCKET_NAME,
            secure_filename_str,
            ExtraArgs={
                "ACL": "public-read",
                "ContentType": content_type
            }
        )
        print(
            f"File successfully uploaded to S3 at {S3_LOCATION}{secure_filename_str}")
        return f"{S3_LOCATION}{secure_filename_str}"

    except Exception as e:
        print(f"S3 Upload Error: {str(e)}")  # More explicit error message
        return None  # Handle None gracefully elsewhere


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    if not recipe or recipe["created_by"] != session.get("user"):
        flash("You are not authorized to edit this recipe.")
        return redirect(url_for("get_recipes"))

    if request.method == "POST":
        # Call upload_file only if a new file is uploaded
        edit_path = upload_file(
        ) if 'file' in request.files and request.files['file'].filename else recipe.get("file")

        edit = {
            "recipe_name": request.form.get("recipe_name"),
            "prep_time": request.form.get("prep_time"),
            "recipe_description": request.form.get("recipe_description"),
            "recipe_ingredients": request.form.get("recipe_ingredients"),
            "file": edit_path,
            "tools_needed": request.form.get("tools_needed"),
            "recipe_instructions": request.form.get("recipe_instructions")
        }
        mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)}, {"$set": edit})
        flash("Recipe edited!")
        return redirect(url_for('get_recipes'))

    return render_template("edit_recipe.html", recipe=recipe)


@app.route('/delete_recipe/<recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    recipe = Recipe.objects(id=recipe_id).first()  # Fetch the recipe by ID
    if recipe and recipe.created_by == session.get("user"):
        recipe.delete()  # Delete the recipe from MongoDB
        flash("Recipe deleted successfully!", "success")
    else:
        flash("You are not authorized to delete this recipe.", "danger")
    return redirect(url_for('get_recipes'))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
