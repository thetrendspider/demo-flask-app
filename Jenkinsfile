pipeline {
    agent any
    stages {
      stage('SonarQube analysis') {
    // requires SonarQube Scanner 2.8+
        def scannerHome = tool 'sonarScanner';
        withSonarQubeEnv('sonarqube 7.6') {
        sh "${scannerHome}/bin/sonar-scanner"
    }
  } 
    }
}
