import connection as con

def insert_user(name, email, password, con_password):
  conn = con.mysql_connect()
  cursor = conn.cursor()

  if ("@" in email):
    if (password == con_password):
      mySql_insert_query = """INSERT INTO nf_users (name, email, password) VALUES ( '"""+name+"""', '""" + \
          email+"""', '"""+password+"""')"""

      
    
      try:
        cursor.execute(mySql_insert_query)
        conn.commit()

        get_id = """
        SELECT id FROM nf_users
        WHERE email = '"""+email+"""'

        """
        cursor.execute(get_id)
        id = cursor.fetchall()
        return id
      except Exception as e:
        print('<script>window.alert("Your email has an account and jump to LOGIN page");</script>')
        print('<script>window.location.replace("http://localhost/netflix_project/login.py");</script>')
        print(e)
        conn.rollback()
        return "failed"
      conn.close()
    else:
      print('<script>window.alert("Please type in password properly");</script>')
      print('<script>window.location.replace("http://localhost/netflix_project/signup.py");</script>')
    return
  else: 
    print('<script>window.alert("Please type in proper email address");</script>')
    return

def sign_in(email, password):
  conn = con.mysql_connect()
  cursor = conn.cursor()

  fetch_user = """
  SELECT * FROM nf_users;
  """
  cursor.execute(fetch_user)
  result = cursor.fetchall()
  for r in result:
    if (r[2] == email):
      if(r[3] == password):
        id = r[0]
        return id
    else:
      continue
      

def check_db(email):
  conn = con.mysql_connect()
  cursor = conn.cursor()

  fetch_user = """
  SELECT * FROM nf_users;
  """
  cursor.execute(fetch_user)
  result = cursor.fetchall()
  for r in result:
    if (r[2] == email):
      return  "success"
    else:
      continue


def insert_movies(name, link, description, category_id, image_path):
  conn = con.mysql_connect()
  cursor = conn.cursor()

  mySql_insert_query = """INSERT INTO nf_movies (name, link, description, category_id, image_path) VALUES ( '"""+name+"""', '""" + \
      link+"""', '"""+description+"""','"""+category_id+ \
      """','"""+image_path+"""')"""

  try:
    cursor.execute(mySql_insert_query)
    conn.commit()
    return "success"
  except Exception as e:
    print(e)
    conn.rollback()
    return "failed"
  conn.close()


BASE_URL = "http://localhost/netflix_project/"
BASE_IMG = "http://localhost/netflix_project/images/"

def get_movies():
  conn = con.mysql_connect()
  cursor = conn.cursor()

  fetch_user = """
  SELECT * FROM nf_movies;
  """
  cursor.execute(fetch_user)
  result = cursor.fetchall()
  return result


def get_users():
  conn = con.mysql_connect()
  cursor = conn.cursor()

  fetch_user = """
  SELECT * FROM nf_users;
  """
  cursor.execute(fetch_user)
  result = cursor.fetchall()
  return result

