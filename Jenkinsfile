pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''chmod +x setup.sh
                      ./setup.sh
                      pip install -r requirements.txt
                      pyinstaller --onefile mlLevel.py'''
            }
        }

        stage('Check') {
            steps {
                sh 'ls -lah'
            }
        }
    }
}