pipeline {
    agent any

    parameters {
        string(name: 'onefile', defaultValue: 'mlLevel', description: 'What to build, without extension')
    }

    stages {
        stage('Build') {
            steps {
                sh '''chmod +x setup.sh
                      ./setup.sh
                      pip install -r requirements.txt
                      pyinstaller --onefile ${params.onefile}.py'''
            }
        }

        stage('Check') {
            steps {
                sh 'ls -lah'
            }
        }
    }
}