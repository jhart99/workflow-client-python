# coding: utf-8

"""
Kubernetes workflow api
"""
from pprint import pformat
from six import iteritems


class DagV1WorkflowStep(object):
    """
    Attributes:
        swagger_types (dict): The key is the attribute name
        and the value is the attribute type.
        attribute_map (dict): The key is the attribute name
        and the value is the json key in the definition.
    """
    swagger_types = {
        'name': 'string',
        'job_template': 'V1beta1JobTemplateSpec',
        'external_ref': 'V1ObjectReference',
        'dependencies': 'list[string]'
    }

    attribute_map = {
        'name': 'name',
        'job_template': 'jobTemplate',
        'external_ref': 'externalRef',
        'dependencies': 'dependencies'
    }

    def __init__(self, name=None, job_template=None, external_ref=None,
                 dependencies=None):
        """
        DagV1WorkflowStep
        """

        self._name = None
        self._job_template = None
        self._external_ref = None
        self._dependencies = None

        if name is not None:
            self.name = name
        if job_template is not None:
            self.job_template = job_template
        if external_ref is not None:
            self.external_ref = external_ref
        if dependencies is not None:
            self.dependencies = dependencies

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
    def job_template(self):
        """
        Gets the job_template
        """

        return self._job_template

    @job_template.setter
    def job_template(self, job_template):
        """
        Sets the job_template
        """
        self._job_template = job_template

    @property
    def external_ref(self):
        """
        Gets the external_ref
        """

        return self._external_ref

    @external_ref.setter
    def external_ref(self, external_ref):
        """
        Sets the external_ref
        """
        self._external_ref = external_ref

    @property
    def dependencies(self):
        """
        Gets the dependencies
        """

        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """
        Sets the dependencies
        """
        self._dependencies = dependencies

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
        if not isinstance(other, DagV1WorkflowStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
