pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('build') {
      steps {
        sh 'pipenv install'
      }
    }
    stage('test') {
      steps {
        sh 'pipenv run python -m pytest -n 4
      }   
    }
  }
}
