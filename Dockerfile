# Dockerfile
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

# `"gunicorn"` é o comando para iniciar o Gunicorn.
# `"-w", "4"` define o número de workers (neste caso, 4).
# `"-b", "0.0.0.0:5000"` especifica o binding (associação) do servidor Gunicorn na porta 5000 acessível de fora do container
# `"app:app"` indica que o Gunicorn deve usar o objeto app localizado no módulo app.py.

# Inicia o Gunicorn com o aplicativo Flask localizado em app.py
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]