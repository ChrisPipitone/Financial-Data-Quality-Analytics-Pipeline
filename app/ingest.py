import csv
import json
from pathlib import Path


def ingest_input(input_path: Path) -> None:
    """
    Ingest raw data from a file or directory.
    If a directory is provided, ingest all supported files inside it.
    If a file is provided, ingest only that file.
    """
    if input_path.is_file():
        ingest_file(input_path)
    elif input_path.is_dir():
        for path in iterate_supported_files(input_path):
            ingest_file(path)
    else:
        raise ValueError(f"Input path does not exist {input_path}")


def iterate_supported_files(root: Path):
    """
    Return supported raw data files from a directory.
    Ignores unsupported files. Non-recursive.
    """
    SUPPORTED_EXTENSIONS = {".csv", ".json"}
    for path in root.iterdir():
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            yield path


def ingest_file(path: Path) -> None:
    """
    Route a file to the appropriate ingestion handler.
    File type is determined by filename or extension.
    """
    if path.name == "companies.csv":
        ingest_companies(path)
    elif path.name == "filings.csv":
        ingest_filings(path)
    elif path.name == "financial_metrics.json":
        ingest_financial_metrics(path)
    else:
        log_unknown_file(path)


def ingest_companies(path: Path) -> None:
    """Ingest company data from CSV to JSONL"""
    print("Ingesting companies...")

    output_file = Path("data/processed/companies.jsonl")
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with path.open("r", encoding="utf-8") as csvfile:
        with output_file.open("w", encoding="utf-8") as outfile:
            for row in csv.DictReader(csvfile):
                outfile.write(json.dumps(row) + "\n")


def ingest_filings(path: Path) -> None:
    """Ingest filing data from a CSV file."""


def ingest_financial_metrics(path: Path) -> None:
    """Ingest financial metrics from a JSON file."""


def log_unknown_file(path: Path) -> None:
    """Log an unsupported or unrecognized file."""
