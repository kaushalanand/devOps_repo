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
                // --unsafe-perm fixes many "gyp" permission errors on macOS
                sh 'npm install --no-optional --unsafe-perm'
            }
        }

        stage("Run Tests") {
            steps {
                sh 'CI=true npm test'
            }
        }
    }

    post {
        failure {
            // This time, we print a more useful command to debug
            sh 'npm config list' 
            echo "Build Failed. Look for 'npm ERR!' above."
        }
    }
}
