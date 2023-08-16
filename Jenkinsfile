pipeline {
    agent any
    environment {
        sonar_scanner_home = '/var/lib/jenkins'
    }

    stages {
      stage('SonarQube analysis') {
        steps{
            script{
            def sonar_scanner_home = tool 'sonarScanner';
            withSonarQubeEnv('sonarQube-7.6') {
            sh "${sonar_scanner_home}/bin/sonar-scanner"
            }
            }
        }
    // requires SonarQube Scanner 2.8+
        
        } 
    }
}
