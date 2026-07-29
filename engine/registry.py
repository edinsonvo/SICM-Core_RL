class Registry:

    _models = {}

    @classmethod
    def register(
        cls,
        model_class
    ):

        cls._models[
            model_class.model_name
        ] = model_class

        return model_class

    @classmethod
    def get(
        cls,
        model_name
    ):

        return cls._models[model_name]
