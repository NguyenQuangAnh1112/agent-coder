from typing import Annotated, List, Optional, TypedDict

from langgraph.graph.message import BaseMessage, add_messages


class SuperState(TypedDict):
    message: Annotated[List[BaseMessage], add_messages]
    plan: str
    final_product: str


class CoderState(TypedDict):
    input: str

    draft_code: str
    execution_error: Optional[str]
    attempt_number: int

    clean_code: str
