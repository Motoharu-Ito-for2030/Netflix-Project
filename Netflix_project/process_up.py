#!C:\Users\sketd\anaconda3\python.exe
import model
import cgi
import cgitb  # useful to debug
import os
print("Content-Type: text/html\n")    # HTML is following
cgitb.enable()  # in case of error, error detail displayed

#CGI and FieldStorage
#Form data from FieldStorage

form = cgi.FieldStorage()
name = form.getvalue('name')
email = form.getvalue('email')
password = form.getvalue('password')
con_password = form.getvalue('confirm_password')

id = model.insert_user(name, email, password, con_password)


if (id):
  id = id[0][0]
  print('<script>window.location.replace("http://localhost/netflix_project/movielist.py?id='+str(id)+'");</script>')
else:
  print('data not inserted')
