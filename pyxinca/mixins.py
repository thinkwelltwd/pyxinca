# -*- coding: utf-8 -*-


class CreateMixin(object):

    def create(self, data, params=None, **kwargs):
        """
        Create a new record.

        :param data: Data to send to the server to create the resource
        :param params: Data to send as query parameters
        :param kwargs: Extra options to send to the server
        :return: dictionary of record
        """
        path = kwargs.pop('path', None) or self.path
        obj = self.xinca.http_post(path, post_data=data, params=params, **kwargs)

        return obj.json()


class GetMixin(object):

    def get(self, oid, params=None, **kwargs):
        """
        Get a single record

        :param oid: ID, such as serial number, udid or numerical ID
        :param params: Data to send as query parameters
        :param kwargs: Extra options to send to the server
        :return: dictionary of record
        """
        path = kwargs.pop('path', None)
        if not path:
            path = '{}/{}'.format(self.path, oid)
        obj = self.xinca.http_get(path, params=params, **kwargs)

        return obj.json()


class ListMixin(object):

    def list(self, params=None, **kwargs):
        """
        Get list of all record.

        :param params: Data to send as query parameters
        :param kwargs: Extra options to send to the server
        :return: list of record dictionaries
        """
        path = kwargs.pop('path', None) or self.path
        obj = self.xinca.http_get(path, params=params, **kwargs)

        return obj.json()


class UpdateMixin(object):

    def update(self, oid, data, params=None, **kwargs):
        """
        Update a single record

        :param data: Data to send to the server to create the resource
        :param oid: ID, such as serial number, udid or numerical ID
        :param params: Data to send as query parameters
        :param kwargs: Extra options to send to the server
        :return: dictionary of record
        """
        path = kwargs.pop('path', None)
        if not path:
            path = '{}/{}'.format(self.path, oid)
        obj = self.xinca.http_put(path, params=params, post_data=data, **kwargs)

        return obj.json()


class DeleteMixin(object):

    def delete(self, oid):
        """
        Delete the record

        :param oid: ID, such as serial number, udid or numerical ID
        """
        path = '{}/{}'.format(self.path, oid)
        self.xinca.http_delete(path)


class CRUDMixin(CreateMixin, GetMixin, ListMixin, UpdateMixin, DeleteMixin):
    pass


class ReadMixin(GetMixin, ListMixin):
    pass
