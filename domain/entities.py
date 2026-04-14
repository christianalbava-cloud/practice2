from dataclasses import dataclass
from typing import List

from typing import Any
from dataclasses import dataclass, field
import datetime

@dataclass(frozen=True)
class Item:
    """
    Represents a single data item with an id, value, and timestamp.
    """
    id: int
    val: str
    date: str = field(default_factory=lambda: datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    def __post_init__(self):
        if not isinstance(self.id, int) or self.id < 1:
            raise ValueError("Item id must be a positive integer.")
        if not isinstance(self.val, str) or not self.val.strip():
            raise ValueError("Item value must be a non-empty string.")
