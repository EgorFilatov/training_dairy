FROM python:latest

#RUN apt-get update \
#	&& apt-get install -y --no-install-recommends \
#		postgresql-client \
#	&& rm -rf /var/lib/apt/lists/*
ENV PYTHONDONTWRITEBYTECODE 1
ENV PUTHONUNBUFFERED 1

WORKDIR /usr/src/training_dairy
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt
COPY . /usr/src/training_dairy

EXPOSE 8000
CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]