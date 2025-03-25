# FastAPI Kubernetes Deployment

This project sets up a FastAPI application and deploys it on a Kubernetes cluster using Kind (Kubernetes in Docker). The application provides basic CRUD operations for managing users.

## Project Structure
```
your-project/
├── kind-config.yaml       # Kind cluster configuration
├── Dockerfile             # Dockerfile for FastAPI application
├── kubernetes/
│   ├── deployment.yaml    # Kubernetes deployment file
│   ├── service.yaml       # Kubernetes service file
│   └── configmap.yaml     # Application configurations (if needed)
├── api/
│   ├── models.py          # Pydantic models for FastAPI
│   ├── main.py            # FastAPI application logic
│   ├── requirements.txt   # Python dependencies
└── README.md              # Documentation
```

## Prerequisites
Ensure you have the following installed:
- [Docker](https://www.docker.com/)
- [Kind](https://kind.sigs.k8s.io/)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)

## Setup and Deployment

### 1. Create a Kind Cluster
Run the following command to create a Kubernetes cluster using the provided `kind-config.yaml`:
```sh
kind create cluster --config=kind-config.yaml
```

### 2. Build and Push Docker Image
Replace `khuselo/my_fastapi` with your own Docker Hub username if necessary:
```sh
docker build -t khuselo/my_fastapi:latest .
docker push khuselo/my_fastapi:latest
```

### 3. Deploy to Kubernetes
Apply the deployment and service configurations:
```sh
kubectl apply -f kubernetes/
```

### 4. Verify Deployment
Check if the pods are running:
```sh
kubectl get pods
```
Check if the service is running:
```sh
kubectl get services
```

### 5. Access the FastAPI Application
The FastAPI service is exposed on port `32334`. You can test it with:
```sh
curl http://localhost:32334
```
Or open it in a browser:
```
http://localhost:32334/docs
```
This will open the interactive Swagger UI for testing the API.

## API Endpoints
The FastAPI app provides the following endpoints:

- `GET /` - Root endpoint
- `GET /api/v1/users` - Fetch all users
- `POST /api/v1/users` - Add a new user
- `DELETE /api/v1/users/{user_id}` - Remove a user
- `PUT /api/v1/users/{user_id}` - Update user details

## Cleanup
To delete the Kind cluster when done:
```sh
kind delete cluster --name fastapi-cluster
```

## Notes
- The `kind-config.yaml` maps port `32334` to allow external access.
- `NodePort` is used to expose the FastAPI service.
- The Docker image should be available on Docker Hub before deploying to Kubernetes.

Enjoy deploying your FastAPI app on Kubernetes! 🚀

