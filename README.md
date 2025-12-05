
# 📊 Simple Streamlit Dashboard

A lightweight and interactive dashboard built using **Streamlit**.
This application demonstrates how to quickly build data visualizations, display metrics, and create user-friendly interfaces with minimal code.

---

## 🚀 Features

* 📈 Interactive charts (line, bar, area, etc.)
* 🧮 Key performance indicators (KPIs)
* 📁 File uploader support (CSV)
* 🎛️ User controls (sliders, dropdowns, date pickers, etc.)
* ⚡ Real-time dashboard updates
* 🧹 Clean and minimal UI

---

## 🗂️ Project Structure

```
simple-dashboard/
│
├── app.py              # Main Streamlit app
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/simple-dashboard.git
cd simple-dashboard
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Dashboard

In the project directory, run:

```bash
streamlit run app.py
```

Your dashboard will automatically open in your browser at:

```
http://localhost:8501
```

---

## 📥 Example Usage

Upload a CSV file to:

* Plot charts
* Filter data
* View summarized statistics
* Monitor KPIs

If no file is uploaded, sample data will be displayed.

---

## 📦 Requirements

Contents of `requirements.txt`:

```
streamlit
pandas
matplotlib
plotly
```

---

## 🛠️ Example Code Snippet (app.py)

```python
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Simple Streamlit Dashboard")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = px.data.gapminder().query("year == 2007")

st.write("### Data Preview")
st.dataframe(df)

st.write("### Scatter Plot")
fig = px.scatter(df, x=df.columns[0], y=df.columns[1])
st.plotly_chart(fig)
```

---

## 🤝 Contributing

Contributions, improvements, and feature suggestions are welcome!
Please open an issue or submit a pull request.

---

## 📄 License

This project is licensed under the **MIT License**.

---

