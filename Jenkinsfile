pipeline {
    agent any

    tools {
        nodejs "node-16" 
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