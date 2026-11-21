
# Duka Sales Exploration and Agent Network Clean-Up

## Project Overview

This project contains two data analytics engagements:

1. Duka Electronics sales exploration.
2. Agent network data cleaning and quality analysis.

## Tools Used

- Python
- Pandas
- NumPy
- Google Colab
- WPS Spreadsheet
- GitHub

## Duka Sales Executive Summary

- The dataset contains 1,000 orders across five branches.
- Total revenue was KES 71,792,500.
- Nairobi was the best-performing branch, generating KES 26,106,100.
- Laptops generated the highest revenue at KES 41,535,000.
- April was the best month, generating KES 13,518,300.

## Agent Network Clean-Up Summary

- Raw transaction records: 612.
- Duplicate transactions removed: 12.
- Clean transaction records: 600.
- Missing or invalid amounts imputed: 20.
- Unknown agent IDs identified: 7.
- Potential outliers flagged: 53.

## Project Files

- `generate_data.py` – generates the datasets.
- `duka_sales_exploration.ipynb` – Duka sales analysis.
- `agent_cleanup.ipynb` – agent data cleaning and analysis.
- `cleaning_pipeline.py` – reusable cleaning function.
- `requirements.txt` – project dependencies.
- `excel/duka_branch_summary.xlsx` – branch summary workbook.
- `outputs/premium_online_coast_capital.csv` – filtered Duka sales.
- `outputs/agent_transactions_clean.csv` – cleaned agent transactions.

## How to Run

1. Install the dependencies:

   `pip install -r requirements.txt`

2. Generate the datasets:

   `python generate_data.py`

3. Open and run `duka_sales_exploration.ipynb`.

4. Open and run `agent_cleanup.ipynb`.

5. Run both notebooks from top to bottom.

## Data Generation

The datasets are generated using fixed random seeds to make the results reproducible.
