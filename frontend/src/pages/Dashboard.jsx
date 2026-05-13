import { motion } from "framer-motion";
import {
  BarChart3,
  Brain,
  FileText,
  TrendingUp,
  Target,
  Award,
} from "lucide-react";
import { useNavigate } from "react-router-dom"; // ✅ ADD

function Dashboard() {
  const navigate = useNavigate(); // ✅ ADD

  return (
    <div className="min-h-screen bg-black text-white p-6">
      
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center md:justify-between mb-10">
        
        <div>
          <h1 className="text-4xl font-bold">
            Student Dashboard
          </h1>

          <p className="text-gray-400 mt-2">
            Track your interview performance and AI insights.
          </p>
        </div>

        {/* ACTION BUTTONS */}
        <div className="flex gap-3 mt-5 md:mt-0 flex-wrap">
          
          <button
            onClick={() => navigate("/interview")}
            className="bg-cyan-500 hover:bg-cyan-400 text-black px-6 py-3 rounded-xl font-semibold transition"
          >
            Start Mock Interview
          </button>

          <button
            onClick={() => navigate("/performance")}
            className="bg-green-500 hover:bg-green-400 text-black px-6 py-3 rounded-xl font-semibold transition"
          >
            View Performance
          </button>

          <button
            onClick={() => navigate("/history")}
            className="bg-purple-500 hover:bg-purple-400 text-white px-6 py-3 rounded-xl font-semibold transition"
          >
            View History
          </button>
        </div>
      </div>

      {/* Stats Cards */}
      <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-12">
        
        <motion.div whileHover={{ scale: 1.03 }} className="bg-white/5 border border-white/10 rounded-2xl p-6">
          <BarChart3 className="text-cyan-400 mb-4" size={40} />
          <h2 className="text-gray-400 text-sm mb-2">Average Score</h2>
          <p className="text-4xl font-bold">82%</p>
        </motion.div>

        <motion.div whileHover={{ scale: 1.03 }} className="bg-white/5 border border-white/10 rounded-2xl p-6">
          <Brain className="text-cyan-400 mb-4" size={40} />
          <h2 className="text-gray-400 text-sm mb-2">Interviews Taken</h2>
          <p className="text-4xl font-bold">14</p>
        </motion.div>

        <motion.div whileHover={{ scale: 1.03 }} className="bg-white/5 border border-white/10 rounded-2xl p-6">
          <Target className="text-cyan-400 mb-4" size={40} />
          <h2 className="text-gray-400 text-sm mb-2">Weak Topic</h2>
          <p className="text-2xl font-bold">System Design</p>
        </motion.div>

        <motion.div whileHover={{ scale: 1.03 }} className="bg-white/5 border border-white/10 rounded-2xl p-6">
          <Award className="text-cyan-400 mb-4" size={40} />
          <h2 className="text-gray-400 text-sm mb-2">ATS Resume Score</h2>
          <p className="text-4xl font-bold">88%</p>
        </motion.div>
      </div>

      {/* Main Grid */}
      <div className="grid lg:grid-cols-3 gap-6">
        
        {/* Recent Interviews */}
        <div className="lg:col-span-2 bg-white/5 border border-white/10 rounded-3xl p-6">
          
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-2xl font-semibold">
              Recent Interview Sessions
            </h2>
            <TrendingUp className="text-cyan-400" />
          </div>

          <div className="space-y-5">
            
            {[
              {
                title: "React Developer Interview",
                desc: "Technical + HR Round",
                score: "84%",
                time: "Yesterday",
              },
              {
                title: "DSA Mock Interview",
                desc: "Graphs + Trees",
                score: "76%",
                time: "2 Days Ago",
              },
              {
                title: "FastAPI Backend Round",
                desc: "APIs + Authentication",
                score: "91%",
                time: "Last Week",
              },
            ].map((item, i) => (
              <div
                key={i}
                className="bg-black/30 border border-white/10 rounded-2xl p-5 flex items-center justify-between"
              >
                <div>
                  <h3 className="text-lg font-semibold">{item.title}</h3>
                  <p className="text-gray-400 text-sm">{item.desc}</p>
                </div>

                <div className="text-right">
                  <p className="text-cyan-400 font-bold text-xl">
                    {item.score}
                  </p>
                  <p className="text-gray-500 text-sm">{item.time}</p>
                </div>
              </div>
            ))}
          </div>

          {/* VIEW FULL HISTORY BUTTON */}
          <button
            onClick={() => navigate("/history")}
            className="mt-6 w-full bg-purple-500 hover:bg-purple-400 py-3 rounded-xl font-semibold"
          >
            View Full History
          </button>
        </div>

        {/* AI Suggestions */}
        <div className="bg-white/5 border border-white/10 rounded-3xl p-6">
          
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-2xl font-semibold">
              AI Suggestions
            </h2>
            <Brain className="text-cyan-400" />
          </div>

          <div className="space-y-5">
            {[
              "Practice scalability, load balancing, and database sharding.",
              "Focus more on graphs and dynamic programming.",
              "Add measurable achievements in resume.",
              "Learn WebSocket vs REST API.",
            ].map((text, i) => (
              <div key={i} className="bg-black/30 border border-white/10 rounded-2xl p-5">
                <p className="text-gray-400 text-sm">{text}</p>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Bottom Section */}
      <div className="grid md:grid-cols-2 gap-6 mt-10">
        
        {/* Resume */}
        <div className="bg-white/5 border border-white/10 rounded-3xl p-6">
          
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-2xl font-semibold">
              Uploaded Resume
            </h2>
            <FileText className="text-cyan-400" />
          </div>

          <div className="bg-black/30 border border-white/10 rounded-2xl p-5">
            <h3 className="font-semibold text-lg">resume_final.pdf</h3>
            <p className="text-gray-400 text-sm mt-2">
              Last uploaded 2 days ago
            </p>

            <button
              onClick={() => navigate("/upload-resume")}
              className="mt-5 bg-cyan-500 hover:bg-cyan-400 text-black px-5 py-2 rounded-xl font-medium transition"
            >
              Analyze Again
            </button>
          </div>
        </div>

        {/* Progress */}
        <div className="bg-white/5 border border-white/10 rounded-3xl p-6">
          
          <div className="flex items-center justify-between mb-6">
            <h2 className="text-2xl font-semibold">
              Progress Overview
            </h2>
            <TrendingUp className="text-cyan-400" />
          </div>

          <div className="space-y-5">
            {[
              { name: "Technical Skills", val: 85 },
              { name: "Communication", val: 72 },
              { name: "Confidence", val: 78 },
            ].map((item, i) => (
              <div key={i}>
                <div className="flex justify-between mb-2">
                  <p>{item.name}</p>
                  <p>{item.val}%</p>
                </div>

                <div className="w-full h-3 bg-white/10 rounded-full">
                  <div
                    className="h-3 bg-cyan-400 rounded-full"
                    style={{ width: `${item.val}%` }}
                  ></div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Dashboard;