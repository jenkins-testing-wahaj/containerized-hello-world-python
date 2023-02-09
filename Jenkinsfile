pipeline {
  agent any
  tools {
    oc 'oc'
  }
  stages {
    stage('Build') {
      steps {
        echo 'Building'        
      }
    }
    stage('Create Container Image') {
      steps {
        echo 'Create Container Image'
        script {
          openshift.withCluster('power9', 'token') {
            openshift.withProject('python-test') {
              echo "Hello from project ${openshift.project()} in cluster ${openshift.cluster()}"
            } 
          }
        }
      }
    }
  }
}