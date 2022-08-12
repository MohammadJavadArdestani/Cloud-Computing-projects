# Cloud-Computing-projects
In this project, we developed an app inspired by [privetnote](https://privnote.com/). 
This lightweight application is implemented by flask, dockerized, and deployed on Kubernetes. 

## Table of Contents




## Web Application
This web application lets you create notes and, after that, gives you a  link to access the notes' content; each note can be read only once. After reading the message or after a specific amount of time (the Default is 30 seconds, but it is configurable), the note will be deleted. 
The web server is implemented using ```Flask```, which is connected to a ```MySQL``` database. You can find codes [here](https://github.com/MohammadJavadArdestani/Cloud-Computing-projects/tree/main/Privenotes/app). 

## Containerize	
We containerized the project by writing a multistage build Dockerfile. You can find the ```Dockerfle``` [here](https://github.com/MohammadJavadArdestani/Cloud-Computing-projects/blob/main/Privenotes/app/Dockerfile), and pull the image by the following command: 
```bash
docker pull mjavadardestani/secretnotes
```
## Deployment via Docker Compose
we created a YML file to define the services with a single command, can spin everything up or tear it all down.To deploy the project via Docker Compose, run the following command:
```bash
docker-compose up -d
```
