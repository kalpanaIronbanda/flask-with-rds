from flask import Flask, render_template
import os
import mysql.connector

app = Flask(__name__)

db_username = os.environ.get('DB_USERNAME')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_name = os.environ.get('DB_NAME')
db_table = os.environ.get('DB_TABLE')

@app.route('/')
def index():
    cnx = mysql.connector.connect(user=db_username, password=db_password,
                                   host=db_host,
                                   database=db_name)
    cursor = cnx.cursor()
    query = "SELECT * FROM {db_table}"
    cursor.execute(query)
    rows = cursor.fetchall()
    cnx.close()
    return render_template('html file name', rows=rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)
