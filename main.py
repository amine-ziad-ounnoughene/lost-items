import sqlite3
import streamlit as st 
conn = sqlite3.connect("item.db",check_same_thread=False)
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS items(
                    item TEXT,
                    num TEXT,
                    time TEXT,
                    date TEXT,
                    mail TEXT,
                    txt TEXT,
                    PRIMARY KEY (txt , item,num,time,date,mail)
                )''')
conn.commit()
def submit(item,num,time,date,mail,txt):
    cur.execute("INSERT INTO items VALUES (?,?,?,?,?,?)" , (item,num,time,date,mail,txt))
    conn.commit()
def itemt(item,o):
    with st.form(str(o)):
        st.header("Losted item : " + item[0])
        st.write("Phone number : " + item[1])
        st.write("e-mail : " + item[4])
        st.write("Date : " + item[3])
        st.write("Time : " + item[2])
        st.write("Item and place description : " + item[-1])
        submitted = st.form_submit_button("")
def form():
    st.title("Declare lost items")
    with st.form("my form"):
        item = st.text_input("Item","glasses")
        num = st.text_input("Phone number","+000000000")
        time = str(st.time_input('Time'))
        date = str(st.date_input("Date"))
        mail = st.text_input("e-mail","thestudent@gmail.com")
        txt = st.text_area('Item and place Description', '''I losted a black and white Gucci glasses next to the french consulat''')
        button = st.form_submit_button(label="submit")
        if button :
            try : 
                
                submit(item,num,time,date,mail,txt)
                st.success("you will find your item soon")
            except:
                st.error("existed item")
        else :
            pass
    c = cur.execute("SELECT * FROM items")
    conn.commit()
    r = c.fetchall()
    conn.close()
    #st.write(c.fetchall())
    st.title("Losted items")
    if r != None:
        a = 0
        for o in r:
            itemt(o,a)
            a += 1

form()
