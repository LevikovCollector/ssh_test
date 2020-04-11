import requests

class OpenCartWebSait:
    def __init__(self, url):
        self.url = url

    def get_url(self):
        respons = requests.get(self.url)
        return respons

    def verify_page(self):
        respons = self.get_url()
        assert respons.status_code == 200
        assert respons.text != ''
