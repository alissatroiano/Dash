# Testing

The following tests have been conducted by the developer. Each test described below was accompanied by the actions taken to ensure the tests passed.

## Navigation

### Navbar Test #1:
- Visit app in web browser.
- Observe navigation bar.
- Click on each link.
- Verify each link directs user to intended template.
- Repeat steps 1-4 on tablet.
- Declare test 'passed'.

### Mobile Side Navbar Test:
- Visit app in mobile web browser.
- Click on 'fas fa-bars' icon.
- Verify sidenav opens properly.
- Declare test 'passed'.

### Navbar State Change Browser Test:
- Visit app in web browser.
- Oberserve navbar links read, 'Recipes', 'Signup' and 'Login'.
- **[Login](https://dash-ms3.herokuapp.com/login)**.
- Observe change in navbar once user is signed in.
- Verify navbar links read, 'Recipes', 'Add Recipe', 'Profile', and, 'Logout' while user is logged in.
- **Log Out** of the application.
- Verify navbar links return to original state (Recipes', 'Signup' and 'Login') once user is logged out.
- Declare test, 'passed'.

### Navbar State Change Mobile Test:
- Visit app on mobile web browser.
- Oberserve navbar links ('Recipes', 'Signup' and 'Login').
- **[Login](https://dash-ms3.herokuapp.com/login)**.
- Observe changes in navbar links once user is signed in.
- Verify navbar reads, 'Recipes', 'Add Recipe', 'Profile', and, 'Logout' while user is logged in.
- **Log Out** of the application.
- Verify navbar links return to original state (Recipes', 'Signup' and 'Login') once user is logged out.
- Declare test, 'passed'.

## Signup


## Login

### Login Browser Test:
- Visit app in web browser.
- Click, [Login](https://dash-ms3.herokuapp.com/login).
- Enter previously created username.
- Enter previously created password. 
- Ensure existing user is able to login successfully. 
- Declare test, 'passed'.

### Login Test 2:
- Visit app in web browser.
- Click, [Login](https://dash-ms3.herokuapp.com/login).
- Enter previously created username.
- Enter incorrect password. 
- Ensure existing user is unable to login with invalid credentials. 
- Declare test, 'passed'.

### Login Test 3:
- Visit app in web browser.
- Click, [Login](https://dash-ms3.herokuapp.com/login).
- Enter username.
- Enter correct password with incorrect cases. 
- Ensure password is case-sensitive.
- Declare test, 'passed'.

## Search 

### Create Index Test 1:
- Visit GitPod worspace
- Type `python3` to activate the Python interpreter
- Type, `from app import mongo` to connect to MongoDB
- Create the Search Index
- Verify the following text printed after creating the index, `recipe_name_text_recipe_description_text`
- Declare Test, 'passed'.

### Create Index Test 2:
- Visit [MongoDB Cloud Atlas](https://cloud.mongodb.com/)
- Visit the, 'Dash' database that was created for this application.
- Click on the, 'recipes' collection.
- Visit the, 'Indexes' tab.
- Verify that the newly created index appears on the page.
- Declare test, 'passed'.

![index](wireframes/index.png)

### Searchbar Not Case-Sensitive Test 1:
- Open deployed project in web browser.
- Visit the searchbar.
- Enter the word, 'tomato' in all lowercase letters in searchbar.
- Ensure that all recipes including the word, 'tomato' in the name and/or description are displayed.
- Repeat the above steps, but with all capital letters.
- Repeat the above steps, using a mixture of lowercase and uppercase letters.
- Verify that all relevant recipes display in search results regardless of letter case.
- Declare test, 'passed'.

### Searchbar Not Case-Sensitive Test 2:
- Open deployed project in mobile web browser.
- Visit the search-bar.
- Enter the word, 'chicken' in all lowercase letters in searchbar.
- Ensure that all recipes including the word, 'chicken' in the name and/or description are displayed.
- Repeat the above steps, but with all capital letters.
- Repeat the above steps, using a mixture of lowercase and uppercase letters.
- Verify that all relevant recipes display in search results.
- Declare test, 'passed'.

### 'Reset' Search Button Test #1:
- Open deployed project in web browser.
- Visit the searchbar.
- Enter the word, "GitHub" to ensure no results are generated.
- Click on the, 'Reset' button.
- Verify that search resets.
- Declare test, 'passed'.

### 'Reset' Search Button Test #2:
- Open deployed project in mobile browser.
- Visit the searchbar.
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
- Open deployed project in mobile web browser.
- Login to the application.
- Visit the, 'Add Recipe' page.
- Fill out the input form with an image uploaded from iPhone photo library.
- Submit the form.
- Observe that a Jinja, error log renders after clicking, `submit.`
- Review the contents of error report. 
- Diagnose problem: Line 125, `app.py`: `"created_by": ["user"]`.
- Visit the workspace and scroll down to line 125.
- Remove conflicting keyvalue pairs from `recipes` dictionary.
- Remove conflicting keyvalue from `submit` dictionary.
- Repeat test steps.
- Observe the flash notification, `Recipe successfully added.`
- Declare test, `passed`.


## File Upload Tests

### Mobile File Upload Test #1:
- Open deployed project in mobile web browser.
- Login to the application.
- Visit, 'Add Recipe' page.
- Fill out the input form with an image uploaded from iPhone photo library.
- Submit the form.
- Visit `Recipes` landing page.
- Observe images uploaded from mobile do not render after submission.


- Observe that a Jinja, error log renders after clicking, `submit.`
- Review the contents of error report. 
- Diagnose problem: Line 125, `app.py`: `"created_by": ["user"]`.
- Visit the workspace and scroll down to line 125.
- Remove conflicting keyvalue pairs from `recipes` dictionary.
- Remove conflicting keyvalue from `submit` dictionary.
- Repeat test steps.
- Observe the flash notification, `Recipe successfully added.`
- Declare test, `passed`.


- Reload the page and visit main recipes page.

