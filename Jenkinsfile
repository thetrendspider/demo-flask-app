pipeline {
    agent any
    environment {
        scannerHome = '/var/lib/jenkins'
    }

    stages {
      stage('SonarQube analysis') {
        steps{
            script{
            def scannerHome = tool name: 'SonarQubeScanner', type: 'hudson.plugins.sonar.SonarRunnerInstallation'

            withSonarQubeEnv('sonarQube-7.6') {
            sh "${scannerHome}/bin/sonar-scanner"
            }
            }
        }
    // requires SonarQube Scanner 2.8+
        
        } 
    }
}
