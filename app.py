import streamlit as st
import pandas as pd
import os

# Load or create the CSV
FILE_PATH = "expenses.csv"

if os.path.exists(FILE_PATH):
    df = pd.read_csv(FILE_PATH)
else:
    df = pd.DataFrame(columns=["Date", "Category", "Amount"])
    df.to_csv(FILE_PATH, index=False)

# Title
st.title("💰 Personal Expense Tracker")

# Input section
st.header("➕ Add a new expense")
date = st.date_input("Date")
category = st.text_input("Category")
amount = st.number_input("Amount", min_value=0.0, step=0.1)

if st.button("Add Expense"):
    new_expense = pd.DataFrame([[date, category, amount]], columns=["Date", "Category", "Amount"])
    df = pd.concat([df, new_expense], ignore_index=True)
    df.to_csv(FILE_PATH, index=False)
    st.success("Expense added!")

# Show data
st.header("📊 All Expenses")
st.dataframe(df)

# Basic analysis
st.header("📈 Analysis")
st.write("**Total amount spent:**", df["Amount"].sum())

if not df.empty:
    st.write("**Spend by Category:**")
    st.bar_chart(df.groupby("Category")["Amount"].sum())

    st.write("**Daily Spend:**")
    st.line_chart(df.groupby("Date")["Amount"].sum())
