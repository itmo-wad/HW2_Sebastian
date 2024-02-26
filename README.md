# Description Basic part
This project implements basic authentication functionality using Flask and MongoDB. The components of this implementation are described below:

Listening on Localhost:5000: The application runs on the local server and listens for requests on port 5000, 
allowing access through the URL http://localhost:5000/.

Authentication Form: An authentication form is presented in the root path (/).
Users can enter their username and password to attempt to log in.

Redirect to Profile Page: If a user successfully authenticates with valid credentials and they are verified against the database,
the user is redirected to their personalized profile page.

Profile Page for Authenticated Users: The profile page is only accessible to users who are successfully logged in.
This page is located in the /profile path.

Secure Credential Storage: Usernames and passwords are stored securely in MongoDB.



In addition to the basic authentication functionality, the following additional improvements have been implemented

Logout Button: A “Logout” button has been added to the top right corner of the profile page, allowing users to log out easily and securely. 
Clicking this button logs the user out and redirects them to the login page, ensuring that access to the profile page is restricted to authenticated users.

Error Messages for Failed Authentication, added the display of error messages when the authentication process fails due to incorrect username or password.

Session Expiration Time Configuration, The user session expiration time has been configured to 2 minutes to increase security. 
This means that if there is no activity for 2 minutes, the user's session will automatically expire, requiring a new login to access the profile page.

# Implementation
Detailed implementation of these features includes configuring routes in Flask to handle login requests,
credential verification against the MongoDB database, and session management to maintain user authentication status.

# Technologies used
-HTML -CSS -Python -MongoDB 

# Author
Sebastian Guevara
