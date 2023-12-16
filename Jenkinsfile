pipeline {
    agent any
    
    stages {

        stage('Stop and Remove Containers') {
            steps {
                script {
                    // Stop and remove existing containers if they are running
                    sh 'docker ps -q --filter "name=my-mongo-container" | xargs docker stop my-mongo-container || true'
                    sh 'docker ps -q --filter "name=my-mongo-container" | xargs docker rm my-mongo-container || true'
                    
                    sh 'docker ps -q --filter "name=my-express-container" | xargs docker stop my-express-container || true'
                    sh 'docker ps -q --filter "name=my-express-container" | xargs docker rm my-express-container || true'
                    
                    sh 'docker ps -q --filter "name=my-react-container" | xargs docker stop my-react-container || true'
                    sh 'docker ps -q --filter "name=my-react-container" | xargs docker rm my-react-container || true'
                }
            }
        }

        stage('Remove Images') {
            steps {
                sh 'docker rmi my-express-image my-react-image mongo || true'
            }
        }
        
        stage('Run and Persist Database') {
            steps {
                sh 'docker run -d -p 27017:27017 --name my-mongo-container -v ./data/data.json:/mongo_data mongo --repair'
            }
        }

        stage('Build and Run Backend') {
            steps {
                sh 'docker build -t my-express-image ./e-comerce-backend'
            }
        }

        stage('Build and Run Frontend') {
            steps {
                sh 'docker build -t my-react-image ./e-comerce-frontend'
            }
        }


        stage('Deploy Backend') {
            steps {
                sh 'docker run -d -p 3000:3000 --name my-express-container --link my-mongo-container:database -e MONGO_URI=mongodb://database:27017/ecom my-express-image'
            }
        }

        stage('Deploy Frontend') {
            steps {
                sh 'docker run -d -p 3001:3000 --name my-react-container --link my-express-container:backend my-react-image'
            }
        }
    }

}
