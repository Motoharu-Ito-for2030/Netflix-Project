#!C:\Users\sketd\anaconda3\python.exe
import view
import cgi
import cgitb
print("Content-type:text/html\r\n")

cgitb.enable()

arguments = cgi.FieldStorage()

id = arguments.getvalue("id")

print(view.html_head() + view.html_movielist(id) + view.html_footer())
