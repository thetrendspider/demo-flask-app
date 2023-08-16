pipeline {
    agent any
    environment {
        scannerHome = '/var/lib/jenkins'
    }

    stages {
      stage('SonarQube analysis') {
        steps{
            script{
            def scannerHome = tool 'SonarScanner 4.0';

            withSonarQubeEnv('sonarQube-7.6') {
            sh "${scannerHome}/bin/sonar-scanner"
            }
            }
        }
    // requires SonarQube Scanner 2.8+
        
        } 
    }
}
