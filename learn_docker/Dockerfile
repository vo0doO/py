# Использовать официальную среду исполнения Python в качестве родительского образа
FROM python:2.7-slim

# Установить рабочий каталог в /app
WORKDIR /app

# Скопируйте содержание текущего каталога в контейнер в /app
COPY . /app

# Установите все необходимые пакеты указанные в файле requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Сделаем порт 80 доступный для мира за пределами контейнера
EXPOSE 80

# Определить переменную среды
ENV NAME World
# Set proxy server, replace host:port with values for your servers
ENV http_proxy 127.0.0.1:80
ENV https_proxy 127.0.0.1:443

# Запустите app.py при запуске контейнера
CMD ["python", "app.py"]
