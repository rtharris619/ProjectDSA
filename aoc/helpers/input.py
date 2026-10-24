from pathlib import Path

class Input:
    def __init__(self, path: Path):
        self.file_path = path / "input.txt"

    def extract(self) -> str:
        text = self.file_path.read_text(encoding="utf-8").strip()
        return text

    def extract_by_newline(self) -> list[str]:
        lines = self.file_path.read_text(encoding="utf-8").strip().splitlines()
        return lines