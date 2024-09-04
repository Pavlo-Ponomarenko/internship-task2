import paramiko

class VirtualMaschine:

    host = '127.0.0.1'
    username = 'vagrant'
    password = 'vagrant'

    def __init__(self, name, port):
        self.name = name
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(hostname=self.host, port=port, username=self.username, password=self.password)

    def pull_logs(self):
        _, stdout, err = self.client.exec_command('cat ../sftp/logfile.log')
        logs = stdout.read().decode()
        self.client.exec_command('sudo chown vagrant ../sftp/logfile.log')
        self.client.exec_command("sudo echo '' > ../sftp/logfile.log")
        return logs