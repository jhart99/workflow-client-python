from setuptools import setup
setup(name='kubernetes_workflow',
      version='0.1',
      description='Workflow for kubernetes',
      url='https://github.com/jhart99/workflow-client-python',
      author='Jonathan Ross Hart',
      author_email='jonathan@jonathanrosshart.com',
      license='Apache 2.0',
      packages=['kubernetes_workflow',
                'kubernetes_workflow.apis',
                'kubernetes_workflow.models'],
      zip_safe=False)
