thonpython
import json
import logging
from pathlib import Path

from extractors.quora_parser import QuoraParser
from extractors.qql_resolver import QQLResolver
from outputs.exporters import JSONExporter

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def load_queries(input_path: str):
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        logging.error(f"Failed to load input queries: {e}")
        return []

def main():
    base = Path(__file__).resolve().parent.parent
    input_file = base / "data" / "inputs.sample.json"
    output_file = base / "data" / "sample_output.json"

    queries = load_queries(str(input_file))

    resolver = QQLResolver()
    parser = QuoraParser()
    results = []

    for q in queries:
        logging.info(f"Processing query: {q}")
        resolved = resolver.resolve(q)
        parsed = parser.parse(resolved)
        results.append(parsed)

    exporter = JSONExporter()
    exporter.export(results, output_file)

    logging.info(f"Extraction complete. Output saved to: {output_file}")

if __name__ == "__main__":
    main()