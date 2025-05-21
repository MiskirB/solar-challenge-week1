# 🌞 Solar Challenge Week 1 - Data Analysis Dashboard
 Countries: Benin 🇧🇯 | Sierra Leone 🇸🇱 | Togo 🇹🇬

This repository presents data analysis and visualization tools developed for Solar Challenge Week 1, focusing on solar energy metrics such as GHI (Global Horizontal Irradiance), DNI (Direct Normal Irradiance), and DHI (Diffuse Horizontal Irradiance) from three West African countries.

🧩 What’s Inside:
📊 Jupyter Notebooks for EDA

📈 Interactive Streamlit Dashboard

🧼 Cleaned & Ready-to-Use Datasets

# 🚀 Live Dashboard
Experience the interactive visualization in your browser:
🔗 https://solar-challenge-week1-miskir.streamlit.app/

# 📁 Project Structure

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

# 📊 Datasets
Datasets are stored in the data/ directory:

benin.csv — Solar and energy-related data for Benin

sierra_leone.csv — Solar and energy-related data for Sierra Leone

togo.csv — Solar and energy-related data for Togo

⚠️ If you face encoding errors when loading CSV files, try using:
pd.read_csv('filename.csv', encoding='latin1')

# 🧪 Features
Interactive dashboard with country comparisons on solar irradiance metrics

Boxplots and ANOVA test results for GHI, DNI, and DHI

Side panel filters to select countries of interest

EDA notebooks for in-depth insights

# 🚀 Deployment Instructions (Streamlit Cloud)
Upload your repo to GitHub

Ensure data files are not in .gitignore
Go to Streamlit Cloud, connect your GitHub repo, and deploy the app/main.py file.

# 🧰 Installation (Local)

# Create and activate a virtual environment

python3 -m venv .venv
source .venv/bin/activate

# Install dependencies

pip install -r requirements.txt

# Run Streamlit dashboard

streamlit run app/main.py

🌿 Working with Branches
To explore or manage branches:


# Show all branches (local + remote)

git branch -a

# Create new branch

git checkout -b feature/new-analysis

# Switch to existing branch

git checkout main

# Delete branch

git branch -d old-branch

📄 Final Report
Check out the final_report_miskir.md or final_report_miskir.pdf for a complete Medium-style write-up summarizing Week 0 analysis, methodology, and findings.

👨‍💻 Author
Miskir Besir Abshir
