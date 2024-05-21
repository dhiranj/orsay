# AI Sales Agent System

This system dynamically manages different workflows for handling leads based on their sources.

## Components

1. **Workflow Configuration**: Defines the workflows in `workflows.json`.
2. **Workflow Manager**: Simple service that loads and saves workflows (`workflows.py`).
3. **Tests**: Check leads processing for different cases (`tests_main.py`).
4. **Logging**: Logs the processing of leads (`workflow.log`).

## Prerequisites
Python 3.10 or higher

## Setup

1. Clone the repository. ( git clone https://github.com/dhiranj/orsay.git , cd orsay)
2. Create and activate a virtual environment. ( python -m venv venv , source venv/bin/activate )
3. Install required packages ( pip install -r requirements.txt ).


## Running the System

1. Start the FastAPI server:
   uvicorn app.main:app --reload

## Running Tests

python tests/test_main.py


