import bigflow


class TheJob(bigflow.Job):
    def execute(self, context: bigflow.JobContext):
        pass


the_workflow = bigflow.Workflow(
    workflow_id='the_workflow',
    definition=[
        TheJob('the_job'),
    ],
)