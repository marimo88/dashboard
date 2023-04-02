import streamlit as st
import math

def calc_field_of_view(height, width, pixel_size):
    # 画素数をピクセルサイズで乗算して実際の画像サイズを求める
    real_height = height * pixel_size / 1000  # mmに変換
    real_width = width * pixel_size / 1000  # mmに変換

    # 対角線の長さを計算する
    diagonal = math.sqrt(real_height ** 2 + real_width ** 2)

    # 視野角を計算する
    fov_vertical = 2 * math.degrees(math.atan(real_height / (2 * 1000)))  # ラジアンから度に変換
    fov_horizontal = 2 * math.degrees(math.atan(real_width / (2 * 1000)))  # ラジアンから度に変換

    # 結果を返す
    return round(diagonal, 2), round(fov_vertical, 2), round(fov_horizontal, 2)

# Streamlitアプリケーションの開始
st.title('カメラの視野計算プログラム')

# 入力項目の表示と値の受け取り
height = st.number_input('縦の画素数を入力してください', value=1080)
width = st.number_input('横の画素数を入力してください', value=1920)
pixel_size = st.number_input('ピクセルサイズを入力してください（単位：マイクロメートル）', value=4.3)

# 計算ボタンの表示とクリックイベントの設定
if st.button('計算'):
    # フィールドオブビューの計算
    fov_diagonal, fov_vertical, fov_horizontal = calc_field_of_view(height, width, pixel_size)
    # 結果の表示
    st.write('縦の長さ：', round(height * pixel_size / 1000, 2), 'mm')
    st.write('横の長さ：', round(width * pixel_size / 1000, 2), 'mm')
    st.write('対角線の長さ：', fov_diagonal, 'mm')
    st.write('垂直方向の視野角：', fov_vertical, '度')
    st.write('水平方向の視野角：', fov_horizontal, '度')
