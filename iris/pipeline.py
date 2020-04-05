import kfp
import kfp.components as comp
from kfp import dsl
@dsl.pipeline(
    name='soojin-iris',
    description='soojin iris test'
)

def soojin_pipeline():
    add_p = dsl.ContainerOp(
        name="load iris data pipeline",
        image="lsjsj92/soojin-iris-preprocessing:0.5",
        arguments=[
            '--data_path', './iris.csv'
        ],
        file_outputs={'iris' : '/iris.csv'}
    )

    ml = dsl.ContainerOp(
        name="training pipeline",
        image="lsjsj92/soojin-iris-train:0.5",
        arguments=[
            '--data', add_p.outputs['iris']
        ]
    )

    ml.after(add_p)
    
if __name__ == "__main__":
    import kfp.compiler as compiler
    compiler.Compiler().compile(soojin_pipeline, __file__ + ".tar.gz")
