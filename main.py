def format_time(seconds):
    if not (0 <= seconds < 8640000):
        return "Некоректне значення! Введіть число від 0 до 8639999."

    days, remainder = divmod(seconds, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, sec = divmod(remainder, 60)

    day_word = "день" if days % 10 == 1 and days % 100 != 11 else "дні" if 2 <= days % 10 <= 4 and not (
                12 <= days % 100 <= 14) else "днів"

    return f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(sec).zfill(2)}"

user_input = int(input("Введіть кількість секунд: "))
print(format_time(user_input))