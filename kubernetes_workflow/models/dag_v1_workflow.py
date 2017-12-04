# coding: utf-8

"""
Kubernetes workflow api
"""
from pprint import pformat
from six import iteritems


class DagV1Workflow(object):
    """
    Attributes:
        swagger_types (dict): The key is the attribute name
        and the value is the attribute type.
        attribute_map (dict): The key is the attribute name
        and the value is the json key in the definition.
    """
    swagger_types = {
        'api_version': 'str',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'spec': 'DagV1WorkflowSpec',
        'status': 'DagV1WorkflowStatus'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'kind': 'kind',
        'metadata': 'metadata',
        'spec': 'spec',
        'status': 'status'
    }

    def __init__(self, api_version="dag.example.com/v1", kind="Workflow",
                 metadata=None, spec=None, status=None):
        """
        DagV1Workflow
        """

        self._api_version = None
        self._kind = None
        self._metadata = None
        self._spec = None
        self._status = None

        if api_version is not None:
            self.api_version = api_version
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status

    @property
    def api_version(self):
        """
        Gets the api_version
        """

        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """
        Sets the api version
        """
        self._api_version = api_version

    @property
    def kind(self):
        """
        Gets the kind
        """

        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind
        """
        self._kind = kind

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
    def spec(self):
        """
        Gets the spec
        """

        return self._spec

    @spec.setter
    def spec(self, spec):
        """
        Sets the spec
        """
        self._spec = spec

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
        if not isinstance(other, DagV1Workflow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
