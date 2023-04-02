import streamlit as st

# 長方形の面積を計算する関数
def calculate_area(width, height):
    area = width * height
    return area

# Streamlitアプリケーションの作成
def main():
    st.title("長方形の面積計算アプリ")
    st.write("縦と横の長さを入力してください")

    # 縦と横の長さを入力するためのテキストボックスの作成
    width = st.text_input("横の長さ", "")
    height = st.text_input("縦の長さ", "")

    # ユーザーが入力した値を数値に変換する
    try:
        width = float(width)
        height = float(height)
    except ValueError:
        st.write("数値を入力してください")
        return

    # 面積を計算して表示する
    if st.button("計算"):
        area = calculate_area(width, height)
        st.write("長方形の面積は、", area, "です。")

if __name__ == "__main__":
    main()
