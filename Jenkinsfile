pipeline {
   environment {
   imagename = "storportapp"
   registry = "deepakdevpro/storportapp"
   registryCredential = 'dockerHubLogin'
   dockerImage = ''
   }
   agent any
   stages {
      stage('Pull Code Commit') {
         steps {
         git([url: 'https://github.com/acoderninja/flaskcicd.git', branch: 'main', credentialsId: 'GitHubLogin'])

         }
      }

      stage('Build') {
         steps {
            // build the docker image from the source code using the BUILD_ID parameter in image name
            script {
               echo 'Building Flask App Docker Container..'
               //dockerImage = docker.build imagename
               dockerImage = docker.build registry + ":$BUILD_NUMBER"
               }
         }
      }

      stage("Delivery"){
         steps {
          script {
            echo 'Uploading the latest build to Docker Hub REPO..'
               docker.withRegistry( '', registryCredential ) {
               dockerImage.push("$BUILD_NUMBER")
               dockerImage.push('latest')
               }
            }
         }
      }

      stage('Remove Unused docker image') {
         steps {
            sh "docker rmi $registry:$BUILD_NUMBER"
            sh "docker rmi $imagename:latest"
         }
      }
   }
}