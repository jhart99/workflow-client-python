# coding: utf-8

"""
Kubernetes workflow api
"""

from kubernetes import client


class WorkflowV1Api(client.CustomObjectsApi):
    """
    Kubernetes workflow Api
    """
    def create_namespaced_workflow(self, namespace, body, **kwargs):
        """
        create a workflow
        This method makes a workflow
        :param str namespace: object name and auth scope, such as for teams
        and projects (required)
        :param  body: required
        """
        api_response = self.create_namespaced_custom_object(
            "dag.example.com", "v1", namespace, "workflows", body, **kwargs)
        return api_response

    def delete_namespaced_workflow(self, namespace, name, body, **kwargs):
        """
        delete a workflow
        This method deletes a workflow
        :param str namespace: object name and auth scope, such as for teams
        and projects (required)
        :param  name: required
        :param  body: required
        """
        api_response = self.delete_namespaced_custom_object(
            "dag.example.com", "v1", namespace, "workflows",
            name, body, **kwargs)
        return api_response

    def get_namespaced_workflow(self, namespace, name, **kwargs):
        """
        get a workflow
        This method gets a workflow
        :param str namespace: object name and auth scope, such as for teams
        and projects (required)
        :param  body: required
        """
        api_response = self.create_namespaced_custom_object(
            "dag.example.com", "v1", namespace, "workflows", name, **kwargs)
        return api_response

    def list_namespaced_workflow(self, namespace, **kwargs):
        """
        list workflows
        This method lists all workflows in a namespace
        :param str namespace: object name and auth scope, such as for teams
        and projects (required)
        """
        api_response = self.list_namespaced_custom_object(
            "dag.example.com", "v1", namespace, "workflows", **kwargs)
        return api_response

    def replace_namespaced_workflow(self, namespace, name, body, **kwargs):
        """
        replace workflow
        This method replaces a workflow in a namespace
        :param str namespace: object name and auth scope, such as for teams
        and projects (required)
        """
        api_response = self.replace_namespaced_custom_object(
            "dag.example.com", "v1", namespace, "workflows",
            name, body, **kwargs)
        return api_response
