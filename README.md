# 📊 Netflix Data Analytics with MySQL & Python

This project analyzes the **Netflix Movies and TV Shows dataset** using **Python, Pandas, NumPy, Matplotlib, Seaborn, and MySQL**.  
It demonstrates an end-to-end data analysis workflow: from storing raw data in a database to visualizing insights.

---

## 🚀 Project Workflow
1. **Data Storage**  
   - CSV file imported into **MySQL database**  
   - Tables created & populated with raw Netflix data  

2. **Data Connection**  
   - Connected to MySQL directly from Python (using `mysql-connector`)  
   - Wrote **raw SQL queries** inside Jupyter Notebook  

3. **Data Cleaning & Transformation**  
   - Handled missing values  
   - Normalized multi-value columns (directors, actors, genres)  
   - Converted date formats & durations  

4. **Exploratory Data Analysis (EDA)**  
   - Number of **Movies vs TV Shows**  
   - Content trends by **release year** and **country**  
   - Most popular **genres/categories**  
   - **Top 15 Directors** and **Top 20 Actors**  
   - Duration distribution of movies  

5. **Visualization**  
   - Used **Matplotlib** and **Seaborn** for data storytelling  
   - Created bar charts, line plots, and trend analysis  

---

## 📈 Key Insights
- Netflix has significantly expanded its catalog after 2015  
- Movies dominate the platform compared to TV Shows  
- USA, India, and UK are top contributors of content  
- Directors like *Rajiv Chilaka* and *Raúl Campos* appear most frequently  
- Actors like *Anupam Kher* and *Shah Rukh Khan* are among the most featured  

---

## 🛠️ Tech Stack
- **Python** → Pandas, NumPy, Matplotlib, Seaborn  
- **MySQL** → Data storage & queries  
- **Jupyter Notebook** → Analysis & visualization environment  

---

## 📂 Project Structure
Netflix_Movie_Analysis/
│
├── data/ # Raw dataset (CSV file)
├── notebooks/ # Jupyter notebooks for analysis
│ └── Netflix_Movie_Analysis.ipynb
├── main.py # Script for MySQL setup (tables, loading data)
├── README.md # Project documentation
└── requirements.txt # Python dependencies

## ⚡ How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/AliRaza7x/netflix-data-analytics.git
   cd Netflix_Movie_Analysis
Install dependencies:
pip install -r requirements.txt

Import dataset into MySQL (script provided in main.py)

Open the notebook:
jupyter notebook notebooks/Netflix_Movie_Analysis.ipynb

📌 Dataset
The dataset used is the Netflix Movies and TV Shows Dataset (publicly available on Kaggle).

