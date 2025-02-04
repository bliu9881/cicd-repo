import aws_cdk as cdk
from constructs import Construct
from aws_cdk.pipelines import CodePipeline, CodePipelineSource, ShellStep
from my_pipeline.my_pipeline_app_stage import MyPipelineAppStage

class MyPipelineStack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        pipeline =  CodePipeline(self, "Pipeline",
                    pipeline_name="MyPipeline",
                    synth=ShellStep("Synth",
                        input=CodePipelineSource.git_hub("bliu9881/cicd-repo", "main"),
                        commands=["npm install -g aws-cdk",
                            "python -m pip install -r requirements.txt",
                            "cdk synth"]
                    )
                    )
        pipeline.add_stage(MyPipelineAppStage(self, "test",
            env=cdk.Environment(account="779227446268", region="us-east-1")))