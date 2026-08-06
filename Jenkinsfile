pipeline {
    agent any

    stages {
        stage('Check Environment') {
            steps {
                sh '''
                    export PATH="/var/lib/jenkins/.local/bin:$PATH"
                    whoami
                    pwd
                    python3 --version
                    pip3 --version
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
