from . import models

def get_models():
    for model_name in models.__all__:
        model = getattr(models, model_name)

        yield model

