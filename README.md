# 🚀 Automated Server Provisioning and Flask App Deployment with Python

This project is a **Python automation script** that connects to a remote Linux server via **SSH**, installs necessary software (**Docker**, **Git**, **Nginx**), pulls a web application from **GitHub**, and deploys it inside a Docker container — **all automatically**.

---

## 📋 Project Features

- **SSH Connection** to a remote server using `paramiko`
- **Automated Software Installation** (Docker, Git, Nginx)
- **Automatic GitHub Code Cloning** to the server
- **Flask App Deployment** inside Docker
- **Zero manual steps** after running the script
- **Clear logs and error outputs** for all operations
- **Infrastructure as Code (IaC)** simplified with Python scripting

---

## 🛠 Technologies Used

- Python 3
- Paramiko (Python SSH library)
- Docker
- Git
- Nginx
- Ubuntu Linux

---

## ⚙️ How It Works

1. **Connects via SSH** to a remote Ubuntu server.
2. **Installs** Docker, Git, and Nginx automatically.
3. **Clones** a specified GitHub repository containing a Flask app and Dockerfile.
4. **Builds** the Docker image.
5. **Runs** the Flask application inside a Docker container.

---

## 📦 Prerequisites

Before you run this script, make sure:

- Python 3 is installed locally.
- `paramiko` Python library is installed (`pip install paramiko`).
- You have:
  - Server IP address
  - Server username and password
  - SSH access enabled (port 22 open)
- Your GitHub repository has:
  - A `Dockerfile`
  - Flask application files

---

## 🚀 How to Use

1. **Clone this Repository** (or copy the script).
2. **Edit the `main()` function** to set:
   - `ip`: your server’s IP address
   - `username`: your server’s username
   - `password`: your server’s password
   - `repo_url`: link to your GitHub repository
3. **Run the script**:

```bash
python3 deploy.py
