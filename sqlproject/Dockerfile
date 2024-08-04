FROM python

WORKDIR /myapp

COPY ./sqlscript.py .

RUN pip install pymysql
RUN pip install cryptography

CMD ["python", "sqlscript.py"]

