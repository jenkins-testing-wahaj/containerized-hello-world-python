pipeline {
  // agent { docker { image 'python:3.7.2' } }
  agent none
  stages {
    stage('build') {
      agent { docker { image 'python:3.7.2' } }
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      agent { docker { image 'python:3.7.2' } }
      steps {
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
  

