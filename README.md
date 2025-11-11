# 🚀 Carbon Track: The QuickBooks for Carbon

This repository is the public HQ for my MSc Dissertation project, "Carbon Track," a SaaS platform to solve the climate reporting gap for SMBs.

This project is being built as a "full-stack" data product to demonstrate advanced skills in both data science and data engineering.
## 1. The Problem
SMBs are under massive supply chain pressure to report their carbon emissions, but all available tools are enterprise-grade platforms costing tens of thousands. The #1 bottleneck is manual data entry from hundreds of unstructured utility bills.

## 2. The Solution
Carbon Track is a simple, automated platform. The core innovation is an **end-to-end data pipeline** that uses OCR and machine learning to automatically ingest, parse, and analyze unstructured utility bills, turning a compliance burden into an immediate, auditable dataset.

## 3. Core Technology
This platform is being built using a modern, cloud-native data stack:

* **Data Ingestion:** A `FastAPI` endpoint for bill uploads.
* **Data Orchestration:** `Apache Airflow` for the main data pipeline.
* **Data Science:** A custom NER/OCR model using `Tesseract` and `spaCy`.
* **Database:** `PostgreSQL` to store structured emissions data.
* **Frontend:** A `Streamlit` dashboard for data visualisation.

## 4. Project Status & Live Demo
* **Live Demo App:** [[CarbonTrack]](https://usecarbontrack.streamlit.app/)
* **Technical Blog Post:** [Link will go here]
* **Published Academic Paper:** [Link will go here]
