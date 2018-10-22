# -*- coding: utf-8 -*-
from __future__ import print_function
import requests
from requests.auth import HTTPBasicAuth

try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

from pyxinca.exceptions import (
    XincaError,
    XincaAuthenticationError,
    XincaAuthorizationError,
    XincaServerError,
)
from pyxinca import records

DELETE = 'DELETE'
GET = 'GET'
POST = 'POST'
PUT = 'PUT'
PATCH = 'PATCH'


class Xinca(object):
    """
    Xinca MDM API Class.
    Represent a connection to a Xinca MDM server.

    Usage:

    xinca = XincaBase(server='https://<url>', token='<token>')

    response = xinca.devices.list()
    """

    def __init__(self,
                 username=None,
                 password=None,
                 server='https://apiv6.xincamdm.com',
                 timeout=30,
                 session=None):
        """
        server: Base URI for Log Cabin web interface
        token: Auth Token string for Token-based Authorization
        timeout: optional connect and read timeout in seconds
        """

        self.server = server
        self.timeout = timeout

        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
            'User-Agent': 'PyXinca and Zuludesk API Wrapper/1.0',
            'X-Server-Protocol-Version': '3',
        }

        self.base_url = '{}'.format(server)
        self.url = self.base_url

        if session:
            self.session = session or requests.Session()
        else:
            self.session = requests.Session()
            if not username and password:
                raise ValueError('A Session or a Username and Password must be provided.')
            self.session.auth = HTTPBasicAuth(username, password)

        self.apps = records.Apps(self)
        self.dep = records.DEP(self)
        self.devices = records.Devices(self)
        self.users = records.Users(self)
        self.groups = records.Groups(self)
        self.profiles = records.Profiles(self)
        self.ibeacons = records.iBeacons(self)

    def http_list(self, path, params=None, **kwargs):
        """Make a GET request to the Xinca server.

        :param path: Path to resource (/devices, or /apps)
        :param params: Data to send as query parameters
        :type path: str
        :type params: dict

        Returns the parsed json returned by the server.
        """
        params = params or {}
        response = self.http_request(
            verb=GET,
            path=path,
            params=params,
            **kwargs)

        return response

    def http_get(self, path, params=None, **kwargs):
        """Make a GET request to the Xinca server.

        :param path: Path to resource (/devices/<udid>, or /apps/<id>)
        :param params: Data to send as query parameters
        :type path: str
        :type params: dict

        Returns the parsed json returned by the server.
        """
        params = params or {}
        response = self.http_request(
            verb=GET,
            path=path,
            params=params,
            **kwargs)

        return response

    def http_post(self, path, params=None, post_data=None, **kwargs):
        """Make a POST request to the Xinca server.

        :param path: Path to resource (/devices/<udid>, or /apps/<id>)
        :param params: Data to send as query parameters
        :param post_data: Data to send in the body (will be converted to json)
        :type path: str
        :type params: dict
        :type post_data: dict

        Returns the parsed json returned by the server.
        """
        params = params or {}
        post_data = post_data or {}
        response = self.http_request(
            verb=POST,
            path=path,
            params=params,
            post_data=post_data,
            **kwargs)

        return response

    def http_put(self, path, params=None, post_data=None, **kwargs):
        """Make a PUT request to the Xinca server.

        :param path: Path to resource (/devices/<udid>, or /apps/<id>)
        :param params: Data to send as query parameters
        :param post_data: Data to send in the body (will be converted to json)
        :type path: str
        :type params: dict
        :type post_data: dict

        Returns the parsed json returned by the server.
        """
        params = params or {}
        post_data = post_data or {}
        response = self.http_request(
            verb=PUT,
            path=path,
            params=params,
            post_data=post_data,
            **kwargs)

        return response

    def http_delete(self, path, **kwargs):
        """Make a DELETE request to the Xinca server.

        :param path: Path to resource (/devices/<udid>, or /apps/<id>)
        :type path: str
        """
        return self.http_request(DELETE, path, **kwargs)

    def http_request(self, verb, path, params=None, post_data=None, **kwargs):
        """Make an HTTP request to the Xinca server.

        :param verb: The HTTP method to call ('get', 'post', 'put', 'delete')
        :param path: Path or full URL to query (/devices, or /apps/<id>)
        :param params: Data to send as query parameters
        :param post_data: Data to send in the body (will be converted to json)
        :type verb: str
        :type path: str
        :type params: dict
        :type post_data: dict

        Returns a request result object.
        """
        params = params or {}
        url = '{}{}'.format(self.url, path)

        request = requests.Request(
            verb, url,
            params=params,
            data=post_data,
            headers=self.headers,
        )

        prepared = self.session.prepare_request(request)
        settings = self.session.merge_environment_settings(
            url, {},
            stream=False,
            verify=False,
            cert=None,
        )
        response = self.session.send(prepared, timeout=self.timeout, **settings)

        if not response.ok:
            try:
                msg = u','.join(response.json()['errors'])
            except (ValueError, TypeError, KeyError):
                if response.reason:
                    msg = response.reason
                else:
                    msg = u'{}: {}'.format(response.status_code, response.text)

            if response.status_code == 401:
                raise XincaAuthenticationError(msg, response=response)

            if response.status_code == 403:
                raise XincaAuthorizationError(msg, response=response)

            # let application code handle remaining 4xx codes
            if 400 <= response.status_code < 500:
                raise response

            raise XincaServerError(
                '{msg} {code}'.format(msg=msg, code=response.status_code), response=response
            )

        if response.status_code == 302:
            raise XincaError('Unexpected Redirect', response=response)

        return response

    def __str__(self):
        return 'Xinca MDM API - Server: {}'.format(self.url)

    def __repr__(self):
        return 'Xinca(server={}, token=<token>, timeout={})'.format(
            self.server, self.timeout
        )


__all__ = (
    'Xinca',
)
