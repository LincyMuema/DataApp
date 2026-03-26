import { useState } from "react";
import api from "../api/axiosConfig";

function ColumnSelector({ columns, filename, setChartData }) {
  // Local state to track user-selected dropdown values
  const [xColumn, setXColumn] = useState("");
  const [yColumn, setYColumn] = useState("");

  const handleGenerateChart = async () => {
    // Prevent API call if selection is incomplete
    if (!xColumn || !yColumn) {
      alert("Please select both columns");
      return;
    }

    try {
      // Sends selected columns and filename to backend 
      const response = await api.post("/chart", {
        filename: filename,
        x_column: xColumn,
        y_column: yColumn,
      });

      // Update parent state with aggregated data for chart rendering
      setChartData(response.data);

    } catch (error) {
      console.error("Error fetching chart data:", error);
    }
  };

  return (
    <div className="box">
      <h2 className="title">Select Columns</h2>
      <div style={{ display: "flex", marginBottom: "15px" }}>
        
        {/* Mapping logic to dynamically generate dropdown options from CSV headers */}
        <label className="label">X-Axis:</label>
        <select onChange={(e) => setXColumn(e.target.value)} className="selector">
          <option value="">Select column</option>
          {columns.map((col, index) => (
            <option key={index} value={col}>{col}</option>
          ))}
        </select>

        <label className="label">Y-Axis:</label>
        <select onChange={(e) => setYColumn(e.target.value)} className="selector">
          <option value="">Select column</option>
          {columns.map((col, index) => (
            <option key={index} value={col}>{col}</option>
          ))}
        </select>
      </div>
      <button onClick={handleGenerateChart} className="button">Generate Chart</button>
    </div>
  );
}

export default ColumnSelector;