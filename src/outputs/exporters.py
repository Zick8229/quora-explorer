thonpython
import json
import logging
from pathlib import Path

class JSONExporter:
    def export(self, data, file_path: Path):
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            logging.info(f"Export successful: {file_path}")
        except Exception as e:
            logging.error(f"Export failed: {e}")