pipeline {
   environment {
   imagename = "flask-app"
   registryCredential = 'dockerHubLogin'
   dockerImage = ''
   }
   agent any
   stages {
      stage('Pull Code Commit') {
         steps {
         //checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/acoderninja/flaskcicd.git']]])
         git([url: 'https://github.com/acoderninja/flaskcicd.git', branch: 'main', credentialsId: 'GitHubLogin'])
         }
      }

      stage('Build') {
         steps {
         // build the docker image from the source code using the BUILD_ID parameter in image name
            echo 'Building Flask App Docker Container..'
            //sh "docker build -t flask-app ."
            script {
            dockerImage = docker.build imagename
            }
         }
      }

      stage("Deploy"){
         steps {
         echo 'Deploying newly built Flask App Docker Container..'
         //sh "docker run -p 8000:8000 --name flask-app -d flask-app "
         script {
            docker.withRegistry( 'https://hub.docker.com/repository/docker/deepakdevpro/automation', registryCredential ) {
            dockerImage.push("$BUILD_NUMBER")
            dockerImage.push('latest')
            }
         }
      }
   }

   stage('Remove Unused docker image') {
      steps {
         sh "docker rmi $imagename:$BUILD_NUMBER"
         sh "docker rmi $imagename:latest"
      }
   }
}
}