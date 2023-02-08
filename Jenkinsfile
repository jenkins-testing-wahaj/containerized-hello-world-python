pipeline {
  environment {
  registry = "default-route-openshift-image-registry.apps.tz-205307.cecc.ihost.com/jenkins/jenkins"
  dockerImage = ''
  }
  agent any
  stages {
    stage('Building the image'){
      steps{
        script{
          dockerImage = docker.inside(registry)
        }
      }
    }
  }
}