pipeline {
    agent any

    parameters {
        string(name: 'onefile', defaultValue: 'mlLevel', description: 'What to build, without extension')
    }

    stages {
        stage('Build') {
            steps {
                sh '''
                      python -m venv .venv
                      . .venv/bin/activate
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