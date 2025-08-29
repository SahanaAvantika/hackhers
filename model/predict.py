import torch
import torch.nn.functional as F
from torchvision import transforms
from model import get_resnet18
from dataset import extract_faces

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor()
])

# Load model
model = get_resnet18()
model.load_state_dict(torch.load("model/saved_models/resnet18.pth"))
model.eval()

def predict_face(img):
    x = transform(img).unsqueeze(0)
    with torch.no_grad():
        out = model(x)
        probs = F.softmax(out, dim=1)
    return probs[0][1].item()  # probability fake
