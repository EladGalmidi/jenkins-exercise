pipeline{
    agent any

    stages
{
        stage('Build') {
            steps {
                echo '=== build stage ===='
            }
        }
        stage('Test') {
            steps {
                echo '=== test stage ===='
            }
        }
        stage('Deploy') {
            steps {
                echo '=== deploy stage ===='
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
    }
}