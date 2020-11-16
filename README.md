# Dash

Dash is an online cookbook for men & women, (ages 24 - 39), who lead healthy lifestyles and wish to find and share recipes with like-minded individuals.

## UX

As the Milestone 3 Project for [Code Institute's](https://codeinstitute.net/) Data Centric Development portion of the Full Stack Developer Program, this project was built with HTML, CSS, JavaScript, jQuery, Python, Flask and MongoDB.

Dash's target market is health-minded adult men & women, ages 24 - 29, that wish to find and share recipes. The target market also seeks a place to manage their own recipes and ingredients.

User stories were created during the Strategy/Planning Phase of this project:

User Story 1:

> *"As a daily Dash user, I want to search for specific recipes, so that I can find the type of stuff I actually want to make!"*
>> -Jane Marino, Homemaker

User Story 2:

> *"As a new user, I want to be able to create an account easily so I can be a member of the community"*
>> -Michael Corona, Yoga Teacher

User Story 3:

> *"As a user, I want to be able to post my own reipes, so I can share them with like-minded individuals."*
>> -Danielle Greenstein, Health-food blogger

User Story 4:

> *"As a member, I want to be able to edit any of the reipes on the page, so I can use my expertise to contribute to the Dash community."*
>> -Andy Fordane, Chef

User Story 5:

> *"As a Dash member, I want other members to edit my recipes, so I can learn what I was doing wrong and how I could have done it differently ."*
>> -Danielle Greenstein, Health-food blogger

The user story worksheet that was completed during the Strategy Plane portion of this project can be viewed here:

![userstories](wireframes/userstories.jpg)

 The following wireframes were created by the developer to guide the development proess:

![wireframes](wireframes/desktop.jpg)

![wireframes](wireframes/tablet.jpg)

![wireframes](wireframes/mobile.jpg)

## Features

### Existing Features

In order to properly develop this full-stack application, the following features were included:

- Sign Up - allows users to create an account, by inputting an original username and a password.

- Log In - Allows users to login to their Dash account, by inputting the correct user and password keys.

- Create Recipe - Permits users to share original content to the Dash community, by granting them write access to the database and having them fill out a form.

- Edit Recipe - Allows users to edit any recipe, by including a functional, 'Edit' button with each recipe.

- Search - Allows users to search for specific recipes, by providing them with a searchbar that fetches and displays relevant data.

### Features Left to Implement

- A 'Grocery List' page - Allows users to create grocery lists, by having them create a checklist and manage/update it accordingly.

## Technologies Used

- [HTML](https://html.com/)

- This project uses HTML to display and format content on the front-end.

- [CSS](https://www.w3.org/Style/CSS/Overview.en.html)

- This project uses **CSS** to add styles and responsiveness to its' content.

- [Python](https://www.python.org/)

- This project uses **Python** to speed up development time and integrate systems.

- [PIP](https://pypi.org)

- This project uses **Pip** to install software dependencies for Python.

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

- This project uses the **Flask** framework to reduce development time and build a more robust application.

- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

- This project uses the **Jinja** templating functionality to create HTML that is returned to the user via HTTP requests.

- [MongoDB](https://www.mongodb.com/)

- This project uses **MongoDB** to simplify data storage and manipulation.

- [PyMongo](https://pypi.org/project/pymongo/)

- This project uses the driver **PyMongo** to interact with MongoDB from Python.

- [Git](https://git-scm.com/)

- This project uses **Git** for code storage and version control.

## Testing

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your user stories from the UX section and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

Whenever it is feasible, prefer to automate your tests, and if you've done so, provide a brief explanation of your approach, link to the test file(s) and explain how to run them.

For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:

1. Contact form:
    1. Go to the "Contact Us" page
    2. Try to submit the empty form and verify that an error message about the required fields appears
    3. Try to submit the form with an invalid email address and verify that a relevant error message appears
    4. Try to submit the form with all inputs valid and verify that a success message appears.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub Pages or Heroku).

In particular, you should provide all details of the differences between the deployed version and the development version, if any, including:

- Different values for environment variables (Heroku Config Vars)?
- Different configuration files?
- Separate git branch?

In addition, if it is not obvious, you should also describe how to run your code locally.

## Credits

### Development Process

- The steps taken to properly configure Flask and MongoDB were learned by following Code Institute's 'Data Centric Development' module.

- The steps taken to properly install node modules via npm were aquired from [Codeburst's](https://codeburst.io) article, ["Deploying a Flask App with NPM modules on Heroku"](https://codeburst.io/deploying-a-flask-app-with-npm-modules-on-heroku-203a73ec5654)

### Content

### Media

- The photos used in this site were obtained from ...

### Acknowledgements

- I received markdown instructions from this [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#blockquotes)

- I received UX inspiration from [Awwwards](https://www.awwwards.com)

- I received UX inspiration from [Behance](https://www.behance.net)

- I took suggestions from [Prototypr's article, '7 Best UX Practices for Designing Long Online Forms'](https://blog.prototypr.io/seven-best-ux-practices-for-designing-long-online-forms-6a670e488bad)