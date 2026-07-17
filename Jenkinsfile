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
        stage('Activate the virtual environment') {
            steps {
                echo 'Activating virtual environment...'
                sh 'poetry show'
                sh 'poetry run python -m fastapi dev src/main.py'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}

