# SkyGeniAssessment
Overview

This project analyzes various aspects of client subscriptions, payments, and financial data using Python (Pandas). The dataset includes information on industries, financial records, payments, and subscriptions.

## Objectives

The following key business questions are addressed in this analysis:

Q. How many Finance Lending and Blockchain clients does the organization have?

Q. Which industry has the highest renewal rate?

Q. What was the average inflation rate when subscriptions were renewed?

Q. What is the median amount paid each year across all payment methods?

##  Dataset Description

The analysis uses the following CSV files:

1. industry_client_details.csv: Contains industry-wise client details.

2. subscription_information.csv: Stores details on client subscriptions and renewals.

3. finanical_information.csv: Includes financial data such as inflation rates.

4. payment_information.csv: Records payment transactions and amounts.

## Technology Stack

- Python (Pandas)

- VS Code (for running scripts)

## Implementation Steps

1. Load the datasets using Pandas.

2.Data Cleaning & Preprocessing (if any)

-Convert date columns to datetime format.(if any)

-Handle missing or inconsistent values.(if any)

3.Data Analysis using Pandas

-Apply filtering, grouping, and merging operations to answer business questions.

4.Results Interpretation


## Results Summary

The total number of Finance Lending & Blockchain clients is calculated using filtering.

The industry with the highest renewal rate is determined via grouping and merging.

The average inflation rate at renewal time is derived using date-based merging.

The median payment per year is calculated using groupby() on the payments dataset.

## Future Enhancements

Expand the analysis with data visualizations (Matplotlib/Seaborn).

Implement SQL-based querying for scalable data handling.

Automate data fetching using AWS (S3/RDS).

## Author

Sanchay . Feel free to reach out for any queries!

