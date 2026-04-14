from domain.entities import Item
from domain.interfaces import DataPersistencePort
from infrastructure.file_persistence import FilePersistence
import datetime



class DataStore:
    """
    Manages a collection of Item objects and delegates persistence operations.
    """
    def __init__(self, persistence: DataPersistencePort):
        self._persistence = persistence
        self._items = self._persistence.load()

    def add(self, value: str) -> None:
        value = value.strip()
        if not value:
            raise ValueError("Value cannot be empty.")
        item = Item(id=len(self._items)+1, val=value)
        self._items.append(item)

    def show(self) -> None:
        if not self._items:
            print("No items.")
        for item in self._items:
            print(f"Item: {item.id} - {item.val} at {item.date}")

    def save(self) -> None:
        self._persistence.save(self._items)
        print("Saved.")



class Command:
    def execute(self, store: DataStore, *args):
        raise NotImplementedError

class AddCommand(Command):
    def execute(self, store: DataStore, *args):
        value = args[0] if args else ""
        try:
            store.add(value)
            print("Added.")
        except ValueError as e:
            print(f"Error: {e}")

class ShowCommand(Command):
    def execute(self, store: DataStore, *args):
        store.show()

class SaveCommand(Command):
    def execute(self, store: DataStore, *args):
        store.save()

class ExitCommand(Command):
    def execute(self, store: DataStore, *args):
        print("Exiting...")
        raise SystemExit

def run_application(persistence=None):
    """
    Run the main application loop for interacting with the DataStore via CLI.
    """
    if persistence is None:
        persistence = FilePersistence()
    store = DataStore(persistence)
    commands = {
        "add": AddCommand(),
        "show": ShowCommand(),
        "save": SaveCommand(),
        "exit": ExitCommand(),
    }
    while True:
        cmd = input("What to do? (add/show/save/exit): ").strip().lower()
        if cmd not in commands:
            print("Unknown command.")
            continue
        if cmd == "add":
            value = input("Value: ")
            commands[cmd].execute(store, value)
        else:
            try:
                commands[cmd].execute(store)
            except SystemExit:
                break
