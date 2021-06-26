# kubeflow_example
This repo is made for kubeflow example


# How to use it?
- I wrote an explain on my blog
  - iris : https://lsjsj92.tistory.com/581
  - titanic : https://lsjsj92.tistory.com/586
  - metrics_evaluation_and_check_condtion : https://lsjsj92.tistory.com/589

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

3. metrics_evaluation_and_check_condtion
  - Make kubeflow evaluation and check condition
  - Use iris data
  - Evaluation
    - Make metrics json
    - Print metrics in kubeflow
    - in 2_model_training/training_model.py
  - Check condition
    - Use dsl.condition
    - in pipeline.py
  - Result
    - ![스크린샷 2020-07-23 오전 6 11 44](https://user-images.githubusercontent.com/24634054/88229282-72758600-ccab-11ea-8a4e-24bdb2a3ab27.png)


