import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    df = pd.read_csv("data.csv")
    df['学生番号'] = df['学生番号'].astype(str).str.zfill(3)
    return df

df = load_data()

st.title("課題1　計算問題 自己チェック")

student_id = st.text_input("学生番号（下3桁）を入力", max_chars=3)
answer1 = st.text_input("問1のあなたの解答（例：1662.8）")
answer2 = st.text_input("問2のあなたの解答（例：4.6597）")

if st.button("判定する"):
    if not student_id.isdigit() or len(student_id) != 3:
        st.error("学生番号は3桁の数字で入力してください。")
    else:
        record = df[df['学生番号'] == student_id]
        if record.empty:
            st.warning("該当する学生番号が見つかりません。")
        else:
            try:
                user_a1 = round(float(answer1), 4)
                user_a2 = round(float(answer2), 4)
                correct_a1 = round(float(record.iloc[0][1]), 4)
                correct_a2 = round(float(record.iloc[0][2]), 4)

                result1 = "正解" if abs(user_a1 - correct_a1) < 0.0001 else "不正解"
                result2 = "正解" if abs(user_a2 - correct_a2) < 0.0001 else "不正解"

                st.success(f"問1：{result1}")
                st.success(f"問2：{result2}")
            except ValueError:
                st.error("解答は数値で入力してください。")
