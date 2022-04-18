pipeline {
   agent any
   stages {
      stage('Pull Updated Code') {
         steps {
         // copy source code from local file system and test
         // for a Dockerfile to build the Docker image
         checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/acoderninja/flaskcicd.git']]])
         }
      }

      stage('Build Flask App Docker Container') {
         steps {
         // build the docker image from the source code using the BUILD_ID parameter in image name
            echo 'Building Flask App Docker Container..'
            sh "docker build -t flask-app ."
         }
      }

      stage("Deploy Docker Container"){
         steps {
         echo 'Deploying newly built Flask App Docker Container..'
         sh "docker run -p 8000:8000 --name flask-app -d flask-app "
         }
      }
   }
}