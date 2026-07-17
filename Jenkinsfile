pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Check poetry version'
                sh 'poetry --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}

