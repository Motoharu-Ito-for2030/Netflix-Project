This is the readme.md To run this project 

Step 1: Create a database in your SQL server named 'netflix_project'

Step 2: In the database, run the SQL file named 'connection.py' provided to you

Step 3: Have a local MySQL Database running

Step 4: In the terminal run: python3 view.py

Step 5: Display HOME page of NETFLIX on screen and you can input email address
  like "Unlimited movies, TV shows and more"

Step 6: If the email informed in step 5 is already uploaded to the database, jump to LOGIN page.
If not, jump to SIGNUP page and you create a new account.

Step 7: As soon as you input the data in SIGNUP page, named 'process_up.py' get the data and insert to the database   with insert_user function from named 'model.py'
or 
as soon as you input the data in LOGIN page, named 'process_in.py' get the data and check if it is in the DB or not.


After LOGIN or SIUNUP page, jump to MOVIELIST page for each user.

Step 8: There are many movies or anime. When you click them, you can jump to each movie detail.

Step 9: You go back and click the humberger button, then will shown your username and SIGNOUT button.

Step10: When you click the SIGNOUT button, you jump to the first HOME page.