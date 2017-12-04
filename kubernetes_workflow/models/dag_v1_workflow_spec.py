# coding: utf-8

"""
Kubernetes workflow api
"""
from pprint import pformat
from six import iteritems


class DagV1WorkflowSpec(object):
    """
    Attributes:
        swagger_types (dict): The key is the attribute name
        and the value is the attribute type.
        attribute_map (dict): The key is the attribute name
        and the value is the json key in the definition.
    """
    swagger_types = {
        'active_deadline_seconds': 'int',
        'steps': 'list[DagV1WorkflowStep]',
        'selector': 'V1LabelSelector'
    }

    attribute_map = {
        'active_deadline_seconds': 'activeDeadlineSeconds',
        'steps': 'steps',
        'selector': 'selector'
    }

    def __init__(self, active_deadline_seconds=None,
                 steps=None, selector=None):
        """
        DagV1WorkflowSpec
        """

        self._active_deadline_seconds = None
        self._steps = None
        self._selector = None

        if active_deadline_seconds is not None:
            self.active_deadline_seconds = active_deadline_seconds
        if steps is not None:
            self.steps = steps
        if selector is not None:
            self.selector = selector

    @property
    def active_deadline_seconds(self):
        """
        Gets the active_deadline_seconds
        """

        return self._active_deadline_seconds

    @active_deadline_seconds.setter
    def active_deadline_seconds(self, active_deadline_seconds):
        """
        Sets the active_deadline_seconds
        """
        self._active_deadline_seconds = active_deadline_seconds

    @property
    def steps(self):
        """
        Gets the steps
        """

        return self._steps

    @steps.setter
    def steps(self, steps):
        """
        Sets the steps
        """
        self._steps = steps

    @property
    def selector(self):
        """
        Gets the selector
        """

        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector
        """
        self._selector = selector

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
        if not isinstance(other, DagV1WorkflowSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
