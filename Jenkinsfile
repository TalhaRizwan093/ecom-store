pipeline {
    agent any

    environment {
        BACKEND_IMAGE = 'toosterr007/e-commerce-store_backend'
        FRONTEND_IMAGE = 'toosterr007/e-commerce-store_frontend'
        NETWORK_NAME = 'my-network'
    }

    stages {
        stage('Build and Run Database') {
            steps {
                sh 'docker run -d -p 27017:27017 --name my-mongo-container mongo'
                // script {
                //     docker.image('mongo').withRun('-p 27017:27017 --name my-mongo-container --network ${NETWORK_NAME} -v data:/data/db -v ./data:/data/db/initialData') { c ->
                //         // Database container is running
                //     }
                //}
            }
        }

        stage('Build and Run Backend') {
            steps {
                    sh 'docker build -t my-express-image ./e-comerce-backend'
                    sh 'docker run -d -p 3000:3000 --name my-express-container --link my-mongo-container:database -e MONGO_URI=mongodb://database:27017/ecom my-express-image'
                // script {
                //     docker.image(BACKEND_IMAGE).withRun("--name my-express-container --network ${NETWORK_NAME} -p 3000:3000 --link my-mongo-container:database -e MONGO_URI=mongodb://database:27017/ecom") { c ->
                //         // Backend container is running
                //     }
                // }
            }
        }

        stage('Build and Run Frontend') {
            steps {
                    sh 'docker build -t my-react-image ./e-comerce-frontend'
                    sh 'docker run -d -p 3001:3000 --name my-react-container --link my-express-container:backend my-react-image'
                // script {
                //     docker.image(FRONTEND_IMAGE).withRun("--name my-react-container --network ${NETWORK_NAME} -p 3001:3000 --link my-express-container:backend") { c ->
                //         // Frontend container is running
                //     }
                // }
            }
        }
    }

    post {
        always {
            // Cleanup steps
            sh 'docker stop my-mongo-container && docker rm my-mongo-container'
            sh 'docker stop my-express-container && docker rm my-express-container'
            sh 'docker stop my-react-container && docker rm my-react-container'
        }
    }

}
