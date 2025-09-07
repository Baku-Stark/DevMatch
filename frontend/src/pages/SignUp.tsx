import { useState } from "react";
import { Github } from "lucide-react";
import { Link } from "react-router-dom";
import { useAuth, type IUserRegister } from "../context/AuthContext";
import { ROUTES } from "../routes/routes";

export default function SignUp() {
    const { signup, signinWithGoogle, signinWithGithub } = useAuth();
    const [formData, setFormData] = useState<IUserRegister | null>();

    const [loading, setLoading] = useState(false);

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    async function handleSubmit(e: React.FormEvent<HTMLFormElement>){
        e.preventDefault();

        if (formData?.password !== formData?.confirmPassword) {
            alert("Passwords do not match!");
            return;
        }

        try {
            setLoading(true);
            await signup({
                name: formData?.name as string,
                email: formData?.email as string,
                password: formData?.password as string,
            });
            alert("Account created successfully!");
        } catch (error) {
            console.error(error);
            alert("Failed to create account.");
        } finally {
            setLoading(false);
        }
    }

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

                {/* Manual Form */}
                <form onSubmit={handleSubmit} className="flex flex-col gap-4 mt-6 text-left">
                    <div>
                        <label htmlFor="name" className="block text-gray-300 text-sm mb-1">
                            Full Name
                        </label>
                        <input
                            id="name"
                            name="name"
                            type="text"
                            required
                            value={formData?.name}
                            onChange={handleChange}
                            className="w-full px-4 py-2 rounded-lg bg-gray-800 border border-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-main-color"
                        />
                    </div>

                    <div>
                        <label htmlFor="email" className="block text-gray-300 text-sm mb-1">
                            Email Address
                        </label>
                        <input
                            id="email"
                            name="email"
                            type="email"
                            required
                            value={formData?.email}
                            onChange={handleChange}
                            className="w-full px-4 py-2 rounded-lg bg-gray-800 border border-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-main-color"
                        />
                    </div>

                    <div>
                        <label htmlFor="password" className="block text-gray-300 text-sm mb-1">
                            Password
                        </label>
                        <input
                            id="password"
                            name="password"
                            type="password"
                            required
                            value={formData?.password}
                            onChange={handleChange}
                            className="w-full px-4 py-2 rounded-lg bg-gray-800 border border-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-main-color"
                        />
                    </div>

                    <div>
                        <label htmlFor="confirmPassword" className="block text-gray-300 text-sm mb-1">
                            Confirm Password
                        </label>
                        <input
                            id="confirmPassword"
                            name="confirmPassword"
                            type="password"
                            required
                            value={formData?.confirmPassword}
                            onChange={handleChange}
                            className="w-full px-4 py-2 rounded-lg bg-gray-800 border border-gray-700 text-white focus:outline-none focus:ring-2 focus:ring-main-color"
                        />
                    </div>

                    <button
                        type="submit"
                        disabled={loading}
                        className={`
                            relative bg-[#0d0d0d] text-white font-semibold px-6 py-3 rounded-xl
                            shadow-md transition-all duration-300 mt-4 disabled:opacity-50
                            hover:bg-[#1a1a1a] hover:shadow-[0_0_15px_var(--main-color)]
                            hover:scale-[1.03] active:scale-[0.97]
                        `}
                    >
                        {loading ? (
                            <span className="flex items-center justify-center gap-2">
                            <svg
                                className="animate-spin h-5 w-5 text-black"
                                xmlns="http://www.w3.org/2000/svg"
                                fill="none"
                                viewBox="0 0 24 24"
                            >
                                <circle
                                className="opacity-25"
                                cx="12"
                                cy="12"
                                r="10"
                                stroke="currentColor"
                                strokeWidth="4"
                                />
                                <path
                                className="opacity-75"
                                fill="currentColor"
                                d="M4 12a8 8 0 018-8v4l3-3-3-3v4a12 12 0 00-12 12h4z"
                                />
                            </svg>
                                Creating account...
                            </span>
                        ) : (
                            "Create Account"
                        )}
                    </button>
                </form>

                {/* Divisor */}
                <div className="flex items-center my-6">
                    <span className="flex-grow border-t border-gray-700"></span>
                    <span className="mx-3 text-gray-400 text-sm">or</span>
                    <span className="flex-grow border-t border-gray-700"></span>
                </div>

                {/* Botões OAuth */}
                <div className="flex flex-col gap-4">
                <button
                    onClick={signinWithGoogle}
                    className="flex items-center justify-center gap-3 bg-white text-gray-800 font-semibold px-5 py-3 rounded-xl shadow-md hover:shadow-lg transition-all duration-300 hover:bg-gray-100"
                >
                    {/* <Mail className="w-5 h-5" /> */}
                    <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/google/google-original.svg" className="w-5 h-5" />
                    Sign up with Google
                </button>

                <button
                    onClick={signinWithGithub}
                    className="flex items-center justify-center gap-3 bg-gray-900 text-white font-semibold px-5 py-3 rounded-xl shadow-md hover:shadow-lg transition-all duration-300 hover:bg-gray-800"
                >
                    <Github className="w-5 h-5" />
                    Sign up with GitHub
                </button>
                </div>

                {/* Link para Sign In */}
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
        </main>
    );
}