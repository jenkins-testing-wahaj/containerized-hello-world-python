pipeline {
  environment {
  registry = "default-route-openshift-image-registry.apps.tz-205307.cecc.ihost.com/jenkins/jenkins"
  dockerImage = ''
  }
  agent { dockerfile true }
  stages {
    stage('Building the image'){
      steps{
        sh "docker version"
      }
    }
  }
}