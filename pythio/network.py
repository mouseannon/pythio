import requests


class Network:

    def __init__(self, token: str, proxy: str, timeout: float):
        self.token: str = token
        self.proxy: str = proxy
        self.timeout: float = timeout
        self.session = requests.session()

    @property
    def url(self) -> str:
        return f'https://api.telegram.org/bot{self.token}/'

    def disconnect(self):
        return self.session.close()

    async def connect(self, method: str, data: dict = None, files: dict = None) -> requests.Response:
        responce = (
            self.session.request(
                'post',
                url=self.url + method,
                timeout=self.timeout, data=data, files=files, proxies=self.proxy
            )
        )
        if responce.status_code != requests.codes.ok:
            raise Exception(responce.status_code, responce.text)

        final_value = responce.json()
        return final_value['result']
