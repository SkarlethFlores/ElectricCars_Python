# ⚡ Electric Vehicle Population Data Analysis

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![MapReduce](https://img.shields.io/badge/mrjob-MapReduce-green)
![PEP8](https://img.shields.io/badge/Code%20Style-PEP%208-blue)

> A comprehensive data analysis and visualization pipeline processing **112,000+ electric vehicle registrations** from the Washington State Department of Licensing dataset.

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Key Analyses](#-key-analyses)
- [Architecture & OOP Design](#-architecture--oop-design)
- [Code Quality](#-code-quality)
- [Author](#-author)

---

## 🔍 Project Overview

This project was developed as part of a **Master's degree program** to demonstrate practical Python skills in data engineering, exploratory data analysis, and distributed computing. It processes a real-world dataset of **112,635 battery electric and plug-in hybrid vehicle registrations** across multiple U.S. states.

The pipeline covers the full data lifecycle: ingestion → transformation → analysis → visualization, with a MapReduce layer for scalable aggregation.

---

## ✨ Features

- 📥 **CSV Parsing & Format Conversion** — Converts comma-delimited files to semicolon format with robust error handling
- 🔄 **ETL Pipeline** — Cleans, transforms, and aggregates multi-state EV registration records
- 📊 **Data Visualization** — Dynamic matplotlib charts for autonomy trends and manufacturer comparisons
- 🗺️ **Geospatial Analysis** — State-level distribution using GeoPandas
- ⚙️ **Distributed Computing** — MapReduce architecture via `mrjob` for scalable vehicle counting
- 📈 **Year-over-Year Trends** — Range/autonomy evolution analysis by model and manufacturer

---

## 🛠️ Tech Stack

| Library | Purpose |
|---|---|
| `pandas` | Data manipulation and aggregation |
| `numpy` | Numerical computing and type handling |
| `matplotlib` | Data visualization and charting |
| `geopandas` | Geographic/spatial data analysis |
| `mrjob` | MapReduce distributed computing framework |

---

## 📁 Project Structure

```
ElectricCars_Python/
│
├── data/
│   └── Electric_Vehicle_Population_Data.csv   # Source dataset (WA Dept. of Licensing)
│
├── src/
│   ├── data_processing.py     # CSV parsing, format conversion, ETL functions
│   ├── analysis.py            # Autonomy trends, state distribution, aggregations
│   ├── visualization.py       # Matplotlib chart generation
│   ├── mapreduce_job.py       # MRVehiculosCount (mrjob MapReduce class)
│   └── geo_analysis.py        # GeoPandas spatial analysis
│
├── notebooks/
│   └── EV_Analysis.ipynb      # Exploratory analysis notebook
│
├── requirements.txt
└── README.md
```

> ⚠️ *Structure may vary slightly — refer to the actual repo files.*

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/SkarlethFlores/ElectricCars_Python.git
cd ElectricCars_Python

# 2. Install dependencies
pip install -r requirements.txt
```

### Running the Analysis

```bash
# Run main data analysis
python src/analysis.py

# Run MapReduce vehicle count job
python src/mapreduce_job.py data/Electric_Vehicle_Population_Data.csv
```

---

## 📊 Key Analyses

### 1. EV Distribution by State
Aggregated 112,635 vehicle records to map electric vehicle adoption across U.S. states, identifying Washington as the dominant market.

### 2. Autonomy (Range) Trends Over Time
Filtered and grouped vehicles by model year to track year-over-year improvements in electric range, revealing consistent technology advancement from 2010 to present.

### 3. Manufacturer Comparison
Compared EV range across top manufacturers (Tesla, Chevrolet, Nissan, etc.) using grouped bar charts.

### 4. Geographic Distribution
Leveraged GeoPandas to visualize state-level EV density on a U.S. map.

---

## 🏗️ Architecture & OOP Design

The MapReduce component uses object-oriented design through the `mrjob` framework:

```python
from mrjob.job import MRJob

class MRVehiculosCount(MRJob):
    """
    Counts electric vehicles per state using MapReduce.
    Inherits from MRJob and overrides mapper/reducer methods.
    """

    def mapper(self, _, line):
        # Emits (state, 1) for each vehicle record
        ...

    def reducer(self, state, counts):
        # Aggregates total count per state
        ...
```

**OOP Concepts Applied:**
- **Inheritance** — `MRVehiculosCount` extends `MRJob`
- **Method Overriding** — Custom `mapper()` and `reducer()` implementations
- **Encapsulation** — Vehicle counting logic contained within the class
- **Design Pattern** — Map-Reduce pattern for distributed aggregation

---

## ✅ Code Quality

This project follows professional Python development standards:

| Practice | Status |
|---|---|
| PEP 8 style compliance | ✅ |
| Docstrings on all functions | ✅ |
| Missing data & type conversion handling | ✅ |
| Single-pass algorithm optimization | ✅ |
| Modular, single-responsibility functions | ✅ |

---

## 👩‍💻 Author

**Skarleth Flores**
Master's Student — Python for Data Science

[![GitHub](https://img.shields.io/badge/GitHub-SkarlethFlores-181717?logo=github)](https://github.com/SkarlethFlores)

---

*Dataset source: [Washington State Department of Licensing — Electric Vehicle Population Data](https://catalog.data.gov/dataset/electric-vehicle-population-data)*
