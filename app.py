from flask import Flask, render_template
import mysql.connector
app = Flask(__name__)
@app.route('/')
def index():
    cnx = mysql.connector.connect(user='give username', password='give the password ',
                                   host='give the endpoint of database',
                                   database='give the name of the database')
    cursor = cnx.cursor()
    query = "SELECT * FROM <Ur-Tablename>"
    cursor.execute(query)
    rows = cursor.fetchall()
    cnx.close()
    return render_template('html file name', rows=rows)
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80,debug=True)


