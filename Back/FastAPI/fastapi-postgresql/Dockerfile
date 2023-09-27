FROM ubuntu:basic

WORKDIR /app
COPY . /app/
RUN  apt-get update && \
     pip install --upgrade pip && \
     pip install -r requirements.txt 

EXPOSE 80

CMD ["uvicorn", "main:app", \
     "--host", "0.0.0.0", "--port", "80"]