# coding: utf-8

"""
Influx API Service.

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

OpenAPI spec version: 0.1.0
Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six
from influxdb_client.domain.create_dashboard_request import CreateDashboardRequest


class Dashboard(CreateDashboardRequest):
    """NOTE: This class is auto generated by OpenAPI Generator.

    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'links': 'object',
        'id': 'str',
        'meta': 'object',
        'cells': 'list[Cell]',
        'labels': 'list[Label]',
        'org_id': 'str',
        'name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'links': 'links',
        'id': 'id',
        'meta': 'meta',
        'cells': 'cells',
        'labels': 'labels',
        'org_id': 'orgID',
        'name': 'name',
        'description': 'description'
    }

    def __init__(self, links=None, id=None, meta=None, cells=None, labels=None, org_id=None, name=None, description=None):  # noqa: E501,D401,D403
        """Dashboard - a model defined in OpenAPI."""  # noqa: E501
        CreateDashboardRequest.__init__(self, org_id=org_id, name=name, description=description)  # noqa: E501

        self._links = None
        self._id = None
        self._meta = None
        self._cells = None
        self._labels = None
        self.discriminator = None

        if links is not None:
            self.links = links
        if id is not None:
            self.id = id
        if meta is not None:
            self.meta = meta
        if cells is not None:
            self.cells = cells
        if labels is not None:
            self.labels = labels

    @property
    def links(self):
        """Get the links of this Dashboard.

        :return: The links of this Dashboard.
        :rtype: object
        """  # noqa: E501
        return self._links

    @links.setter
    def links(self, links):
        """Set the links of this Dashboard.

        :param links: The links of this Dashboard.
        :type: object
        """  # noqa: E501
        self._links = links

    @property
    def id(self):
        """Get the id of this Dashboard.

        :return: The id of this Dashboard.
        :rtype: str
        """  # noqa: E501
        return self._id

    @id.setter
    def id(self, id):
        """Set the id of this Dashboard.

        :param id: The id of this Dashboard.
        :type: str
        """  # noqa: E501
        self._id = id

    @property
    def meta(self):
        """Get the meta of this Dashboard.

        :return: The meta of this Dashboard.
        :rtype: object
        """  # noqa: E501
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Set the meta of this Dashboard.

        :param meta: The meta of this Dashboard.
        :type: object
        """  # noqa: E501
        self._meta = meta

    @property
    def cells(self):
        """Get the cells of this Dashboard.

        :return: The cells of this Dashboard.
        :rtype: list[Cell]
        """  # noqa: E501
        return self._cells

    @cells.setter
    def cells(self, cells):
        """Set the cells of this Dashboard.

        :param cells: The cells of this Dashboard.
        :type: list[Cell]
        """  # noqa: E501
        self._cells = cells

    @property
    def labels(self):
        """Get the labels of this Dashboard.

        :return: The labels of this Dashboard.
        :rtype: list[Label]
        """  # noqa: E501
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Set the labels of this Dashboard.

        :param labels: The labels of this Dashboard.
        :type: list[Label]
        """  # noqa: E501
        self._labels = labels

    def to_dict(self):
        """Return the model properties as a dict."""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Return the string representation of the model."""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`."""
        return self.to_str()

    def __eq__(self, other):
        """Return true if both objects are equal."""
        if not isinstance(other, Dashboard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
