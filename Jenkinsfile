pipeline {
  agent { any { image 'python:3.7.2' } }
  
  stages {
    stage('build') {
      steps {
        sh 'pip3 install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python test.py'
      }
      // """smoke test"""
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
