import time
from WorkSSH import SSHClientOpenCart
from OpencartWeb import OpenCartWebSait

def test_restart_opecart_server(create_connect):
    client = SSHClientOpenCart(create_connect)
    client.restart_server()
    client.verify_status('active')
    time.sleep(3)
    web = OpenCartWebSait('http://192.168.1.78/opencart/')
    web.verify_page()



