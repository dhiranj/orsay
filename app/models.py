from pydantic import BaseModel, field_validator, ValidationError
from datetime import datetime
from typing import ClassVar


class Workflow(BaseModel):
    source: str
    persona: str
    channel: str

    VALID_SOURCES: ClassVar[set] = {"Salesforce", "LinkedIn", "HubSpot"}  
    VALID_PERSONAS: ClassVar[set] = {"Eva", "Sofia", "Liam","Alex"}  

    @field_validator('source')
    def validate_source(cls, value):
        if value not in cls.VALID_SOURCES:
            raise ValueError(f'source must be one of {cls.VALID_SOURCES}')
        return value

    @field_validator('persona')
    def validate_persona(cls, value):
        if value not in cls.VALID_PERSONAS:
            raise ValueError(f'persona must be one of {cls.VALID_PERSONAS}')
        return value
    
class Lead(BaseModel):
    source: str
    name: str
    timestamp: float


    @field_validator('timestamp')
    def validate_timestamp(cls, value):
        min_valid_timestamp = 0  # 1970-01-01 00:00:00 UTC
        max_valid_timestamp = datetime.now().timestamp()  # Current time
        if not (min_valid_timestamp <= value <= max_valid_timestamp):
            raise ValueError('timestamp must be a valid epoch time between 1970 and the current date')
        return value

