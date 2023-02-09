pipeline {
  agent any
  tools{
    com.openshift.jenkins.plugins.OpenShiftClientTools 'openshift-origin-client-tools-v3.11.0-0cbc58b-linux-64bit'
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
              echo "${openshift.raw( "version" ).out}"
            } 
          }
        }
      }
    }
  }
}