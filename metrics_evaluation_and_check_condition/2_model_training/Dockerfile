FROM lsjsj92/keras-tensorflow:1.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
ENTRYPOINT ["python", "training_model.py"]