import psycopg2
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://csdse100_render_db_user:bL3ajxMLfeF7OWTwcMgL4Hdf56oa0XXr@dpg-cj461sqip7vuasjc1jig-a/csdse100_render_db")
    conn.close()
    return "Database Connection Successful"