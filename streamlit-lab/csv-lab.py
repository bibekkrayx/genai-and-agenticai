import  streamlit as st
import pandas as pd
import requests


st.title("CSV LAB")

file = st.file_uploader("Upload file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data preview")
    st.dataframe(df)

st.write("---")
st.title("API CALL")

amount = st.number_input("Amount")

target_currency = st.selectbox("Select currency", ["USD", "INR", "NPR"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/NPR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][target_currency]
        converted = amount * rate
        st.success(f"NPR {amount} = {target_currency} {converted}")
    else:
        st.error("FAILED")

st.write("---")
st.title("KPI by ChatGPT")


st.set_page_config(
    page_title="Sales Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("Sales Dashboard")
st.caption("Demo data")

# Demo data
total_sales = 128_500
orders = 1_248
customers = 842
conversion_rate = 8.4

# KPI cards
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total Sales",
        value="$128.5K",
        delta="+12.5%"
    )

with col2:
    st.metric(
        label="Orders",
        value="1,248",
        delta="+8.2%"
    )

with col3:
    st.metric(
        "Refunds",
        "$3.2K",
        delta="-8.5%",
        delta_color="red"
    )

with col4:
    st.metric(
        label="Conversion Rate",
        value="8.4%",
        delta="0%",
        delta_color="blue"
    )