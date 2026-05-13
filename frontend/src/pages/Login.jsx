import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { motion } from "framer-motion";
import { Mail, Lock, Brain } from "lucide-react";

function Login() {
  const navigate = useNavigate();

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post("http://127.0.0.1:8000/auth/login", {
        email,
        password,
      });

      // save token
      localStorage.setItem("token", res.data.access_token);
      localStorage.setItem("user", JSON.stringify(res.data.user));

      alert("Login successful!");

      // ✅ redirect to upload resume page
      navigate("/upload-resume");

    } catch (err) {
      console.log(err);
      alert(err.response?.data?.detail || "Login failed");
    }
  };

  return (
    <div className="min-h-screen bg-black text-white flex items-center justify-center px-6">

      <motion.div className="w-full max-w-md bg-white/5 p-8 rounded-3xl border border-white/10">

        <h1 className="text-3xl font-bold text-center mb-6">Welcome Back</h1>

        <form onSubmit={handleLogin} className="space-y-5">

          {/* Email */}
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="w-full p-3 rounded-xl bg-white/5 border border-white/10"
          />

          {/* Password */}
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="w-full p-3 rounded-xl bg-white/5 border border-white/10"
          />

          <button
            type="submit"
            className="w-full bg-cyan-500 text-black py-3 rounded-xl font-semibold"
          >
            Login
          </button>

        </form>
      </motion.div>
    </div>
  );
}

export default Login;