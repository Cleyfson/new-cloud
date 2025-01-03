# DevOps - Playlist Recommendation System  

## Project Structure  
```plaintext
/playlist-recommendation-service
├── /config                # Arquivos de configuração para implantação no Kubernetes
│   ├── deployment.yaml    # Definições de implantação para o Kubernetes
│   ├── service.yaml       # Definições de serviço para o Kubernetes
│   ├── namespace.yaml     # Definições de namespace para isolamento no cluster Kubernetes
│   ├── pvc.yaml           # Persistent Volume Claim para armazenamento de dados
│   └── ml-job.yaml        # Definição do Job para tarefas de machine learning

├── /api-server            # Contêiner com a API e scripts de implantação relacionados
│   ├── Dockerfile         # Dockerfile para construção do contêiner da API
│   ├── app.py             # Lógica principal da REST API para recomendações

├── /rules-generator       # Contêiner com a lógica backend e de aprendizado de máquina
│   ├── Dockerfile         # Dockerfile para construção do contêiner backend
│   ├── app.py             # Lógica de recomendação de playlists utilizando algoritmos de machine learning

├── wget-example           # Arquivos de exemplo de requisição wget
├── manifest               # Manifesto do ArgoCD para monitoramento do repositório GitHub e sincronização com Kubernetes

└── README.md              # Visão geral do projeto e instruções de configuração

