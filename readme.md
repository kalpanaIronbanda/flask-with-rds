Flask Application with RDS Credentials from Secret Manager
-----------------------------------------------------------

This Flask application demonstrates how to retrieve RDS credentials from AWS Secret Manager and use them to connect to a database. 

The application fetches data from the database and returns it as a response.

Prerequisites
-------------

Before running the Flask application, make sure you have the following:

Python 3.7 or above installed

AWS account with access to AWS Secret Manager and RDS

AWS CLI configured with appropriate credentials

Jenkins server configured with necessary plugins

Installation
------------

Clone the repository or download the source code.
        git clone https://github.com/kalpanaIronbanda/python-flask.git

Navigate to the project directory.
        cd python-flask

It is recommended to use a virtual environment to isolate project dependencies. Create and activate a virtual environment.

        python3 -m venv venv
        source venv/bin/activate

Install the required dependencies using pip.

        sh dependencies.sh

Configuration
--------------

Create an mysql Database in the RDS.

you can take reference of document 

Create an AWS Secret Manager secret with the RDS credentials. Make sure to note down the secret name.

you can take referance of document how to store credentials in the secret manager

Update the AWS region and the secret name in the code.


Running the Application
------------------------

Start the Flask application by running the app.py file.

        python app.py
The application will start running on http://localhost:5000.

Till now we have to do manually.

Now let's use jenkins pipeline

Jenkins Pipeline
----------------

Ensure that Jenkins server is set up and running with the necessary plugins installed.

Create a new Jenkins pipeline job.

In the pipeline configuration, configure the following:

Set the pipeline script from SCM.

Provide the repository URL https://github.com/kalpanaIronbanda/python-flask.git .

Specify the Jenkinsfile path within the repository (e.g., Jenkinsfile).

Save the pipeline configuration and trigger the pipeline job.

Jenkins will fetch the code, install dependencies, and run the Flask application in a build environment.


Endpoints
----------

/

Method: GET

Description: Returns the data from the database as a response.