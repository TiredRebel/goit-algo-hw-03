import argparse
import shutil
from pathlib import Path
import sys


def parse_args() -> argparse.Namespace:
    """
    Парсить аргументи командного рядка.
    """
    parser = argparse.ArgumentParser(
        description="Recursively copy and sort files by extension."
    )
    parser.add_argument("source", type=Path, help="Path to the source directory")
    parser.add_argument(
        "destination",
        type=Path,
        nargs="?",
        default=Path("dist"),
        help="Path to the destination directory (default: dist)",
    )
    return parser.parse_args()


def process_directory(source: Path, destination: Path) -> None:
    """
    Рекурсивно читає вихідну директорію та копіює файли до директорії призначення,
    сортуючи їх за розширенням.

    Args:
        source (Path): Шлях до вихідної директорії.
        destination (Path): Шлях до директорії призначення.
    """
    try:
        for item in source.iterdir():
            if item.is_dir():
                process_directory(item, destination)
            elif item.is_file():
                copy_file(item, destination)
    except PermissionError:
        print(f"Permission denied: Cannot access directory '{source}'.")
    except FileNotFoundError:
        print(f"Directory not found: '{source}'.")
    except Exception as e:
        print(f"An error occurred while processing directory '{source}': {e}")


def copy_file(file_path: Path, destination: Path) -> None:
    """
    Копіює файл до директорії призначення, розміщуючи його у піддиректорії,
    названій за його розширенням.

    Args:
        file_path (Path): Шлях до файлу, який потрібно скопіювати.
        destination (Path): Базова директорія призначення.
    """
    try:
        # Get extension without the dot, or 'no_extension' if empty
        extension = file_path.suffix[1:].lower()
        if not extension:
            extension = "no_extension"

        target_dir = destination / extension
        target_dir.mkdir(parents=True, exist_ok=True)

        target_file = target_dir / file_path.name
        
        # Handle duplicates by adding a counter
        counter = 1
        while target_file.exists():
            target_file = target_dir / f"{file_path.stem}_{counter}{file_path.suffix}"
            counter += 1

        shutil.copy2(file_path, target_file)
        print(f"Copied: '{file_path}' -> '{target_file}'")

    except PermissionError:
        print(f"Permission denied: Cannot copy file '{file_path}'.")
    except Exception as e:
        print(f"Error copying file '{file_path}': {e}")


def main() -> None:
    args = parse_args()
    source_path: Path = args.source.resolve()
    dest_path: Path = args.destination.resolve()

    if not source_path.exists():
        print(f"Error: Source directory '{source_path}' does not exist.")
        sys.exit(1)

    if not source_path.is_dir():
        print(f"Error: '{source_path}' is not a directory.")
        sys.exit(1)

    print(f"Starting copy from '{source_path}' to '{dest_path}'...")
    process_directory(source_path, dest_path)
    print("Operation completed.")


if __name__ == "__main__":
    main()
