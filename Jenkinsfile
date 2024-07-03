pipeline {
    agent {
    docker {
      image 'docker:dind'
      args '-v /var/run/docker.sock:/var/run/docker.sock'
    }
  }

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        // stage('Cleanup Previous Containers') {
        //     steps {
        //         script {
        //             sh 'docker-compose down'
        //         }
        //     }
        // }

        // stage('Build and Test') {
        //     steps {
        //         script {
        //             sh 'docker-compose build'
        //             sh 'docker-compose run web python manage.py test'
        //         }
        //     }
        // }

        // stage('Deploy') {
        //     steps {
        //         script {
        //             sh 'docker-compose up -d'
        //         }
        //     }
        // }
    }

    post {
        always {
            script {
                // Clean up Docker resources
                sh 'echo "y" | docker system prune -a --volumes'
            }
        }
    }

}
