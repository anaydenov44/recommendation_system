FROM python:3.11-slim

# Установка системных библиотек
RUN apt-get update && \
    apt-get install -y gcc libmariadb-dev-compat libmariadb-dev

# Установка Python-зависимостей
RUN pip install --no-cache-dir flask flask-sqlalchemy pymysql cryptography

# Копируем приложение
COPY app.py .

# Запуск
CMD ["python", "app.py"]
