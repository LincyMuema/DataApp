import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from './assets/vite.svg'
import heroImg from './assets/hero.png'
import './App.css'
import FileUpload from "./components/fileupload";
import ColumnSelector from "./components/column";
import ChartDisplay from "./components/chart";

function App() {
  const [columns, setColumns] = useState([]);
  const [filename, setFilename] = useState("");
  const [chartData, setChartData] = useState(null);

  return (
    <div>
      <h1>Data Analytics Web App</h1>

      {/* FILE UPLOAD */}
      <FileUpload 
        setColumns={setColumns} 
        setFilename={setFilename} 
      />

      {/* SELECT COLUMN */}
      {columns.length > 0 && (
        <ColumnSelector
          columns={columns}
          filename={filename}
          setChartData={setChartData}
        />
      )}

      {/* Show Chart */}
      {chartData && (
        <ChartDisplay chartData={chartData} />
      )}
    </div>
  );
}

export default App;
