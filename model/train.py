import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from create_dataset import train_dataset
from model import get_resnet18

model = get_resnet18()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-4)
loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

for epoch in range(5):
    for imgs, labels in loader:
        optimizer.zero_grad()
        out = model(imgs)
        loss = criterion(out, labels)
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, Loss={loss.item():.4f}")

torch.save(model.state_dict(), "saved_models/resnet18.pth")
