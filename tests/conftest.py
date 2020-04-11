import pytest
import paramiko

@pytest.fixture
def create_connect():
    con_data = {'host':'192.168.1.78',
                'port': 22,
                'login':'vb',
                'pas':'qq1234'}

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
    client.connect(hostname=con_data['host'],
                   username=con_data['login'],
                   password=con_data['pas'],
                   port=con_data['port'])

    yield client
    client.close()
