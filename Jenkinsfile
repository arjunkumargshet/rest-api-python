pipeline {
    agent any

    // Step 1: Define input parameters
    parameters {
        choice(name: 'TEST_SUITE', choices: ['smoke', 'regression', 'sanity', 'all'], description: 'Select test suite to run')
    }

    environment {
        PYTHON_ENV = 'venv'  // Optional: Your virtual environment folder if needed
    }

    stages {
        stage('Setup Environment') {
            steps {
                echo "Setting up Python environment..."
                sh '''
                    python3 -m venv ${PYTHON_ENV}
                    source ${PYTHON_ENV}/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run PyTest Suite') {
            steps {
                echo "Running ${params.TEST_SUITE} tests..."

                script {
                    def pytestCommand = ""

                    if (params.TEST_SUITE == "all") {
                        pytestCommand = "pytest --alluredir=allure-results"
                    } else {
                        pytestCommand = "pytest -m ${params.TEST_SUITE} --alluredir=allure-results"
                    }

                    sh """
                        source ${PYTHON_ENV}/bin/activate
                        ${pytestCommand}
                    """
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                echo 'Generating Allure report...'
                sh '''
                    allure generate allure-results --clean -o allure-report
                '''
            }
        }

        stage('Publish Allure Report') {
            steps {
                echo 'Publishing Allure report...'
                allure includeProperties: false, jdk: '', reportBuildPolicy: 'ALWAYS', results: [[path: 'allure-results']]
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'deactivate || true'
        }
        failure {
            echo 'Tests failed. Check reports for details.'
        }
        success {
            echo 'Tests ran successfully!'
        }
    }
}
