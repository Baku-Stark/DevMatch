import { Github } from "lucide-react";
import { Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";
import { ROUTES } from "../routes/routes";
import { useEffect, useState } from "react";
import { RoleSelectionModal } from "../components/RoleSelectionModal";


export default function SignUp() {
    const { AuthWithGoogle, AuthWithGithub, user, signup } = useAuth();
    const [showRoleModal, setShowRoleModal] = useState(false);

    useEffect(() => {
        const pending = localStorage.getItem("devmatch:pendingRole");
        if (user && pending) setShowRoleModal(true);
    }, [user]);

    const handleRoleSelect = async (role: "mentor" | "mentee") => {
        localStorage.removeItem("devmatch:pendingRole");
        setShowRoleModal(false);
        user!.role = role;

        //console.log(user);
        
        signup(user!);

        alert(`Welcome to DevMatch as a ${role}!`);
    };

    return (
        <main className="min-h-screen flex items-center justify-center bg-main-bg-color px-6">
            <div className="bg-[#1a1a1a] shadow-lg rounded-2xl p-10 max-w-md w-full text-center border border-gray-800">
                
                {/* Logo */}
                <div className="flex flex-col items-center mb-6">
                <img
                    src="/assets/images/devmatch_logo.png"
                    alt="DevMatch Logo"
                    className="w-16 h-16 mb-3"
                />
                <h1 className="text-3xl font-extrabold" style={{ color: "var(--main-color)" }}>
                    Create Account
                </h1>
                <p className="subtext">
                    Join DevMatch and start connecting with developers 🚀
                </p>
                </div>

                {/* Botões OAuth */}
                <div className="flex flex-col gap-4">
                <button
                    onClick={AuthWithGoogle}
                    className="cursor-pointer flex items-center justify-center gap-3 bg-white text-gray-800 font-semibold px-5 py-3 rounded-xl shadow-md hover:shadow-lg transition-all duration-300 hover:bg-gray-100"
                >
                    {/* <Mail className="w-5 h-5" /> */}
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/google/google-original.svg" className="w-5 h-5" />
                    Sign up with Google
                </button>

                <button
                    onClick={AuthWithGithub}
                    className="cursor-pointer flex items-center justify-center gap-3 bg-gray-900 text-white font-semibold px-5 py-3 rounded-xl shadow-md hover:shadow-lg transition-all duration-300 hover:bg-gray-800"
                >
                    <Github className="w-5 h-5" />
                    Sign up with GitHub
                </button>
                </div>

                {/* Link to Sign In */}
                <p className="text-gray-400 text-sm mt-6">
                    Already have an account?{" "}
                    <Link
                        to={ROUTES.SIGN_IN}
                        className="font-semibold hover:underline"
                        style={{ color: "var(--main-color)" }}
                    >
                        Sign In
                    </Link>
                </p>
            </div>

            {showRoleModal && <RoleSelectionModal onSelect={handleRoleSelect} />}
        </main>
    );
}