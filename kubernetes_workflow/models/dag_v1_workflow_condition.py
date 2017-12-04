# coding: utf-8

"""
Kubernetes workflow api
"""
from pprint import pformat
from six import iteritems


class DagV1WorkflowCondition(object):
    """
    Attributes:
        swagger_types (dict): The key is the attribute name
        and the value is the attribute type.
        attribute_map (dict): The key is the attribute name
        and the value is the json key in the definition.
    """
    swagger_types = {
        'type': 'string',
        'status': 'string',
        'last_time_probe': 'datetime',
        'last_transition_time': 'datetime',
        'reason': 'string',
        'message': 'string'
    }

    attribute_map = {
        'type': 'type',
        'status': 'status',
        'last_time_probe': 'lastTimeProbe',
        'last_transition_time': 'lastTransitionTime',
        'reason': 'reason',
        'message': 'message'
    }

    def __init__(self, type_=None, status=None, last_time_probe=None,
                 last_transition_time=None, reason=None, message=None):
        """
        DagV1WorkflowSpec
        """

        self._type_ = None
        self._status = None
        self._last_time_probe = None
        self._last_transition_time = None
        self._reason = None
        self._message = None

        if type_ is not None:
            self.type_ = type_
        if status is not None:
            self.status = status
        if last_time_probe is not None:
            self.last_time_probe = last_time_probe
        if last_transition_time is not None:
            self.last_transition_time = last_transition_time
        if reason is not None:
            self.reason = reason
        if message is not None:
            self.message = message

    @property
    def type_(self):
        """
        Gets the type_
        """

        return self._type_

    @type_.setter
    def type_(self, type_):
        """
        Sets the type_
        """
        self._type_ = type_

    @property
    def status(self):
        """
        Gets the status
        """

        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status
        """
        self._status = status

    @property
    def last_time_probe(self):
        """
        Gets the last_time_probe
        """

        return self._last_time_probe

    @last_time_probe.setter
    def last_time_probe(self, last_time_probe):
        """
        Sets the last_time_probe
        """
        self._last_time_probe = last_time_probe

    @property
    def last_transition_time(self):
        """
        Gets the last_transition_time
        """

        return self._last_transition_time

    @last_transition_time.setter
    def last_transition_time(self, last_transition_time):
        """
        Sets the last_transition_time
        """
        self._last_transition_time = last_transition_time

    @property
    def reason(self):
        """
        Gets the reason
        """

        return self._reason

    @reason.setter
    def reason(self, reason):
        """
        Sets the reason
        """
        self._reason = reason

    @property
    def message(self):
        """
        Gets the message
        """

        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message
        """
        self._message = message

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
        if not isinstance(other, DagV1WorkflowCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
