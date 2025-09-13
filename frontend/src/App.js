import { useState } from "react";
import axios from "axios";

export default function App() {
  // State to hold user input, summary output, loading status, and errors
  const [repoUrl, setRepoUrl] = useState("");
  const [summary, setSummary] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  // Use an environment variable for the backend API URL (production),
  // fallback to localhost for local development
  const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

  // Handle form submission
  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent default form refresh
    setLoading(true);   // Show loading indicator
    setError("");       // Clear any previous errors
    setSummary("");     // Clear any previous summary

    try {
      // Send POST request to backend with the repo URL
      const res = await axios.post(`${API_URL}/summarize`, {
        repo_url: repoUrl,
      });
      setSummary(res.data.summary); // Display returned summary
    } catch (err) {
      // Show error message, using fallback if no detail provided
      setError(
        err.response?.data?.detail || "Error fetching summary. Check URL."
      );
    } finally {
      setLoading(false); // Always turn off loading spinner
    }
  };

  // Main UI
  return (
    <div style={{ maxWidth: 600, margin: "2rem auto", fontFamily: "Arial" }}>
      <h1>GitHub Repo Summarizer</h1>

      {/* Form for user to enter GitHub repo URL */}
      <form onSubmit={handleSubmit}>
        <input
          type="url"
          placeholder="Enter GitHub repo URL"
          value={repoUrl}
          onChange={(e) => setRepoUrl(e.target.value)} // Update input value
          required
          style={{ width: "100%", padding: "0.5rem", fontSize: "1rem" }}
        />
        <button type="submit" disabled={loading} style={{ marginTop: "1rem" }}>
          {loading ? "Summarizing..." : "Summarize"}
        </button>
      </form>

      {/* Show error message if any */}
      {error && <p style={{ color: "red", marginTop: "1rem" }}>{error}</p>}

      {/* Show summary if available */}
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
