import datetime as dt

text = []
lines = 1

while 1:
    user_in = input(f"{lines}: ")
    if user_in == "EOF":
        break
    user_in = user_in + "\n"
    text.append(user_in)
    lines += 1

today = dt.datetime.now().strftime('%Y%m%d_%H%M')

with open(f"{today}.txt", "w", encoding="utf-8") as f:
    f.writelines(text)
    f.flush()