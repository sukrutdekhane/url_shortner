pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Check poetry version'
                sh 'poetry --version'
                sh 'python3 --version'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}
