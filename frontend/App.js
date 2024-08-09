
import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState("");

  const handleFileUpload = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append("file", file);

    try {
      const uploadResponse = await axios.post("http://127.0.0.1:8000/upload/", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });

      const filename = uploadResponse.data.filename;
      const summarizeResponse = await axios.post("http://127.0.0.1:8000/summarize/", {
        filename,
      });

      setSummary(summarizeResponse.data.summary);
    } catch (error) {
      console.error("Error uploading or summarizing the file:", error);
    }
  };

  return (
    <div className="App">
      <h1>Document Summarizer</h1>
      <form onSubmit={handleFileUpload}>
        <input
          type="file"
          accept=".txt"
          onChange={(e) => setFile(e.target.files[0])}
        />
        <button type="submit">Upload and Summarize</button>
      </form>
      {summary && (
        <div>
          <h2>Summary:</h2>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}

export default App;
