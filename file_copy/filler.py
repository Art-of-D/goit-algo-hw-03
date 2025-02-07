from pathlib import Path

class Filler:
    def __init__(self, path: str, destination="dist"):
        self.path = Path(path)
        self.destination = Path(destination)

    def recursive_copy(self, current_path=None) -> None:
        if current_path is None:
            current_path = self.path
        
        try:
            for path in current_path.iterdir():
                if path.is_dir():
                    target_folder = self.destination / path.relative_to(self.path)
                    target_folder.mkdir(parents=True, exist_ok=True)
                    self.recursive_copy(path)
                else:
                    target_file = self.destination / path.relative_to(self.path)
                    self.copy_file(path, target_file)
        except PermissionError:
            print(f"Доступ заборонено: {current_path}")
        except FileNotFoundError:
            print(f"Файл або директорія не знайдені: {current_path}")
        except OSError as e:
            print(f"Помилка файлової системи: {e}")

    def copy_file(self, source, destination):
        try:
            destination.parent.mkdir(parents=True, exist_ok=True)
            with open(source, 'rb') as src, open(destination, 'wb') as dst:
                dst.write(src.read())
        except PermissionError:
            print(f"Немає доступу до файлу: {source}")
        except FileNotFoundError:
            print(f"Файл не знайдено: {source}")
        except OSError as e:
            print(f"Помилка файлової системи під час копіювання {source}: {e}")