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

// pipeline {
//     agent any

//     stages {
//         stage('Run FastAPI Application') {
//             steps {
//                 withCredentials([file(credentialsId: 'dotenv', variable: 'ENV_FILE')]) {
//                     sh '''
//                         if [ -f /var/lib/jenkins/workspace/Project-Pipeline/.env ]; then
//                             rm -f /var/lib/jenkins/workspace/Project-Pipeline/.env
//                         fi
//                         cp "$ENV_FILE" .env
//                         poetry run fastapi dev src/main.py
//                     '''
//                 }
//             }
//         }
//     }
// }
