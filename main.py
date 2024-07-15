import streamlit as st
import pandas as pd
import plotly.express as px

st.title("タイトル")
st.write("何でも書ける")
st.markdown("##マークダウンで書く $x^2$")
df = px.data.iris()
st.write(df.head())
st.table(df.head())
st.write(px.scatter(df, x="sepal_length", y="sepal_width", color="species"))

if st.button("Say hello"):
    st.write("Hello")
    st.button("Say Goodbye")
else:
    st.write("Goodbye")

agree = st.checkbox("チェックしてください")
if agree:
    st.write("Great!")

fruit = st.radio(label="好きなフルーツは？", options=["バナナ", "リンゴ", "イチゴ"], index=1)
st.write(fruit)

option = st.selectbox("今日はなにする？", ("なわとび", "野球", "ゲーム"))
def f(i):
    play = ("なわとび", "野球", "ゲーム")
    return play[i]

option_1 = st.selectbox("今日はなにする(2)？", (0,1,2), format_func=f)
st.write("よし ", option, " をしよう!")

options = st.multiselect(
    "何色が好き？", options=["Green", "Yellow", "Red", "Blue"],
    default=["Yellow", "Red"]
)
st.write("You selected:", options)

age = st.slider("何歳？", min_value=0, max_value=130, value=25)
st.write(age)

from datetime import datetime,date,time

interval = st.slider(
    "計画期間は？",
    value = (datetime(2019,1,1,9,30),datetime(2020,1,1,9,30)),
    format="MM/DD/YY - hh:mm",
)
color = st.select_slider(
    "色を選んでね",
    options = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
)

title = st.text_input("お名前は？", value="ななしのごんべえ")

number = st.number_input("数字を入れてね",
                         min_value=1.0, max_value=10.0, value=5.0, step=0.1)

d = st.date_input("誕生日は？", date(2019,7,6))

alarm = st.time_input("アラームセット", time(8,45))
uploaded_file = st.file_uploader("ファイル選択")

# サイドバーに表示
add_selectbox = st.sidebar.selectbox("連絡方法は？", ("Email", "Home phone", "Mobile phone"))

col1, col2 = st.columns([1, 2])
with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg", use_column_width=True)
with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", use_column_width=True)

import time

@st.cache
def f(input):
    time.sleep(3)
    return input*10

st.write(f(10))
st.write(f(100))
st.write(f(10)) #キャッシュされているので1瞬で終わる

import random 
@st.cache(allow_output_mutation=True) #返り血が変わる場合にはTrueにする
def f(input):
    time.sleep(3)
    return input*random.random()

st.write(f(10))
st.write(f(100))
st.write(f(10)) #キャッシュされているので1瞬で終わる

#データフレームのハッシュ地をidとする
@st.cache(hash_funcs={pd.DataFrame: id})
def f(data):
    time.sleep(3)
    return data.values

df = px.data.iris()

if "count" not in st.session_state:
    st.session_state.count = 0

increment = st.button("Increment")
if increment:
    st.session_state.count += 1
st.write("Count = ",st.session_state.count)

if "celsius" not in st.session_state:
    st.session_state.celsius = 50.0
st.slider("Temperature in Celsius", min_value=0.0, max_value=100.0, key="celsius")
st.write(st.session_state.celsius )

with st.form(key="basic_form"):
    n_jobs = st.number_input("最大ジョブ数", min_value=1, max_value=10000, value=100)
    n_shipment = st.number_input("最大輸送数", min_value=1, max_value=10000, value=100)
    submit = st.form_submit_button(label="データ更新")

if submit:
    st.write(n_jobs, n_shipment)