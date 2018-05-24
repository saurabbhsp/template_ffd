import os

params_dir = os.path.join(os.path.dirname(__file__), 'params')
if not os.path.isdir(params_dir):
    os.makedirs(params_dir)


def get_params_path(model_id):
    return os.path.join(params_dir, '%s.json' % model_id)


def load_params(model_id):
    import json
    path = get_params_path(model_id)
    if not os.path.isfile(path):
        raise ValueError('No parameter file found at %s for model %s' %
                         (path, model_id))
    with open(path, 'r') as fp:
        params = json.load(fp)
    return params


def get_builder(model_id):
    from template_ffd_builder import TemplateFfdBuilder
    params = load_params(model_id)
    return TemplateFfdBuilder(model_id, params)
