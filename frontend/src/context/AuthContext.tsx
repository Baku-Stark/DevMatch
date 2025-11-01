import { createContext, useContext, useState, useEffect, type ReactNode } from "react";

import axios from "axios";
import { auth } from "../services/firebase";
import { GoogleAuthProvider, signInWithPopup } from "firebase/auth";
import { ENV } from "../config/env";

interface User {
  name: string;
  email: string;
  role: string;
  avatar_url?: string;
}

export interface IUserLogin{
    email?: string,
    password?: string
}

interface AuthContextProps {
  user: User | null;
  loading: boolean;
  signin: (email: string, password: string) => Promise<void>;
  signup: (data: User) => Promise<void>;
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
    const signup = async (data: User) => {
        try {
            setLoading(true);
            const response = await axios.post(
                `${ENV.APIROUTE}/users/sign_up`, 
                {
                    name: data.name,
                    email: data.email,
                    role: data.role,
                    avatar_url: data.avatar_url
                }
            );

            const dataResponse = response.data;

            if(response.status == 201){
                console.log(dataResponse);

                setUser(dataResponse.data);
                localStorage.setItem("devmatch:user", dataResponse.data.email);
                localStorage.setItem("devmatch:token", dataResponse.token);
            }
        
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
            localStorage.setItem("devmatch:token", "JWT_signIn");
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
        try{

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
                    //console.log(user);
    
                    const newUser = {
                        name: user.displayName ?? "",
                        email: user.email ?? "",
                        role: "",
                        avatar_url: user.photoURL ?? "",
                    };
                    //console.log(newUser);
                    setUser(newUser);

                    //localStorage.setItem("devmatch:token", token ?? "");
                    localStorage.setItem("devmatch:pendingRole", "true");
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
        } catch (error){
            console.error("Google Auth Error:", error);
        }
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
