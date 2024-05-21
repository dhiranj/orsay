from fastapi import FastAPI, HTTPException
from typing import List
from .models import Lead, Workflow
from .workflows import WorkflowManager
from .mock_service import mock_send_message, mock_crm_integration
import logging

logging.basicConfig(filename='workflow.log', level=logging.INFO)

app = FastAPI()
workflow_manager = WorkflowManager('workflows.json')

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Sales Agent System"}

@app.get("/workflows", response_model=List[Workflow])
def get_workflows():
    return workflow_manager.workflows

@app.post("/workflows", response_model=Workflow)
def create_workflow(workflow: Workflow):
    workflow_manager.add_workflow(workflow)
    return workflow

@app.post("/leads")
def process_lead(lead: Lead):
    workflow = workflow_manager.find_workflow(lead.source)
    if workflow:
        # Mock CRM integration
        crm_response = mock_crm_integration(lead.model_dump())
        # Mock sending a message via the specified channel
        message_response = mock_send_message(workflow.persona, workflow.channel, lead.model_dump())
        logging.info(f"Processed lead {lead.name} from {lead.source} using {workflow.persona} via {workflow.channel}")
        return {
            "crm_response": crm_response,
            "message_response": message_response
        }
    else:
        raise HTTPException(status_code=404, detail="No workflow found for this lead source")
