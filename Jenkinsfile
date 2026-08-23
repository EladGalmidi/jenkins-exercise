pipeline{
    agent any

    stages
{
        stage('Build') {
            steps {
                echo '=== build stage ===='
                sh 'echo he need some milk >> app.txt'
            }
        }
        stage('Test') {
            steps {
                echo '=== test stage ===='
                sh 'test -f app.txt'
            }
        }
        stage('Deploy') {
            steps {
                echo '=== deploy stage ===='
                sh 'mkdir depolo'
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