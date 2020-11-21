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

### Navbar Changing State Test:
- Visit app in web browser.
- Oberserve navbar links read, 'Recipes', 'Signup' and 'Login'.
- **Sign In** to the database.
- Observe changes in navbar links once user is signed in.
- Verify navbar links read, 'Recipes', 'Add Recipe', 'Profile', and, 'Logout' while user is logged in.
- **Log Out** of the application.
- Verify navbar links return to original state (Recipes', 'Signup' and 'Login') once user is logged out.
- Declare test, 'passed'.