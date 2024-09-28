from art import text2art
import random

# テキストアートの生成
def generate_ascii_art():
    words = ["Hello", "GitHub", "Push", "Action", "Fun", "Art"]
    art_style = random.choice(["block", "bulbhead", "random"])  # スタイルをランダムに選択
    return text2art(random.choice(words), art_style)

if __name__ == "__main__":
    art = generate_ascii_art()
    with open("art.txt", "w") as f:
        f.write(art)
