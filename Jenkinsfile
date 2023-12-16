pipeline {
    agent any
    
    stages {

        stage('Stop and Remove Containers') {
            steps {
                script {
                    // Stop and remove existing containers if they are running
                    sh 'docker ps -q --filter "name=my-mongo-container" | xargs docker stop || true'
                    sh 'docker ps -q --filter "name=my-mongo-container" | xargs docker rm || true'
                    
                    sh 'docker ps -q --filter "name=my-express-container" | xargs docker stop || true'
                    sh 'docker ps -q --filter "name=my-express-container" | xargs docker rm || true'
                    
                    sh 'docker ps -q --filter "name=my-react-container" | xargs docker stop || true'
                    sh 'docker ps -q --filter "name=my-react-container" | xargs docker rm || true'
                }
            }
        }
        
        stage('Build and Run Database') {
            steps {
                sh 'docker run -d -p 27017:27017 --name my-mongo-container mongo'
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
