FROM python:3.14-slim

WORKDIR /randomizer

COPY requirements.txt .

RUN apt update
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "App/randomizer.py"]

EXPOSE 5000
