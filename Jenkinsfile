pipeline {
  agent { dockerfile true }
  stages {
    stage('Build') {
      steps {
        echo 'Building'        
      }
    }
    stage ("Dynamic Analysis - DAST with OWASP ZAP") {
			steps {
				sh "docker run -t owasp/zap2docker-stable zap-baseline.py -t http://192.168.18.23:5000/ || true"
			}
		
		}
    stage('Docker Build') {
    	agent any
      steps {
      	sh 'docker build -t jenkins-testing-wahaj/containerized-hello-world-python:latest .'
      }
    }
    
  }
}