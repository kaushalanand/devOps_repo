pipeline {
    agent any

    tools {
        nodejs 'NodeJs_20'
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