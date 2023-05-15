'''
  Simple Flask app
'''
import json
import os
from pathlib import Path
import flask

# Templates
# In a proper Flask application all these templates should be in indepent files
STYLE = """
body {
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
    <h1>This is the photo gallery from {{ student }}</h1>
    <ul>{% for kitten in kittens %}
      <li><img src='{{ kitten }}'/> {{ kitten }}</li>
    {% endfor %}</ul>
  </body>
</html>
"""

# Default configuration
defaults = {
    "student": "??????",
    "debug": False}

config = {}

# Flask app object
app = flask.Flask(__name__,
                  static_url_path='/static',
                  static_folder='/static')

# Routes
# Routes are used to bind a python function to a url. 
# Here we tell that when someone tries to access "localhost:5000/", i.e nothing after /, we have to run home() function
@app.route("/", methods=['GET'])
def home():
    '''
      Hello page, shows photos in the /static folder
    '''
    kittens = Path('/static/').rglob('*.jpg') 
    # render_template function is used to render or display a webpage. 
    # Here, we used render_template_string which  renders from a string that is passed in rather than from a file in the templates folder.
    return flask.render_template_string(
        PAGE,
        student=config["student"],
        kittens=kittens)

# Entry function
def main():
    '''
      Main entry function
    '''

    # Load student name from file
    global config
    try:
        with open('/etc/flask/config.json') as custom_config_file:
            config = json.load(custom_config_file)
    except FileNotFoundError:
        config = defaults

    try:
        if os.environ['DEBUG']:
            config["debug"] = True
    except KeyError:
        pass

    print('Configuration:')
    print(json.dumps(config))

    app.run(debug=config["debug"],
            port=8080,
            host='0.0.0.0')

if __name__ == "__main__":
    main()
