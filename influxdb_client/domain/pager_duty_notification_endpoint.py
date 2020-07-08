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
from influxdb_client.domain.notification_endpoint import NotificationEndpoint


class PagerDutyNotificationEndpoint(NotificationEndpoint):
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
        'client_url': 'str',
        'routing_key': 'str'
    }

    attribute_map = {
        'client_url': 'clientURL',
        'routing_key': 'routingKey'
    }

    def __init__(self, client_url=None, routing_key=None):  # noqa: E501,D401,D403
        """PagerDutyNotificationEndpoint - a model defined in OpenAPI."""  # noqa: E501
        NotificationEndpoint.__init__(self)  # noqa: E501

        self._client_url = None
        self._routing_key = None
        self.discriminator = None

        self.client_url = client_url
        self.routing_key = routing_key

    @property
    def client_url(self):
        """Get the client_url of this PagerDutyNotificationEndpoint.

        :return: The client_url of this PagerDutyNotificationEndpoint.
        :rtype: str
        """  # noqa: E501
        return self._client_url

    @client_url.setter
    def client_url(self, client_url):
        """Set the client_url of this PagerDutyNotificationEndpoint.

        :param client_url: The client_url of this PagerDutyNotificationEndpoint.
        :type: str
        """  # noqa: E501
        if client_url is None:
            raise ValueError("Invalid value for `client_url`, must not be `None`")  # noqa: E501
        self._client_url = client_url

    @property
    def routing_key(self):
        """Get the routing_key of this PagerDutyNotificationEndpoint.

        :return: The routing_key of this PagerDutyNotificationEndpoint.
        :rtype: str
        """  # noqa: E501
        return self._routing_key

    @routing_key.setter
    def routing_key(self, routing_key):
        """Set the routing_key of this PagerDutyNotificationEndpoint.

        :param routing_key: The routing_key of this PagerDutyNotificationEndpoint.
        :type: str
        """  # noqa: E501
        if routing_key is None:
            raise ValueError("Invalid value for `routing_key`, must not be `None`")  # noqa: E501
        self._routing_key = routing_key

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
        if not isinstance(other, PagerDutyNotificationEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Return true if both objects are not equal."""
        return not self == other
