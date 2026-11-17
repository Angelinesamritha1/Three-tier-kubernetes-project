# Three-Tier Web Application Deployment Using Kubernetes on AWS

## Project Overview

This project demonstrates the deployment of a three-tier web application on AWS EC2 using Docker and Kubernetes.

The application is a car and bike-themed website called **CARZONE**. Visitors can submit messages through a contact form, which are processed by a Python Flask backend and stored in a MySQL database.

## Architecture

The application consists of three layers:

1. **Frontend – Nginx**
   - Hosts the CARZONE website.
   - Provides the contact form interface.
   - Communicates with the backend using HTTP requests.

2. **Backend – Python Flask**
   - Handles contact form submissions.
   - Processes incoming JSON data.
   - Connects to the MySQL database.
   - Saves visitor messages.

3. **Database – MySQL**
   - Stores contact form submissions.
   - Uses persistent storage through Kubernetes Persistent Volumes and Persistent Volume Claims.

## Technologies Used

- AWS EC2
- Ubuntu Linux
- Docker
- Kubernetes
- kubeadm
- Nginx
- Python
- Flask
- MySQL
- YAML
- NFS Storage
- Git and GitHub

## Project Structure

```text
three-tier-project/
│
├── frontend/
│   ├── index.html
│   ├── frontend.yaml
│   ├── pv.yaml
│   └── pvc.yaml
│
├── backend/
│   ├── app.py
│   ├── Dockerfile
│   ├── backend.yaml
│   └── dockerinstall.sh
│
├── database/
│   ├── sql.yaml
│   ├── pv.yaml
│   └── pvc.yaml
│
└── .gitignore
```

## Kubernetes Concepts Implemented

- Deployments and Pods
- Multiple replicas for frontend and backend
- NodePort Services for external access
- ClusterIP Services for internal communication
- Kubernetes Secrets for database credentials
- Persistent Volumes (PV)
- Persistent Volume Claims (PVC)
- NFS shared storage
- Containerized application deployment

## Application Workflow

1. A visitor opens the CARZONE website.
2. The visitor submits a contact form.
3. Nginx serves the frontend website.
4. The frontend sends the form data to the Flask backend.
5. Flask connects to MySQL using Kubernetes Secret-based environment variables.
6. MySQL stores the submitted message in the `contactsdb` database.
7. The website displays a success message after a successful submission.

## Testing and Verification

The application was tested by submitting contact form messages.

Verified results:
- Frontend website accessible through the Kubernetes NodePort service.
- Backend successfully received HTTP POST requests.
- Flask successfully connected to MySQL.
- Contact messages were successfully inserted into the MySQL `messages` table.
- Database records were verified using SQL queries.

## Deployment Environment

The Kubernetes cluster was configured using AWS EC2 instances with one control-plane node and two worker nodes.

The application components were deployed using Kubernetes YAML manifests.

**Note:** This is a hands-on learning and portfolio project, not a production-hardened deployment.

## Author

**Angeline Samritha**

GitHub: [Angelinesamritha1](https://github.com/Angelinesamritha1)
