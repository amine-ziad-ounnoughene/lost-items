import streamlit as st
st.subheader("Losted item")
lost = st.text_input("what did you lost ??","ex : phone , bagpack ...")
st.subheader("Date")
date = st.date_input(
     "When did you lost it ??")
st.subheader("Time")
time = st.time_input('when exactly did you lost it')
st.subheader("description")
txt = st.text_area('describe the losted object and where did you losted it ??', '''I losted a black and white Gucci glasses in the hamri street near the karan store mourad''')
des = f"losted item : {lost} \n date : {date}  {time} \n {txt}"
st.write(des)
