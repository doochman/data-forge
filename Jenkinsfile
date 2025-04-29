pipeline {
    agent any

    environment {
        COMPOSE_FILE = 'docker-compose.yml'
        STACK_NAME = 'data-ingestion-stack'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Lint Dockerfiles') {
            steps {
                echo 'Linting Dockerfiles...'
                sh '''
                  docker run --rm -i hadolint/hadolint < mage/Dockerfile || true
                  docker run --rm -i hadolint/hadolint < flink/Dockerfile || true
                  docker run --rm -i hadolint/hadolint < beam/Dockerfile || true
                '''
            }
        }

        stage('Build Docker Images') {
            steps {
                sh 'docker-compose build'
            }
        }

        stage('Start Stack') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Run Health Checks') {
            steps {
                sh '''
                  echo "Waiting for Mage to boot..."
                  sleep 20
                  curl -f http://localhost:6789 || (echo "Mage failed" && exit 1)

                  echo "Checking Flink UI..."
                  curl -f http://localhost:8081 || (echo "Flink failed" && exit 1)
                '''
            }
        }

        stage('Optional Tests') {
            steps {
                sh 'echo "Add your Mage or Beam tests here!"'
            }
        }

        stage('Teardown') {
            steps {
                sh 'docker-compose down -v'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up Docker volumes...'
            sh 'docker volume prune -f || true'
        }
    }
}
