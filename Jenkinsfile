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
               dockerImage = docker.build registry + "imagename:$BUILD_NUMBER"
               }
         }
      }

      stage("Deploy"){
         steps {
          script {
            echo 'Deploying newly built Flask App Docker Container..'
               docker.withRegistry( '', registryCredential ) {
               dockerImage.push("$BUILD_NUMBER")
               dockerImage.push('latest')
               }
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