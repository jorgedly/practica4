pipeline {
    agent any
    stages {
		stage('Probando Repositorio') {
            steps {
                sh '''
					bash -c ls
					
				'''
            }
        }
		stage('Ansible') {
           steps {
                sh 'ansible-playbook ansibleConfigurations.yml'
            }
        }
        stage('Ejecutar servidor de python') {
           steps {
                sh 'python servidor.py'
            }
        }
    }
}
