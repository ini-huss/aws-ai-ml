Week 1 — Small Python Data-Processing App
Overview
This project is a small Python data-processing application that loads a raw student-score dataset, cleans it using reusable functions, and performs numerical analysis with NumPy.
The project demonstrates a basic data-processing workflow, from loading raw data to producing meaningful statistical results.
Objectives
Load a dataset from a CSV file.
Clean missing, invalid, and duplicate records.
Organize the program into reusable functions.
Use NumPy to calculate statistical measures.
Run the analysis in a Google Colab notebook.
Manage project dependencies using a virtual environment and requirements.txt.
Dataset
The dataset contains student names and their scores. It intentionally includes data-quality issues such as missing values, duplicate records, and scores outside the valid range.
The cleaning process removes records that cannot be used for the analysis and retains valid scores between 0 and 100.
Data-Processing Workflow
Load: Read the CSV dataset using pandas.
Clean: Handle missing names and scores, remove invalid scores, and eliminate duplicate records.
Process: Convert scores into a NumPy array.
Analyze: Calculate the number of valid students, average score, highest score, lowest score, and pass rate.
Display: Present the cleaned dataset and statistical results.
Technologies Used
Python
NumPy
pandas
Jupyter Notebook
Google Colab
venv for virtual environment management
requirements.txt for dependency management
Project Files
File
Description
student_data_processing.py
Python source code containing the data-loading, cleaning, and analysis functions.
student_data_processing.ipynb
Google Colab notebook containing code, outputs, and explanations.
student_scores.csv
Raw dataset used by the application.
How to Run Locally
1. Create and activate a virtual environment
Windows:
py -m venv .venv
.venv\Scripts\activate
macOS / Linux:
python3 -m venv .venv
source .venv/bin/activate
2. Install dependencies
python -m pip install -r requirements.txt
3. Run the application
python student_data_processing.py
Run the notebook in Google Colab or Jupyter Notebook to view the step-by-step analysis and outputs.
Expected Results
After cleaning the sample dataset, the application should retain six valid student records and calculate:
Average score: 72.5
Highest score: 95
Lowest score: 45
Pass rate: 83.33%
Learning Outcomes
Through this project, I practiced data cleaning, function design, numerical computation with NumPy, notebook-based analysis, and Python dependency management.
