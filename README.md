# kubeflow_example
This repo is made for kubeflow example

1. iris
  - Make kubeflow pipeline for simple example : iris data
  - Doing load data -> training data
  - If you want to start this example do this:
    1. Make each dokcer image(preprocessing, training)
    2. Make kubeflow pipeline(pipeline.py)
    3. Start kubeflow
    4. Upload pipeline and start experiment

2. titanic
  - Make kubeflow pipline for simple AWS example with titanic data
  - The process of this kubeflow pipeline :
    In preprocessing
    1. Get data from AWS s3
    2. Preprocessing data
    3. Upload to AWS s3 after preprocessing data
    Until here, doing in preprocessing

    In train_model
    4. Get preprocessing data from s3
    5. Training model
    6. Upload model to s3