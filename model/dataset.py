import cv2, os
from mtcnn import MTCNN

detector = MTCNN()

def extract_faces(video_path, save_dir, label, frame_rate=60, max_faces=20):
    os.makedirs(save_dir, exist_ok=True)
    detector = MTCNN()
    
    path_parts = video_path.split(os.sep)
    method_name = path_parts[-2] 
    video_name = os.path.splitext(path_parts[-1])[0]
    
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    interval = max(1, fps // frame_rate)
    frame_idx = 0
    saved = 0

    while cap.isOpened() and saved < max_faces:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_idx % interval == 0:
            faces = detector.detect_faces(frame)
            for i, f in enumerate(faces):
                if saved >= max_faces:
                    break
                x, y, w, h = f['box']
                face_crop = frame[y:y+h, x:x+w]
                
                out_path = os.path.join(save_dir, f"{label}_{method_name}_{video_name}_{saved}.jpg")
                cv2.imwrite(out_path, face_crop)
                saved += 1
        frame_idx += 1
    cap.release()
    print(f"Extracted {saved} faces from {video_path}")