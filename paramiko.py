import paramiko
ssh= paramiko.SSHClient()
ssh.seet_missing_host_key_polic(paramiko.AutoAddPolicy())
ssh.connect("10.10.10.10 ",username="msfadmin",password="msfadmin")
stdint(stdout.read())