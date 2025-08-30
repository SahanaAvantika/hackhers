// import { ref, uploadBytes, getDownloadURL } from "firebase/storage";
// import { collection, addDoc, serverTimestamp } from "firebase/firestore";
// import { auth, db, storage } from "./firebaseConfig";

// //User uploads from gallery
// export async function uploadVideoFromGallery(file) {
//   const user = auth.currentUser;
//   if (!user) throw new Error("Not logged in");

//   const storageRef = ref(storage, `videos/${user.uid}/${Date.now()}-${file.name}`);
//   await uploadBytes(storageRef, file);
//   const downloadURL = await getDownloadURL(storageRef);

//   await addDoc(collection(db, user.uid, "uploads"), {
//     videoUrl: downloadURL,
//     probability: null,
//     uploadedAt: serverTimestamp()
//   });
// }
// //User provides internet video URL
// export async function uploadVideoFromURL(videoUrl) {
//   const user = auth.currentUser;
//   if (!user) throw new Error("Not logged in");

//   await addDoc(collection(db, user.uid, "uploads"), {
//     videoUrl,
//     probability: null,
//     uploadedAt: serverTimestamp()
//   });
// }


// firebase/src/videoService.js
import { auth } from "./firebaseConfig";

/**
 * Unified function to upload a video (from gallery file or internet URL)
 * Sends video to backend, backend handles Firestore updates
 * @param {File|null} file - optional, local file from gallery
 * @param {string|null} videoUrl - optional, internet video URL
 * @returns {Promise<Object>} - JSON response from backend
 */
export async function uploadVideo(file = null, videoUrl = null) {
  const user = auth.currentUser;
  if (!user) throw new Error("Not logged in");

  const formData = new FormData();
  formData.append("uid", user.uid);

  if (file) {
    formData.append("file", file);
  } else if (videoUrl) {
    formData.append("videoUrl", videoUrl);
  } else {
    throw new Error("No file or video URL provided");
  }

  const response = await fetch("http://localhost:8000/upload", {
    method: "POST",
    body: formData,
  });

  return response.json(); // {status, uploadId, videoUrl}
}

/**
 * Call backend analyze endpoint
 * @param {string} uploadId - Firestore upload document ID
 * @returns {Promise<Object>} - analysis result
 */
export async function analyzeVideo(uploadId) {
  const user = auth.currentUser;
  if (!user) throw new Error("Not logged in");

  const formData = new FormData();
  formData.append("uid", user.uid);
  formData.append("uploadId", uploadId);

  const response = await fetch("http://localhost:8000/analyze", {
    method: "POST",
    body: formData,
  });

  return response.json(); // {status, result}
}

//Get results for an upload
export async function getResults(uploadId) {
  const user = auth.currentUser;
  if (!user) throw new Error("Not logged in");

  const response = await fetch(`http://localhost:8000/results/${user.uid}/${uploadId}`);
  return response.json();
}
