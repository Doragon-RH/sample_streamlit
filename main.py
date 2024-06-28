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
