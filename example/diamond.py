"""
The diamond example from workflows recreated using the python interface
"""

from pprint import pprint
from kubernetes import client, config
from kubernetes_workflow.apis import WorkflowV1Api
from kubernetes_workflow.models import (
    DagV1Workflow, DagV1WorkflowStep, DagV1WorkflowSpec)


def create_workflow_object():
    """
    Creates the diamond DAG from the workflow examples
    Looks something like this where we flow from left to right
    one -> (two, three) -> four
    """
    container = client.V1Container(
        name="busybox",
        image="gcr.io/google-containers/busybox",
        command=["sh", "-c",
                 "echo Starting on: $(date); sleep 5; \
                 echo Goodbye cruel world at: $(date)"])
    stepone = DagV1WorkflowStep(
        name="stepone",
        job_template=client.V1beta1JobTemplateSpec(
            spec=client.V1JobSpec(
                template=client.V1PodTemplateSpec(
                    metadata=client.V1ObjectMeta(
                        labels={"workflow": "stepone"}),
                    spec=client.V1PodSpec(
                        containers=[container],
                        restart_policy="Never")))))
    steptwo = DagV1WorkflowStep(
        name="steptwo",
        dependencies=['stepone'],
        job_template=client.V1beta1JobTemplateSpec(
            spec=client.V1JobSpec(
                template=client.V1PodTemplateSpec(
                    metadata=client.V1ObjectMeta(
                        labels={"workflow": "steptwo"}),
                    spec=client.V1PodSpec(
                        containers=[container],
                        restart_policy="Never")))))
    stepthree = DagV1WorkflowStep(
        name="stepthree",
        dependencies=['stepone'],
        job_template=client.V1beta1JobTemplateSpec(
            spec=client.V1JobSpec(
                template=client.V1PodTemplateSpec(
                    metadata=client.V1ObjectMeta(
                        labels={"workflow": "stepthree"}),
                    spec=client.V1PodSpec(
                        containers=[container],
                        restart_policy="Never")))))
    stepfour = DagV1WorkflowStep(
        name="stepfour",
        dependencies=['steptwo', 'stepthree'],
        job_template=client.V1beta1JobTemplateSpec(
            spec=client.V1JobSpec(
                template=client.V1PodTemplateSpec(
                    metadata=client.V1ObjectMeta(
                        labels={"workflow": "stepfour"}),
                    spec=client.V1PodSpec(
                        containers=[container],
                        restart_policy="Never")))))

    workflow = DagV1Workflow(metadata=client.V1ObjectMeta(name="diamond"),
                             spec=DagV1WorkflowSpec(
                                 selector=client.V1LabelSelector(
                                     match_labels={"workflow": "diamond"}),
                                 steps=[stepone, steptwo,
                                        stepthree, stepfour]))
    return workflow


def main():
    """
    The flow of configuring the API interface, creating the workflow
    and submitting the Workflow

    """
    config.load_kube_config()
    coa = WorkflowV1Api()
    workflow = create_workflow_object()
    api_response = coa.create_namespaced_workflow("default", workflow)
    pprint(api_response)


if __name__ == '__main__':
    main()
