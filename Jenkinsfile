pipeline {
    agent any

    stages {
        stage('Check Environment') {
            steps {
                sh '''
                    whoami
                    pwd
                    python3 --version
                    pip3 --version
                    which poetry
                    poetry --version
                '''
            }
        }
        stage('Build') {
            steps {
                echo 'Check poetry version'
                sh 'poetry --version'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
