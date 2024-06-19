import streamlit as st
import pandas

st.set_page_config(layout="wide")

st.title("The best Company")

st.write("Loremipsdaiwnnewi  iewfjojeww oi joe jwfoiwjeijw ")

st.header("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("extra/company_website/resources/data.csv")

with col1:
    for index, row in df[:4].iterrows():
        st.header(row["first name"] + " " + row["last name"])
        st.write(row["role"])
        st.image("extra/company_website/resources/images/" + row["image"])

with col2:
    for index, row in df[4:8].iterrows():
        st.header(row["first name"] + " " + row["last name"])
        st.write(row["role"])
        st.image("extra/company_website/resources/images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.header(row["first name"] + " " + row["last name"])
        st.write(row["role"])
        st.image("extra/company_website/resources/images/" + row["image"])