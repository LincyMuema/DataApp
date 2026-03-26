from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
from pydantic import BaseModel
from services.csv_service import get_columns, get_chart_data

router = APIRouter()

# Directory where uploaded CSV files are stored temporarily
UPLOAD_DIR = "uploads"

@router.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    """
    DESCRIPTION:
    Receives a CSV file from the frontend, saves it to the local 'uploads' 
    directory, and extracts the column headers for selection.

    PARAMETERS:
    - file (UploadFile): The multi-part form data file sent via POST.

    RETURNS:
    - dict: { "filename": str, "columns": list[str] }
    
    EXCEPTIONS/ERRORS:
    - IOError: Raised if the server fails to write the file to the disk.
    - ValueError: Raised if 'get_columns' fails to parse the CSV format.

    EXAMPLE USAGE:
    POST /api/upload (Form-Data: file=@data.csv)

    NOTES/EDGE CASES:
    - If a file with the same name exists, it will be overwritten.
    - Ensure the 'uploads' folder has write permissions on the server.
    """
    # DEBUG/TEST: Ensure the upload directory exists
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save the file using a buffer to prevent memory overflow for large files
    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"File Save Error: {str(e)}")

    # Extract columns from the saved file
    columns = get_columns(file_path)

    return {
        "filename": file.filename,
        "columns": columns
    }


class ChartRequest(BaseModel):
    """Data model for chart generation requests."""
    filename: str
    x_column: str
    y_column: str


@router.post("/chart")
def get_chart(request: ChartRequest):
    """
    DESCRIPTION:
    Processes a specific CSV file to return aggregated data for Chart.js.
    It groups the data by the X column and calculates the mean of the Y column.

    PARAMETERS:
    - request (ChartRequest): Object containing:
        - filename (str): Name of the file previously uploaded.
        - x_column (str): The column used for grouping (e.g., 'Gender').
        - y_column (str): The numeric column for calculation (e.g., 'Age').

    RETURNS:
    - dict: { "labels": list, "values": list }
    
    EXCEPTIONS/ERRORS:
    - FileNotFoundError: If the filename provided does not exist in /uploads.
    - KeyError: If the provided column names do not match the CSV headers.

    EXAMPLE USAGE:
    POST /api/chart (JSON: {"filename": "test.csv", "x_column": "A", "y_column": "B"})

    NOTES/EDGE CASES:
    - TESTED: Non-numeric data in y_column is converted to NaN and ignored.
    - TESTED: Duplicate X categories are automatically grouped and averaged.
    """
    file_path = os.path.join(UPLOAD_DIR, request.filename)

    # DEBUG: Check if file exists before processing
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="CSV file not found on server.")

    # Call service to perform Pandas aggregation
    data = get_chart_data(
        file_path,
        request.x_column,
        request.y_column
    )

    return data