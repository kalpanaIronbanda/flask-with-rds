from flask import Flask, render_template
import mysql.connector
import boto3
import json

app = Flask(__name__)

def get_secret():
    # Create a Secrets Manager client
    client = boto3.client('secretsmanager')
    secret_name = "your-secret-name" # replace with your own secret name
    response = client.get_secret_value(SecretId=secret_name)
    secret_value = response['SecretString']
    return json.loads(secret_value)

@app.route('/')
def index():
    # Retrieve the database credentials from Secrets Manager
    secret = get_secret()
    username = secret['username']
    password = secret['password']
    
    # Connect to the database
    cnx = mysql.connector.connect(user=username, password=password,
                                   host='collage.ct3ipxrkwhfs.ap-south-1.rds.amazonaws.com',
                                   database='collage')
    cursor = cnx.cursor()
    
    # Execute the SQL query
    query = "SELECT * FROM studentlist"
    cursor.execute(query)
    rows = cursor.fetchall()
    
    # Close the database connection
    cnx.close()
    
    # Render the template with the query results
    return render_template('table.html', rows=rows)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
