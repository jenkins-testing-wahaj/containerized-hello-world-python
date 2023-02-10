pipeline {
  tools{
    oc 'openshift'
  }
  agent { dockerfile true }
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
          openshift.withCluster() {
            openshift.withProject('python-test') {
              echo "Hello from project ${openshift.project()} in cluster ${openshift.cluster()}"
              def selector = openshift.selector("pods")
              selector.describe()
            } 
          }
        }
      }
    }
  }
}