import kfp
import kfp.components as comp
from kfp import dsl
from kfp import compiler

@dsl.pipeline(
    name='soojin-kubeflow-titanic',
    description = "This is a pipeline of titanic made by soojin(lsjsj92.tistory.com)"
)
def titanic_pipeline(
    BUCKETNAME,
    ACCESSKEY,
    SECRETKEY,
    REGIONNAME,
    ORIKEY,
    SAVEKEY,
    MODELKEY):
    
    step_1_preprocessing = dsl.ContainerOp(
        name = 'cleaning titanic data',
        image = 'lsjsj92/titanic_preprocessing:latest',
        arguments=[
            '--bucket_name' , BUCKETNAME,
            '--ACCESSKEY' , ACCESSKEY,
            '--SECRETKEY' , SECRETKEY,
            '--region_name' , REGIONNAME,
            '--data_key' , ORIKEY,
            '--save_key' , SAVEKEY
        ]
    )

    step_2_training = dsl.ContainerOp(
        name = 'training model',
        image = 'lsjsj92/titanic_modeling:latest',
        arguments=[
            '--bucket_name' , BUCKETNAME,
            '--ACCESSKEY', ACCESSKEY,
            '--SECRETKEY', SECRETKEY,
            '--region_name' , REGIONNAME,
            '--model_key' , MODELKEY,
            '--data' , SAVEKEY
        ]
    )

    step_2_training.after(step_1_preprocessing)

compiler.Compiler().compile(titanic_pipeline, 'soojin_titanic.tar.gz')