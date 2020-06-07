import kfp
import kfp.components as comp
from kfp import dsl

def print_op(msg):
    """Print a message."""
    return dsl.ContainerOp(
        name='Print',
        image='alpine:3.6',
        command=['echo', msg],
)

@dsl.pipeline(
    name='soojin-iris',
    description='soojin iris test'
)

def soojin_pipeline():
    add_p = dsl.ContainerOp(
        name="load iris data pipeline",
        image="lsjsj92/soojin-iris-load:0.7",
        arguments=[
            '--data_path', './Iris.csv'
        ],
        file_outputs={'iris' : '/iris.csv'}
    )

    train_and_eval = dsl.ContainerOp(
        name="training pipeline",
        image="lsjsj92/soojin-iris-train_and_eval:0.4",
        arguments=[
            '--data', add_p.outputs['iris']
        ],
        file_outputs={
            'accuracy' : '/accuracy.json',
            'mlpipeline-metrics' : '/mlpipeline-metrics.json'
        }
    )

    train_and_eval.after(add_p)
    baseline = 0.7
    with dsl.Condition(train_and_eval.outputs['accuracy'] > baseline ) as check_condition:
        print_op(f"accuracy는 {train_and_eval.outputs['accuracy']}로 accuracy baseline인 {baseline}보다 큽니다!")
    
    with dsl.Condition(train_and_eval.outputs['accuracy'] < baseline) as check_condition:
        print_op(f"accuracy는 {train_and_eval.outputs['accuracy']}로 accuracy baseline인 {baseline}보다 작습니다.")
    
if __name__ == "__main__":
    import kfp.compiler as compiler
    compiler.Compiler().compile(soojin_pipeline, __file__ + ".tar.gz")
