# Search
    https://github.com/mathare
    pytest bdd selenium website github

# Chrome
Lựa chọn phiên bản Chrome

    chrome://settings/help
    https://www.selenium.dev/downloads/
    https://chromedriver.chromium.org/

Trong conftest.py có hai lựa chọn cho webdriver.Chrome 

    Invisible: webdriver.Chrome(ChromeDriverManager().install(), options=opts)
    Visible: webdriver.Chrome(executable_path=r'C:/Users/{name}/{project}/chromedriver_win32/chromedriver.exe')

# Cài đặt các phần mềm
    pip install -r requirements

# Pytest-BDD
features: 

    Scenario: Truyền giá trị "value"
    Scenario Outline: Truyền biến <variable> 
    Scenario Outline: Truyền biến "<variable>"

step_defs: 

    Nhận giá trị "{param}"
    Nhận biến {param}
    Nhận biến "{param}"
----------------------github info---------------
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 token git tuuvv
-----------------------jenkins------------------
http://18.217.82.216:8080/
tuuvv
bean1991
----------------------
pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
               git branch: 'main', credentialsId: '111222333', url: 'https://github.com/tuuvv/selenium_browserstack'
            }
        }
        stage('Test') {
            steps {
                dir('/var/lib/jenkins/workspace/selenium_browserstack/step_defs'){
                sh 'pip3 install -r requirements.txt'
                sh 'python3 -m pytest --html=report/report1.html --css=report/highcontrast.css --css=report/accessible.css --self-contained-html test_home_page_steps.py'
                }
            }
        }
        stage('Update GIT') {
          steps {
            script {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    withCredentials([usernamePassword(credentialsId: '111222333', 
                    passwordVariable: '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', usernameVariable: 'vuvantuu@gmail.com')]) {
                        sh "git config user.email vuvantuu@gmail.com"
                        sh "git config user.name tuuvv"
                        sh "git add ."
                        sh "git commit -m 'Triggered Build: ${env.BUILD_NUMBER}'"
                        sh "git push https://tuuvv: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@github.com/tuuvv/selenium_browserstack.git"
                    }
                }
              }
          }
        }
    }
}


or: 

pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
               git branch: 'main', credentialsId: '111222333', url: 'https://github.com/tuuvv/selenium_browserstack'
                sh 'pip3 install pipenv'
                sh 'pip3 install pytest'
                sh 'pip3 install pytest-bdd'
                sh 'pip3 install selenium'
                sh 'pip3 install sttable'
                sh 'pip3 install webdriver-manager'
            }
        }
        stage('Test') {
            steps {
                dir('/var/lib/jenkins/workspace/selenium_browserstack/step_defs'){
                sh 'python3 -m pytest --html=report/report1.html --css=report/highcontrast.css --css=report/accessible.css --self-contained-html test_home_page_steps.py'
                }
            }
        }
        stage('Update GIT') {
          steps {
            script {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    withCredentials([usernamePassword(credentialsId: '111222333', 
                    passwordVariable: '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', usernameVariable: 'vuvantuu@gmail.com')]) {
                        sh "git config user.email vuvantuu@gmail.com"
                        sh "git config user.name tuuvv"
                        sh "git add ."
                        sh "git commit -m 'Triggered Build: ${env.BUILD_NUMBER}'"
                        sh "git push https://tuuvv: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@github.com/tuuvv/selenium_browserstack.git"
                    }
                }
              }
          }
        }
    }
}