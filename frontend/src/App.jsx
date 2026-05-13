import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Dashboard from "./pages/Dashboard";
import Interview from "./pages/Interview";
import UploadResume from "./pages/UploadResume";
import Login from "./pages/Login";
import Signup from "./pages/Signup";
import Performance from "./pages/Performance";
import History from "./pages/History"; // ✅ ADD THIS

function App() {
  return (
    <div className="bg-black text-white min-h-screen">
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/dashboard" element={<Dashboard />} />
        <Route path="/interview" element={<Interview />} />
        <Route path="/upload-resume" element={<UploadResume />} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />

        {/* ✅ Performance Page */}
        <Route path="/performance" element={<Performance />} />

        {/* ✅ NEW: History Page */}
        <Route path="/history" element={<History />} />

        {/* ✅ 404 fallback */}
        <Route path="*" element={<h1 className="p-10">Page Not Found</h1>} />
      </Routes>
    </div>
  );
}

export default App;