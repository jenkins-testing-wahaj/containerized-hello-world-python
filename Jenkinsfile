pipeline {
  // agent { docker { image 'python:3.7.2' } }
  agent {
        docker { image 'default-route-openshift-image-registry.apps.tz-205307.cecc.ihost.com/jenkins/jenkins' }
    }
  stages {
    stage('build') {
      steps {
        sh 'pip3 install -r requirements.txt'
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
  

