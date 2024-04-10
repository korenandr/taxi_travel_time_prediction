## Setup minikube cluster
```bash
minikube start --addons=ingress --vm=true --cpus 8 --memory 8192 --namespace="taxi-travel-time-prediction"
minikube image load ./taxi_travel_time_prediction.tar
kubectl apply -f deploy/kube
```


## Check that everything is good
```bash
kubectl get pods
kubectl logs <your pod id> -f
kubectl describe ingress
```


## Test request
```bash
curl -X POST $(minikube ip)/api/echo/ -H "Host: taxi-travel-time-prediction.local" -H "accept: application/json" -H "Content-Type: application/json" -d '{"message": "Hello, world!"}'
```