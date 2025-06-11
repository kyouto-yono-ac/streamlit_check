import streamlit as st
import random
from datetime import datetime

st.markdown(
    """
    <style>
        body {
            background-color: #f0f8ff;
        }
        .stApp {
            background-color: #f0f8ff;
        }
        .stButton>button {
            background-color: #0288d1;
            color: white;
            border-radius: 10px;
            padding: 0.5em 1em;
            font-weight: bold;
        }
        .stButton>button:hover {
            background-color: #0277bd;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #01579b;
        }
        .stMarkdown {
            color: #004d6d;
        }
    </style>
    """,
    unsafe_allow_html=True
)

omikuji_list = ["大吉", "吉", "中吉", "小吉", "凶"]

omikuji_messages = {
    "大吉": "今日は最高！何をやってもうまくいくよ！",
    "吉": "いいかんじ！色々挑戦してみよう！",
    "中吉": "まあまあいいかなぁ。無理せず行動しよう！",
    "小吉": "ちょっと注意が必要。慎重に進もう！",
    "凶": "今日は大注意！落ち着いて行動しよう～",
}

meals = [
    {"name": "カレーライス", "image": "images/pic1.jpg"},
    {"name": "ラーメン", "image": "images/pic2.jpg"},
    {"name": "ハンバーグ", "image": "images/pic3.jpg"},
    {"name": "寿司", "image": "images/pic4.jpg"},
    {"name": "おでん", "image": "images/pic5.jpg"},
    {"name": "肉じゃが", "image": "images/pic6.jpg"},
    {"name": "天ぷら", "image": "images/pic7.jpg"},
    {"name": "おそば", "image": "images/pic8.jpg"},
    {"name": "パスタ", "image": "images/pic9.jpg"},
    {"name": "焼肉", "image": "images/pic10.jpg"},
]

sweets = [
    {"name": "ショートケーキ", "image": "images/sweets1.jpg"},
    {"name": "プリン", "image": "images/sweets2.jpg"},
    {"name": "チョコクッキー", "image": "images/sweets3.jpg"},
    {"name": "ソフトクリーム", "image": "images/sweets4.jpg"},
    {"name": "シュークリーム", "image": "images/sweets5.jpg"},
]

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
    st.title("♪ 今日の運勢 ♬♩ ")

    if not st.session_state.show_result:
        st.write("↓↓ボタンを押しておみくじを引こう！")
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
            st.write("🍰 とくべつスイーツ♡ 🍰")
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
