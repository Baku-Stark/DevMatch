import { createContext, useContext, useState, useEffect, type ReactNode } from "react";

import axios from "axios";

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
  signinWithGoogle: () => void;
  signinWithGithub: () => void;
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
     */
    const signinWithGoogle = () => {
        window.location.href = `${import.meta.env.VITE_API_URL}/auth/google`;
    };

    /**
     * # OAuth GitHub
     * 
     * File: `AuthConext`
     */
    const signinWithGithub = () => {
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
            signinWithGoogle,
            signinWithGithub,
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
