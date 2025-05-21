🌞 Solar Challenge Week 1 - Data Analysis Dashboard (Benin, Sierra Leone, Togo)
This repository presents data analysis and visualization tools developed for Solar Challenge Week 1, focusing on solar energy metrics (GHI, DNI, DHI) from Benin, Sierra Leone, and Togo. It includes:

Cleaned datasets

Jupyter Notebooks for Exploratory Data Analysis (EDA)

A Streamlit web dashboard for interactive data exploration

📊 Live Demo
🚀 Check out the live dashboard (hosted on Streamlit Cloud)
📍 https://solar-challenge-week1-miskir.streamlit.app/

📁 Project Structure
bash
Copy
Edit
solar-challenge-week1/
│
├── app/ # Streamlit app
│ └── main.py
│
├── scripts/ # Utility scripts
│ └── utils.py
│
├── data/ # Solar datasets (CSV files)
│ ├── benin.csv
│ ├── sierra_leone.csv
│ └── togo.csv
│
├── notebooks/ # EDA notebooks
│ ├── benin_eda.ipynb
│ ├── sierra_leone_eda.ipynb
│ └── togo_eda.ipynb
│
├── .gitignore
├── README.md
└── requirements.txt
📊 Datasets
Datasets are stored in the data/ directory:

benin.csv — Solar and energy-related data for Benin

sierra_leone.csv — Solar and energy-related data for Sierra Leone

togo.csv — Solar and energy-related data for Togo

⚠️ If you face encoding errors when loading CSV files, try using:
pd.read_csv('filename.csv', encoding='latin1')

🧪 Features
Interactive dashboard with country comparisons on solar irradiance metrics

Boxplots and ANOVA test results for GHI, DNI, and DHI

Side panel filters to select countries of interest

EDA notebooks for in-depth insights

🚀 Deployment Instructions (Streamlit Cloud)
Upload your repo to GitHub

Ensure data files are not in .gitignore

bash
Copy
Edit
git add -f data/
git commit -m "Add data files for deployment"
git push origin main
Go to Streamlit Cloud, connect your GitHub repo, and deploy the app/main.py file.

🧰 Installation (Local)
bash
Copy
Edit

# Create and activate a virtual environment

python3 -m venv .venv
source .venv/bin/activate

# Install dependencies

pip install -r requirements.txt

# Run Streamlit dashboard

streamlit run app/main.py
