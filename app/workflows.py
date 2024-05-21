import json
from typing import List, Optional
from .models import Workflow

class WorkflowManager:
    def __init__(self, config_file: str):
        self.config_file = config_file
        self.workflows = self.load_workflows()

    def load_workflows(self) -> List[Workflow]:
        with open(self.config_file, 'r') as file:
            config = json.load(file)
        return [Workflow(**wf) for wf in config['workflows']]

    def find_workflow(self, source: str) -> Optional[Workflow]:
        for workflow in self.workflows:
            if workflow.source == source:
                return workflow
        return None

    def add_workflow(self, workflow: Workflow):
        if workflow not in self.workflows:
            self.workflows.append(workflow)
            self.save_workflows()

    def save_workflows(self):
        with open(self.config_file, 'w') as file:
            json.dump({"workflows": [wf.model_dump() for wf in self.workflows]}, file)
