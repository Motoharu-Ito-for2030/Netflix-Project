import model
def html_head():
  html ="""
  <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Sample Netflix</title>
  <link rel="stylesheet" href="styles.css">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<body>
  """
  return html
def html_body():
  html = """
  <div class="home content">
    <header>
      <a href="index.py"><img src="images/netflix-logo.png" class="logo"></a>
      <a href="login.py"><button>Sign in</button></a>
    </header>
    <main>
      <h1>Unlimited movies, TV<br>shows and more.</h1>
      <p>watch anywhere. Cancel anytime.</p>
      <form action="process_check.py" method="post">
        <p>Ready to watch? Enter your email to create or restart your membership.</p>
        <input type="text" placeholder="Email address" name="email">
        <button>GET STARTED</button>
      </form>
    </main>
  </div>
  """
  return html
def html_footer():
  html = """
  </body>
  </html>
  """
  return html

def html_login():
  html = """
  <div class="content login">
    <header>
      <a href="index.py"><img src="images/netflix-logo.png" class="logo"></a>
    </header>
    <main>
      <form action="process_in.py" method="post">
        <h1>Sign In</h1>
        <input type="text" placeholder="Email" name="email">
        <input type="text" placeholder="Password" name="password">
        <button>Sign In</button>    
      </form>
    </main>
  </div>
  """
  return html

def html_signup():
  html = """
  <div class="content login">
    <header>
      <a href="index.py"><img src="images/netflix-logo.png" class="logo"></a>
    </header>
    <main>
      <form action="process_up.py" method="post">
        <h1>Sign Up</h1>
        <input type="text" placeholder="name" name="name">
        <input type="text" placeholder="Email" name="email">
        <input type="text" placeholder="Password" name="password">        
        <input type="text" placeholder="Confirm Password" name="confirm_password">
        <button type="submit">Sign Up</button>
      </form>
    </main>
  </div>
  """
  return html

def html_movielist(id):
  user = model.get_users()
  movies = model.get_movies()
  html = """
  <div class="list content">
    <header>
        <div id="humberger">
          <div></div>
          <div></div>
          <div></div>
        </div>
      </a>
      <img src="images/netflix-logo.png" class="logo"/>
    </header>
  """
  for u in user:
    if(u[0] == int(id)):
      html += """
          <div class="balloon">
            <p>Hi!  """+str(u[1])+""" !</p>
          </div>
          <div id="user">
            <img src="images/user_image.png"/>
            <h1>UserName: """+str(u[1])+"""</h1>
            <a href="index.py"><button>Sign Out</button></a>
          </div>
        <main>
          <h1>Manga</h1>
          <div class="movies genre">
      """
  for m in movies:
    if(m[4] == 1):
      html += """
        <a href="moviedetail.py?id="""+str(m[0])+""""><img src=" """+str(m[5])+""" "></a>
      """
  html += """
      </div>
      <h1>Avengers</h1>
      <div class="drama genre">
  """
  for m in movies:
      if(m[4] == 2):
        html += """
          <a href="moviedetail.py?id="""+str(m[0])+""""><img src=" """+str(m[5])+""" "></a>
        """
  html += """
      </div>
      <h1>Favorite</h1>
      <div class="trend genre">
  """
  for m in movies:
      if(m[4] == 3):
        html += """
          <a href="moviedetail.py?id="""+str(m[0])+""""><img src=" """+str(m[5])+""" "></a>
        """
  html += """
        
      </div>   
    </main>
    <script src="main.js"></script>
  </div>
  """
  return html

def html_moviedetail(id):
  movies = model.get_movies()
  html = """
  <div class="detail content">
    <header>
      <a href="movielist.py"><img src="images/netflix-logo.png" class="logo"></a>
    </header>
    <main>
  """
  for m in movies:
    if(m[0] == int(id)):
      html += """
          <img src=" """+str(m[5])+""" ">
          <h1>"""+str(m[1])+"""</h1>
          <p>"""+str(m[3])+"""</p>
          <button>Play</button>
        </main>
      </div>
      """
  return html


