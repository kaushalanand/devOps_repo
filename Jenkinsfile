pipeline {
    agent any

    tools {
        nodejs "node-20" 
    }

    stages{
        stage("Install Dependencies") {
            steps{
                sh 'npm install'
            }
        }

        stage("Run Tests") {
            steps{
                sh 'npm test'
            }
        }
    }
}