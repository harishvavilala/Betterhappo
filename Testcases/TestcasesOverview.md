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

<h2>Events Page</h2>


Sr.No. | Functional Test cases |Type-Negative/Positive Test Case
---|---|---|
1  |Verify if all of the  buttons like Seasons and responsibilities are clickable. |Positive
2  |Verify that Navigations are working.  |Positive
3  |Verify that Scroll bar is working.  |Positive
4  |Verify that Navigation bar is working. |Positive

<h2>Home Page</h2>


Sr.No. | Functional Test cases |Type-Negative/Positive Test Case
---|---|---|
1|Verify that the scroll bar are working|Positive
2|Verify that the churches are clickable and it navigates to their respective events page quickly.|Performance and Positive 
3| Verify if the font, text color, and color coding of the Home page is as per the standard.|UI Testing & Positive Testing

<h2>Specific Season Page</h2>


Sr.No.  |Functional Test cases |Type-Negative/Positive Test Case
---|---|---|
1  |Verify that Banners scrollbar is working.|Positive
2  |Verify that all the banners are clickable.|Positive

<h2>Specific Banner Page</h2>


Sr.No.  |Functional Test cases |Type-Negative/Positive Test Case
---|---|---|
1  |Verify that 'Edit info' option is asking Admin Credentials to access it.|Positive
2  |Verify that 'Edit info' option should successfully login the admin.|Positive
3  |Verify if a admin cannot login with a invalid username or password.|	Negative
4|  Verify that admin can able to edit all the banner informantion.|Positive
5|Verify that 'delete banner' button is asking for admin credentials.|positive
6|Verify that 'delete banner' button should automatically pop up the message to ensure activity.|positive
7|Ensure that 'used the banner' button is clickable and it tracks the infomation properly.|positive
8|Verify if the 'used the banner'  button is clicked it shows the last used date and time.|Positive

<h2>All Seasons Page</h2>


Sr.No.  |Functional Test cases |Type-Negative/Positive Test Case
---|---|---|
1|Verify if the banners under each season are clickable and navigates into appropriate page fastly.|Performance & Positive Testing
2|Verify if the scroll bars are working.|Browser Compatibility & Positive Testing.


<h2>Contact Information Page</h2>


Sr.No.  |Functional Test cases |Type-Negative/Positive Test Case
---|---|---|
1| Verify if the font, text color, and color coding of the Contact information page is as per the standard.|	UI Testing & Positive Testing
2| Verify that 'delete contact' button is clickable and asks for admin credentials.|Positive testing
3|Verify that 'done' and 'cancel' buttons in the admin credentails pop up dialog box are clickable and 'done' will delete the particular member and 'cancel' button will redirect back to the contact information page witlout deleting any contacts.| Usability Testing and positive testing

<h2>Add Contact Page</h2>


Sr.No.  |Functional Test cases |Type-Negative/Positive Test Case
---|---|---|
1| verify all the text boxes like name, Email id, Contact number, address are editable and respond  quickly.|  Performance & Positive Testing
2|Verify if the 'done' button navigates  quickly to the contact information page with new contact updated.|Performance & Positive Testing
3|verify if the 'cancel' button navigates quickly to the contact information without adding any contact.|Performance & Positive Testing 

<h2>Admin Page</h2>


Sr.No.  |Functional Test cases |Type-Negative/Positive Test Case
---|---|---|
1|Verify all the buttons are clickable.|Positive Testing
2|Verify if the 'Add guild member' button is clicked then it should navigate to the add guild member page quickly.|Performance & Positive Testing 
3|Verify if the 'Add Banner' button is clicked it navigates to the add banner page quickly.|Performance & Positive Testing 
4|Verify if the 'Add church' button is clicked it navigates to the add church page quickly.|Performance & Positive Testing 
5|Verify if the 'Delete church' button is clicked it navigates to the delete church page quickly.|Performance & Positive Testing 


<h2>Assigned Guild Member page</h2>


Sr.No.  |Functional Test cases |Type-Negative/Positive Test Case
---|---|---|
1|Verify if the list of the Guild members are selectable with a checkbox.|performance and positive 
2|Verify if the font, text color, and color coding of the Assigned Guild Member page is as per the standard.|	UI Testing & Positive Testing
3|Verify if the 'Select Month' is a drop down list and can select the required month| performance and positive
4|Verify if the 'Select Season' is a drop down list and can select the required month| performance and positive
5|Verify if the 'Create team' is clickable and assigns the  guildmembers to the selected season and month.|Positive testing


<h2>Add banner page</h2>


Sr.No.  |Functional Test cases |Type-Negative/Positive Test Case
---|---|---|
1|Verify that the choose file button, an window dialog box of local drive should pop up.|Performane and positive testing
2|Verify that All the details of the banners are editable text boxes which can store banner info.|Positive testing
3|Verify that 'done' and 'cancel' buttons are clickable.|Positive Testing
4|Verify that when 'done' button is clicked, a new banner should be added.|Performance and positive testing
5|Verify that when 'Cancel' button is clicked, it should navigate to the admin page without taking more time.|Usability and Positive testing

<h2>Logout</h2>


Sr.No.  |Functional Test cases |Type-Negative/Positive Test Case
---|---|---|
1|Verify that when logout button is clicked, it should navigate to the Home Page.|Performance and positive testing