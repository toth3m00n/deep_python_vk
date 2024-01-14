import requests
from collections import Counter
from bs4 import BeautifulSoup
import re


def count_words(url, k):

    # Получаем текст с веб-страницы
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()

    # Очищаем текст от символов пунктуации и лишних пробелов
    cleaned_text = re.sub(r'[^\w\s]', '', text)

    words = cleaned_text.lower().split()

    word_counts = Counter(words)
    most_common_words = dict(word_counts.most_common(k))

    return most_common_words


# print(count_words("https://en.wikipedia.org/wiki/Python_(programming_language)", 10))

for i in range(10):
    print(count_words("https://realpython.com/python-gil/#:~:text=The%20Python%20Global%20Interpreter%20Lock,in%20CPU%2Dbound%20and%20multi%2Dthreaded%20code", 10))