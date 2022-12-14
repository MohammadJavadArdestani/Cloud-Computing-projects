# Cloud-Computing-projects
In this project, we developed an app inspired by [privetnote](https://privnote.com/). 
This application is by flask, dockerized, and deployed on Kubernetes. 

 we implemented all parts of projects as a team of two:<br>
> [Mahvash Siavashpour](https://github.com/mahvash-siavashpour) <br>
> [MohammadJavad Ardestani](https://github.com/MohammadJavadArdestani) <br>




## Table of Contents
- [Requirements](https://github.com/MohammadJavadArdestani/Cloud-Computing-projects/blob/main/Privenotes/README.md#requirements)
- [Web Application](https://github.com/MohammadJavadArdestani/Cloud-Computing-projects/blob/main/Privenotes/README.md#web-application)
- [Containerize](https://github.com/MohammadJavadArdestani/Cloud-Computing-projects/blob/main/Privenotes/README.md#containerize)
- [Deployment by Docker Compose](https://github.com/MohammadJavadArdestani/Cloud-Computing-projects/blob/main/Privenotes/README.md#deployment-by-docker-compose)
- [Deployment in Kubernetes](https://github.com/MohammadJavadArdestani/Cloud-Computing-projects/blob/main/Privenotes/README.md#deployment-in-kubernetes)
- [Test the Project](https://github.com/MohammadJavadArdestani/Cloud-Computing-projects/blob/main/Privenotes/README.md#test-the-project)

## Requirements
* Install [Docker](https://docs.docker.com/get-docker/). 
* Install [Minikube](https://minikube.sigs.k8s.io/docs/start/).
```bash
pip install -r requirements.txt
```
## Web Application
This web application lets you create notes and, after that, gives you a  link to access the notes' content; each note can be read only once. After reading the message or after a specific amount of time (the Default is 30 seconds, but it is configurable), the note will be deleted. 
The web server is implemented using ```Flask```, which is connected to a ```MySQL``` database. You can find codes [here](https://github.com/MohammadJavadArdestani/Cloud-Computing-projects/tree/main/Privenotes/app). 

## Containerize	
We containerized the project by writing a multistage build Dockerfile. You can find the ```Dockerfle``` [here](https://github.com/MohammadJavadArdestani/Cloud-Computing-projects/blob/main/Privenotes/app/Dockerfile), and pull the image by the following command: 
```bash
docker pull mjavadardestani/secretnotes
```
## Deployment by Docker Compose
we created a YML file to define the services with a single command, can spin everything up or tear it all down. You can fine the file [here](https://github.com/MohammadJavadArdestani/Cloud-Computing-projects/blob/main/Privenotes/docker-compose.yml) and deploy the project by Docker Compose, run the following command:
```bash
docker-compose up -d
```

## Deployment in Kubernetes
For deployment in Kubernetes, we have to write ConfigMap, Secret, PV, PVC, Deployment, and Service files and apply them. We also use an HPA component on the Kubernetes cluster for auto-scaling.

We use the StatefulSet object, and we have replicated MySQL pods. To deploy the project, run the following command in the K8s_files directory:
```bash
for l in $(ls | grep '.yaml'); do kubectl apply -f $l; done;
```

This commcand applys the following yaml files which can be found in [K8s_files](https://github.com/MohammadJavadArdestani/Cloud-Computing-projects/tree/main/Privenotes/K8s_files): 

* components.yaml
* config-map.yaml
* db_deployment.yaml
* db_service.yaml
* flaskapi-deployment.yaml
* flaskapi-service.yaml
* hpa.yaml
* persistentv.yaml
* persistentvc.yaml
* secret.yaml
* statefulset.yaml

## Test the Project
By the following command you can access the Home page of secretnotes by 127.0.0.1:8080 and use this application.
```bash
kubectl port-forward service/flask-service 8080:8080 Forwarding from 127.0.0.1:8080 ->8080
```

