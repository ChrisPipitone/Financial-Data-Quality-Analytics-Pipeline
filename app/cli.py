import argparse
from pathlib import Path

from app.ingest import ingest_companies


def run_cli():
    parser = argparse.ArgumentParser(prog="python -m app.main")
    subparsers = parser.add_subparsers(dest="command", required=True)

    ingest_parser = subparsers.add_parser("ingest")
    ingest_parser.add_argument("--input", default="data/raw/")

    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--input", default="data/raw/")

    load_parser = subparsers.add_parser("load")
    load_parser.add_argument("--db", default="data/app.db")

    report_parser = subparsers.add_parser("report")
    report_subparsers = report_parser.add_subparsers(dest="report_name", required=True)

    report_subparsers.add_parser("latest-filings")

    args = parser.parse_args()

    if args.command == "ingest":
        print(f"INGEST input={args.input}")
        input_path = Path(args.input)
        # ingest_input(input_path)
        ingest_companies(input_path)

    elif args.command == "validate":
        print(f"VALIDATE input={args.input}")

    elif args.command == "load":
        print(f"LOAD db={args.db}")

    elif args.command == "report":
        if args.report_name == "latest-filings":
            print("REPORT latest-filings")
