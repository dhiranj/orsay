# tests/test_main.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 
import unittest
from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime

client = TestClient(app)

class TestMain(unittest.TestCase):

    def test_get_workflows(self):
        response = client.get("/workflows")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_workflow(self):
        new_workflow = {
            "source": "LinkedIn",
            "persona": "Eva",
            "channel": "Email"
        }
        response = client.post("/workflows", json=new_workflow)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), new_workflow)

    def test_process_lead(self):
    
        new_workflow = {
            "source": "Salesforce",
            "persona": "Sofia",
            "channel": "Whatsapp"
        }
        client.post("/workflows", json=new_workflow)

        lead = {
            "source": "Salesforce",
            "name": "Alice",
            "timestamp": datetime.now().timestamp()
        }
        response = client.post("/leads", json=lead)
        self.assertEqual(response.status_code, 200)
        expected_message = "Sofia is sending a message to Alice via Whatsapp"
        self.assertEqual(response.json()["message_response"]["message"], expected_message)

    def test_process_lead_invalid_timestamp(self):
        # Future timestamp
        future_lead = {
            "source": "Salesforce",
            "name": "Alice",
            "timestamp": datetime(3000, 1, 1).timestamp()
        }
        response = client.post("/leads", json=future_lead)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

        # Before epoch timestamp
        past_lead = {
            "source": "Salesforce",
            "name": "Alice",
            "timestamp": -1
        }
        response = client.post("/leads", json=past_lead)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_create_workflow_invalid_source(self):
        new_workflow = {
            "source": "InvalidSource",
            "persona": "Eva",
            "channel": "Email"
        }
        response = client.post("/workflows", json=new_workflow)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

    def test_create_workflow_invalid_persona(self):
        new_workflow = {
            "source": "LinkedIn",
            "persona": "InvalidPersona",
            "channel": "Email"
        }
        response = client.post("/workflows", json=new_workflow)
        self.assertEqual(response.status_code, 422)  # Unprocessable Entity

if __name__ == '__main__':
    unittest.main()
