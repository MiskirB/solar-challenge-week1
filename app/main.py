import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.utils import load_data


import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import f_oneway


st.set_page_config(page_title="Solar Irradiance Dashboard", layout="wide")

st.title("🌞 Solar Irradiance Dashboard by Miskir")
st.markdown("Compare GHI, DNI, and DHI across Benin, Sierra Leone, and Togo.")

# Load data
try:
    data = load_data()
except Exception as e:
    st.error(f"Failed to load data: {e}")
    st.stop()

# Sidebar filters
country_selection = st.sidebar.multiselect("Select countries", data['Country'].unique(), default=data['Country'].unique())

filtered_data = data[data['Country'].isin(country_selection)]

# Boxplots
metric = st.selectbox("Select metric to compare", ['GHI', 'DNI', 'DHI'])

st.subheader(f"{metric} Comparison")
fig, ax = plt.subplots(figsize=(10, 6))
sns.boxplot(data=filtered_data, x='Country', y=metric, ax=ax)
ax.set_ylabel(f"{metric} (W/m²)")
ax.set_title(f"{metric} Distribution by Country")
st.pyplot(fig)

# ANOVA Test
if st.button("Run ANOVA Test"):
    groups = [group[metric].values for name, group in filtered_data.groupby('Country')]
    result = f_oneway(*groups)
    st.write(f"**ANOVA p-value for {metric}:** {result.pvalue:.4f}")
