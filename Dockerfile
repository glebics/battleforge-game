# Используем легковесный образ Python 3.10 (без лишних пакетов)
FROM python:3.10-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей requirements.txt в контейнер
COPY requirements.txt .

# Устанавливаем все зависимости внутри контейнера
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы проекта (из локального каталога в /app внутри контейнера)
COPY . .

# Добавляем файл ожидания БД
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Запускаем Django-сервер при старте контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
