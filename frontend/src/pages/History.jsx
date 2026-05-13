import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

function History() {
  const [history, setHistory] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const stored = JSON.parse(localStorage.getItem("interviewHistory")) || [];
    setHistory(stored);
  }, []);

  return (
    <div className="min-h-screen bg-black text-white p-10">
      <h1 className="text-3xl mb-8 text-cyan-400">Interview History</h1>

      {history.length === 0 ? (
        <p className="text-gray-400">No past interviews found</p>
      ) : (
        <div className="space-y-4">
          {history.map((item, index) => (
            <div
              key={index}
              className="bg-white/5 p-5 rounded-xl border border-white/10"
            >
              <p className="text-lg">
                Interview #{index + 1}
              </p>

              <p className="text-sm text-gray-400">
                Date: {item.date}
              </p>

              <p className="text-green-400">
                Avg Score: {item.avgScore}/10
              </p>

              <button
                onClick={() =>
                  navigate("/performance", {
                    state: {
                      scores: item.scores,
                      feedbacks: item.feedbacks,
                    },
                  })
                }
                className="mt-3 bg-cyan-500 px-4 py-2 rounded-lg"
              >
                View Performance
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default History;