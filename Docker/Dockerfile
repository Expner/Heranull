FROM python:3.12.0-alpine3.18

WORKDIR /my_heranull

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add git
RUN git clone https://github.com/Expner/Heranull.git
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "Heranull/heranull/manage.py", "runserver", "0.0.0.0:8000"]