FROM python:3.8
RUN apt-get update && apt-get install -y python3
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python"]
CMD ["app.py"]