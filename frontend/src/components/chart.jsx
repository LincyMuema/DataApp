import { Bar } from "react-chartjs-2";
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from "chart.js";

// Register Chart.js modules needed for rendering Bar graphs
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

function ChartDisplay({ chartData }) {
  // Conditional rendering: Hide component if no data is available
  if (!chartData) return null;

  // Format data specifically for Chart.js requirement
  const data = {
    labels: chartData.labels, // Categories from X-axis
    datasets: [
      {
        label: " Dataset Output",
        data: chartData.values, // Aggregated values from Y-axis
        borderWidth: 1,
        backgroundColor: "rgba(255, 126, 0, 1)", 
        borderColor: "rgba(54, 162, 235, 1)",
      },
    ],
  };

  return (
    <div style={{
      backgroundColor: "white",     // White card background for high contrast
      padding: "20px",              
      borderRadius: "15px",         
      maxWidth: "1000px",            
      margin: "30px auto",          
    }}>
      <h2 style={{ color: "rgb(255, 165, 0)", fontSize: "30px", fontWeight: "bold" }}>Chart</h2>
      {/* Renders the Bar component with formatted dataset */}
      <Bar data={data} />
    </div>
  );
}

export default ChartDisplay;