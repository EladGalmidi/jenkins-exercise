pipeline {
    agent any

    environment {
        APP_NAME = 'wallak applications'

        APP_VERSION = '1.0'

        DOCKER_REPO = 'eladgalmidi/'

        FILE_TO_TEST = './build-info.txt'
    }

    stages {
        stage('Build') {
            steps {
                echo '=== build stage ===='

                sh 'echo he need some milk >> app.txt'

                sh "echo 'welcome to the pipeline of application ${APP_NAME} we are in version ${APP_VERSION}'"

                sh '''
                    echo "application name: $APP_NAME" >> $FILE_TO_TEST
                    echo "$BUILD_NUMBER" >> $FILE_TO_TEST
                    date >> $FILE_TO_TEST
                '''
            sh 'ls'
            sh 'cat $FILE_TO_TEST'
            }
        }

        stage('Test') {
            steps {
                echo '=== test stage ===='

                sh 'test -f app.txt'

                echo "for any details please visit: ${JOB_URL}. for build #${BUILD_NUMBER}"
            }
            parallel{
                stage("file test"){
                    steps{
                        sh '''
                            if [ -f app.txt ] then;
                                echo app exists
                            else
                                echo ERROR: app.txt does not exist
                                exit 1
                            fi
                        '''
                        }
                }
                stage("build into test"){
                    steps{
                        sh 'python3 test.py wallak'
                    }
                }
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