import kfp
from kfp import components
from kfp import dsl

sagemaker_train_op = components.load_component_from_file("../../train/component.yaml")


@dsl.pipeline(name="SageMaker Training", description="SageMaker training job test")
def training_pipeline(
    region="",
    endpoint_url="",
    image="",
    job_name="",
    training_input_mode="",
    hyperparameters="",
    channels="",
    instance_type="",
    instance_count="",
    volume_size="",
    max_run_time="",
    model_artifact_path="",
    output_encryption_key="",
    vpc_security_group_ids="",
    vpc_subnets="",
    network_isolation="",
    traffic_encryption="",
    spot_instance="",
    max_wait_time="",
    checkpoint_config="",
    debug_hook_config="",
    debug_rule_config="",
    tensorboard_output_config="",
    role="",
):
    sagemaker_train_op(
        region=region,
        endpoint_url=endpoint_url,
        image=image,
        job_name=job_name,
        training_input_mode=training_input_mode,
        hyperparameters=hyperparameters,
        channels=channels,
        instance_type=instance_type,
        instance_count=instance_count,
        volume_size=volume_size,
        max_run_time=max_run_time,
        model_artifact_path=model_artifact_path,
        output_encryption_key=output_encryption_key,
        vpc_security_group_ids=vpc_security_group_ids,
        vpc_subnets=vpc_subnets,
        network_isolation=network_isolation,
        traffic_encryption=traffic_encryption,
        spot_instance=spot_instance,
        max_wait_time=max_wait_time,
        checkpoint_config=checkpoint_config,
        debug_hook_config=debug_hook_config,
        debug_rule_config=debug_rule_config,
        tensorboard_output_config=tensorboard_output_config,
        role=role,
    )


if __name__ == "__main__":
    kfp.compiler.Compiler().compile(
        training_pipeline, "SageMaker_training_pipeline" + ".yaml"
    )
