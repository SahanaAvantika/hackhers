import cv2, os
from mtcnn import MTCNN

detector = MTCNN()

def extract_faces(video_path, save_dir, label, frame_rate=10):
    os.makedirs(save_dir, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    interval = max(1, fps // frame_rate)
    frame_idx = 0
    saved = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if frame_idx % interval == 0:
            faces = detector.detect_faces(frame)
            for i, f in enumerate(faces):
                x, y, w, h = f['box']
                face_crop = frame[y:y+h, x:x+w]
                out_path = os.path.join(save_dir, f"{label}_{frame_idx}_{i}.jpg")
                cv2.imwrite(out_path, face_crop)
                saved += 1
        frame_idx += 1
    cap.release()
    print(f"Extracted {saved} faces from {video_path}")
