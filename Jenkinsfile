pipeline {
    agent any

    environment {
        AWS_REGION = "us-east-1"
        S3_BUCKET  = "parameswar.online"
    }

    stages {

        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/parameswar-patra/Amazon_s3_static_website_hosting.git'
            }
        }

        stage('Deploy to S3') {
            steps {
                sh '''
                    aws s3 sync . s3://$S3_BUCKET \
                    --region $AWS_REGION \
                    --delete \
                    --exclude ".git" \
                    --exclude "Jenkinsfile" \
                    --exclude "README.md" \
                    --exclude "lambda_cloudfront.py" \
                    --exclude "install_git_java_jenkins.sh"
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline finished"
        }
        success {
            echo "Deployment successful"
        }
        failure {
            echo "Pipeline failed – check logs"
        }
    }
}