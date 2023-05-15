import com.amazonaws.services.secretsmanager.AWSSecretsManagerClientBuilder
import com.amazonaws.services.secretsmanager.model.GetSecretValueRequest

pipeline{
    agent any
    parameters{
        string(name: 'bucketname', defaultValue: 'bucket name', description: 'bucket name')
        string(name: 'hostname', defaultValue: 'host name', description: 'host name')
    }
    stages{
        stage('Build') {
            steps {
                script{
                sh '''
                echo 'Building Flask application...'
                rm -fr *.zip
                zip -r college-$BUILD_NUMBER.zip *
                aws s3 cp college-$BUILD_NUMBER.zip s3://${bucketname}/
                scp dependencies.sh ec2-user@${hostname}:/home/ec2-user/
                rm -fr *
                echo 'Flask application built successfully!'
                '''
                }
            }
        }
        stage('Deploy') {
            steps {
                script{
                sh '''
                echo 'Deploying Flask application...'
                ssh ec2-user@${hostname} "cd /home/ec2-user/ && sudo rm -rf *"
                aws s3 cp s3://${bucketname}/college-${BUILD_NUMBER}.zip .
                scp college-${BUILD_NUMBER}.zip ec2-user@${hostname}:/home/ec2-user/
                ssh ec2-user@${hostname} "cd /home/ec2-user/ && unzip college-${BUILD_NUMBER}A.zip"
                ssh ec2-user@${hostname} "cd /home/ec2-user/ && sudo rm -rf *.zip"
                rm -fr *.zip
                echo 'Flask application deployed successfully!'
                '''
                }
            }
        }
        stage('Installation'){
            steps{
                script{
                sh '''
                echo 'installing the dependencies...'
                ssh ec2-user@${hostname} "sh dependencies.sh"
                echo 'installed successfully'
                '''
                }
            }
        }
        stage('Retrieve Database Credentials and Run') {
            steps {
                script {
                    // retrieve secrets from AWS Secrets Manager and store them as environment variables
                    def secrets_client = AWSSecretsManagerClientBuilder.standard().build().createSecretsManager()
                    def response = secrets_client.getSecretValue(new GetSecretValueRequest().withSecretId("arn:aws:secretsmanager:ap-south-1:419740680543:secret:dummydatabase-MXL2Xu"))
                    def secret_string = response.getSecretString()
                    def secret_dict = new groovy.json.JsonSlurper().parseText(secret_string)
                    withEnv(['DB_USERNAME=${secret_dict.username}', 'DB_PASSWORD=${secret_dict.password}', "DB_HOST=${secret_dict.host}", "DB_NAME=${secret_dict.dbname}", "DB_TABLE=${secret_dict.table}"]) {
                        // call your application code here
                        sh '''
                        echo 'running the flask application'
                        ssh ec2-user@${hostname} "sudo gunicorn app:app -b 0.0.0.0:80 -D"
                        echo 'completed successfully'
                        '''
                    }
                }
            }
        }
    }
}
    

