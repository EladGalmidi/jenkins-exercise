pipeline{
    agent any
    environment {
        APP_NAME = 'wallak applications'
        APP_VERSION = '1.0'
        DOCKER_REPO = 'eladgalmidi/'
    }
    stages
{
        stage('Build') {
            steps {
                echo '=== build stage ===='
                sh 'echo he need some milk >> app.txt'
                sh "echo 'welcome to the pipeline of application ${APP_NAME} we are in version ${APP_VERSION}'"}
        }
        stage('Test') {
            steps {
                echo '=== test stage ===='
                sh 'test -f app.txt'
                echo "for any details please visit: ${JOB_URL}. for build #${BUILD_NUMBER}"
            }
        }
        stage('Deploy') {
            steps {
                echo '=== deploy stage ===='            
                sh 'mkdir deploy'
                sh 'cp app.txt deploy/'
                sh 'ls deploy'
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}