pipeline {
  agent {
    node {
      label 'NEW_linux'
    }

  }
  stages {
    stage('Build') {
      steps {
        echo 'Building-multi1..'
        sh '''echo "run date"
date
'''
      }
    }

    stage('Test') {
      steps {
        echo 'Testing..'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploying-multi1....'
      }
    }

  }
}