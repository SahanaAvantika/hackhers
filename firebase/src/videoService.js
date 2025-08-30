// src/videoService.js
import { ref, uploadBytes, getDownloadURL } from "firebase/storage";
import { collection, addDoc, serverTimestamp } from "firebase/firestore";
import { auth, db, storage } from "./firebaseConfig";

//User uploads from gallery
export async function uploadVideoFromGallery(file) {
  const user = auth.currentUser;
  if (!user) throw new Error("Not logged in");

  const storageRef = ref(storage, `videos/${user.uid}/${Date.now()}-${file.name}`);
  await uploadBytes(storageRef, file);
  const downloadURL = await getDownloadURL(storageRef);

  await addDoc(collection(db, user.uid, "uploads"), {
    videoUrl: downloadURL,
    probability: null,
    uploadedAt: serverTimestamp()
  });
}
//User provides internet video URL
export async function uploadVideoFromURL(videoUrl) {
  const user = auth.currentUser;
  if (!user) throw new Error("Not logged in");

  await addDoc(collection(db, user.uid, "uploads"), {
    videoUrl,
    probability: null,
    uploadedAt: serverTimestamp()
  });
}
