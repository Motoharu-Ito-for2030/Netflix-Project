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
email = form.getvalue('email')
password = form.getvalue('password')

id = model.sign_in(email, password)

if (id):
  print('<script>window.location.replace("http://localhost/netflix_project/movielist.py?id='+str(id)+'");</script>')
else:
  print('<script>window.alert("did NOT login");</script>')
  print('<script>window.location.replace("http://localhost/netflix_project/login.py ");</script>')
