# 🌟CHECK OUT OUR WEBSITE!!🌟
**Click this link:**
https://nafeesa-mahek.github.io/BigDataProject-WEBSITE/

# Resilient Clinical Outcome Prediction from Noisy Medical Records 🏥💻

![Apache Spark](https://img.shields.io/badge/Apache%20Spark-3.5-E25A1C?style=for-the-badge&logo=apachespark&logoColor=white)
![Hadoop](https://img.shields.io/badge/Hadoop-HDFS-66CC00?style=for-the-badge&logo=apachehadoop&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Machine Learning](https://img.shields.io/badge/PySpark-MLlib-FFCC00?style=for-the-badge)

---

## Course Information

**Course:** CS4074 – Big Data Analytics  
**Instructor:** Dr. Naila Marir  
**University:** Effat University  
**Semester:** Spring 2026  

---

## Team Members

- Nafeesa Mahek  
- Jumanah Al Nahdi  
- Aseel Bajaber  
- Hams Al Johani  

---

## Project Title

**Clinical Outcome Prediction from Noisy Medical Records**

---

## Project Description

This project builds a scalable distributed PySpark pipeline to predict 30-day hospital readmission for diabetic patients using the UCI Diabetes 130-US Hospitals dataset (101,766 encounters, 50 features).

Healthcare datasets present major Big Data challenges such as:

- Missing values  
- Duplicate records  
- Inconsistent formats  
- Severe class imbalance  
- Noisy and incomplete medical records  

To address these, we use **Apache Spark, Hadoop HDFS, and Spark MLlib** to build a fault-tolerant distributed pipeline covering data cleaning, preprocessing, feature engineering, machine learning, and evaluation.

We also simulate adversarial noise (NULLs, outliers, label flipping) to evaluate model robustness.

---

## Dataset Information

**Dataset:** UCI Diabetes 130-US Hospitals Dataset  

### Size
- 101,766 patient encounters  
- 50 features  

### Target Variable
**readmitted**
- 1 = Readmitted within 30 days  
- 0 = Not Readmitted  

---

## Pipeline Architecture

Raw Data → Noise Injection → Cleaning → Feature Engineering → ML Preprocessing → Model Training → Evaluation → Scalability Analysis  

---

## Project Workflow

### 1. Spark Session Initialization
Distributed Spark environment setup.

### 2. Data Loading
Load `diabetic_data.csv` into Spark DataFrames.

### 3. Exploratory Data Analysis (EDA)
- Readmission distribution  
- Age analysis  
- Missing values  
- Diagnosis patterns  
- Hospital stay trends  

### 4. Noise Injection
- NULL injection  
- Sentinel values  
- Outliers  
- Label flipping  

### 5. Data Cleaning
- Missing value handling  
- Duplicate removal  
- Type correction  
- Outlier capping (approxQuantile)  

### 6. Feature Engineering
- Total healthcare utilization  
- Medication volatility  

### 7. MLlib Preprocessing
- Imputer  
- StringIndexer  
- OneHotEncoder  
- StandardScaler  

### 8. Model Training
- Logistic Regression  
- Decision Tree  
- Random Forest  

### 9. Model Evaluation
- Accuracy  
- Precision  
- Recall  
- F1 Score  
- ROC-AUC  
- Confusion Matrix  

### 10. Scalability Benchmarking
Spark performance under increasing data sizes.

---

## Key Results

### Logistic Regression
- **F1 Score: 0.710**
- Best balance of precision & recall  

### Random Forest
- **AUC: 0.589**
- Most stable performance  

### Decision Tree
- **AUC: 0.498**
- Weak performance on noisy high-dimensional data  

### Data Recovery
- **89.97% corrupted data successfully recovered**

### Scalability
- Data volume ↑ 300%  
- Training time ↑ only 29%  

✔ Shows strong Spark scalability and efficiency  

---

## Installation Instructions

### Prerequisites

Install:

- Python 3.12+
- Java 8+
- Apache Spark 3.5+
- Hadoop (HDFS)
- VS Code or Google Colab  

---

## Clone Repository

## Install Dependencies
pip install -r requirements.txt

## Run Project
python main.py
This runs the full pipeline from data loading → preprocessing → training → evaluation.
## Dependencies

Main libraries used:
pyspark
pandas
numpy
matplotlib
seaborn
scikit-learn
findspark

## Example Output
Logistic Regression
AUC: 0.6331
Accuracy: 0.8883
F1: 0.710

Random Forest
AUC: 0.589

Decision Tree
AUC: 0.498

## Generated Figures
Model comparison charts
Confusion matrices
EDA visualizations
Scalability analysis plots

## Portfolio Website (GitHub Pages)
Website Link:
https://hams770.github.io/Resilient-Clinical-Outcome-Prediction-from-Noisy-Medical-Records/

Website Includes
Project overview
Pipeline architecture
Key findings
Interactive visualizations
Team members
GitHub repository link
Technical report
How It Was Created
Created index.html
Added figures and report links
Connected GitHub repo
Enabled GitHub Pages (main branch)

## GitHub Repository

https://github.com/Hams770/Resilient-Clinical-Outcome-Prediction-from-Noisy-Medical-Records

## Live Demo 
https://diabetes-readmission-ml-nvzkdxudbqfejnrc3gtsr3.streamlit.app/

## Conclusion

This project demonstrates how Apache Spark can be used to build scalable and resilient machine learning pipelines for noisy healthcare data.

By combining distributed processing, adversarial noise simulation, and MLlib models, the system achieves strong robustness, scalability, and meaningful clinical prediction performance in Big Data environments.

```bash
git clone https://github.com/Hams770/Resilient-Clinical-Outcome-Prediction-from-Noisy-Medical-Records.git
cd Resilient-Clinical-Outcome-Prediction-from-Noisy-Medical-Records
