import csv
from pathlib import Path
from typing import Iterator


def iterate_supported_files(root: Path) -> Iterator[Path]:
    """
    Return supported raw data files from a directory.
    Ignores unsupported files. Non-recursive.
    """
    SUPPORTED_EXTENSIONS = {".csv", ".json"}
    for path in root.iterdir():
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            yield path


def validate_input(input_path: Path) -> None:
    """
    Validate raw data from a file or directory.
    If a directory is provided, validate all supported files inside it.
    If a file is provided, validate only that file.
    """
    if input_path.is_file():
        validate_file(input_path)
    elif input_path.is_dir():
        for path in iterate_supported_files(input_path):
            validate_file(path)
    else:
        raise ValueError(f"Input path does not exist {input_path}")


def validate_file(path: Path) -> None:
    """
    Route a file to the appropriate ingestion handler.
    File type is determined by filename or extension.
    """
    if path.name == "companies.csv":
        validate_companies(path)
    #   elif path.name == "filings.csv":
    #       ingest_filings(path)
    #   elif path.name == "financials.json":
    #       ingest_financials(path)
    else:
        log_unknown_file(path)


def is_empty_value(value):
    """check if a value is empty"""
    if value is None or value == "":
        return True
    return False


def validate_required_fields(row: dict, required_fields: list[str]) -> list[str]:
    """Validate dict doesnt contain empty or null values"""
    return [field for field in required_fields if is_empty_value(row.get(field))]


def validate_companies(path: Path) -> None:
    """Validate companies.csv data"""
    required_fields = ["company_id", "company_name", "ticker", "sector"]

    with path.open("r", encoding="utf-8") as csvfile:
        for line_number, row in enumerate(csv.DictReader(csvfile), start=2):
            is_valid = all(not is_empty_value(row[field]) for field in required_fields)
            if not is_valid:
                print(f"invalid line {line_number}:", row)


def log_unknown_file(path: Path) -> None:
    """Log an unsupported or unrecognized file."""
    print(f"Unsupported or unrecognized file {path}")
