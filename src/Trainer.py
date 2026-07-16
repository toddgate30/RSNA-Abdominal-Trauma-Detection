import torch

class Trainer():
    def before_train():
        raise NotImplementedError
    
    def train():
        raise NotImplementedError
    
    def after_train():
        raise NotImplementedError