### example for Package installation problem solving
import numpy as np
import torch
import torch.nn as nn
import torchvision
from torchvision import models

### example for understanding versions, cuda, gpu count
print("torch version : ", torch.__version__)
print("cuda available? : ", torch.cuda.is_available())
print("cuda version: ",torch.version.cuda)
print("cuda device count: ", torch.cuda.device_count())
device_ids=list(range(torch.cuda.device_count()))
print("cuda device id: ", *device_ids, sep=", ")

### example for basic dataParallel using multi-gpu in Pytorch
from torch.utils.data import Dataset, DataLoader

# Parameters and DataLoaders
input_size = 5
output_size = 2

batch_size = 30
data_size = 100

class RandomDataset(Dataset):

    def __init__(self, size, length):
        self.len = length
        self.data = torch.randn(length, size)

    def __getitem__(self, index):
        return self.data[index]

    def __len__(self):
        return self.len

rand_loader = DataLoader(dataset=RandomDataset(input_size, data_size),
                         batch_size=batch_size, shuffle=True)

class Model(nn.Module):
    # Our model

    def __init__(self, input_size, output_size):
        super(Model, self).__init__()
        self.fc = nn.Linear(input_size, output_size)

    def forward(self, input):
        output = self.fc(input)
        print("\tIn Model: input size", input.size(),
              "output size", output.size())

        return output

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

model = Model(input_size, output_size)
if torch.cuda.device_count() > 1:
  print("Let's use", torch.cuda.device_count(), "GPUs!")
  # dim = 0 [30, xxx] -> [10, ...], [10, ...], [10, ...] on 3 GPUs
  model = nn.DataParallel(model)

model.to(device)

for data in rand_loader:
    input = data.to(device)
    output = model(input)
    print("Outside: input size", input.size(),
          "output_size", output.size())