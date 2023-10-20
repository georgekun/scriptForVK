FROM python:3.8

# Установите переменную окружения для отключения вывода буферизации Python
ENV PYTHONUNBUFFERED 1


# Установите рабочую директорию внутри контейнера
WORKDIR /app

# Скопируйте файлы проекта в рабочую директорию
COPY . /app/

# Установите зависимости проекта
RUN pip install -r requirements.txt

# Запустите Django приложение и celery одновременно
RUN  echo "Сборка завершен"
CMD ["python3", "/app/main.py"]
