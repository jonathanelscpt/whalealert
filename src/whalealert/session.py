from base64 import b64encode
from requests import Session


__all__ = ['WhaleAlertAPISession']


class WhaleAlertAPISession(Session):

    def __init__(self):
        """
        Creates a new WhaleAlertAPISession instance.
        """
        super().__init__()

        self.headers.update({
            'Accept-Charset': 'utf-8',
            'Content-Type': 'text/plain',
        })

    def init_auth(self, api_key):
        self.headers.update({
            'X-WA-API-KEY': f'{api_key}'
        })
