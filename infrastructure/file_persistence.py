from domain.entities import Item
from domain.interfaces import DataPersistencePort
from typing import List


class FilePersistence(DataPersistencePort):
    """
    File-based implementation of the DataPersistencePort interface.
    """
    def __init__(self, path: str = "data.txt"):
        """
        Initialize the FilePersistence with a file path.
        Args:
            path (str): The file path to save data to.
        """
        self._path = path


    import logging
    import json
    import os
    import tempfile
    from domain.entities import Item
    from domain.interfaces import DataPersistencePort
    from typing import List

        def save(self, items: List[Item]) -> None:
            """
            Save a list of Item objects to a file as JSON, using atomic write.
            Args:
                items (List[Item]): The items to save.
            """
            temp_dir = os.path.dirname(os.path.abspath(self._path)) or "."
            try:
                with tempfile.NamedTemporaryFile("w", dir=temp_dir, delete=False, encoding="utf-8") as tmp_file:
                    json.dump([item.__dict__ for item in items], tmp_file)
                    tempname = tmp_file.name
                os.replace(tempname, self._path)
            except (IOError, OSError, PermissionError) as e:
                logging.error(f"Failed to save data atomically: {e}")

        def load(self) -> List[Item]:
            """
            Load and return a list of Item objects from the file.
            Returns:
                List[Item]: The loaded items.
            """
            if not os.path.exists(self._path):
                logging.info(f"Data file {self._path} does not exist. Returning empty list.")
                return []
            try:
                with open(self._path, "r", encoding="utf-8") as file:
                    data = json.load(file)
                    return [Item(**item) for item in data]
            except (IOError, OSError, json.JSONDecodeError, PermissionError) as e:
                logging.warning(f"Failed to load data: {e}")
                return []
