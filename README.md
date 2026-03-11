# API and Data Science Learning (Basic Level) 🚀

This project is a workspace created to learn modern API development tools (FastAPI) and data analysis libraries (Pandas, Numpy, Matplotlib, Seaborn) in the Python ecosystem. It serves as a "Hello World!" project for the world of data analysis.

## 🎯 Motivation (Why?)

In the software development process, it is a critical skill to not just write code, but also to make sense of data and create services (APIs) that expose this data to the outside world. The main goals of this project are:
- Learning to develop fast and reliable asynchronous APIs with **FastAPI**.
- Gaining practice in manipulating datasets using **Pandas** and **Numpy**.
- Presenting meaningful reports by visualizing data with **Matplotlib** and **Seaborn**.
- Developing problem-solving skills by analyzing real-world data (Video Game Sales, Traffic Data, etc.).

## 📂 File Structure

- `main.py`: Basic API endpoints created with FastAPI (GET/POST examples).
- `vgsalesanaliz.py`: **Advanced regional and annual analyses** performed on video game sales data (`vgsales.csv`).
- `trafikanaliz.py`: Script that analyzes traffic data (`trafik_verisi.csv`) and generates visual reports.
- `pandasdeneme.py` & `numpydeneme.py`: Example scripts created to test the basic features of these libraries.
- `requirements.txt`: List of libraries required for the project to run.
- `vgsales.csv` & `trafik_verisi.csv`: Sample datasets used in the analyses.

## 📊 Advanced Analysis Features (vgsalesanaliz.py)

In the final stage of the project, in-depth regional and temporal analyses were performed on video game sales data:

### 1. Regional Sales Visualization
Using the Seaborn library, the 5 most popular game genres for 4 different regions (Japan, North America, Europe, Other) were visualized in a 2x2 subplot structure.
- **Color Palettes**: Visual depth was provided in the analyses by using `magma`, `viridis`, `rocket`, and `mako` palettes.

### 2. Regional Bests
The top-selling games and genres according to regions were determined through queries performed on the dataset:

| Region | Best Selling Game | Most Popular Genre |
| :--- | :--- | :--- |
| **North America (NA)** | Wii Sports | Sports |
| **Europe (EU)** | Wii Sports | Sports |
| **Japan (JP)** | Pokemon Red/Pokemon Blue | Role-Playing |
| **Other** | Grand Theft Auto: San Andreas | Action |

### 3. Best Sellers By Years
The global sales champions of each year since 1980 were analyzed using Pandas' `groupby` and `idxmax` functions. Some notable years:

- **1985**: Super Mario Bros. (40.24M)
- **1989**: Tetris (30.26M)
- **1996**: Pokemon Red/Blue (31.37M)
- **2004**: GTA: San Andreas (20.81M)
- **2006**: Wii Sports (82.74M - All-time record!)
- **2013**: Grand Theft Auto V (21.40M)

## 🛠️ Installation

You can follow these steps to run the project locally:

1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the API Server:**
   ```bash
   uvicorn main:app --reload
   ```

3. **Run the Analysis Scripts:**
   ```bash
   python vgsalesanaliz.py
   ```

## 📈 Learning Notes
- **Time Series Analysis**: Tracking trends by grouping data by years.
- **Data Grouping**: Extracting specific information from complex datasets using `groupby()` and `idxmax()` functions.
- **Visualization**: Presenting multiple graphs (`plt.subplots`) in a single window in an organized manner.
- **API Development**: Data validation with Pydantic models and asynchronous process management.
