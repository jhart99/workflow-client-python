# coding: utf-8

"""
Kubernetes workflow api
"""
from pprint import pformat
from six import iteritems


class DagV1WorkflowStatus(object):
    """
    Attributes:
        swagger_types (dict): The key is the attribute name
        and the value is the attribute type.
        attribute_map (dict): The key is the attribute name
        and the value is the json key in the definition.
    """
    swagger_types = {
        'conditions': 'list[DagV1WorkflowCondtion]',
        'start_time': 'datetime',
        'completion_time': 'datetime',
        'statuses': 'list[DagV1WorkflowStepStatus]'
    }

    attribute_map = {
        'conditions': 'conditions',
        'start_time': 'startTime',
        'completion_time': 'completionTime',
        'statuses': 'statuses'
    }

    def __init__(self, conditions=None, start_time=None,
                 completion_time=None, statuses=None):
        """
        DagV1WorkflowStatuses
        """

        self._conditions = None
        self._start_time = None
        self._completion_time = None
        self._statuses = None

        if conditions is not None:
            self.conditions = conditions
        if start_time is not None:
            self.start_time = start_time
        if completion_time is not None:
            self.completion_time = completion_time
        if statuses is not None:
            self.statuses = statuses

    @property
    def conditions(self):
        """
        Gets the conditions
        """

        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """
        Sets the conditions
        """
        self._conditions = conditions

    @property
    def start_time(self):
        """
        Gets the start_time
        """

        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """
        Sets the start_time
        """
        self._start_time = start_time

    @property
    def completion_time(self):
        """
        Gets the completion_time
        """

        return self._completion_time

    @completion_time.setter
    def completion_time(self, completion_time):
        """
        Sets the completion_time
        """
        self._completion_time = completion_time

    @property
    def statuses(self):
        """
        Gets the statuses
        """

        return self._statuses

    @statuses.setter
    def statuses(self, statuses):
        """
        Sets the statuses
        """
        self._statuses = statuses

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
        if not isinstance(other, DagV1WorkflowStatus):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
