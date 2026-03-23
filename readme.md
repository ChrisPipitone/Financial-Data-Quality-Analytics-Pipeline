# Financial Data Quality & Analytics Pipeline

## Overview

This project simulates a real-world financial data pipeline similar to systems used in financial analytics and credit rating environments.

It ingests messy financial filings, validates and normalizes the data, stores it in a relational database, and exposes analytical queries for downstream users.

The project is intentionally designed to reflect:

- real-world data quality challenges
- structured engineering workflows
- production-style code organization

---

## Key Features

- Ingestion of CSV and JSON financial data
- Robust validation and normalization layer
- Deduplication of filings based on latest submission
- Relational data modeling using SQLite
- Analytical SQL queries (joins, aggregations, window functions)
- Python analytics layer for reporting

---

## Tech Stack

- Python 3.x
- SQLite
- Standard library (csv, json, datetime)
- Optional: pytest for testing

---

## Project Structure

```
financial-data-pipeline/
├── data/
│   ├── raw/
│   ├── processed/
│   └── app.db
├── sql/
├── app/
├── tests/
├── docs/
└── README.md
```

---

## Development Process

This project is being built using a structured, ticket-driven workflow to simulate a professional engineering environment.

- Tasks are tracked using GitHub Issues
- Work is managed via a Kanban board (GitHub Projects)
- Each task is implemented via pull requests linked to issues

### Project Board

https://github.com/users/ChrisPipitone/projects/2

---

## Data Pipeline Flow

1. **Ingestion**

   - Load raw CSV and JSON files

2. **Parsing**

   - Convert raw data into structured internal format

3. **Validation & Normalization**

   - Normalize dates and numeric fields
   - Capture validation errors without crashing

4. **Deduplication**

   - Keep latest filing per (company, year, quarter)

5. **Storage**

   - Load clean data into SQLite

6. **Analytics**

   - Execute SQL queries for financial insights

---

## Example CLI Commands

```
python -m app.main ingest --input data/raw/
python -m app.main validate --input data/raw/
python -m app.main load --db data/app.db
python -m app.main report latest-filings
```

---

## Example Analytical Questions

- What is the latest filing per company?
- Which companies have the highest debt-to-cash ratio?
- Which companies show declining revenue over multiple quarters?
- Which filings were amended after initial submission?
- Which companies have the most missing data?

---

## Engineering Decisions

### Separation of Concerns

Parsing, validation, and loading are separated to improve:

- testability
- readability
- maintainability

### Deduplication Strategy

Latest `filed_at` per (company, fiscal_year, fiscal_quarter) is treated as source of truth.

### Database Choice

SQLite is used for simplicity and local development, with the option to migrate to PostgreSQL.

---

## How to Run

1. Clone the repo
2. Add sample data to `data/raw/`
3. Run ingestion and validation commands
4. Load data into database
5. Execute reports

---

## Future Improvements

- Move to PostgreSQL for scalability
- Add streaming ingestion for large datasets
- Introduce workflow orchestration (Airflow-style)
- Add API layer for query access

---

## Why This Project Exists

This project was built to:

- simulate real-world data engineering problems
- practice SQL and Python in a production-like context
- demonstrate structured problem-solving and workflow management

---

## Author Notes

This is a work in progress some features may not be fully implemented until I mark the project as completed.
