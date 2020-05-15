from typing import List

from pydantic import BaseModel


class LinkData(BaseModel):
    links: List[str]
