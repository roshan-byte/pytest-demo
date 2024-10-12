import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
pem_file_path = '/home/roshan/Documents/Devops course/aws_slave.pem'

def connect(hostname, username):
    key = paramiko.RSAKey.from_private_key_file(pem_file_path)
    ssh.connect(hostname=hostname, username=username, pkey=key)
    return ssh

