node {
   stage('Get Source') {
      // copy source code from local file system and test
      // for a Dockerfile to build the Docker image
      checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/acoderninja/flaskjenkinscicd.git']]])
      git ('https://github.com/acoderninja/flaskjenkinscicd.git')
      if (!fileExists("Dockerfile")) {
         error('Dockerfile missing.')
      }
   }
   stage('Build Docker') {
       // build the docker image from the source code using the BUILD_ID parameter in image name
         sh "docker build -t flask-app ."
   }
   stage("run docker container"){
        sh "docker run -p 8000:8000 --name flask-app -d flask-app "
    }
}