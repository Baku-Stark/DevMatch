import { createContext, useContext, useState, useEffect, type ReactNode } from "react";

import axios from "axios";
import { auth } from "../services/firebase";
import { GoogleAuthProvider, signInWithPopup } from "firebase/auth";

interface User {
  id: string;
  name: string;
  email: string;
  avatar?: string;
}

export interface IUserLogin{
    email?: string,
    password?: string
}

export interface IUserRegister{
    name?: string,
    email?: string,
    password?: string,
    confirmPassword?: string,
}

interface AuthContextProps {
  user: User | null;
  loading: boolean;
  signin: (email: string, password: string) => Promise<void>;
  signup: (data: { name: string; email: string; password: string }) => Promise<void>;
  AuthWithGoogle: () => void;
  AuthWithGithub: () => void;
  logout: () => void;
}

const AuthContext = createContext<AuthContextProps>({} as AuthContextProps);

export function AuthProvider({ children }: { children: ReactNode }) {

    const [user, setUser] = useState<User | null>(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const savedUser = localStorage.getItem("devmatch:user");
        if (savedUser) setUser(JSON.parse(savedUser));
        setLoading(false);
    }, []);

    /**
     * # Manual create account Method
     * 
     * File: `AuthConext`
     * 
     * @param data JSON
     */
    const signup = async (data: { name: string; email: string; password: string }) => {
        try {
            setLoading(true);
            const response = await axios.post("/api/auth/signup", data);
            setUser(response.data.user);
            localStorage.setItem("devmatch:user", JSON.stringify(response.data.user));
            localStorage.setItem("devmatch:token", response.data.token);
        } finally {
            setLoading(false);
        }
    };

    /**
     * # Login Auth Method
     * 
     * File: `AuthConext`
     * 
     * @param email User's email
     * @param password User's password
    */
    const signin = async (email: string, password: string) => {
        try {
            setLoading(true);
            const response = await axios.post("/api/auth/signin", { email, password });
            setUser(response.data.user);
            localStorage.setItem("devmatch:user", JSON.stringify(response.data.user));
            localStorage.setItem("devmatch:token", response.data.token);
        } finally {
            setLoading(false);
        }
    };

    /**
     * # OAuth Google 
     * 
     * File: `AuthConext`
     * Link: https://firebase.google.com/docs/auth/web/google-signin?hl=pt-br
     */
    const AuthWithGoogle = async () => {
        console.log(`%c AUTH %c GOOGLE `, 
            'background: #C4473A; color: #f0eff5; font-weight: bold;',
            'background: #f0f8ff; color: #111111; font-weight: bold;'
        );

        const provider = new GoogleAuthProvider();
        provider.addScope('https://www.googleapis.com/auth/contacts.readonly');
        provider.setCustomParameters({
            'login_hint': 'user@example.com'
        });

        signInWithPopup(auth, provider)
            .then((result) => {
                // This gives you a Google Access Token. You can use it to access the Google API.
                const credential = GoogleAuthProvider.credentialFromResult(result);
                const token = credential?.accessToken;
                // The signed-in user info.
                const user = result.user;
                // IdP data available using getAdditionalUserInfo(result)
                // ...
                console.log(user);
             }).catch((error) => {
                // Handle Errors here.
                const errorCode = error.code;
                const errorMessage = error.message;
                // The email of the user's account used.
                const email = error.customData.email;
                // The AuthCredential type that was used.
                const credential = GoogleAuthProvider.credentialFromError(error);
                // ...
                //console.error(errorMessage);
            });
    };

    /**
     * # OAuth GitHub
     * 
     * File: `AuthConext`
     */
    const AuthWithGithub = () => {
        window.location.href = `${import.meta.env.VITE_API_URL}/auth/github`;
    };

    const logout = () => {
            localStorage.removeItem("devmatch:user");
            localStorage.removeItem("devmatch:token");
            setUser(null);
    };

    return (
        <AuthContext.Provider
        value={{
            user,
            loading,
            signin,
            signup,
            AuthWithGoogle,
            AuthWithGithub,
            logout,
        }}
        >
            {children}
        </AuthContext.Provider>
    );
}

export function useAuth() {
  return useContext(AuthContext);
}
