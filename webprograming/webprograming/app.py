import streamlit as st
import random
from datetime import datetime

# --- ページ全体の背景・文字色をCSSで設定 ---
st.markdown("""
    <style>
    body {
        background-color: #f0f8ff;
    }
    .main {
        background-color: #f0f8ff;
        color: #003366;
    }
    .stButton>button {
        background-color: #3399ff;
        color: white;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# 運勢リスト
omikuji_list = ["大吉", "吉", "中吉", "小吉", "凶"]

# 運勢ごとのメッセージ
omikuji_messages = {
    "大吉": "今日は最高！何をやってもうまくいくよ！",
    "吉": "いいかんじ！色々挑戦してみよう！",
    "中吉": "まあまあいいかなぁ。無理せず行動しよう！",
    "小吉": "ちょっと注意が必要。慎重に進もう！",
    "凶": "今日は大注意！落ち着いて行動しよう～",
}

# おすすめ料理（パスをすべて webprograming/webprograming/images/ に変更）
meals = [
    {"name": "カレーライス", "image": "webprograming/webprograming/images/pic1.jpg"},
    {"name": "ラーメン", "image": "webprograming/webprograming/images/pic2.jpg"},
    {"name": "ハンバーグ", "image": "webprograming/webprograming/images/pic3.jpg"},
    {"name": "寿司", "image": "webprograming/webprograming/images/pic4.jpg"},
    {"name": "おでん", "image": "webprograming/webprograming/images/pic5.jpg"},
    {"name": "肉じゃが", "image": "webprograming/webprograming/images/pic6.jpg"},
    {"name": "天ぷら", "image": "webprograming/webprograming/images/pic7.jpg"},
    {"name": "おそば", "image": "webprograming/webprograming/images/pic8.jpg"},
    {"name": "パスタ", "image": "webprograming/webprograming/images/pic9.jpg"},
    {"name": "焼肉", "image": "webprograming/webprograming/images/pic10.jpg"},
]

# スイーツ（パスをすべて webprograming/webprograming/images/ に変更）
sweets = [
    {"name": "ショートケーキ", "image": "webprograming/webprograming/images/sweets1.jpg"},
    {"name": "プリン", "image": "webprograming/webprograming/images/sweets2.jpg"},
    {"name": "チョコクッキー", "image": "webprograming/webprograming/images/sweets3.jpg"},
    {"name": "ソフトクリーム", "image": "webprograming/webprograming/images/sweets4.jpg"},
    {"name": "シュークリーム", "image": "webprograming/webprograming/images/sweets5.jpg"},
]

# セッションの初期化
if "history" not in st.session_state:
    st.session_state.history = []
if "show_result" not in st.session_state:
    st.session_state.show_result = False
if "current_result" not in st.session_state:
    st.session_state.current_result = None

def draw_omikuji():
    omikuji = random.choice(omikuji_list)
    message = omikuji_messages[omikuji]
    meal = random.choice(meals)

    sweets_selected = None
    if omikuji in ["大吉", "吉"]:
        sweets_selected = random.choice(sweets)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    result = {
        "omikuji": omikuji,
        "message": message,
        "meal": meal,
        "sweets": sweets_selected,
        "time": timestamp,
    }

    st.session_state.history.append(result)
    return result

def main():
    st.title("🎋 今日の運勢 🎋")

    if not st.session_state.show_result:
        st.write("👇 ボタンを押しておみくじを引こう！")
        if st.button("おみくじを引く"):
            result = draw_omikuji()
            st.session_state.current_result = result
            st.session_state.show_result = True
    else:
        result = st.session_state.current_result

        st.subheader(f"🎯 運勢: {result['omikuji']}")
        st.write(result["message"])

        st.write("🍽️ おすすめ料理 🍽️")
        st.write(f"**{result['meal']['name']}**")
        st.image(result["meal"]["image"], width=300)

        if result["sweets"] is not None:
            st.write("🍰 +αスイーツ♪ 🍰")
            st.write(f"- {result['sweets']['name']}")
            st.image(result["sweets"]["image"], width=200)

        st.write("---")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("もう一回引く！"):
                result = draw_omikuji()
                st.session_state.current_result = result
        with col2:
            if st.button("ホームに戻る"):
                st.session_state.show_result = False

        if len(st.session_state.history) > 1:
            st.write("---")
            st.subheader("🔎 過去のおみくじ履歴")
            for i, item in enumerate(st.session_state.history[-2::-1], 1):
                st.write(f"{i}. {item['time']}｜**{item['omikuji']}** - {item['meal']['name']}")

if __name__ == "__main__":
    main()
