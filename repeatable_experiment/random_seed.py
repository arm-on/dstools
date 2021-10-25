def fix(libraries=['tf','np','pt'] , seed_number=1234):
    if 'tf' in libraries:
        import tensorflow as tf
        tf.random.set_seed(seed_number)
    if 'np' in libraries:
        import numpy as np
        np.random.seed(seed_number)
    if 'pt' in libraries:
        import torch
        torch.manual_seed(seed_number)