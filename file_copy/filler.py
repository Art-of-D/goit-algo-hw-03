from pathlib import Path

class Filler:
    def __init__(self, path: str, destination="dist"):
        self.path = Path(path)
        self.destination = Path(destination)

    def recursive_copy(self, current_path=None) -> None:
        if current_path is None:
            current_path = self.path
        
        for path in current_path.iterdir():
            if path.is_dir():
                target_folder = self.destination / path.relative_to(self.path)
                target_folder.mkdir(parents=True, exist_ok=True)
                self.recursive_copy(path)
            else:
                target_file = self.destination / path.relative_to(self.path)
                self.copy_file(path, target_file)

    def copy_file(self, source, destination):
        destination.parent.mkdir(parents=True, exist_ok=True)
        with open(source, 'rb') as src, open(destination, 'wb') as dst:
            dst.write(src.read())

filler = Filler("Temp")
filler.recursive_copy()