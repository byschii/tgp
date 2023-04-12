import torch

# check cuda is available
hopefully = torch.cuda.is_available()
divices = torch.cuda.device_count()
print(hopefully)
print(divices)