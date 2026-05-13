import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { Mic, Send, Bot } from "lucide-react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function Interview() {
  const navigate = useNavigate();

  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [question, setQuestion] = useState("");
  const [count, setCount] = useState(1);
  const [time, setTime] = useState(60);

  const [interviewType, setInterviewType] = useState("");
  const [started, setStarted] = useState(false);
  const [completed, setCompleted] = useState(false);

  const [feedback, setFeedback] = useState("");
  const [score, setScore] = useState(null);

  const [listening, setListening] = useState(false);

  // ✅ store all scores
  const [allScores, setAllScores] = useState([]);

  // =========================
  // ✅ SAVE HISTORY
  // =========================
  const saveToHistory = () => {
    const existing =
      JSON.parse(localStorage.getItem("interviewHistory")) || [];

    const avg =
      allScores.length > 0
        ? (
            allScores.reduce((a, b) => a + b.score, 0) /
            allScores.length
          ).toFixed(2)
        : 0;

    const newEntry = {
      date: new Date().toLocaleString(),
      interviewType,
      scores: allScores,
      avgScore: avg,
    };

    localStorage.setItem(
      "interviewHistory",
      JSON.stringify([newEntry, ...existing])
    );
  };

  // =========================
  // START INTERVIEW
  // =========================
  const startInterview = async () => {
    try {
      const res = await axios.get(
        `http://127.0.0.1:8000/interview/start?interview_type=${interviewType}`
      );

      setQuestion(res.data.question);
      setMessages([{ sender: "ai", text: res.data.question }]);

      setStarted(true);
      setCount(1);
      setCompleted(false);
      setAllScores([]);
    } catch (err) {
      console.log(err);
    }
  };

  // =========================
  // SEND ANSWER
  // =========================
  const handleSend = async () => {
    if (!input.trim() || completed) return;

    const userMessage = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/interview/next",
        {
          answer: input,
          previous_question: question,
          question_count: count,
          interview_type: interviewType,
        }
      );

      // ✅ STOP CONDITION
      if (res.data.completed || count >= 10) {
        setCompleted(true);

        setMessages((prev) => [
          ...prev,
          { sender: "ai", text: "🎉 Interview Completed!" },
        ]);

        // ✅ SAVE HISTORY HERE
        setTimeout(() => {
          saveToHistory();
        }, 500);

        return;
      }

      let parsed;
      try {
        parsed = JSON.parse(res.data.data);
      } catch {
        parsed = {
          score: 0,
          feedback: res.data.data,
          next_question: res.data.data,
        };
      }

      setScore(parsed.score);
      setFeedback(parsed.feedback);

      // ✅ STORE SCORE
      setAllScores((prev) => [
        ...prev,
        {
          question: count,
          score: Number(parsed.score) || 0,
        },
      ]);

      const nextQ = parsed.next_question;

      setMessages((prev) => [
        ...prev,
        { sender: "ai", text: nextQ },
      ]);

      setQuestion(nextQ);
      setCount((prev) => prev + 1);
      setTime(60);
    } catch (err) {
      console.log(err);
    }

    setInput("");
  };

  // =========================
  // TIMER
  // =========================
  useEffect(() => {
    if (started && time > 0 && !completed) {
      const timer = setTimeout(() => setTime(time - 1), 1000);
      return () => clearTimeout(timer);
    }

    if (time === 0 && !completed) {
      handleSend();
    }
  }, [time, started, completed]);

  // =========================
  // VOICE INPUT
  // =========================
  const startVoice = () => {
    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
      alert("Speech Recognition not supported");
      return;
    }

    const recognition = new SpeechRecognition();

    recognition.lang = "en-US";
    recognition.continuous = false;

    recognition.start();

    recognition.onstart = () => setListening(true);

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;

      setInput(transcript);

      setTimeout(() => {
        handleSend();
      }, 1000);
    };

    recognition.onerror = (e) => {
      alert("Mic error: " + e.error);
      setListening(false);
    };

    recognition.onend = () => setListening(false);
  };

  return (
    <div className="min-h-screen bg-black text-white flex">

      {/* Sidebar */}
      <div className="w-72 bg-white/5 border-r p-6 hidden md:block">
        <h1 className="text-2xl text-cyan-400 mb-10">AI Interview</h1>

        <div className="space-y-5">
          <div className="bg-cyan-500/10 p-4 rounded">
            <p>{interviewType || "Not Selected"}</p>
          </div>

          <div className="bg-white/5 p-4 rounded">
            <p>{count} / 10</p>
          </div>

          <div className="bg-white/5 p-4 rounded">
            <p>00:{time < 10 ? `0${time}` : time}</p>
          </div>

          {score && (
            <div className="bg-white/5 p-4 rounded">
              <p>{score}/10</p>
              <p className="text-xs">{feedback}</p>
            </div>
          )}
        </div>
      </div>

      {/* Main */}
      <div className="flex-1 flex flex-col">

        <div className="border-b p-4 flex justify-between">
          <h2 className="flex gap-2">
            <Bot /> AI Mock Interview
          </h2>

          <button
            onClick={() => window.location.reload()}
            className="bg-red-500 px-4 py-2 rounded"
          >
            Restart
          </button>
        </div>

        {!started ? (
          <div className="flex flex-col items-center justify-center flex-1 gap-6">
            <div className="flex gap-4">
              <button
                onClick={() => setInterviewType("technical")}
                className="bg-cyan-500 px-6 py-3 rounded"
              >
                Technical
              </button>

              <button
                onClick={() => setInterviewType("hr")}
                className="bg-pink-500 px-6 py-3 rounded"
              >
                HR
              </button>
            </div>

            <button
              onClick={startInterview}
              disabled={!interviewType}
              className="bg-green-500 px-6 py-3 rounded"
            >
              Start Interview
            </button>
          </div>
        ) : (
          <>
            <div className="flex-1 overflow-y-auto p-6 space-y-4">
              {messages.map((msg, i) => (
                <motion.div key={i}>
                  <div className={msg.sender === "user" ? "text-right" : ""}>
                    <div className="inline-block bg-white/10 p-3 rounded">
                      {msg.text}
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>

            {completed ? (
              <div className="p-6 text-center">
                <h2 className="text-green-400 text-xl">
                  🎉 Interview Completed
                </h2>

                <button
                  onClick={() =>
                    navigate("/performance", {
                      state: { scores: allScores },
                    })
                  }
                  className="mt-4 bg-cyan-500 px-6 py-3 rounded"
                >
                  Generate Performance
                </button>
              </div>
            ) : (
              <div className="p-4 flex gap-2">
                <input
                  value={input}
                  onChange={(e) => setInput(e.target.value)}
                  className="flex-1 p-3 bg-white/10 rounded"
                />

                <button
                  onClick={startVoice}
                  className={`p-3 rounded ${
                    listening ? "bg-red-500" : "bg-white/10"
                  }`}
                >
                  <Mic />
                </button>

                <button
                  onClick={handleSend}
                  className="bg-cyan-500 p-3 rounded"
                >
                  <Send />
                </button>
              </div>
            )}
          </>
        )}
      </div>
    </div>
  );
}

export default Interview;