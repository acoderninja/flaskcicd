pipeline {
   environment {
   imagename = "flask-app"
   registry = "deepakdevpro/automation"
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

            //sh "docker build -t flask-app ."
            script {
               echo 'Building Flask App Docker Container..'
               //dockerImage = docker.build imagename
               dockerImage = docker.build registry + ":$BUILD_NUMBER"
               // sh "docker build -t deepakdevpro/automation:flask-app ."
            }
         }
      }

      stage("Deploy"){
         steps {
          script {
            echo 'Deploying newly built Flask App Docker Container..'
            // sh "docker run -p 8000:8000 --name flask-app -d flask-app "
            // sh "docker push deepakdevpro/automation:flask-app"
               // docker.withRegistry( '', registryCredential ) {
               //    dockerImage.push("$BUILD_NUMBER")
               //    dockerImage.push('latest')
               // }
            }
         }
      }

      //stage('Remove Unused docker image') {
         //steps {
            //sh "docker rmi $registry:$BUILD_NUMBER"
            //sh "docker rmi $imagename:latest"
         //}
      //}
   }
}