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


class TaskLinks(object):
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
        '_self': 'str',
        'owners': 'str',
        'members': 'str',
        'runs': 'str',
        'logs': 'str',
        'labels': 'str'
    }

    attribute_map = {
        '_self': 'self',
        'owners': 'owners',
        'members': 'members',
        'runs': 'runs',
        'logs': 'logs',
        'labels': 'labels'
    }

    def __init__(self, _self=None, owners=None, members=None, runs=None, logs=None, labels=None):  # noqa: E501,D401,D403
        """TaskLinks - a model defined in OpenAPI."""  # noqa: E501
        self.__self = None
        self._owners = None
        self._members = None
        self._runs = None
        self._logs = None
        self._labels = None
        self.discriminator = None

        if _self is not None:
            self._self = _self
        if owners is not None:
            self.owners = owners
        if members is not None:
            self.members = members
        if runs is not None:
            self.runs = runs
        if logs is not None:
            self.logs = logs
        if labels is not None:
            self.labels = labels

    @property
    def _self(self):
        """Get the _self of this TaskLinks.

        URI of resource.

        :return: The _self of this TaskLinks.
        :rtype: str
        """  # noqa: E501
        return self.__self

    @_self.setter
    def _self(self, _self):
        """Set the _self of this TaskLinks.

        URI of resource.

        :param _self: The _self of this TaskLinks.
        :type: str
        """  # noqa: E501
        self.__self = _self

    @property
    def owners(self):
        """Get the owners of this TaskLinks.

        URI of resource.

        :return: The owners of this TaskLinks.
        :rtype: str
        """  # noqa: E501
        return self._owners

    @owners.setter
    def owners(self, owners):
        """Set the owners of this TaskLinks.

        URI of resource.

        :param owners: The owners of this TaskLinks.
        :type: str
        """  # noqa: E501
        self._owners = owners

    @property
    def members(self):
        """Get the members of this TaskLinks.

        URI of resource.

        :return: The members of this TaskLinks.
        :rtype: str
        """  # noqa: E501
        return self._members

    @members.setter
    def members(self, members):
        """Set the members of this TaskLinks.

        URI of resource.

        :param members: The members of this TaskLinks.
        :type: str
        """  # noqa: E501
        self._members = members

    @property
    def runs(self):
        """Get the runs of this TaskLinks.

        URI of resource.

        :return: The runs of this TaskLinks.
        :rtype: str
        """  # noqa: E501
        return self._runs

    @runs.setter
    def runs(self, runs):
        """Set the runs of this TaskLinks.

        URI of resource.

        :param runs: The runs of this TaskLinks.
        :type: str
        """  # noqa: E501
        self._runs = runs

    @property
    def logs(self):
        """Get the logs of this TaskLinks.

        URI of resource.

        :return: The logs of this TaskLinks.
        :rtype: str
        """  # noqa: E501
        return self._logs

    @logs.setter
    def logs(self, logs):
        """Set the logs of this TaskLinks.

        URI of resource.

        :param logs: The logs of this TaskLinks.
        :type: str
        """  # noqa: E501
        self._logs = logs

    @property
    def labels(self):
        """Get the labels of this TaskLinks.

        URI of resource.

        :return: The labels of this TaskLinks.
        :rtype: str
        """  # noqa: E501
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Set the labels of this TaskLinks.

        URI of resource.

        :param labels: The labels of this TaskLinks.
        :type: str
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
        if not isinstance(other, TaskLinks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
