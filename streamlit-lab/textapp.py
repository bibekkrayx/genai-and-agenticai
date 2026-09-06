import streamlit as st


st.header("Heading")
st.subheader("Subheading")
st.text("**Text**")

st.write("*Streamlit* **write example**")
st.write(100)
st.write([1, 2, 3])
st.write({"name": "Bibek", "age": 22})


lang = st.selectbox("you fav lang: ", ["java", "c", "c#", "c++"])

st.write(f"you fav lang: {lang}")

st.success(f"{lang} selected")

oop = st.selectbox(
    "which lang have OOP",
    ["Java", "C", "Fortan"],
    index=None,
    placeholder="Select a language...",
)
if oop is None:
    st.info("Please select an option")
elif oop == "Java":
    st.success("CORRECT")
else:
    st.error("INCORRECT")

st.write("---")

st.header("Widget")

customer_name = st.text_input("Name")
date = st.date_input("Date")
time = st.time_input("Time", value="now")
cup = st.number_input("Select no. of cup", step=1)
tea_base = st.selectbox("Choose base", ["Milk", "Water", "Almond milk"])
ingredient  = st.multiselect("Special ingredient", [
  "cardamom",
  "ginger",
  "cloves",
  "cinnamon",
  "star anise",
  "mint leaves",
  "lemongrass",
  "saffron",
  "fennel seeds",
  "tulsi"
]
)
sugar = st.slider("Sugar", 0, 5, 0)

pay = st.radio(
    "Select payment option",
    ["Online", "Cash"],
    index=None
)

confirm = st.checkbox("Confirm")

if pay is None:
    st.info("Select payment method")

if not confirm:
    st.info("Confirm order")


if pay and confirm and st.button("Order Now"):
    st.subheader("Order Summary")

    st.write(f"**Date:** {date}")
    st.write(f"**Time:** {time}")
    st.write(f"**Customer:** {customer_name}")

    st.divider()

    st.write("**Order Details**")
    st.write(f"- Cup: {cup}")
    st.write(f"- Tea Base: {tea_base}")
    st.write(f"- Ingredients: {ingredient}")
    st.write(f"- Sugar: {sugar}")

    st.divider()

    st.write("**Payment**")
    st.write(f"- Method: {pay}")

    st.divider()

    st.success("Order placed successfully")




























