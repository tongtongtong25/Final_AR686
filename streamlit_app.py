import streamlit as st
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import plotly.figure_factory as ff

st.title("Life Expectancy : ช่วงชีวิต โดยองค์การอนามัยโลก (WHO)")
st.subheader('AR686: ASSIGNMENT 30/11/22')
st.caption("By Thapanawong Phamornpongamporn 6416030069")


st.image("https://www.pennlive.com/resizer/MZPzWMRqpxSkSBLt5-w8iOOSclA=/800x0/smart/cloudfront-us-east-1.images.arcpublishing.com/advancelocal/A7QUW3357FFW5BW4YE22YHP2EY.jpg")
st.caption('"Your time is limited, so dont waste your time." by Steve Jobs')

st.write("")
df = pd.read_csv('Life Expectancy Data.csv')


with st.expander("See data frames : ตารางแสดงชุดข้อมูล "):

   st.dataframe(df)

st.header('Sunburst Chart : Developing & Developed')
st.subheader("Adult Mortality : อัตราการเสียชีวิตในผู้ใหญ่ในประเทศกำลังพัฒนา&ประเทศพัฒนาแล้ว")
fig = px.sunburst(df[df["Year"]==2015], path=['Status', 'Country'], values='Adult Mortality', color='Status', width = 1000, height=1000)
st.plotly_chart(fig, use_container_width=True)

st.subheader("GDP : ผลิตภัณฑ์รวมในประเทศของประเทศกำลังพัฒนา&ประเทศพัฒนาแล้ว")
fig = px.sunburst(df[df["Year"]==2015], path=["Status",'Country',], values='GDP', color='Status', width = 1000, height=1000)
st.plotly_chart(fig, use_container_width=True)


col1, col2 = st.columns([2, 2])
data = np.random.randn(10, 1)

col1.subheader("Displot")
sns.lineplot(data=df, x="Year", y="Hepatitis B", hue="Status")

col2.subheader("")


fig = plt.figure(figsize=(10, 4))
sns.countplot(x=df[option])

fig = px.sunburst(df, path=['Status', 'Country'], values='Adult Mortality', color='Status', width = 1000, height=1000)
fig.show()

st.write("""
# แสดงกราฟ

อธิบาย xxx
""")
st.pyplot(fig)



st.write("""
# Scatter Plot

อธิบาย xxx
""")
fig = plt.figure(figsize=(10, 4))
sns.scatterplot(x="math score", y="reading score", data=df)

st.pyplot(fig)

#st.write()

df2 = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [13.8, 100.55],
    columns=['lat', 'lon'])

st.map(df2)

df.hist(figsize=(40,30))
plt.show()