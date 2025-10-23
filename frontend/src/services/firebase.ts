// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
//import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDZ3g-XMBKZoCQvdZ0UpO3NQt_wf5CQ_Js",
  authDomain: "devmatch-auth-521a1.firebaseapp.com",
  projectId: "devmatch-auth-521a1",
  storageBucket: "devmatch-auth-521a1.firebasestorage.app",
  messagingSenderId: "515640480811",
  appId: "1:515640480811:web:024e8f9120751c1bd3466e",
  measurementId: "G-V0XYMQN2TX"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
//const analytics = getAnalytics(app);

export const auth = getAuth(app);