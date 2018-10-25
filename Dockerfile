FROM python:3.6

WORKDIR /usr/src/app
RUN pip install --upgrade ptvsd

COPY . .
EXPOSE 3000
CMD python -m ptvsd --host 0.0.0.0 --port 3000 ./run.py