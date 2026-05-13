import { motion } from "framer-motion";
import { Upload, FileText, Brain, CheckCircle } from "lucide-react";
import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function UploadResume() {
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState("");
  const [result, setResult] = useState(null);
  const [pdfUrl, setPdfUrl] = useState(null);
  const [loading, setLoading] = useState(false);

  const navigate = useNavigate();

  // =========================
  // FILE SELECT
  // =========================
  const handleFileChange = (e) => {
    const selectedFile = e.target.files?.[0];

    if (selectedFile) {
      setFile(selectedFile);
      setFileName(selectedFile.name);
    }
  };

  // =========================
  // UPLOAD + ANALYZE
  // =========================
  const handleAnalyze = async () => {
    if (!file) {
      alert("Please upload a resume first");
      return;
    }

    setLoading(true);

    try {
      const formData = new FormData();
      formData.append("file", file);

      const res = await axios.post(
        "http://127.0.0.1:8000/resume/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      console.log("Backend Response:", res.data);

      // ✅ store FULL response
      setResult(res.data);

      // ✅ store PDF URL
      setPdfUrl(res.data?.pdf_url || null);

    } catch (err) {
      console.log("Upload Error:", err.response?.data || err.message);
      alert("Analysis failed. Check backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-black text-white px-6 py-10">

      {/* Heading */}
      <div className="text-center mb-14">
        <motion.h1
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-5xl font-bold"
        >
          Upload Your Resume
        </motion.h1>

        <p className="text-gray-400 mt-4 text-lg">
          Let AI analyze your resume and generate interview questions.
        </p>
      </div>

      {/* Card */}
      <motion.div className="max-w-3xl mx-auto bg-white/5 border border-white/10 rounded-3xl p-10 backdrop-blur-xl">

        {/* Upload */}
        <label className="border-2 border-dashed border-cyan-400/40 hover:border-cyan-400 transition rounded-3xl p-12 flex flex-col items-center justify-center cursor-pointer bg-white/5">

          <Upload size={60} className="text-cyan-400 mb-5" />

          <h2 className="text-2xl font-semibold mb-2">
            Drag & Drop Resume
          </h2>

          <p className="text-gray-400 mb-4">
            PDF, DOCX, TXT Supported
          </p>

          <div className="bg-cyan-500 hover:bg-cyan-400 text-black px-6 py-3 rounded-xl font-semibold transition">
            Browse Files
          </div>

          <input
            type="file"
            accept=".pdf,.docx,.txt"
            className="hidden"
            onChange={handleFileChange}
          />
        </label>

        {/* File Display */}
        {fileName && (
          <motion.div className="mt-8 bg-cyan-500/10 border border-cyan-400/20 rounded-2xl p-5 flex items-center gap-4">

            <FileText className="text-cyan-400" />

            <div>
              <p className="font-medium">{fileName}</p>
              <p className="text-sm text-gray-400">
                Ready for analysis
              </p>
            </div>

            <CheckCircle className="ml-auto text-green-400" />
          </motion.div>
        )}

        {/* Analyze Button */}
        <button
          onClick={handleAnalyze}
          disabled={loading}
          className="w-full mt-8 bg-cyan-500 hover:bg-cyan-400 text-black font-semibold py-4 rounded-2xl flex items-center justify-center gap-3 transition disabled:opacity-50"
        >
          <Brain />
          {loading ? "Analyzing..." : "Analyze Resume with AI"}
        </button>

        {/* Result */}
        {result?.analysis && (
          <div className="mt-8 bg-white/5 p-6 rounded-2xl border border-white/10">

            <h3 className="text-xl font-semibold mb-3">
              AI Analysis Result
            </h3>

            <p>
              <b>Skills:</b> {result.analysis.skills_found?.join(", ")}
            </p>

            <p className="mt-2">
              <b>Level:</b> {result.analysis.experience_level}
            </p>

            <div className="mt-4">
              <b>Interview Questions:</b>
              <ul className="list-disc ml-6 mt-2 text-gray-300">
                {result.analysis.suggested_interview_questions?.map((q, i) => (
                  <li key={i}>{q}</li>
                ))}
              </ul>
            </div>

            {/* ✅ DOWNLOAD PDF */}
            {pdfUrl && (
              <button
                onClick={() =>
                  window.open(`http://127.0.0.1:8000/${pdfUrl}`, "_blank")
                }
                className="mt-6 w-full bg-green-500 hover:bg-green-400 text-black font-semibold py-3 rounded-xl transition"
              >
                Download Analysis PDF
              </button>
            )}

            {/* 🚀 START INTERVIEW BUTTON */}
            <button
              onClick={() =>
                navigate("/interview", {
                  state: {
                    questions:
                      result.analysis.suggested_interview_questions || [],
                  },
                })
              }
              className="mt-4 w-full bg-purple-500 hover:bg-purple-400 text-black font-semibold py-4 rounded-xl transition"
            >
              Start Mock Interview 🚀
            </button>

          </div>
        )}

      </motion.div>
    </div>
  );
}

export default UploadResume;