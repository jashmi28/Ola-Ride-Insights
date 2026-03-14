import streamlit as st
import pandas as pd

# ===== Title =====
st.title("OLA Ride Insights Dashboard")

st.write("This project analyzes ride booking patterns, cancellations, and revenue insights.")

# ===== Load Dataset (limited rows for faster loading) =====
df = pd.read_csv("ola_data_cleaned.csv")
# ===== Dataset Columns =====
st.subheader("Dataset Columns")
st.write(df.columns)

# ===== Dataset Preview =====
st.subheader("Dataset Preview")
st.dataframe(df.head())

# ===== Booking Status Distribution =====
st.subheader("Booking Status Distribution")
booking_counts = df['Booking_Status'].value_counts()
st.bar_chart(booking_counts)

# ===== Payment Method Distribution =====
st.subheader("Payment Method Distribution")
payment_counts = df['Payment_Method'].value_counts()
st.bar_chart(payment_counts)

# ===== Driver Ratings Distribution =====
st.subheader("Driver Ratings Distribution")
rating_counts = df['Driver_Ratings'].value_counts()
st.bar_chart(rating_counts)

# ===== Power BI Dashboard PDF =====
st.subheader("Power BI Dashboard")

pdf_file = "Jashmiiii_internship_olaride.pdf"

with open(pdf_file, "rb") as file:
    st.download_button(
        label="Download Power BI Dashboard PDF",
        data=file,
        file_name="OLA_Dashboard.pdf",
        mime="application/pdf"
    )
