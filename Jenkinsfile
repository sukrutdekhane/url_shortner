// pipeline {
//     agent any

//     stages {
//         stage('Build') {
//             steps {
//                 echo 'Check poetry version'
//                 sh 'poetry --version'
//                 sh 'python3 --version'
//             }
//         }
//         stage('Activate the virtual environment') {
//             steps {
//                 echo 'Activating virtual environment...'
//                 sh 'poetry show'
//                 sh 'poetry run python -m fastapi dev src/main.py'
//             }
//         }
//         stage('Deploy') {
//             steps {
//                 echo 'Deploying....'
//             }
//         }
//     }
// }

pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull code from your repository
                checkout scm
            }
        }

        stage('Run FastAPI Application') {
            steps {
                // Run the server in the background so Jenkins doesn't hang indefinitely
                sh '''
                poetry install --no-root
                poetry run python -m fastapi dev src/main.py
                '''
            }
        }
    }
}
