import { useState } from "react";
import axios from "axios";

export default function App() {
  const [repoUrl, setRepoUrl] = useState("");
  const [summary, setSummary] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setSummary("");

    try {
      const res = await axios.post("http://localhost:8000/summarize", {
        repo_url: repoUrl,
      });
      setSummary(res.data.summary);
    } catch (err) {
      setError(
        err.response?.data?.detail || "Error fetching summary. Check URL."
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 600, margin: "2rem auto", fontFamily: "Arial" }}>
      <h1>GitHub Repo Summarizer</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="url"
          placeholder="Enter GitHub repo URL"
          value={repoUrl}
          onChange={(e) => setRepoUrl(e.target.value)}
          required
          style={{ width: "100%", padding: "0.5rem", fontSize: "1rem" }}
        />
        <button type="submit" disabled={loading} style={{ marginTop: "1rem" }}>
          {loading ? "Summarizing..." : "Summarize"}
        </button>
      </form>

      {error && <p style={{ color: "red", marginTop: "1rem" }}>{error}</p>}

      {summary && (
        <pre
          style={{
            marginTop: "1rem",
            padding: "1rem",
            backgroundColor: "#f0f0f0",
            borderRadius: "4px",
            whiteSpace: "pre-wrap",
          }}
        >
          {summary}
        </pre>
      )}
    </div>
  );
}
