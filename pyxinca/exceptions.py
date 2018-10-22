# -*- coding: utf-8 -*-
from requests.exceptions import HTTPError


class XincaError(HTTPError):
    """A generic error while attempting to communicate with Xinca"""


class XincaServerError(XincaError):
    """The Xinca Server encountered an error while processing the request"""


class XincaAuthenticationError(XincaError):
    """Invalid authentication credentials"""


class XincaAuthorizationError(XincaError):
    """Credentials have inadequate authorization to perform operation"""
