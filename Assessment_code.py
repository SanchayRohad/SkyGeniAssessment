import pandas as pd

# ---------------------------------------------------------------------------------------------------------------------------------------------
#Q1 How many finance lending and blockchain clients does the organization have?

industry_client_df = pd.read_csv("industry_client_details.csv") #reading industry client details csv file


finance_blockchain_clients = industry_client_df[industry_client_df["industry"].isin(["Finance Lending", "Block Chain"])].shape[0] # Counting no. of clients in Finance_lending & Blockchain_industries

print('---------------------Q1-----------------------')
print(f"Total Finance Lending & Blockchain clients: {finance_blockchain_clients}")


# ----------------------------------------------------------------------------------------------------------------------------------------------
#Q2 Which industry in the organization has the highest renewal rate?

subscription_df = pd.read_csv("subscription_information.csv") #reading subscription info csv file

renewed_clients = subscription_df[subscription_df["renewed"] == True] #filter - who renewed subscription and store in new variable

merged_df = renewed_clients.merge(industry_client_df, on="client_id", how="left") # Merge with industry data to find renewal rates by industry

# Identify the industry with the highest number of renewals
highest_renewal_industry = merged_df["industry"].value_counts().idxmax()

print('---------------------Q2-----------------------')
print(f"Industry with the highest renewal rate: {highest_renewal_industry}")


# -------------------------------------------------------------------------------------------------------------------------------------------------
#Q3 What was the average inflation rate when their subscriptions were renewed?

financial_df = pd.read_csv("finanical_information.csv") #reading financial (note:- file name is not financial) details csv file 

# Convert 'end_date' columns to datetime for accurate merging
financial_df["end_date"] = pd.to_datetime(financial_df["end_date"])
subscription_df["end_date"] = pd.to_datetime(subscription_df["end_date"])

# Merge financial data with subscriptions to get the closest inflation rate at renewal
closest_inflation = pd.merge_asof(
    subscription_df.sort_values("end_date"),
    financial_df.sort_values("end_date"),
    on="end_date",
    direction="backward"
)


avg_inflation_rate = closest_inflation["inflation_rate"].mean() #average inflation rate at renewal

print('---------------------Q3-----------------------')
print(f"Average inflation rate when subscriptions were renewed: {avg_inflation_rate:.2f}%")


# ---------------------------------------------------------------------------------------------------------------------------------------------------
#Q4- What is the median amount paid each year for all payment methods? 

payment_df = pd.read_csv("payment_information.csv") #reading payment info csv file

payment_df["payment_date"] = pd.to_datetime(payment_df["payment_date"]) #Exrract payment-date

payment_df["year"] = payment_df["payment_date"].dt.year #Exrract year


median_payment_per_year = payment_df.groupby("year")["amount_paid"].median() # median amount paid each year across all payment methods

print('---------------------Q4-----------------------')
print("Median amount paid per year:")
print(median_payment_per_year)