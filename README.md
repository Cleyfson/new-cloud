# DevOps - Playlist Recommendation System  

## Project Structure  
```plaintext
/playlist-recommendation-service
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
