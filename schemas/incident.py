from pydantic import BaseModel


class IncidentRequest(BaseModel):
    message: str
    status_code: int
    duration_ms: int