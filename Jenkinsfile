pipeline {
    agent any

    stages {
      stage('SonarQube analysis') {
        environment {
        scannerHome = tool 'SonarQubeScanner'
        }
        steps{
            

            withSonarQubeEnv('sonarQube-7.6') {
            sh "${scannerHome}/bin/sonar-scanner"
            }
            
        }
    // requires SonarQube Scanner 2.8+
        
        } 
    }
}
