FROM python:3.12

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /src

COPY requirements.txt /src/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /src/

ENV DJANGO_SETTINGS_MODULE=config.settings

RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
