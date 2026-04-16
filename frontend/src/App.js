import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  const API = "https://ai-document-assistant-b2i2.onrender.com";

  const handleUpload = async () => {
    if (!file) return alert("Please select a file");

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      await axios.post(`${API}/upload`, formData);
      alert("File uploaded successfully!");
    } catch (error) {
      alert("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  const handleChat = async () => {
    if (!question) return;

    try {
      setLoading(true);
      const res = await axios.post(`${API}/chat`, {
        question: question,
      });
      setAnswer(res.data.answer);
    } catch (error) {
      setAnswer("Error getting response");
    } finally {
      setLoading(false);
    }
  };

  const handleSummary = async () => {
    try {
      setLoading(true);
      const res = await axios.post(`${API}/summary`);
      setSummary(res.data.summary);
    } catch (error) {
      setSummary("Error getting summary");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="glass-container">
        <h1>AI Document Assistant</h1>
        

        {/* Upload Option*/}
        <div className="card">
          <h3>Upload File</h3>
          <input type="file" onChange={(e) => setFile(e.target.files[0])} />
          <button onClick={handleUpload} disabled={loading}>
            {loading ? "Uploading..." : "Upload"}
          </button>
        </div>

        {/* Chat Option*/}
        <div className="card">
          <h3>Ask Questions</h3>
          <input
            type="text"
            placeholder="Ask something about your PDF..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
          />
          <button onClick={handleChat} disabled={loading}>
            Ask AI
          </button>

          {answer && (
            <div className="output-box">
              <strong>Answer:</strong>
              <p>{answer}</p>
            </div>
          )}
        </div>

        {/* Summary Option*/}
        <div className="card">
          <h3>Summary</h3>
          <button onClick={handleSummary} disabled={loading}>
            Generate Summary
          </button>

          {summary && (
            <div className="output-box">
              <strong>Summary:</strong>
              <p>{summary}</p>
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;