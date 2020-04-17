FROM frolvlad/alpine-python-machinelearning
RUN pip3 install boto3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code COPY . /code/
ENTRYPOINT ["python", "preprocessing.py"]