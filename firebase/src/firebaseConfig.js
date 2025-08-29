import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";
import { getStorage } from "firebase/storage";

const firebaseConfig = {
    apiKey: "AIzaSyATCQtcg_6FaiBumXcaaZ7O0UWqz_ALAxw",
    authDomain: "hackhers-9bd46.firebaseapp.com",
    projectId: "hackhers-9bd46",
    storageBucket: "hackhers-9bd46.firebasestorage.app",
    messagingSenderId: "432429959615",
    appId: "1:432429959615:web:2381a30affbacc5428790a",
    measurementId: "G-Y7VLPFK66E"
};

const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
export const auth = getAuth(app);
export const db = getFirestore(app);
export const storage = getStorage(app);
