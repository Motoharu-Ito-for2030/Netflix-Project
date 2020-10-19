#!C:\Users\sketd\anaconda3\python.exe
import model
import cgi
import cgitb  # useful to debug

print("Content-Type: text/html\n")    # HTML is following
cgitb.enable()  # in case of error, error detail displayed

#CGI and FieldStorage
#Form data from FieldStorage

form = cgi.FieldStorage()
email = form.getvalue('email')

response = model.check_db(email)

if response == "success" :
  print('<script>window.location.replace("http://localhost/netflix_project/login.py");</script>')
else:
  print('<script>window.location.replace("http://localhost/netflix_project/signup.py");</script>')
