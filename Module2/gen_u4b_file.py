with open("unicode_text.txt", "wb") as f:
    for i in range(100):
        f.write("\N{DEVANAGARI LETTER AA}".encode("utf-8"))