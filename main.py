def format_time(seconds):
    if not 0 <= seconds < 8640000:
        return "Некоректне значення! Введіть число від 0 до 8639999."

    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, sec = divmod(seconds, 60)

    day_forms = {1: "день", 2: "дні", 3: "дні", 4: "дні"}
    day_word = (
        day_forms.get(days % 10, "днів")
        if days % 100 not in (11, 12, 13, 14)
        else "днів"
    )

    return f"{days} {day_word}, {hours:02}:{minutes:02}:{sec:02}"


user_input = int(input("Введіть кількість секунд: "))
print(format_time(user_input))