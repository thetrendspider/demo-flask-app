pipeline {
    agent any
    stages {
      stage('SonarQube analysis') {
        steps{
            script{
            def scannerHome = tool 'sonarScanner';
            withSonarQubeEnv('sonarQube-7.6') {
            sh "${scannerHome}/bin/sonar-scanner"
            }
            }
        }
    // requires SonarQube Scanner 2.8+
        
        } 
    }
}
