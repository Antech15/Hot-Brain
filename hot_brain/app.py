from flask import Flask,render_template,request
from flask_json import FlaskJSON, JsonError, json_response, as_json
import jwt

import datetime
import bcrypt


#from db_con import get_db_instance, get_db

app = Flask(__name__, static_url_path="/static")
FlaskJSON(app)

#global_db_con = get_db()

@app.route('/') #endpoint
def index():
    return render_template('index.html')

app.run(host='0.0.0.0', port=80)

if __name__ == "__main__":
    app.run(debug=True)