from typing import List, Protocol
from domain.entities import Item



class DataPersistencePort(Protocol):
    """
    Protocol for data persistence operations.
    """
    def save(self, items: List[Item]) -> None:
        """
        Save a list of Item objects.
        Args:
            items (List[Item]): The items to save.
        """
        ...

    def load(self) -> List[Item]:
        """
        Load and return a list of Item objects.
        Returns:
            List[Item]: The loaded items.
        """
        ...
