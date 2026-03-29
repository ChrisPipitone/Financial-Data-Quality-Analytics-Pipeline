import csv
import json
from pathlib import Path


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
