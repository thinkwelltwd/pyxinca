# -*- coding: utf-8 -*-
from pyxinca.mixins import (
    UpdateMixin,
    DeleteMixin,
    CRUDMixin,
    ReadMixin,
)


class XincaRecord(object):
    """Base class for CRUD operations on Xinca Records.

    Subclasses class must define ``_path``.

    ``_path``: Base URL path on which requests will be sent (e.g. '/devices')
    """

    _path = None

    def __init__(self, xinca):
        """MDMObject manager constructor.

        :param xinca: `xinca.Xinca` connection to make requests
        """
        self.xinca = xinca

    @property
    def path(self):
        return self._path


class Apps(ReadMixin, XincaRecord):
    _path = '/apps'


class DEP(ReadMixin, UpdateMixin, XincaRecord):
    _path = '/dep'


class Devices(ReadMixin, DeleteMixin, XincaRecord):
    _path = '/devices'


class Profiles(ReadMixin, XincaRecord):
    _path = '/profiles'


class Users(CRUDMixin, XincaRecord):
    _path = '/users'


class Groups(CRUDMixin, XincaRecord):
    _path = '/user/groups'


class iBeacons(CRUDMixin, XincaRecord):
    _path = '/ibeacons'
