# AMFI NAV Extractor
Python script to extract AMFI NAV data as TSV and JSON

This is a Python script to extract **Scheme Name** and **Asset Value** from the [AMFI NAV data](https://www.amfiindia.com/spages/NAVAll.txt).  
It saves the output in both **TSV** and **JSON** formats.

---

## 📌 Features

- ✅ Downloads and parses AMFI NAV data
- ✅ Extracts relevant fields: Scheme Name and Asset Value
- ✅ Saves data in:
  - `scheme_asset_data.tsv` (tab-separated file)
  - `scheme_asset_data.json` (JSON structured file)

---

## 🚀 How to Run

### 1. Install dependencies (if not already):

```bash
pip install requests
