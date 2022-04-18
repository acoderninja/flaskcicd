pipeline {
   agent any
   stages {
      node {
      stage('CheckOut Source') {
         // copy source code from local file system and test
         // for a Dockerfile to build the Docker image
         checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/acoderninja/flaskcicd.git']]])
         // git ('https://github.com/acoderninja/flaskcicd.git')
         if (!fileExists("Dockerfile")) {
            error('Dockerfile missing.')
         }
      }
      stage('Build Flask App in Docker') {
         // build the docker image from the source code using the BUILD_ID parameter in image name
            sh "docker build -t flask-app ."
      }
      stage("run docker container"){
         sh "docker run -p 8000:8000 --name flask-app -d flask-app "
         }
      }
   }
}