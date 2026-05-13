import { useState } from "react";
import axios from "axios";
import { motion } from "framer-motion";
import { User, Mail, Lock, Brain } from "lucide-react";

function Signup() {
  // ========================
  // STATE
  // ========================
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: ""
  });

  const [loading, setLoading] = useState(false);

  // ========================
  // INPUT CHANGE
  // ========================
  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  // ========================
  // SUBMIT (FIXED)
  // ========================
  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/auth/signup",
        formData
      );

      console.log("Signup success:", res.data);
      alert("Account created successfully!");

      // redirect
      window.location.href = "/login";

    } catch (err) {
      console.log("Signup error:", err.response?.data || err.message);
      alert("Signup failed!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-black text-white flex items-center justify-center px-6">

      {/* Glow */}
      <div className="absolute w-96 h-96 bg-cyan-500/20 blur-3xl rounded-full top-20 left-20"></div>
      <div className="absolute w-96 h-96 bg-blue-500/20 blur-3xl rounded-full bottom-20 right-20"></div>

      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        className="relative z-10 w-full max-w-md bg-white/5 border border-white/10 backdrop-blur-xl rounded-3xl p-8"
      >

        <div className="flex justify-center mb-6">
          <Brain className="text-cyan-400" size={40} />
        </div>

        <h1 className="text-3xl font-bold text-center mb-2">
          Create Account
        </h1>

        <p className="text-gray-400 text-center mb-8">
          Start your AI interview journey
        </p>

        {/* FORM */}
        <form onSubmit={handleSubmit} className="space-y-5">

          {/* NAME */}
          <div className="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-4 py-3">
            <User className="text-cyan-400" size={20} />
            <input
              type="text"
              name="name"
              placeholder="Enter your name"
              value={formData.name}
              onChange={handleChange}
              className="bg-transparent outline-none w-full"
              required
            />
          </div>

          {/* EMAIL */}
          <div className="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-4 py-3">
            <Mail className="text-cyan-400" size={20} />
            <input
              type="email"
              name="email"
              placeholder="Enter your email"
              value={formData.email}
              onChange={handleChange}
              className="bg-transparent outline-none w-full"
              required
            />
          </div>

          {/* PASSWORD */}
          <div className="flex items-center gap-3 bg-white/5 border border-white/10 rounded-xl px-4 py-3">
            <Lock className="text-cyan-400" size={20} />
            <input
              type="password"
              name="password"
              placeholder="Create password"
              value={formData.password}
              onChange={handleChange}
              className="bg-transparent outline-none w-full"
              required
            />
          </div>

          {/* BUTTON */}
          <button
            type="submit"
            disabled={loading}
            className="w-full bg-cyan-500 hover:bg-cyan-400 text-black font-semibold py-3 rounded-xl"
          >
            {loading ? "Creating Account..." : "Create Account"}
          </button>
        </form>

        {/* LOGIN */}
        <p className="text-center text-gray-400 text-sm mt-6">
          Already have an account?{" "}
          <a href="/login" className="text-cyan-400">
            Login
          </a>
        </p>
      </motion.div>
    </div>
  );
}

export default Signup;