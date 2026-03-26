import { useState } from "react";
import "/style.css";
import api from "../api/axiosConfig";

function FileUpload({ setColumns, setFilename }) {
  // Local state to store the physical file selected by the user
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    // Captures the first file from the input selection
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    // Ensure a file exists before starting upload
    if (!file) {
      alert("Please select a file first");
      return;
    }

    // Encapsulate file in FormData to handle multi-part/form-data POST
    const formData = new FormData();
    formData.append("file", file);

    try {
      // API call to upload logic
      const response = await api.post("/upload", formData);

      // Store response data (filename and detected columns) in App.js state
      setColumns(response.data.columns);
      setFilename(response.data.filename);

    } catch (error) {
      console.error("Upload failed:", error);
    }
  };

  return (
    <div className="box">
      <h2 className="title">Upload CSV File</h2>
      {/* Restricts input selection to .csv files only */}
      <input type="file" accept=".csv" onChange={handleFileChange} className="csv"/>
      <button onClick={handleUpload} className="button">Upload</button>
    </div>
  );
}

export default FileUpload;