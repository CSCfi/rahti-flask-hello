'''
  Simple Flask app
'''
import json

from pathlib import Path
import flask

# EDIT THE FOLLOWING LINE
STUDENT = "????????"

# Templates
# In a proper Flask application all these templates should be in idepent files
STYLE = """
body {
  background-color: #f5f5f5;
  font-family: "Helvetica Neue",Helvetica,"Liberation Sans",Arial,sans-serif;
  font-size: 14px;
  padding: 10%;
}
"""

PAGE = """

<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width" />

    <title>""" + STUDENT + """</title>
    <style>""" + STYLE + """</style>
  </head>
  <body>
  <h1>Hello """ + STUDENT + """!</h1>
  <p>See the <a href='/kitten'>kittens</a></p>
  </body>
</html>"""



# Default configuration
config = {
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
    print('Configuration:')
    print(json.dumps(config))

    app.run(debug=config["debug"],
            port=8080,
            host='0.0.0.0')

if __name__ == "__main__":
    main()
