<h2>Login Page</h2>


Sr. No.|	Functional Test Cases|	Type- Negative/ Positive Test Case
---|---|---|
1|	Verify if a user will be able to login with a valid username and valid password.|	Positive
2|	Verify if a user cannot login with a valid username and an invalid password.|	Negative
3|	Verify the login page for both, when the field is blank and Submit button is clicked.|	Negative
4|	Verify the messages for invalid login.|	Positive
5|	Verify if the data in password field is either visible as asterisk or bullet signs.|	Positive
6|	Verify if a user is able to login with a new password only after he/she has changed the password.|	Positive
7|	Verify if the login page allows to log in simultaneously with different credentials in a different browser.|	Positive
8|	Verify if the ‘Login’ key of the keyboard is working correctly on the login page.|	Positive
|Other Test Cases
9|	Verify the time taken to log in with a valid username and password.|	Performance & Positive Testing
10|	Verify if the font, text color, and color coding of the Login page is as per the standard.|	UI Testing & Positive Testing
11|	Verify if there is a ‘Cancel’ button available to erase the entered text.|	Usability Testing
12|	Verify the login page and all its controls in different browsers.|	Browser Compatibility & Positive Testing.
13| Verify the user cannot sign up again when he is already signed up.|Negative



Sr. No.	|Non-functional Security test cases|	Type- Negative/ Positive Test Case
---|---|---|
1	|Verify if a user cannot enter the characters more than the specified range in each field (Username and Password).	|Negative
2	|Verify if a user cannot enter the characters more than the specified range in each field (Username and Password).|	Positive
3	|Verify the login page by pressing ‘Back button’ of the browser. It should not allow you to enter into the system once you log out.|	Negative
4	|Verify if a user should not be allowed to log in with different credentials from the same browser at the same time.|	Negative
5	|Verify if a user should be able to login with the same credentials in different browsers at the same time.	|Positive
6	|Verify the Login page against SQL injection attack.|	Negative

<h2>Home Page</h2>


Sr.No. | Functional Test cases |Type-Negative/Positive Test Case
---|---|---|
1  |Verify if all of the  buttons like Seasons and responsibilities are clickable. |Positive
2  |Verify that Navigations are working.  |Positive
3  |Verify that Scroll bar is working.  |Positive
4  |verify that Navigation bar is working. |Positive

<h2>Specific Season Page</h2>


Sr.No.  |Functional Test cases |Type-Negative/Positive Test Case
---|---|---|
1  |verify that Banners scrollbar is working.|Positive
2  |verify that all the banners are clickable.|Positive

<h2>Specific Banner Page</h2>


Sr.No.  |Functional Test cases |Type-Negative/Positive Test Case
---|---|---|
1  |Verify that 'Edit info' option is asking Admin Credentials to access it.|Positive
2  |verify that 'Edit info' option should successfully login the admin.|Positive
3  |Verify if a admin cannot login with a invalid username or password.|	Negative
4|  verify that admin can able to edit all the banner informantion.|Positive
5|verify that 'delete banner' button is asking for admin credentials.|positive
6|verify that 'delete banner' button should automatically pop up the message to ensure activity.|positive
7|Ensure that 'used the banner' button is clickable and it tracks the infomation properly.|positive
