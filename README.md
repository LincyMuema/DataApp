
# Data Analytic Chart Page 
A streamlined, full-stack web application that allows users to transform raw CSV data into meaningful visual insights. By uploading a file and selecting specific axes, the app automatically calculates statistical averages (means) and renders them in a clean, interactive bar chart.

## Features Overview
* **Secure File Upload:** Upload `.csv` files directly to a managed backend directory.
* **Intelligent Column Mapping:** Automatically parses CSV headers to populate X and Y axis selectors.
* **Automated Aggregation:** Uses Pandas to group categorical data and calculate the **Mean** (Average) of numerical values.
* **Dynamic Visualization:** High-contrast Bar Charts with a dedicated white-background card for maximum readability.
* **Responsive UI:** A modern interface featuring an orange-accented theme and intuitive layout.

---

## Technologies Used
* **Frontend:** React.js, Chart.js, Axios, Vite.
* **Backend:** FastAPI (Python), Pandas (Data Processing), Uvicorn.
* **Styling:** Inline CSS and External CSS Modules.

---

##  Code Structure Overview

```text
/backend
├── uploads/               # Stores uploaded CSV files
├── routes/
│   └── upload.py          # API endpoints (/upload, /chart)
├── services/
│   └── csv_service.py     # Logic for column extraction and data grouping
└── main.py                # FastAPI initialization and CORS settings

/frontend
├── src/
│   ├── api/
│   │   └── axiosConfig.js # Centralized API base URL configuration
│   ├── components/
│   │   ├── FileUpload.jsx    # File input and upload logic
│   │   ├── ColumnSelector.jsx # Dropdown logic for axis selection
│   │   └── ChartDisplay.jsx   # Chart.js rendering and styling
│   └── App.jsx            # Main state management
├── .env                   # Environment variables (API URLs)
└── style.css              # Global orange-theme styling
```

---

## Installation & Requirements

### Prerequisites
* Python 3.8+
* Node.js (v16 or higher)
* npm or yarn

### 1. Backend Setup
1. Navigate to the backend directory: `cd backend`
2. Install dependencies:
   ```bash
   pip install fastapi uvicorn pandas python-multipart
   ```
3. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

### 2. Frontend Setup
1. Navigate to the frontend directory: `cd frontend`
2. Install dependencies:
   ```bash
   npm install axios chart.js react-chartjs-2
   ```
3. Set up the Environment Variable in a `.env` file:
   ```text
   VITE_API_BASE_URL=http://127.0.0.1:8000/api
   ```
4. Run the development server:
   ```bash
   npm run dev
   ```

---

## Basic Usage
1.  **Upload:** Click the "Upload CSV File" button to send your data to the server.
2.  **Select:** Use the orange-bordered dropdowns to pick your X-Axis (e.g., *Gender*) and Y-Axis (e.g., *Age*).
3.  **Generate:** Click "Generate Chart." The app will calculate the average Y-value for every unique X-category.
4.  **Analyze:** View your results on the white-background chart card.

---

## Configuration Options
* **API URL:** Change the `VITE_API_BASE_URL` in `.env` if your backend is hosted on a different port or server.
* **Aggregation Method:** Currently defaults to `.mean()`. To change to `.sum()`, modify the `get_chart_data` function in `csv_service.py`.

---

## Troubleshooting
* **"404 Not Found" on Upload:** Ensure your frontend is calling `http://127.0.0.1:8000/api/upload` (including the `/api` prefix).
* **Chart shows axes but no bars:** Check that your Y-Axis column contains numbers. Text values in the Y-column are ignored for calculations.
* **Blank Screen:** Ensure your inline styles are passed as objects `{{ color: "orange" }}` and not strings.


## License
This project is licensed under the MIT License.

