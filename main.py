import streamlit as st
st.title("Losted items in Oran")
st.header("Losted item")
lost = st.text_input("what did you lost ??","glasses")
st.header("contact")
lo = st.text_input("how can we contact you??","+000000000")
st.header("Date")
date = st.date_input(
     "When did you lost it ??")
st.header("Time")
time = st.time_input('when exactly did you lost it')
st.header("description")
txt = st.text_area('describe the losted object and where did you losted it ??', '''I losted a black and white Gucci glasses in the hamri street near the karan store mourad''')
st0.
st.title("losted items")
st.subheader(lost)
st.subheader(f"date : {date}  {time}")
st.subheader(f"contact : {lo}")
st.subheader(txt)
