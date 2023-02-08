pipeline {
  environment {
  registry = "default-route-openshift-image-registry.apps.tz-205307.cecc.ihost.com/jenkins/jenkins"
  dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning From Git As First Step'){
      steps{
        git 'https://github.com/Knickkennedy/containerized-hello-world-python.git'
      }
    }
    stage('Building the image'){
      steps{
        script{
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
  }
}