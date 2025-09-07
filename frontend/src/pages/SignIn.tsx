import { Github, Mail } from "lucide-react";
import { useAuth } from "../context/AuthContext";
import { Link } from "react-router-dom";
import { ROUTES } from "../routes/routes";

export default function SignIn() {
  const { signinWithGoogle, signinWithGithub } = useAuth();

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
            Sign In
          </h1>
          <p className="subtext">
            Connect with mentors, developers, and grow your network 🚀
          </p>
        </div>

        {/* Botões OAuth */}
        <div className="flex flex-col gap-4 mt-6">
          <button
            onClick={signinWithGoogle}
            className="flex items-center justify-center gap-3 bg-white text-gray-800 font-semibold px-5 py-3 rounded-xl shadow-md hover:shadow-lg transition-all duration-300 hover:bg-gray-100"
          >
            <Mail className="w-5 h-5" />
            Sign in with Google
          </button>

          <button
            onClick={signinWithGithub}
            className="flex items-center justify-center gap-3 bg-gray-900 text-white font-semibold px-5 py-3 rounded-xl shadow-md hover:shadow-lg transition-all duration-300 hover:bg-gray-800"
          >
            <Github className="w-5 h-5" />
            Sign in with GitHub
          </button>
        </div>

        {/* Divisor */}
        <div className="flex items-center my-6">
          <span className="flex-grow border-t border-gray-700"></span>
          <span className="mx-3 text-gray-400 text-sm">or</span>
          <span className="flex-grow border-t border-gray-700"></span>
        </div>

        {/* Link para Sign Up */}
        <p className="text-gray-400 text-sm">
          Don't have an account?{" "}
          <Link
            to={ROUTES.SIGN_UP}
            className="font-semibold hover:underline"
            style={{ color: "var(--main-color)" }}
          >
            Sign Up
          </Link>
        </p>
      </div>
    </main>
  );
}