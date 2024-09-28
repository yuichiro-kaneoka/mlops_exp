from art import text2art
import random

# アスキーアートの生成と幅制限
def generate_ascii_art():
    words = ["Hello", "GitHub", "Push", "Action", "Fun", "Art"]
    art_style = random.choice(["block", "bulbhead", "random"])  # スタイルをランダムに選択
    
    art = text2art(random.choice(words), art_style)
    
    # 各行の幅を50文字以内に制限
    limited_art += "```\n"
    limited_art = "\n".join([line[:100] for line in art.splitlines()])
    limited_art += "\n```"
    return limited_art

if __name__ == "__main__":
    art = generate_ascii_art()
    with open("art.txt", "w") as f:
        f.write(art)
