# Dash

![responsive](wireframes/amiresponsive.jpg)

Dash is a recipe sharing application for men & women, (ages 24 - 39), who want to find and share recipes.

## UX

To make for a more organized development process, the developer used [GitHub Projects](https://github.com/users/alissatroiano/projects/4) to manage sprints and tasks. 

As the Milestone 3 Project for [Code Institute's](https://codeinstitute.net/) Data-Centric Development portion of the Full Stack Developer Program, this project was built with HTML, CSS, JavaScript, jQuery, Python, Flask, and MongoDB.

Dash's target market is comprised of men & women, ages 24 - 39, that wish to find and share recipes. To become a contributor on Dash, a user must create an account. Creating an account is quick, easy and free. Once an account has been created, a user may login to create new recipes or edit any of the recipes on Dash.

### User Stories

User stories were created first during the Strategy Plane phase of this milestone project to guide the wireframing process:

User Story 1:

> *"As a daily Dash user, I want to be able to search, so that I can find the recipes I actually want to use!"*
>> -Jane Marino, Homemaker

User Story 2:

> *"As a new user, I want to find the 'Sign Up' page right away, so I can create and update recipes."*
>> -Michael Corona, Yoga Teacher

User Story 3:

> *"As a user, I want to be able to post my own recipes, so I can share them with like-minded individuals."*
>> -Danielle Greenstein, Food Blogger

User Story 4:

> *"As a member, I want to be able to edit any of the recipes on the page, so I can use my expertise to contribute to the Dash community."*
>> -Andy Fjordane, Chef

User Story 5:

> *"As a Dash member, I want other members to edit my recipes, so I can learn new ways to prepare dishes."*
>> -Michelle Greene, Cafe Owner

The user story worksheet that was completed during the Strategy Plane portion of this project can be viewed here:

![userstories](wireframes/userstories.jpg)

### Trade-Off Exercise

To determine what features were the most important and most viable, the following Strategy Plane activity was completed during the planning phase of this project:

![Trade Off Table](wireframes/tradeoff.jpg)

To view a PDF version of this exercise, please refer to [this document](wireframes/tradeoff.pdf)

### Wireframes

 The following wireframes were created by the developer to guide the development process:

![wireframes](wireframes/desktop.png)

![wireframes](wireframes/tablet.jpg)

![wireframes](wireframes/mobile.jpg)

These [wireframes](wireframes/dash.pdf) can also be viewed in the attached PDF. 

## Features

### Existing Features

To properly develop this full-stack application, the following features were included:

- Sign Up - allows users to create an account, by inputting an original username and a password.

- Login - Allows users to log in to their Dash account, by inputting the correct user and password keys.

- Create Recipe - Allows **existing** users to share original content with the Dash community, by granting them write access to the database and having them fill out a form.

- Edit Recipe - Allows users to edit any recipe, by including a functional, 'Edit' button with each recipe.

- Search - Allows users to search for specific recipes, by providing them with a search bar that fetches and displays relevant data.

### Features Left to Implement

- A 'Profile' page - Allows users to upload an imnage, view content they have created and change their username and/or password.

### Database Design

To create a functional CRUD application, I took the following steps when creating my datastore:

1. Choose a database: **MongoDB**.

I chose to use MongoDB to store Dash's data. Dash is a crowdsourcing app, so it involves obtaining information, or data, from a large group of people. Because of this, it was determined crucial that Dash be connected to a database that can handle a lot of data and send/receive data requests to and from the application.

2. Design the Datastore:

    - Though my initial plans were a bit more complex, I decided to make the database as simple and efficient as possible. To do this, I took the following steps:
        - Create a new database named, 'Dash'.

        - Create 2 collections:
            1. recipes - Contains the contents for each recipe.
            2. users - Contains identifying information that is essential to user authentication.

        ![database](wireframes/dashdatabase.png)
        
    - Include the following documents in each collection:

        1. recipes:
            - recipe_name: The name of the recipe (string).
            - recipe_description - A brief description of the recipe (a string).
            - prep_time - How long the recipe takes to make (I contemplated using an integer, but decided to use a string so users can write minutes, etc.).
            - tools_needed - What tools are required to make the recipe (string)
            - recipe_ingredients - The ingredients of the recipe (string)
            - file - An image file that users can upload when creating or editing a recipe. (string).
            - recipe_instructions - The steps taken to create the recipe (string)

        ![recipesdb](wireframes/recipesdb.png)

        2. users:
            - username: The username that the user creates at signup and logins in with to perform any write actions on the database. ***(Note: a user can read any of the recipes without an account, but must be signed in to create or edit a recipe)***
            - password: The password will be used by the user to login and perform C.R.U.D operations on the database.

3. Add some data:

    - When building a C.R.U.D application, it makes it easier for the developer to build out the backend when there is already some data in place. Because of this, I added some data to each of the collections in my datastore. Once I had some data to work with, I created the Flask App, deployed it to **Heroku**, connected it to my database, and constructed the frontend.

To read more about my process, visit the Deployment section of this documentation.

## Technologies Used

- [HTML](https://html.com/)

- This project uses HTML to display and format content on the front-end.

- [CSS](https://www.w3.org/Style/CSS/Overview.en.html)

- This project uses **CSS** to add styles and responsiveness to its' content.

- [Python](https://www.python.org/)

- This project uses **Python** to speed up development time and integrate systems.

- [PyPy](https://doc.pypy.org/en/latest/)
- This project uses **PyPy** to improve processing performance.

- [Pip3](https://pip.pypa.io/en/stable/)

- This project uses **Pip3** to install software dependencies for Python.

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

- This project uses the **Flask** framework to reduce development time and build a more robust application.

    **Flask Dependencies:**

    - [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/serving/)

    - This project uses Flask's dependencies, including the WSGI web application library, **Werkzeug** to serve the WSGI application with powerful structure and patterns.

- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

- This project uses the **Jinja** templating functionality to create HTML that is returned to the user via HTTP requests.

- [MongoDB](https://www.mongodb.com/)

- This project uses **MongoDB** to simplify data storage and manipulation.

- [PyMongo](https://pypi.org/project/pymongo/)

- This project uses the driver **PyMongo** to fetch and insert data to MongoDB from Python.

- [DNSPython](https://www.dnspython.org/)

- This application uses **dnspython**  to handle queries and data manipulation.

- [request]()

- This project uses **request** to get the JSON out of the response body on new inserts.

- [Git](https://git-scm.com/)

- This project uses **Git** for code storage and version control.

- [GitHub](https://github.com/)

- This project uses **GitHub** for version control and project management.

- [Materialize](https://materializecss.com/)

- This project used **Materialize** to add frontend styles and improve user experience.

- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

- This project uses **Boto3** to create, configure, and manage the AWS S3 service.

- [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html)

- This application uses Amazon S3 to streamline file storage and transfer.

- [Werkzeug.security](https://werkzeug.palletsprojects.com/en/1.0.x/utils/)

- This application uses **Werkzeug.security** to create secure, reliable user authentication.

## Testing

Thorough testing was conducted by the developer for this project and can be viewed in [TESTING.md](TESTING.md)

## Deployment

### Heroku

This project was deployed by Heroku. 

In order to successfully deploy the app, the following steps were taken:

- Visit GitPod workspace.
- Create the Flask App.
- Use the CLI to tell Heroku which applications and dependencies are rquired to run the application via the, `pip3 freeze --local > requirements.txt` command.
- Create the Procfile via `echo web: python app.py > Procfile`.
- Visit [Heroku](https://www.heroku.com).
- Click, 'Create a New App'.
- Create an application on Heroku with a unique name **('dash-ms3')** to satisfy Heroku requirements.
- Create the Heroku application.
- Add the following configuration vars to Heroku application:
    - `IP`
    - `PORT`
    - `MONGO_URI`
    - `SECRET_KEY`
    - `MONGO_DBNAME`
- Visit workspace/IDE.
- Push newly created `requirements.txt` and `Procfile` to Git.
- Navigate back to Heroku and enable automatic deployment.
- Connect Heroku to deploy from the **master** branch of Dash's repository.
- Successfully deploy the application.

Once the application was deployed, I navigated back to my workspace and began to build out templating with Jinja. Upon testing my application, I discovered an issue regarding file storage and decided to use Amazon S3 Photo Bucket, a third party service, to store file uploads.

I then had to add the following configuration vars to my Heroku app;
    - `S3_BUCKET_NAME`
    - `S3_KEY`
    - `S3_SECRET`
    - `S3_LOCATION`

To view this project on Heroku, visit https://git.heroku.com/dash-ms3.git.

## Credits

### Development Process

- The steps taken to properly configure Flask and MongoDB were learned by following [Code Institute's](https://codeinstitute.net/) 'Data-Centric Development: Flask Mini Project' lesson.

- The steps taken to import the favicon into the head element of the base HTML page were copied from (Stack Overflow)(https://stackoverflow.com/questions/11893478/add-favicon-to-website) and [Hostinger](https://www.hostinger.com/tutorials/how-to-add-favicon-to-website).

- The developer made use of [GitHub Projects](https://github.com/users/alissatroiano/projects/4) to manage development and efficiently set sprints.

- The media queries defined in the stylesheet for tablets and large devices were copied/learned from [W3 Schools](https://www.w3schools.com/css/css_rwd_mediaqueries.asp).

- I followed the steps provided by this article, [How to use Flask to upload files to Amazon s3](https://www.zabana.me/notes/flask-tutorial-upload-files-amazon-s3) to understand and implement uploading files to an Amazon S3 bucket using the Flask web framework for Python.

### Content

- The grid layout and responsive design were made possible by importing [Materialize](https://materializecss.com/) front-end framework and using the built-in classes.

- The 'Cauliflower Grilled Cheese' recipe was copied from [delish](https://www.delish.com/cooking/recipe-ideas/g3733/healthy-dinner-recipes/).

- Text shadow styles were copied from [CSS Tricks](https://css-tricks.com/almanac/properties/t/text-shadow/).

### Media

- Dash's favicon was copied from [Openclipart.org](https://openclipart.org/detail/321362/kitchen-utensils) and is licensed under Creative Commons.

- The default photo that is selected when a user does not upload an image was copied from [unsplash](https://unsplash.com/photos/fnztlIb52gU).

- The icon in the branded navigation menu, responsive sidebar, and footer was copied from [Font Awesome](http://fontawesome.com/)

- The footer styles were copied from [Materialize]() and altered via copying [W3 Schools](https://www.w3schools.com/howto/howto_css_fixed_footer.asp).

- The stock images used to create the recipes were copied from:

    - Cauliflower Grilled Cheese; [Unsplash](https://unsplash.com/photos/SqYmTDQYMjo)

    - Tomato Chicken Garlic [Unsplash](https://unsplash.com/photos/9WfO94SjhmE)

    - Broccoli Quinoa Cakes - [Feasting at Home](https://www.feastingathome.com/broccoli-cakes/)

    - [ifoodreal.com](https://ifoodreal.com/clean-eating-recipes-dinners/)

- The responsive view image at the top of this documentation was created with [AmIResposnive](http://ami.responsivedesign.is/).

### Acknowledgements

- I received markdown instructions from this [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#blockquotes)

- I received UX inspiration from [Awwwards](https://www.awwwards.com)

- I received UX inspiration from [Behance](https://www.behance.net)

- I learned about Flask file upload configurations from [Flask's Documentation](https://flask-uploads.readthedocs.io/en/latest/).

- I utilized the free web-tool provided by [Amiresponsive](http://ami.responsivedesign.is/) to get an idea of how my project looks on different screens.

- I obtained information about project dependencies and what they actually do from, [Inserting and Reading MongoDB Documents from a Python Flask API](https://medium.com/swlh/inserting-and-reading-mongodb-documents-from-a-python-flask-api-4fa7be61e45).

- I proofread and corrected this documentation with [Grammarly]([grammarly](https://app.grammarly.com/).