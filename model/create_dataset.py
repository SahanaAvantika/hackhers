import torch
from torch.utils.data import Dataset
from torchvision import transforms
from PIL import Image
import os

class SimpleFaceDataset(Dataset):
    def __init__(self, data_dir, transform=None):
        self.data_dir = data_dir
        self.transform = transform
        self.images = []
        self.labels = []
        
        print(f"Looking in data_dir: {data_dir}")
        print(f"data_dir exists: {os.path.exists(data_dir)}")
        
        real_dir = "../dataset/train/real"
        print(f"Real dir exists: {os.path.exists(real_dir)}")
        
        if os.path.exists(real_dir):
            real_files = [f for f in os.listdir(real_dir) if f.endswith('.jpg')]
            print(f"Found {len(real_files)} real images")
            for filename in real_files:
                self.images.append(os.path.join(real_dir, filename))
                self.labels.append(0)  # 0 for real
        
        fake_dir = "../dataset/train/fake"
        print(f"Fake dir path: {fake_dir}")
        print(f"Fake dir exists: {os.path.exists(fake_dir)}")
        
        if os.path.exists(fake_dir):
            fake_files = [f for f in os.listdir(fake_dir) if f.endswith('.jpg')]
            print(f"Found {len(fake_files)} fake images")
            for filename in fake_files:
                self.images.append(os.path.join(fake_dir, filename))
                self.labels.append(1)  # 1 for fake
        
        print(f"Total loaded: {len(self.images)} images")
    
    def __len__(self):
        return len(self.images) 
    
    def __getitem__(self, idx):
        img_path = self.images[idx]
        label = self.labels[idx]
        
        try:
            image = Image.open(img_path).convert('RGB')
            if self.transform:
                image = self.transform(image)
            return image, label
        except Exception as e:
            print(f"Error loading image {img_path}: {e}")
            return torch.zeros(3, 224, 224), label

def get_train_dataset():
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])
    
    return SimpleFaceDataset("dataset/train", transform=transform)

print("Creating training dataset from existing extracted faces...")
train_dataset = get_train_dataset()

print(f"Dataset created successfully!")
print(f"Total images: {len(train_dataset)}")
print(f"Real images: {sum(1 for _, label in train_dataset if label == 0)}")
print(f"Fake images: {sum(1 for _, label in train_dataset if label == 1)}")

print("Dataset is ready for training!")