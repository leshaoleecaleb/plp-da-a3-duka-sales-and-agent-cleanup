
import pandas as pd

def clean_agent_data(txns, agents):
    """
    Clean agent transaction data and return:
    1. A cleaned transaction DataFrame
    2. A data-quality audit log
    """

    clean_df = txns.copy()
    audit_log = []

    # 1. Remove duplicate transaction IDs
    before = len(clean_df)
    clean_df = clean_df.drop_duplicates(
        subset="txn_id",
        keep="first"
    )
    removed = before - len(clean_df)

    audit_log.append({
        "issue": "Duplicate transactions",
        "dimension": "Uniqueness",
        "column": "txn_id",
        "rows affected": removed
    })

    # 2. Standardize transaction types
    original_types = clean_df["txn_type"].copy()

    clean_df["txn_type"] = (
        clean_df["txn_type"]
        .str.strip()
        .str.lower()
        .str.capitalize()
    )

    changed_types = (
        original_types != clean_df["txn_type"]
    ).sum()

    audit_log.append({
        "issue": "Transaction type standardization",
        "dimension": "Consistency",
        "column": "txn_type",
        "rows affected": int(changed_types)
    })

  

    # 3. Convert amount to numeric
    clean_df["amount"] = pd.to_numeric(
        clean_df["amount"],
        errors="coerce"
    )

    # Flag missing amounts before filling them
    missing_mask = clean_df["amount"].isna()
    missing_count = missing_mask.sum()

    median_amount = clean_df["amount"].median()

    clean_df["amount_imputed"] = missing_mask
    clean_df["amount"] = clean_df["amount"].fillna(median_amount)

    audit_log.append({
        "issue": "Missing or invalid amounts",
        "dimension": "Completeness",
        "column": "amount",
        "rows affected": int(missing_count)
    })

    # 4. Convert transaction dates
    clean_df["txn_date"] = pd.to_datetime(
        clean_df["txn_date"],
        format="mixed",
        errors="coerce"
    )

    invalid_dates = clean_df["txn_date"].isna().sum()

    audit_log.append({
        "issue": "Invalid transaction dates",
        "dimension": "Validity",
        "column": "txn_date",
        "rows affected": int(invalid_dates)
    })

    # 5. Detect outliers using IQR
    q1 = clean_df["amount"].quantile(0.25)
    q3 = clean_df["amount"].quantile(0.75)
    iqr = q3 - q1

    lower_limit = q1 - 1.5 * iqr
    upper_limit = q3 + 1.5 * iqr

    clean_df["is_outlier"] = (
        (clean_df["amount"] < lower_limit) |
        (clean_df["amount"] > upper_limit)
    )

    outlier_count = clean_df["is_outlier"].sum()

    audit_log.append({
        "issue": "Potential outliers",
        "dimension": "Accuracy",
        "column": "amount",
        "rows affected": int(outlier_count)
    })

    # 6. Merge transactions with agent register
    clean_df = clean_df.merge(
        agents[["agent_id", "county"]],
        on="agent_id",
        how="left"
    )

    unknown_count = clean_df["county"].isna().sum()
    clean_df["county"] = clean_df["county"].fillna("Unknown")

    audit_log.append({
        "issue": "Unknown agent IDs",
        "dimension": "Consistency",
        "column": "agent_id",
        "rows affected": int(unknown_count)
    })

    return clean_df, audit_log
