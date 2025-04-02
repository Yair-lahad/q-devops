@echo off
echo [1/4] Building Docker image...
docker build -t my-k8s-app:latest .

echo [2/4] Applying Kubernetes deployment...
kubectl apply -f k8s/deployment.yaml

echo [3/4] Applying Kubernetes service...
kubectl apply -f k8s/service.yaml

echo [4/4] Done. Access your app at:
echo http://localhost:30081
