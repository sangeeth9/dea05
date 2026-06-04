MVP Library Project

This repository contains the work completed during a 4-day apprenticeship session, where the goal was to build a product end-to-end. This repo is not a production-ready project, but it demonstrates the skills and tasks covered during the session.

Project Overview

The MVP Library project focuses on:

Loading, cleaning, and enriching library datasets.
Storing cleaned data in SQL Server.
Building an end-to-end data pipeline with Python.
Visualizing and reporting data in Power BI.
Packaging the app with Docker and testing it.
Day-by-Day Breakdown
Day 1

Tasks:

Load datasets using Jupyter Notebook.
Explore, clean, and visualize the data.
Output cleaned CSV files.

Stretch Task:

Explore SQLAlchemy to write cleaned data to a local SQL Server.
Day 2

Tasks:

Convert Jupyter Notebook workflow into a Python .py script for cleaning and outputting library datasets.
Include reusable functions, such as:
fileLoader – load data from file.
duplicateChecker – remove duplicate rows.
naChecker – handle missing values.
dataEnrich – add calculated or transformed columns (e.g., number of days a book was on loan).

Stretch Tasks:

Use argparse to toggle writing to SQL on/off.
Work with APIs: request data from a public API and print the results.
Example API list: Public API Lists
Day 4 (AM Task)

Tasks:

Write unit tests for Python app (especially the data enrichment calculations).
Package the data cleaning app as a Docker image and demonstrate it runs successfully.

Unit Test References:

assertEqual(a, b) – a == b
assertNotEqual(a, b) – a != b
assertTrue(x) – bool(x) is True
assertFalse(x) – bool(x) is False
assertIs(a, b) – a is b
assertIsNot(a, b) – a is not b
assertIsNone(x) – x is None
assertIsNotNone(x) – x is not None
assertIn(a, b) – a in b
assertNotIn(a, b) – a not in b
assertIsInstance(a, b) – isinstance(a, b)
assertNotIsInstance(a, b) – not isinstance(a, b)
Skills and Tools Covered
VSCode – development environment
Docker – containerization of the app
Power BI – visualization and dashboards
GitHub – version control
ETL pipeline – data extraction, transformation, and loading
CI/CD – continuous integration and deployment
APIs – data retrieval from public APIs
Unit Testing – Python testing best practices
SQL & Databases – storing and querying data
Python – scripting, data manipulation, and automation
