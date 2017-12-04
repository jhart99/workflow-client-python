# coding: utf-8

"""
Kubernetes workflow api
"""
from pprint import pformat
from six import iteritems


class DagV1WorkflowList(object):
    """
    Attributes:
        swagger_types (dict): The key is the attribute name
        and the value is the attribute type.
        attribute_map (dict): The key is the attribute name
        and the value is the json key in the definition.
    """
    swagger_types = {
        'metadata': 'V1ObjectMeta',
        'items': 'list[DagV1Workflow]'
    }

    attribute_map = {
        'metadata': 'metadata',
        'items': 'items'
    }

    def __init__(self, metadata=None, items=None):
        """
        DagV1WorkflowList
        """

        self._metadata = None
        self._items = None

        if metadata is not None:
            self.metadata = metadata
        if items is not None:
            self.items = items

    @property
    def metadata(self):
        """
        Gets the metadata
        """

        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata
        """
        self._metadata = metadata

    @property
    def items(self):
        """
        Gets the items
        """

        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items
        """
        self._items = items

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}
        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, DagV1WorkflowList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
