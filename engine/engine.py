class Engine:

    def __init__(self):

        self.pipeline = Pipeline()

    def run(

        self,

        experiment

    ):

        context = ExecutionContext(
            experiment=experiment
        )

        return self.pipeline.execute(
            context
        )
