import pandas as pd

def get_columns(file_path: str):
    """
    DESCRIPTION:
    Reads a CSV file and extracts all header names to populate the 
    frontend dropdown selectors.

    PARAMETERS:
    - file_path (str): The absolute or relative path to the saved CSV file.

    RETURNS:
    - list[str]: A list of strings containing all column headers.
    
    EXCEPTIONS/ERRORS:
    - FileNotFoundError: If the file_path is invalid.
    - pd.errors.EmptyDataError: If the CSV file is empty.

    EXAMPLE USAGE:
    columns = get_columns("uploads/data.csv") # Returns ['Name', 'Age', 'Gender']

    NOTES/EDGE CASES:
    - Assumes the first row of the CSV is the header.
    - Special characters in headers are preserved as strings.
    """
    df_upload = pd.read_csv(file_path)
    return df_upload.columns.tolist()

def get_chart_data(file_path: str, x_column: str, y_column: str):
    """
    DESCRIPTION:
    Processes the CSV data by grouping unique categories in the X-column 
    and calculating the average (mean) for the corresponding Y-column.

    PARAMETERS:
    - file_path (str): Path to the CSV file to be processed.
    - x_column (str): The categorical column name (X-axis labels).
    - y_column (str): The numerical column name (Y-axis values).

    RETURNS:
    - dict: A dictionary containing "labels" (list) and "values" (list) 
      formatted for Chart.js.
    
    EXCEPTIONS/ERRORS:
    - KeyError: Thrown if the user selects a column that has been renamed or deleted.
    - TypeError: Thrown if the Y-column contains non-numeric data that cannot be averaged.

    EXAMPLE USAGE:
    data = get_chart_data("uploads/data.csv", "Department", "Salary")
    # Returns {"labels": ["HR", "IT"], "values": [50000.0, 75000.0]}

    NOTES/EDGE CASES:
    - .dropna(): Rows with missing values in either selected column are excluded.
    - .mean(): If a category has only one entry, the mean is equal to that value.
    - Large Datasets: Pandas handles this in-memory; very large files (>1GB) may 
      require chunking.
    """
    # Load the dataset into a Pandas DataFrame
    df_upload = pd.read_csv(file_path)

    # Filtering: Keep only relevant columns and remove null/empty entries
    df_upload = df_upload[[x_column, y_column]].dropna()

    # Core Logic: Grouping and Aggregation
    # This prevents duplicate X-axis labels by averaging their Y-values.
    grouped_df = df_upload.groupby(x_column)[y_column].mean().reset_index()
    
    # Convert dataframe columns back to standard Python lists for JSON serialization
    x_axis = grouped_df[x_column].tolist()
    y_axis = grouped_df[y_column].tolist()

    return {
        "labels": x_axis,
        "values": y_axis
    }