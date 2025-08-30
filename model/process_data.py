import os
import shutil
from dataset import extract_faces

def organize_faces():

    os.makedirs("dataset/train", exist_ok=True)
    
    faceforensics_root = "../FaceForensics++_C23"
    
    print("Processing real videos...")
    real_dir = os.path.join(faceforensics_root, "original")
    if os.path.exists(real_dir):
        for video_file in os.listdir(real_dir)[:10]: 
            if video_file.endswith('.mp4'):
                video_path = os.path.join(real_dir, video_file)
                print(f"Processing {video_file}...")
                extract_faces(video_path, "../dataset/train/real", "real")
    
    print("Processing fake videos...")
    fake_methods = ["Deepfakes", "Face2Face", "FaceSwap", "NeuralTextures", "FaceShifter", "DeepFakeDetection"]
    
    for method in fake_methods:
        method_dir = os.path.join(faceforensics_root, method)
        if os.path.exists(method_dir):
            print(f"Processing {method}...")
            for video_file in os.listdir(method_dir)[:10]:
                if video_file.endswith('.mp4'):
                    video_path = os.path.join(method_dir, video_file)
                    extract_faces(video_path, "../dataset/train/fake", "fake")

if __name__ == "__main__":
    organize_faces()
    print("Data organization complete!")