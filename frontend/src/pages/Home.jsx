import { motion } from "framer-motion";
import { Brain, FileText, Mic, BarChart3 } from "lucide-react";

function Home() {
  return (
    <div className="min-h-screen bg-black text-white overflow-hidden">

      {/* Navbar */}
      <nav className="flex items-center justify-between px-8 py-5 border-b border-white/10 backdrop-blur-lg">

        <h1 className="text-2xl font-bold text-cyan-400">
          AI Interview Coach
        </h1>

        <div className="flex gap-6 items-center text-sm">

          <a href="/" className="hover:text-cyan-400 transition">
            Home
          </a>

          <a href="/dashboard" className="hover:text-cyan-400 transition">
            Dashboard
          </a>

          <a href="/login" className="hover:text-cyan-400 transition">
            Login
          </a>

          <a
            href="/signup"
            className="bg-cyan-500 hover:bg-cyan-400 text-black px-5 py-2 rounded-xl font-semibold transition"
          >
            Sign Up
          </a>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="flex flex-col items-center justify-center text-center px-6 py-24">

        <motion.h1
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          className="text-6xl md:text-7xl font-bold leading-tight"
        >
          Crack Interviews with <br />

          <span className="text-cyan-400">
            AI-Powered Preparation
          </span>
        </motion.h1>

        <motion.p
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="mt-6 text-gray-400 max-w-2xl text-lg"
        >
          Upload your resume, generate personalized interview questions,
          practice mock interviews, and get AI-powered feedback instantly.
        </motion.p>

        {/* Buttons */}
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.4 }}
          className="flex gap-5 mt-10"
        >

          {/* Existing User */}
          <a
            href="/login"
            className="bg-cyan-500 hover:bg-cyan-400 text-black px-7 py-3 rounded-xl font-semibold transition"
          >
            Get Started
          </a>

          {/* New User */}
          <a
            href="/signup"
            className="border border-white/20 px-7 py-3 rounded-xl hover:bg-white/10 transition"
          >
            Create Account
          </a>
        </motion.div>
      </section>

      {/* Features Section */}
      <section className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 px-8 pb-20">

        {/* Card 1 */}
        <motion.div
          whileHover={{ scale: 1.05 }}
          className="bg-white/5 border border-white/10 rounded-2xl p-6 backdrop-blur-lg"
        >
          <FileText className="text-cyan-400 mb-4" size={40} />

          <h2 className="text-xl font-semibold mb-2">
            Resume Analysis
          </h2>

          <p className="text-gray-400 text-sm">
            AI analyzes your resume and detects skills, projects,
            technologies, and improvement areas.
          </p>
        </motion.div>

        {/* Card 2 */}
        <motion.div
          whileHover={{ scale: 1.05 }}
          className="bg-white/5 border border-white/10 rounded-2xl p-6 backdrop-blur-lg"
        >
          <Brain className="text-cyan-400 mb-4" size={40} />

          <h2 className="text-xl font-semibold mb-2">
            AI Interview Questions
          </h2>

          <p className="text-gray-400 text-sm">
            Generate personalized technical, HR, DSA,
            and project-based interview questions.
          </p>
        </motion.div>

        {/* Card 3 */}
        <motion.div
          whileHover={{ scale: 1.05 }}
          className="bg-white/5 border border-white/10 rounded-2xl p-6 backdrop-blur-lg"
        >
          <Mic className="text-cyan-400 mb-4" size={40} />

          <h2 className="text-xl font-semibold mb-2">
            Mock Interviews
          </h2>

          <p className="text-gray-400 text-sm">
            Practice real-time AI interviews with timer,
            voice input, and interactive conversation mode.
          </p>
        </motion.div>

        {/* Card 4 */}
        <motion.div
          whileHover={{ scale: 1.05 }}
          className="bg-white/5 border border-white/10 rounded-2xl p-6 backdrop-blur-lg"
        >
          <BarChart3 className="text-cyan-400 mb-4" size={40} />

          <h2 className="text-xl font-semibold mb-2">
            Performance Analytics
          </h2>

          <p className="text-gray-400 text-sm">
            Track interview scores, weak topics,
            confidence levels, and improvement progress.
          </p>
        </motion.div>

      </section>
    </div>
  );
}

export default Home;