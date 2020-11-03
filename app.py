'''
  Simple Flask app
'''
import json
from pathlib import Path
import flask

# Templates
# In a proper Flask application all these templates should be in idepent files
STYLE = """
body {
  # CHANGE background color from 'silver' to 'beige'
  background-color: silver;
  font-family: "Helvetica Neue",Helvetica,"Liberation Sans",Arial,sans-serif;
  font-size: 14px;
  padding: 10%;
}
img {
  width: 90%;
}
"""

PAGE = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width" />
    <title>{{ student }}</title>
    <style>""" + STYLE + """</style>
  </head>
  <body>
  <h1>Hello {{student}}!</h1>
  <p>See the <a href='/kitten'>kittens</a></p>
  </body>
</html>
"""

KITTEN_PAGE = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width" />
    <title>{{ student }}</title>
    <style>""" + STYLE + """</style>
  </head>
  <body>
    <h1>This is the kitten page from {{ student }}</h1>
    <ul>{% for kitten in kittens %}
      <li><img src='{{ kitten }}'/> {{ kitten }}</li>
    {% endfor %}</ul>
  </body>
</html>
"""

# Default configuration
config = {
    "student": "??????",
    "debug": False}

# Flask app object
app = flask.Flask(__name__,
                  static_url_path='/static',
                  static_folder='/static')

# Routes
@app.route("/", methods=['GET'])
def home():
    '''
      Hello page
    '''
    return flask.render_template_string(
        PAGE)

@app.route("/kitten", methods=['GET'])
def kitten():
    '''
      Displays all JPG files in /static, if any
    '''
    kittens = Path('/static/').rglob('*.jpg')
    return flask.render_template_string(
        KITTEN_PAGE,
        kittens=kittens)

# Entry function
def main():
    '''
      Main entry function
    '''

    # Change debug if env DEBUG exists

    # Load student name from file

    print('Configuration:')
    print(json.dumps(config))

    app.run(debug=config["debug"],
            port=8080,
            host='0.0.0.0')

if __name__ == "__main__":
    main()
