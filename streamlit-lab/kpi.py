import streamlit as st


st.title("You Fav. Animal")

col1, col2 = st.columns(2)

with col1:
    st.header("Cow")
    st.image(
        "https://images.pexels.com/photos/31586191/pexels-photo-31586191.jpeg",
        width=200,
        caption="Baby Cow",
    )
    vote1 = st.button("Vote Cow")

with col2:
    st.header("Dog")
    st.image(
        "https://images.pexels.com/photos/35445398/pexels-photo-35445398.jpeg",
        width=200,
        caption="Puppy",
    )
    vote2 = st.button("Vote Dog")

if vote1:
    st.success("+1 Cow")
elif vote2:
    st.success("+1 Dog")

sidebar = st.sidebar.text("Sidebar")
name = st.sidebar.text_input("Name")
email = st.sidebar.text_input("Email")

if st.sidebar.button("Done"):
    st.write(f"Thank You for voting: {name}, {email}")

with st.expander("Dog Cow"):
    st.write("""
    ### The Cutest
    * **The puppy looks cuter** because of its small size, soft fur, and playful appearance.
    * **The baby cow is also adorable**, especially because of its gentle face and innocent expression.
    * The **puppy has a more playful and energetic look**, while the cow appears calmer and more gentle.
    * Both animals have features commonly associated with cuteness, such as **large eyes, small bodies, and youthful appearances**.
    * **Overall, I would choose the puppy as the cutest**, but the baby cow is a close second.

    """)
