import os
import logging
from datetime import datetime

import pandas as pd
import numpy as np


# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "cleaned_superstore_sales.csv"
)

OUTPUT_DIR = os.path.join(
    BASE_DIR,
    "outputs"
)

PROCESSED_DATA_PATH = os.path.join(
    OUTPUT_DIR,
    "processed_data.csv"
)

EXCEL_OUTPUT_PATH = os.path.join(
    OUTPUT_DIR,
    "sales_kpis.xlsx"
)

LOG_PATH = os.path.join(
    OUTPUT_DIR,
    "pipeline_log.txt"
)


# Create output directory
os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)


# ============================================================
# LOGGING
# ============================================================

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# ============================================================
# 1. LOAD RAW DATA
# ============================================================

def load_data():

    logging.info("Loading raw dataset...")

    df = pd.read_csv(
        DATA_PATH
    )

    logging.info(
        f"Dataset loaded: {df.shape[0]} rows, "
        f"{df.shape[1]} columns"
    )

    return df


# ============================================================
# 2. CLEAN DATA
# ============================================================

def clean_data(df):

    logging.info("Starting data cleaning...")

    # Remove duplicate rows
    duplicate_count = df.duplicated().sum()

    if duplicate_count > 0:

        df = df.drop_duplicates()

        logging.info(
            f"Removed {duplicate_count} duplicate rows"
        )

    else:

        logging.info(
            "No duplicate rows found"
        )


    # Convert date columns
    df["Order Date"] = pd.to_datetime(
        df["Order Date"],
        errors="coerce"
    )

    df["Ship Date"] = pd.to_datetime(
        df["Ship Date"],
        errors="coerce"
    )


    # Calculate shipping days
    df["Shipping Days"] = (
        df["Ship Date"] -
        df["Order Date"]
    ).dt.days


    # Handle missing numerical values
    numeric_columns = [
        "Sales",
        "Quantity",
        "Discount",
        "Profit",
        "Shipping Days"
    ]

    for column in numeric_columns:

        if column in df.columns:

            df[column] = df[column].fillna(
                df[column].median()
            )


    # Handle missing categorical values
    categorical_columns = [
        "Ship Mode",
        "Segment",
        "Country/Region",
        "City",
        "State/Province",
        "Region",
        "Category",
        "Sub-Category",
        "Product Name"
    ]

    for column in categorical_columns:

        if column in df.columns:

            df[column] = df[column].fillna(
                "Unknown"
            )


    logging.info(
        "Data cleaning completed."
    )

    return df


# ============================================================
# 3. FEATURE ENGINEERING
# ============================================================

def create_features(df):

    logging.info(
        "Creating additional features..."
    )

    # Year
    df["Order Year"] = (
        df["Order Date"].dt.year
    )

    # Month
    df["Order Month"] = (
        df["Order Date"].dt.month
    )

    # Month name
    df["Order Month Name"] = (
        df["Order Date"].dt.month_name()
    )

    # Quarter
    df["Order Quarter"] = (
        df["Order Date"].dt.quarter
    )

    # Profit Margin
    df["Profit Margin (%)"] = np.where(
        df["Sales"] != 0,
        (df["Profit"] / df["Sales"]) * 100,
        0
    )

    logging.info(
        "Feature engineering completed."
    )

    return df


# ============================================================
# 4. CALCULATE KPIs
# ============================================================

def calculate_kpis(df):

    logging.info(
        "Calculating business KPIs..."
    )


    total_sales = df["Sales"].sum()

    total_profit = df["Profit"].sum()

    total_quantity = df["Quantity"].sum()

    total_orders = df["Order ID"].nunique()

    total_customers = df["Customer ID"].nunique()

    average_order_value = (
        total_sales / total_orders
        if total_orders > 0
        else 0
    )

    profit_margin = (
        total_profit / total_sales * 100
        if total_sales != 0
        else 0
    )


    kpi_data = {

        "KPI": [
            "Total Sales",
            "Total Profit",
            "Total Quantity",
            "Total Orders",
            "Total Customers",
            "Average Order Value",
            "Profit Margin (%)"
        ],

        "Value": [
            total_sales,
            total_profit,
            total_quantity,
            total_orders,
            total_customers,
            average_order_value,
            profit_margin
        ]
    }


    kpi_df = pd.DataFrame(
        kpi_data
    )


    logging.info(
        "KPI calculation completed."
    )

    return kpi_df


# ============================================================
# 5. CATEGORY ANALYSIS
# ============================================================

def category_analysis(df):

    category_df = (
        df.groupby("Category")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum"),
            Orders=("Order ID", "nunique")
        )
        .reset_index()
    )

    category_df[
        "Profit Margin (%)"
    ] = np.where(
        category_df["Sales"] != 0,
        (
            category_df["Profit"] /
            category_df["Sales"]
        ) * 100,
        0
    )

    return category_df


# ============================================================
# 6. REGION ANALYSIS
# ============================================================

def region_analysis(df):

    region_df = (
        df.groupby("Region")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum"),
            Orders=("Order ID", "nunique")
        )
        .reset_index()
    )

    region_df[
        "Profit Margin (%)"
    ] = np.where(
        region_df["Sales"] != 0,
        (
            region_df["Profit"] /
            region_df["Sales"]
        ) * 100,
        0
    )

    return region_df


# ============================================================
# 7. SEGMENT ANALYSIS
# ============================================================

def segment_analysis(df):

    segment_df = (
        df.groupby("Segment")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum"),
            Orders=("Order ID", "nunique"),
            Customers=("Customer ID", "nunique")
        )
        .reset_index()
    )

    return segment_df


# ============================================================
# 8. MONTHLY SALES
# ============================================================

def monthly_sales_analysis(df):

    monthly_df = (
        df.set_index("Order Date")
        .resample("ME")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum")
        )
        .reset_index()
    )

    return monthly_df


# ============================================================
# 9. TOP PRODUCTS
# ============================================================

def top_products(df):

    product_df = (
        df.groupby("Product Name")
        .agg(
            Sales=("Sales", "sum"),
            Profit=("Profit", "sum"),
            Quantity=("Quantity", "sum")
        )
        .reset_index()
    )

    product_df = product_df.sort_values(
        "Sales",
        ascending=False
    )

    return product_df.head(10)


# ============================================================
# 10. EXPORT RESULTS TO EXCEL
# ============================================================

def export_results(
    df,
    kpi_df,
    category_df,
    region_df,
    segment_df,
    monthly_df,
    top_product_df
):

    logging.info(
        "Exporting results to Excel..."
    )


    with pd.ExcelWriter(
        EXCEL_OUTPUT_PATH,
        engine="openpyxl"
    ) as writer:

        kpi_df.to_excel(
            writer,
            sheet_name="KPIs",
            index=False
        )

        category_df.to_excel(
            writer,
            sheet_name="Category Analysis",
            index=False
        )

        region_df.to_excel(
            writer,
            sheet_name="Region Analysis",
            index=False
        )

        segment_df.to_excel(
            writer,
            sheet_name="Segment Analysis",
            index=False
        )

        monthly_df.to_excel(
            writer,
            sheet_name="Monthly Sales",
            index=False
        )

        top_product_df.to_excel(
            writer,
            sheet_name="Top Products",
            index=False
        )


    # Save processed dataset
    df.to_csv(
        PROCESSED_DATA_PATH,
        index=False
    )


    logging.info(
        "Results exported successfully."
    )


# ============================================================
# 11. MAIN PIPELINE
# ============================================================

def main():

    start_time = datetime.now()

    logging.info(
        "=" * 60
    )

    logging.info(
        "AUTOMATED SALES PIPELINE STARTED"
    )


    try:

        # Load
        df = load_data()


        # Clean
        df = clean_data(df)


        # Features
        df = create_features(df)


        # KPIs
        kpi_df = calculate_kpis(
            df
        )


        # Analysis
        category_df = category_analysis(
            df
        )

        region_df = region_analysis(
            df
        )

        segment_df = segment_analysis(
            df
        )

        monthly_df = monthly_sales_analysis(
            df
        )

        top_product_df = top_products(
            df
        )


        # Export
        export_results(
            df,
            kpi_df,
            category_df,
            region_df,
            segment_df,
            monthly_df,
            top_product_df
        )


        end_time = datetime.now()

        duration = (
            end_time - start_time
        ).total_seconds()


        logging.info(
            f"Pipeline completed successfully "
            f"in {duration:.2f} seconds"
        )


        print(
            "========================================"
        )

        print(
            "PIPELINE COMPLETED SUCCESSFULLY"
        )

        print(
            "========================================"
        )

        print(
            f"Rows processed: {len(df)}"
        )

        print(
            f"Total Sales: ₹{df['Sales'].sum():,.2f}"
        )

        print(
            f"Total Profit: ₹{df['Profit'].sum():,.2f}"
        )

        print(
            f"Total Orders: "
            f"{df['Order ID'].nunique():,}"
        )

        print(
            f"Total Customers: "
            f"{df['Customer ID'].nunique():,}"
        )

        print(
            f"Excel output: {EXCEL_OUTPUT_PATH}"
        )

        print(
            f"Processed data: "
            f"{PROCESSED_DATA_PATH}"
        )


    except Exception as e:

        logging.error(
            f"Pipeline failed: {str(e)}"
        )

        print(
            "PIPELINE FAILED"
        )

        print(
            "Error:",
            str(e)
        )

        raise


# ============================================================
# RUN PIPELINE
# ============================================================

if __name__ == "__main__":

    print("Starting Apexplanet Task 5 Pipeline...")

    main()

    print("Pipeline execution finished.")