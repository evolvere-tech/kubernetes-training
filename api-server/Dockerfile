FROM python:3.6.9
COPY requirements.txt /
RUN  pip3 install -r /requirements.txt
COPY ./*.py /app/
COPY ./*.yaml /app/
WORKDIR /app
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "wsgi:app"]
