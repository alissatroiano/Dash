# Testing

The following tests have been conducted by the developer. The tests were accompanied by the steps outlined below to ensure each test passed.

## Navigation

### Navbar Test #1:
- Visit the app in web browser.
- Observe the navigation bar.
- Click on each link.
- Verify each link directs the user to the correct HTML template.
- Repeat steps 1-4 on a tablet.
- Declare test 'passed'.

### Navbar Test #2 - `target=_blank`
- Visit the app in workspace while reading through the `Code Institute Student Pre-Submission Checklist`.
- Observe, `target=_blank` is not set for all `<a>` elements (as outlined in presubmission checklist).
- Visit the navigation menu in `base.html`.
- Add `target=_blank` to all `<a>` elements.
- Commit and push all code changes.
- Reload web browser.
- Observe that links now open in a new tab to satisfy grading criteria.
- Declare test 'passed'.

### Side Navigation Test #1:
- Visit the app in web browser.
- Resize browser tab to make, `fas fa-bars` icon visible.
- Click the icon.
- Observe that the side nav is not opening on click.
- Navigate to `static/js/script.js`.
- Ispect the jQuery code.
- Observe that jQuery is formatted correctly.
- Vist `base.html`.
- Scroll to the section containing **scripts**.
- Observe the following incorrect script src:
`<script src="{{ url_for('static', filename='/script.js') }}"></script>`
-  Fix the script so it reads:
`<script src="{{ url_for('static', filename='js/script.js') }}"></script>`
- Save code and push to GitHub.
- Reload browser and repeat steps 1-3.
- Observe that the side nav now opens correctly.
- Ensure each link works (by clicking each link).
- Declare test 'passed'.

### Mobile Side Navigation Test #1:
- Visit the app in mobile web browser.
- Click on 'fas fa-bars' icon.
- Verify side nav opens properly.
- Declare test 'passed'.

### Navbar State Change Browser Test:
- Visit the app in web browser.
- Observe navbar links read, 'Recipes', 'Signup' and 'Login'.
- **[Login](https://dash-ms3.herokuapp.com/login)**.
- Observe changed state in the navbar once a user is signed in.
- Verify navbar links read, 'Recipes', 'Add Recipe', 'Profile', and, 'Logout' while a user is logged in.
- **Log Out** of the application.
- Verify navbar links return to the original state (Recipes', 'Signup', and 'Login') once a user is logged out.
- Declare test, 'passed'.

### Navbar State Change Mobile Test:
- Visit the app on a mobile web browser.
- Observe navbar links ('Recipes', 'Signup' and 'Login').
- **[Login](https://dash-ms3.herokuapp.com/login)**.
- Observe changes in navbar links once a user is signed in.
- Verify navbar reads, 'Recipes', 'Add Recipe', 'Profile', and, 'Logout' while a user is logged in.
- **Log Out** of the application.
- Verify navbar links return to the original state (Recipes', 'Signup', and 'Login') once a user is logged out.
- Declare test, 'passed'.

## Signup

## Login

### Login Browser Test:
- Visit app in a web browser.
- Click, [Login](https://dash-ms3.herokuapp.com/login).
- Enter the previously created username.
- Enter the previously created password. 
- Ensure the existing user can log in successfully. 
- Declare test, 'passed'.

### Login Test 2:
- Visit the app in web browser.
- Click, [Login](https://dash-ms3.herokuapp.com/login).
- Enter the previously created username.
- Enter an incorrect password. 
- Ensure the existing user is unable to login with invalid credentials. 
- Declare test, 'passed'.

### Login Test 3:
- Visit app in web browser.
- Click, [Login](https://dash-ms3.herokuapp.com/login).
- Enter a username.
- Enter the password with incorrect text-cases. 
- Ensure the password is case-sensitive.
- Log out.
- Visit `Login` again.
- Enter the correct username and correct password.
- Log in to the application successfully.
- Repeat these steps on mobile and tablet.
- Declare test, 'passed'.

## Search 

### Create Index Test 1:
- Visit GitPod workspace
- Type `python3` to activate the Python interpreter
- Type, `from app import mongo` to connect to MongoDB
- Create the Search Index
- Verify the following text printed after creating the index, `recipe_name_text_recipe_description_text`
- Declare Test, 'passed'.

### Create Index Test 2:
- Visit [MongoDB Cloud Atlas](https://cloud.mongodb.com/)
- Visit the 'Dash' database that was created for this application.
- Click on the 'recipes' collection.
- Visit the 'Indexes' tab.
- Verify that the newly created index appears on the page.
- Declare test, 'passed'.

![index](wireframes/index.png)

### Searchbar Not Case-Sensitive Test 1:
- Open the deployed project in a web browser.
- Visit the search bar.
- Enter the word, 'tomato' in all lowercase letters in the search bar.
- Ensure that all recipes including the word, 'tomato' in the name and/or description are displayed.
- Repeat the above steps, but with all capital letters.
- Repeat the above steps, using a mixture of lowercase and uppercase letters.
- Verify that all relevant recipes display in search results regardless of letter case.
- Declare test, 'passed'.

### Searchbar Not Case-Sensitive Test 2:
- Open the deployed project in my mobile web browser.
- Visit the search-bar.
- Enter the word, 'chicken' in all lowercase letters in the search bar.
- Ensure that all recipes including the word, 'chicken' in the name and/or description are displayed.
- Repeat the above steps, but with all capital letters.
- Repeat the above steps, using a mixture of lowercase and uppercase letters.
- Verify that all relevant recipes display in search results.
- Declare test, 'passed'.

### 'Reset' Search Button Test #1:
- Open the deployed project in a web browser.
- Visit the search bar.
- Enter the word, "GitHub" to ensure no results are generated.
- Click on the, 'Reset' button.
- Verify that search resets.
- Declare test, 'passed'.

### 'Reset' Search Button Test #2:
- Open the deployed project in a mobile browser.
- Visit the search bar.
- Enter the word, "GitHub" to ensure no results are generated.
- Click on the, 'Reset' button.
- Verify that search resets.
- Declare test, 'passed'.

## CREATE (C.R.U.D Testing)

### Add Recipe W3C Test 1:
- Copy all of `add_recipe.html`
- Paste code in [W3C HTML Validator](https://validator.w3.org/)
- Observe **textarea** errors, `Attribute type not allowed on element textarea at this point.`.
- Open workspace.
- Delete `type="text"` from all textareas.
- Copy contents of `add_recipe.html` and paste in W3C html validator.
- Ensure all textarea related errors are no longer present.
- Declare test, 'passed'.

### Add Recipe Mobile Test:
- Open the deployed project in a mobile web browser.
- Login to the application.
- Visit the 'Add Recipe' page.
- Fill out the input form with an image uploaded from the iPhone photo library.
- Submit the form.
- Observe that a Jinja, error log renders after clicking, `submit.`
- Review the contents of the error report. 
- Diagnose the problem: Line 125, `app.py` (`add_recipe` function).
- Visit the workspace and scroll down to line 125.
- Inspect the `recipe` dictionary that is sent to MongoDB upon creating a new recipe.
- Scroll to the `edit_recipe` function and notice conflicting key-value pairs. 
 - Rename and repair.
- Push all changes to GitHub.
- Reload web browser and repeat steps 4-5.
- Observe flash notification, `Recipe successfully added.`
- Declare test, `passed`.

## File Upload Tests

### Mobile File Upload Test #1:
- Open the deployed project in a mobile web browser.
- Login to the application.
- Visit, 'Add Recipe' page.
- Fill out the input form with an image uploaded from the iPhone photo library.
- Submit the form.
- Visit the `Recipes` landing page.
- Observe images uploaded from mobile do not render after submission.
- Open Chrome Developer Tools and inspect the failed image uploads.
- Notice the request type reads, `text/HTML`. 
- Add the `accept` attribute with value `image/*` to file input.
- Reload the page to see if the problem persists.
- Open Dev Tools.
- Observe all mobile uploaded images are now rendering as, `image/jpeg`, `image/png`, etc.
- Declare test, 'passed'.

## W3C Testing

### Jigsaw Test One:
- Visit W3C Jigsaw Validator.
- Copy `style.css` and paste via 'direct upload'.
- Observe one `Parse Error`
- Open the stylesheet and scroll to the line of code where the error is.
- Notice the second closing `}` is not present in the media query.
- Add the closing bracket.
- Test CSS again via direct upload.
- Observe that there are zero errors remaining.
- Declare test, 'passed'.