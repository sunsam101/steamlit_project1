import streamlit as st
st.title("這是我的第一個streamlit專案")
st.header("請是我的次標題")
st.subheader("這是我的次次標題")
st.write("這是段落1")
st.write("這是段落2")
st.write("這是段落3")
st.sidebar.markdown('''
this is markdown
abc 
def 
klg
'''
)
st.button("按鈕1")

print("程式結束")