import logging

def mock_send_message(persona, channel, lead):
    """
    Mock function to simulate sending a message via a messaging platform.
    """
    message = f"{persona} is sending a message to {lead['name']} via {channel}"
    logging.info(message)
    print(message)
    return {"status": "success", "message": message}

def mock_crm_integration(lead):
    """
    Mock function to simulate CRM integration.
    """
    logging.info(f"Lead {lead['name']} from {lead['source']} integrated with CRM.")
    print(f"Lead {lead['name']} from {lead['source']} integrated with CRM.")
    return {"status": "success", "message": "Lead integrated with CRM"}
