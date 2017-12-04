# coding: utf-8

"""
Kubernetes workflow api
"""
from pprint import pformat
from six import iteritems


class DagV1WorkflowStepStatus(object):
    """
    Attributes:
        swagger_types (dict): The key is the attribute name
        and the value is the attribute type.
        attribute_map (dict): The key is the attribute name
        and the value is the json key in the definition.
    """
    swagger_types = {
        'name': 'string',
        'complete': 'boolean',
        'reference': 'V1ObjectReference'
    }

    attribute_map = {
        'name': 'name',
        'complete': 'complete',
        'reference': 'reference'
    }

    def __init__(self, name=None, complete=None, reference=None):
        """
        DagV1WorkflowStepStatus
        """

        self._name = None
        self._complete = None
        self._reference = None

        if name is not None:
            self.name = name
        if complete is not None:
            self.complete = complete
        if reference is not None:
            self.reference = reference

    @property
    def name(self):
        """
        Gets the name
        """

        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name
        """
        self._name = name

    @property
    def complete(self):
        """
        Gets the complete
        """

        return self._complete

    @complete.setter
    def complete(self, complete):
        """
        Sets the complete
        """
        self._complete = complete

    @property
    def reference(self):
        """
        Gets the reference
        """

        return self._reference

    @reference.setter
    def reference(self, reference):
        """
        Sets the reference
        """
        self._reference = reference

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
        if not isinstance(other, DagV1WorkflowStepStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
