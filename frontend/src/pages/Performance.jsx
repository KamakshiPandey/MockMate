import { useLocation, useNavigate } from "react-router-dom";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
  ResponsiveContainer,
} from "recharts";

function Performance() {
  const location = useLocation();
  const navigate = useNavigate();

  const { scores = [] } = location.state || {};

  const avg =
    scores.length > 0
      ? scores.reduce((a, b) => a + b.score, 0) / scores.length
      : 0;

  return (
    <div className="min-h-screen bg-black text-white p-6">

      <h1 className="text-3xl text-cyan-400 mb-6">
        📊 Performance Report
      </h1>

      {scores.length === 0 ? (
        <p>No data available</p>
      ) : (
        <>
          {/* CHART */}
          <div className="w-full h-96 bg-white/5 rounded-xl p-4">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={scores}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="question" />
                <YAxis domain={[0, 10]} />
                <Tooltip />
                <Line type="monotone" dataKey="score" strokeWidth={3} />
              </LineChart>
            </ResponsiveContainer>
          </div>

          {/* SUMMARY */}
          <div className="mt-6">
            <p className="text-xl text-green-400">
              Average Score: {avg.toFixed(1)} / 10
            </p>

            <p className="text-gray-400 mt-2">
              {avg > 7
                ? "🔥 Excellent performance!"
                : avg > 5
                ? "👍 Good, but improve more"
                : "⚠️ Needs improvement"}
            </p>
          </div>
        </>
      )}

      {/* BACK BUTTON */}
      <button
        onClick={() => navigate("/")}
        className="mt-6 bg-cyan-500 px-4 py-2 rounded-lg"
      >
        Back to Interview
      </button>
    </div>
  );
}

export default Performance;