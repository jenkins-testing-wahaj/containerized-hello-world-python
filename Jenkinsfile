pipeline {
  // agent { docker { image 'python:3.7.2' } }
  agent { dockerfile true }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'registry.access.redhat.com/ubi8/python-39 --version'
        sh 'python test.py'
      }
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }    
    }
    stage('Deploy') {
      steps {
          echo 'Deploying'
      }
    }
  }
}
  

