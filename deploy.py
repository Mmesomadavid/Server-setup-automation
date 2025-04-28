import paramiko
import time

def ssh_connect(ip, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, username=username, password=password)
        return ssh
    except Exception as e:
        print(f"Connection failed: {e}")
        return None

def execute_command(ssh, command, password=None):
    if "sudo" in command and password:
        command = f"echo {password} | sudo -S {command[5:]}"  # remove 'sudo' and prefix with echo password
    stdin, stdout, stderr = ssh.exec_command(command)
    if password and "sudo" in command:
        stdin.write(password + "\n")
        stdin.flush()
    print(f"Executing: {command}")
    print(stdout.read().decode())
    print(stderr.read().decode())

def install_software(ssh, password):
    commands = [
        "sudo apt update",
        "sudo apt install -y docker.io",
        "sudo apt install -y git",
        "sudo apt install -y nginx",
        "sudo systemctl enable --now docker",
        "sudo systemctl enable --now nginx"
    ]
    for command in commands:
        execute_command(ssh, command, password=password)
        time.sleep(2)

def clone_repo(ssh, repo_url):
    command = f"git clone {repo_url} /home/your-username/app"
    execute_command(ssh, command)

def deploy_flask_app(ssh):
    commands = [
        "cd /home/your-username/app && docker build -t flask-app .",
        "docker run -d -p 5000:5000 flask-app"
    ]
    for command in commands:
        execute_command(ssh, command)

def main():
    ip = "your-server-ip"  # Example: "192.168.1.100"
    username = "your-ssh-username"  # Example: "ubuntu"
    password = "your-ssh-password"  # Provide the SSH password
    repo_url = "your-github-repo-url"  # Example: "https://github.com/yourname/yourrepo.git"

    ssh = ssh_connect(ip, username, password)

    if ssh:
        install_software(ssh, password)
        clone_repo(ssh, repo_url)
        deploy_flask_app(ssh)
        print("Yayy, Deployment is Successful!")
        ssh.close()

if __name__ == "__main__":
    main()
