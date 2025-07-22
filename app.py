import ipywidgets as widgets
from IPython.display import display, clear_output

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

current_key = "start"
answers = []

# ウィジェット作成
question_label = widgets.HTML(value="<b>質問がここに表示されます</b>")
radio = widgets.RadioButtons(options=["はい", "いいえ"], value=None)
button = widgets.Button(description="次へ")
result_output = widgets.Output()

# 表示レイアウト
display(question_label, radio, button, result_output)

# 次へボタンの処理
def on_next_clicked(b):
    global current_key, answers

    answer = radio.value
    if answer is None:
        with result_output:
            clear_output()
            print("「はい」か「いいえ」を選んでください。")
        return

    bit = 1 if answer == "はい" else 0
    answers.append(bit)
    next_key = question_tree[current_key]["yes" if bit == 1 else "no"]

    if isinstance(question_tree.get(next_key), str):
        # 結果を表示
        question_label.value = "<b>診断結果：</b>"
        radio.disabled = True
        button.disabled = True
        with result_output:
            clear_output()
            print(question_tree[next_key])
           
    else:
        # 次の質問に進む
        current_key = next_key
        question_label.value = f"<b>{question_tree[current_key]['text']}</b>"
        radio.value = None
        with result_output:
            clear_output()

# イベント登録
button.on_click(on_next_clicked)

# 最初の質問表示
question_label.value = f"<b>{question_tree[current_key]['text']}</b>"