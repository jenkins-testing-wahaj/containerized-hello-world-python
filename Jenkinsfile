pipeline {
  tools{
    oc 'openshift'
    dockerTool 'dockerTool'
  }
  agent { 
    docker { image 'default-route-openshift-image-registry.apps.tz-205307.cecc.ihost.com/jenkins/jenkins' }
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