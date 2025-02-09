pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''./setup.sh
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