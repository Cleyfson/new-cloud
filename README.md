# DevOps - Playlist Recommendation System  

![Kubernetes](https://img.shields.io/badge/Kubernetes-✓-blue) ![ArgoCD](https://img.shields.io/badge/ArgoCD-✓-orange) ![MachineLearning](https://img.shields.io/badge/Machine%20Learning-✓-green)  

## Description  

This project was developed as part of the **Cloud Computing** course in the second semester of 2024 at the **Federal University of Minas Gerais (UFMG)**. It implements a playlist recommendation system based on machine learning. The solution is deployed in a **Kubernetes** environment, using **DevOps** and **MLOps** practices for continuous integration and delivery (CI/CD). The system analyzes Spotify datasets, generates association rules (using Frequent Itemset Mining), and recommends personalized playlists to users based on their listening preferences.

### Key Features:  
- **Machine Learning Backend**: Trains models and generates association rules to provide personalized playlist recommendations.  
- **Kubernetes-Orchestrated Deployment**: All services are deployed in a Kubernetes environment for better scalability and management.  
- **Continuous Delivery**: ArgoCD automates deployment to ensure continuous delivery and monitoring of application updates.  
- **Persistent Storage**: Models and datasets are stored in a Persistent Volume for reliable data handling across pods.

## Architecture  

The system architecture consists of:  

- **Machine Learning Backend**: Implements the recommendation algorithm and manages model training and rule generation.  
- **Persistent Volume (PV)**: Used for storing models, datasets, and other important data that need to persist across container restarts.  
- **Kubernetes**: Orchestrates containerized services and manages system resources.  
- **ArgoCD**: Ensures continuous integration and deployment (CI/CD), automatically pushing new updates to the production environment.  

## Project Structure  

## Technologies  

- **Languages**: Python, Flask  
- **Tools**: Docker, Kubernetes, ArgoCD  
- **Machine Learning**: Association Rules (Frequent Itemset Mining)  
- **Database/Storage**: Persistent Volume for data storage  
- **CI/CD**: ArgoCD for continuous deployment management  

```plaintext
/playlist-recommendation-service
│
├── /datasets              # Datasets and music lists
│   ├── dataset.csv        # Example dataset used to train the recommendation model

├── /config                # Kubernetes configuration files for service deployment
│   ├── deployment.yaml    # Deployment definitions for Kubernetes
│   ├── service.yaml       # Service definitions for Kubernetes
│   ├── namespace.yaml     # Namespace definitions for Kubernetes cluster isolation
│   ├── pvc.yaml           # Persistent Volume Claim for data storage
│   └── ml-job.yaml        # Job definition for machine learning tasks

├── /api-server            # Container with the API and related deployment scripts
│   ├── Dockerfile         # Dockerfile for building the API server container
│   ├── app.py             # Main logic of the REST API handling recommendations
│
├── /rules-generator       # Container with the backend and machine learning logic
│   ├── Dockerfile         # Dockerfile for building the backend container
│   ├── app.py             # Playlist recommendation logic using machine learning algorithms
│
└── README.md              # Project overview and setup instructions
