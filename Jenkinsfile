pipeline {
    agent any
    
    stages {
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

    // post {
    //     always {
    //         // Cleanup steps
    //         sh 'docker stop my-mongo-container && docker rm my-mongo-container'
    //         sh 'docker stop my-express-container && docker rm my-express-container'
    //         sh 'docker stop my-react-container && docker rm my-react-container'
    //     }
    // }
}
