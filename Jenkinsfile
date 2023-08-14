pipeline {
    agent any

    environment {
        SONAR_SCANNER_HOME = tool name: 'SonarQubeScanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'
        SONAR_TOKEN = credentials('3322cbeacaec31aa0cdbbfae4a5432656b3f99c4') // Replace with the actual credential ID
    }

    stages {

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool name: 'SonarQubeScanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'

                    withSonarQubeEnv('SonarQubeServer') {
                        sh "${scannerHome}/bin/sonar-scanner -Dsonar.login=${SONAR_TOKEN}"
                    }
                }
            }
        }
    }

    post {
        always {
            // Archive artifacts, clean up, or perform other post-build actions
        }
    }
}
