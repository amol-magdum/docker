FROM python

WORKDIR /myapp

RUN pip install requests

COPY . .

CMD ["python3", "facts.py"]

#docker build -t dogfacts .
# docker run --rm dogfacts