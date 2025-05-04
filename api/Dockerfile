FROM ubuntu:latest

# Instala dependências
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv

# Cria ambiente virtual e instala pacotes
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"
RUN pip install flask flask-cors

WORKDIR /app
COPY . /app

EXPOSE 5000

CMD ["python", "app.py"]
