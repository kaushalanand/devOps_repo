pipeline {
    agent any

    tools {
        nodejs 'NodeJs_20'
    }

    environment {
        // Force a local cache to avoid permission issues in system folders
        npm_config_cache = 'npm-cache'
        PATH = "${env.PATH}:/usr/local/bin"
    }

    stages {
        stage("Fix Permissions") {
            steps {
                // creates a local cache directory so we don't need root access
                sh 'mkdir -p npm-cache' 
            }
        }

        stage("Install Dependencies") {
            steps {
                // Clean any potential leftovers first
                sh 'rm -rf node_modules'
                
                // Use --unsafe-perm to allow npm to run scripts as the Jenkins user on Mac
                // We removed --ignore-scripts so jest-circus can install properly
                sh 'npm install --unsafe-perm --no-user-config'
            }
        }


        stage("Run Tests") {
            steps {
                sh 'CI=true npm test'
            }
        }
    }

    post {
        success {
            emailext (
                to: "hereiskaushal@gmail.com"
                subject: "SUCCESS: Job nodeJs development J1",
                body: "Build was successful! View details here: B1",
                recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']]
            )
        }
        failure {
            sh 'npm config list'
            emailext (
                // to: "${env.RECIPIENT_EMAIL}",
                to: "hereiskaushal@gmail.com"
                subject: "FAILED: Job nodeJs development J1",
                body: """<p>Build Failed. Check console output at: B1</p>
                         <p>Check the 'Install Dependencies' or 'Run Tests' stages for npm errors.</p>""",
                mimeType: 'text/html',
                recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']]
            )
        }
    }
}
