import re


class SSHClientOpenCart:

    def __init__(self, ssh_client):
        self.client = ssh_client
        self.__sudo_pas = 'qq1234\n'
        self.status_template = "Active: [a-z]+"

    def restart_server(self):
        stdin, stdout, stderr = self.client.exec_command('sudo -S systemctl restart apache2')
        self.__sudo_auth(stdin)


    def __sudo_auth(self, stdin):
        stdin.write(self.__sudo_pas)
        stdin.flush()

    def server_status(self):
        stdin, stdout, stderr = self.client.exec_command('systemctl status apache2')
        data = (stdout.read()).decode('utf-8')
        return data

    def verify_status(self, expected_status):
        req_status = self.server_status()
        status = re.search(self.status_template, req_status).group(0).split(':')[1].strip()
        assert status == expected_status