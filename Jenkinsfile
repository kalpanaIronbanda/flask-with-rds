pipeline {
    agent any

    parameters {
        string(name: 'BUILD_NUMBER', defaultValue: '1', description: 'Build Number')
    }

    stages {
        stage('Build') {
            steps {
                echo 'Building Flask application...'
                sh 'rm -fr *.zip'
                sh 'zip -r college-$BUILD_NUMBER.zip *'
                sh 'aws s3 cp college-$BUILD_NUMBER.zip s3://python-flask-application/'
                sh 'scp dependencies.sh ec2-user@172.31.7.208:/home/ec2-user/'
                sh 'rm -fr *'
                echo 'Flask application built successfully!'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying Flask application...'
                sh 'ssh ec2-user@172.31.7.208 "cd /home/ec2-user/ && sudo rm -rf *"'
                sh 'aws s3 cp s3://python-flask-application/college-3.zip .'
                sh 'scp college-3.zip ec2-user@172.31.7.208:/home/ec2-user/'
                sh 'ssh ec2-user@172.31.7.208 "cd /home/ec2-user/ && unzip college-3.zip && sh dependencies.sh"'
                sh 'ssh ec2-user@172.31.7.208 "cd /home/ec2-user/ && sudo rm -rf *.zip"'
                sh 'rm -fr *.zip'
                echo 'Flask application deployed successfully!'
            }
        }
    }
}
