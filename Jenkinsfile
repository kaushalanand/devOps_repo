pipeline {
    agent any

    tools {
        // Ensure 'NodeJs_20' exactly matches the name in Manage Jenkins > Tools
    // On macOS, this will automatically download/install the Darwin binary
        nodejs 'NodeJs_20'
    }

    environment {
        // macOS sometimes requires explicit PATH settings for npm binaries
        PATH = "${env.PATH}:/usr/local/bin"
    }

    stages {
        stage("Environment Check") {
            steps {
                // Debug step: Useful on Mac to see which node/npm is being used
                sh 'node -v'
                sh 'npm -v'
                sh 'which npm'
            }
        }

        stage("Install Dependencies") {
            steps {
                // Use '--no-optional' to avoid common macOS compilation errors 
                // with native modules (like fsevents) during CI
                sh 'npm install --no-optional'
            }
        }

        stage("Run Tests") {
            steps {
                // Ensure CI mode is on (prevents watch mode from hanging the build)
                sh 'CI=true npm test'
            }
        }
    }

    post {
        always {
            // Clean up to save space on your Mac's drive
            deleteDir()
        }
        failure {
            echo "Build failed on macOS. Check System Logs or Keychain permissions if code signing was involved."
        }
    }
}
