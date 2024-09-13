from pydantic import BaseModel


class RetrieveVoteResultResponse(BaseModel):
    menu_id: int
    total_point: int