pipeline {
  agent any
  tools{
    oc 'openshift'
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
              echo "Hello from project ${openshift.project()} in cluster ${openshift.cluster()}"
              def created = openshift.newApp( 'https://github.com/openshift/ruby-hello-world' )
              created.describe()
          }
        }
      }
    }
  }
}