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
            openshift.withProject("python-test") {
              def buildConfigExists = openshift.selector("bc", "containerized-hello-world-python").exists() 
              if(!buildConfigExists){ 
                openshift.newBuild("--name=containerized-hello-world-python", "--docker-image=default-route-openshift-image-registry.apps.tz-205307.cecc.ihost.com/python-test/containerized-hello-world-python", "--binary") 
              }
              openshift.selector("bc", "containerized-hello-world-python").startBuild("--from-file=target/simple-servlet-0.0.1-SNAPSHOT.war", "--follow") 
            } 
          }
        }
      }
    }
    stage('Deploy') {
      steps {
        echo 'Deploying'
        script{
          openshift.withCluster('power9', 'token') { 
            openshift.withProject("python-test") { 
            def deployment = openshift.selector("dc", "containerized-hello-world-python") 
            if(!deployment.exists()){ 
              openshift.newApp('containerized-hello-world-python', "--as-deployment-config").narrow('svc').expose() 
            }
            timeout(5) { 
              openshift.selector("dc", "containerized-hello-world-python").related('pods').untilEach(1) { 
                return (it.object().status.phase == "Running") 
              } 
            } 
            } 
          }
        }
      }
    }
  }
}