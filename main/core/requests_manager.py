"""Module for requests"""
import json
import requests
from requests import Session, Request
from requests_oauthlib import OAuth1
from main.core.utils.request_utils import RequestUtils as utils
from main.core.utils.api_constants import HttpMethods as method


class RequestsManager:
    """Request Manager basic Implementation"""

    __instance = None

    def __init__(self):
        self.basic_url = "https://api.trello.com/1"
        self.headers = {"Accept": "application/json"}
        self.auth = OAuth1('668fe425619b44578f6b5dd9a02e09a4',
                           'c96a92fc1940b3648744f19ab5bca9a3c49213dea7c08f8a5c8bb068b9674183',
                           'c96a92fc1940b3648744f19ab5bca9a3c49213dea7c08f8a5c8bb068b9674183',
                           '68665b1c48cc20381d1c7f3f75f80db7298cba95a02dbc86a564bf9890aa83e8')
        self.session = Session()
    
    @staticmethod
    def get_instance():
        """This method get a instance of the RequestsManager class.

        Returns:
            RequestManager -- return a instance of RequestsManager class.
        """
        if RequestsManager.__instance is None:
            RequestsManager.__instance = RequestsManager()
        return RequestsManager.__instance
    
    def do_request(self, http_method, endpoint, body=None, **kwargs):
        """Sends request

        :param http_method: HTTP method
        :type http_method: string
        :param endpoint: Application's endpoint method
        :type endpoint: obj
        """
        self.auth = kwargs.get("auth",self.auth)
        url = f"{self.basic_url}{endpoint}"
        if http_method == method.GET.value:
            response = self.session.request(http_method, url, headers=self.headers, auth=self.auth)
        elif http_method == method.DELETE.value:
            response = self.session.request(method.DELETE.value, 
                                            f"{url}/{kwargs.get('id')}",
                                            headers=self.headers, auth=self.auth)
        else:
            data = utils.generate_data(body)
            response = self.session.request(http_method, url, headers=self.headers,
                                        auth=self.auth, data=data)
        return response.status_code, response.json()

    def close_session(self):
        self.session.close()
