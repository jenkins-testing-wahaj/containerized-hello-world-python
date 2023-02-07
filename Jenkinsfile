pipeline {
  agent { docker { image 'python:3' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
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
  

