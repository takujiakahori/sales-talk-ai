import streamlit as st
import openai

# ✅ Streamlit secrets からAPIキーを取得
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("営業トーク自動生成アプリ（たくじ専用）")

name = st.text_input("お客様の名前")
industry = st.text_input("業種")
problem = st.text_area("抱えている悩み")

if st.button("営業トークを生成する"):
    with st.spinner("ChatGPTが営業トークを生成中..."):
        prompt = f"""
あなたは優秀な営業パーソンです。
以下の顧客に対して、最も刺さる営業トークを作成してください。

■ 顧客名：{name}
■ 業種：{industry}
■ 抱えている課題：{problem}

30秒程度で話せる営業トークを提案してください。
"""
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )
        result = response.choices[0].message.content
        st.success("営業トークが完成しました！")
        st.write(result)