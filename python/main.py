from flask import Flask
import random
import string


app = Flask(__name__)


# Список фактов
facts_list = [
    "Python назван в честь шоу Monty Python, а не вида птиц.",
    "Функция print() в Python 3 — это функция, а не ключевое слово, как в Python 2.",
    "В Python всё является объектом, включая числа, строки и функции.",
    "Оператор // в Python означает целочисленное деление.",
    "Python использует отступы вместо фигурных скобок, что делает код читаемым."
]


@app.route("/")
def index():
    return '<h1>Добро пожаловать!</h1><p><a href="/random_fact">Получить случайный факт о Python</a></p><p><a href="/secret">Тайная страница (генератор паролей)</a></p>'


@app.route("/random_fact")
def random_fact():
    fact = random.choice(facts_list)
    return f'<h1>Случайный факт о Python</h1><p>{fact}</p><p><a href="/">Вернуться на главную</a></p>'


@app.route("/secret")
def secret():
    # Генератор случайного пароля длиной 12 символов
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(12))
    return f'<h1>🔐 Ты нашёл тайную страницу!</h1><p>Твой случайный пароль: <strong>{password}</strong></p><p><a href="/">Вернуться на главную</a></p>'


if __name__ == "__main__":
    app.run(debug=True)