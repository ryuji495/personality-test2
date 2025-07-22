import streamlit as st

# 質問と選択肢の設定
question_tree = {
    "start": {
        "text": "あなたはよく外出をするほうですか？",
        "yes": "q1",
        "no": "q2"
    },
    "q1": {
        "text": "コミュ力があると思う？",
        "yes": "q3",
        "no": "q4"
    },
    "q2": {
        "text": "思考力があるほうだと思う？",
        "yes": "q4",
        "no": "q5"
    },
    "q3": {
        "text": "仲間が失敗しても許してあげる?",
        "yes": "q6",
        "no": "q7"
    },
    "q4": {
        "text": "自分は聞き上手だと思う？",
        "yes": "q8",
        "no": "q9"
    },
    "q5": {
        "text": "自分には特別な力があると思う",
        "yes": "j",
        "no": "i"
    },
    "q6": {
        "text": "自分より他人のことを優先する",
        "yes": "a",
        "no": "b"
    },
    "q7": {
        "text": "失敗してしまったら落ち込むよりもイライラする",
        "yes": "c",
        "no": "d"
    },
    "q8": {
        "text": "一人よりも大人数のほうがいい",
        "yes": "e",
        "no": "f"
    },
    "q9": {
        "text": "感情的になりやすいと思う？",
        "yes": "g",
        "no": "h"
    },
    "a": "あなたはポジティブタイプです！",
    "b": "あなたは優しいタイプです！",
    "c": "あなたはネガティブタイプです！",
    "d": "あなたは怒りっぽいタイプです！",
    "e": "あなたはクールタイプです！",
    "f": "あなたはおとなしいタイプです！",
    "g": "あなたは感情豊かなタイプです！",
    "h": "あなたは熱血タイプです！",
    "i": "あなたは天然タイプです！",
    "j": "あなたは変人タイプです！",
}

# セッション状態を使って進行管理
if 'current_key' not in st.session_state:
    st.session_state.current_key = "start"

current_key = st.session_state.current_key

st.title("性格診断テスト")
st.markdown(f"**{question_tree[current_key]['text']}**")

# ボタンで回答
col1, col2 = st.columns(2)
if col1.button("はい"):
    answer = "yes"
elif col2.button("いいえ"):
    answer = "no"
else:
    answer = None

# 回答処理
if answer:
    next_key = question_tree[current_key][answer]
    if isinstance(question_tree[next_key], str):
        st.markdown("### 診断結果")
        st.success(question_tree[next_key])
        st.session_state.current_key = "start"
    else:
        st.session_state.current_key = next_key
        st.rerun()

