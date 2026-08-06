pipeline {
    agent any

    environment {
        IMAGE_NAME = "sukrut123/url-shortener"
        IMAGE_TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Build') {
            steps {
                sh 'docker compose build'
            }
        }

        stage('Tag') {
            steps {
                sh """
                docker tag ${IMAGE_NAME}:latest ${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: '1a2f0705-27b9-405f-a4b6-7c733e4de058',
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )
                ]) {

                    sh '''
                    echo $DOCKER_PASS | docker login \
                        -u $DOCKER_USER \
                        --password-stdin
                    '''
                }
            }
        }

        stage('Push') {
            steps {
                sh """
                docker push ${IMAGE_NAME}:${IMAGE_TAG}
                docker push ${IMAGE_NAME}:latest
                """
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}