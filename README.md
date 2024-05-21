# AI Sales Agent System

This system dynamically manages different workflows for handling leads based on their sources.

## Components

1. **Workflow Configuration**: Defines the workflows in `workflows.json`.
2. **Workflow Manager**: Simple service that loads and saves workflows (`workflows.py`).
3. **Tests**: Check leads processing for different cases (`tests_main.py`).
4. **Logging**: Logs the processing of leads (`workflow.log`).

## Setup

1. Clone the repository. (  )
3. Ensure Python 3 is installed on your system.
4. Install required packages (if any).
5. Configure your workflows in `workflows.json`.

## Running the System

1. Start the Lead Simulator:
   ```sh
   python lead_simulator.py
