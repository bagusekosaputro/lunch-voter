from typing import Optional

from pydantic import BaseModel, Field


class VoteMenuRequest(BaseModel):
    id: int
    point: Optional[int] = Field(default=None, ge=1, le=3)