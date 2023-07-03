# FLASK API - USER MANAGEMENT

___
Restful API for basic user management such as signing up users, signing in, resetting user passwords amongst other operations.


# API Design

GET  
`/allusers`  
Lookup the details of all users registered onto the platform.

POST  
`/users`  
Sign up users onto the platform using a username, unique email and password.


POST  
`/login`  
Allow the users to sign in to their accounts using their email and password. Appropriate responses are returned for failures and successes.


POST  
`/resetpassword`  
Allow existing users who have forgotten their passwords to reset their passwords and login afterwards.


# Meta

___

**Requirements**

python version >= 3.9.0