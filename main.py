import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import torchvision
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import time
import os
import copy
from utils import initialize_model
from data import get_data_loader
from train import train_model

if __name__ == "__main__":
    data_dir = "D:\github\Cifar100\dataset\hymenoptera_data"
    model_name = "resnet"
    num_classes = 2
    batch_size = 8
    num_epochs = 15
    feature_extract = True
    model_ft = initialize_model(model_name, num_classes, feature_extract, use_pretrained = True)
    model_ft = model_ft.cuda()
    params_to_update = model_ft.parameters()
    if feature_extract:
        params_to_update = []
        for name,param in model_ft.named_parameters():
            if param.requires_grad == True:
                params_to_update.append(param)

    # Observe that all parameters are being optimized
    optimizer_ft = optim.SGD(params_to_update, lr=0.001, momentum=0.9)
    criterion = nn.CrossEntropyLoss()
    dataloaders_dict = get_data_loader(data_dir = data_dir, batch_size=batch_size)
    model_ft, hist = train_model(model_ft, dataloaders_dict, criterion, optimizer_ft, num_epochs=num_epochs)