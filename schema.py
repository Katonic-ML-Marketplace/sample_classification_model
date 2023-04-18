from pydantic import BaseModel
from typing import List,Any,Dict,Union

class PredictSchema(BaseModel):
    data: List[List[Any]]
