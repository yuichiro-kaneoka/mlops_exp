from art import text2art
import random

# アスキーアートの生成と幅制限
def generate_ascii_art():
    words = ["Hello", "GitHub", "Push", "Action", "Fun", "Art"]
    small_fonts = ["small", "mini", "thin", "tiny", "cybermedium", "fancy1"]
    art_style = random.choice(small_fonts)
    
    art = text2art(random.choice(words), art_style)
    
    # 各行の幅を50文字以内に制限
    limited_art = "\n".join([line[:50] for line in art.splitlines()])
    return limited_art

if __name__ == "__main__":
    art = generate_ascii_art()
    with open("art.txt", "w") as f:
        f.write(art)
