pipeline{
    agent any

    parameters{
        string(name: 'BUILD_NUMBER', defaultValue: '3', description: 'Build Number')
        string(name: 'bucketname', defaultValue: 'bucket name', description: 'bucket name')
        string(name: 'hostname', defaultValue: 'host name', description: 'host name')
    }

    stages{
        stage('Build') {
            steps {
                scripts{
                    sh '''
                echo 'Building Flask application...'
                rm -fr *.zip
                zip -r college-$BUILD_NUMBER.zip *
                aws s3 cp college-$BUILD_NUMBER.zip s3://${bucketname}/
                scp dependencies.sh ec2-user@172.31.7.208:/home/ec2-user/
                rm -fr *
                echo 'Flask application built successfully!'
                '''
                }
            }
        }
    }

        stage('Deploy') {
            steps {
                scripts{
                sh '''
                echo 'Deploying Flask application...'
                ssh ec2-user@${hostname} "cd /home/ec2-user/ && sudo rm -rf *"
                aws s3 cp s3://${bucketname}/college-3.zip .
                scp college-3.zip ec2-user@${hostname}:/home/ec2-user/
                ssh ec2-user@${hostname} "cd /home/ec2-user/ && unzip college-3.zip"
                ssh ec2-user@${hostname} "cd /home/ec2-user/ && sudo rm -rf *.zip"
                rm -fr *.zip
                echo 'Flask application deployed successfully!'
                '''
                }
            }
        }
        stage('Installation'){
            steps{
                scripts{
                sh '''
                echo 'installing the dependencies...'
                ssh ec2-user@${hostname} "sh dependencies.sh"
                echo 'installed successfully'
                '''
                }
            }
        }
        stage('Run'){
            steps{
                scripts{
                sh '''
                echo 'running the flask application'
                ssh ec2-user@${hostname} "python3 app.py"
                echo 'completed successfully'
                '''
                }
            }
        }
    }

