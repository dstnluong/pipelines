# Simple pipeline with train component and debugger

An example pipeline with only [train component](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker/train). The training component has


## Prerequisites 

This pipeline uses the exact same setup as [simple_training_pipeline](https://github.com/kubeflow/pipelines/tree/master/samples/contrib/aws-samples/simple_train_pipeline).

## Steps 
1. Compile the pipeline:  
   `dsl-compile --py training-pipeline.py --output training-pipeline.tar.gz`
2. In the Kubeflow UI, upload this compiled pipeline specification (the .tar.gz file) and click on create run.
3. Once the pipeline completes, you can view the results of each debugger rule under 'Logs'.

Inputs format to `debug_hook_config`, `collection_config`, and `debug_rule_config` :
```buildoutcfg
debug_hook_config = {
    "S3OutputPath": "s3://<your_bucket_name>/path/for/data/emission/",
    "LocalPath": "/local/path/for/data/emission/",
    "HookParameters": {
        "save_interval": "10"
    }
}
collection_config = {
    "collection_name_1": {
        "include_regex": ".*"
    },
    "collection_name_2: {
        "include_regex": ".*"
    }
}
debug_rule_config = { 
    "RuleConfigurationName": "rule_name"
    "RuleEvaluatorImage": "123456789011.dkr.ecr.<region>.amazonaws.com/sagemaker-xgboost:0.90-2-cpu-py3"
    "RuleParameters": {
        "rule_to_invoke": "LossNotDecreasing",
        "tensor_regex": ".*"
    }
}
```
The provided demo pipeline `training_pipeline.py` uses a built-in rule. When using a built-in rule, `RuleConfigurationName` and `RuleParameters` will take on values listed [here](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-built-in-rules.html) and `RuleEvaluatorImage`'s possible values are listed [here](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-docker-images-rules.html#debuger-built-in-registry-ids) will depend on the specified region.

In the case of using and writing your own custom rule, `RuleEvaluatorImage` will take on a value from [here](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-docker-images-rules.html#debuger-custom-rule-registry-ids). An example of a custom debugger rule can be found [here](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html#debugger-custom-rules-api).

# Resources
* [Amazon SageMaker Debugger] (https://docs.aws.amazon.com/sagemaker/latest/dg/train-debugger.html)
* [Debugger Built-In Rules] (https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-built-in-rules.html)
* [Pre-built Docker Images for Rules] (https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-docker-images-rules.html)
* [Debugger API Examples] (https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-createtrainingjob-api.html)

