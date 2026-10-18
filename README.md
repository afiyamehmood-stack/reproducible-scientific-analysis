# Reproducible Scientific Analysis: Cell Viability

## Overview
A beginner Python project demonstrating data validation, descriptive statistics, and reproducible analysis using a simulated cell viability dataset.

## Project Goals
- Load measurements from a CSV file.
- Validate data types, required columns, and measurement ranges.
- Calculate mean viability and sample standard deviation for each concentration.
- Compare treatment groups with the control group.
- Test data validation and statistical calculations using Python's `unittest` framework.

## Dataset
The dataset contains 18 simulated measurements across six concentrations, with three replicates per concentration.

**Important:** These values are simulated for educational purposes. They are not real laboratory measurements or scientific evidence.

## Analysis Methods
- **Mean viability:** Average viability across replicates at each concentration.
- **Standard deviation:** Sample standard deviation across replicates.
- **Change vs. control:** Difference in mean viability between each concentration and the control, expressed in percentage points.

## Project Structure
```text
reproducible-scientific-analysis/
├── data/
│   └── cell_viability.csv
├── analyze_viability.py
└── test_analyze_viability.py
```

## Requirements
Python 3. No external packages are required for the current analysis and tests.

## Run the Analysis
```bash
python analyze_viability.py
```

## Run the Tests
```bash
python -m unittest test_analyze_viability.py
```

## Limitations
This project uses a small simulated dataset with three replicates per concentration. It demonstrates programming and basic descriptive statistics, not a validated biological model or a substitute for laboratory research.

## Skills Demonstrated
- Python programming
- CSV file handling
- Input validation and error handling
- Descriptive statistics
- Unit testing
- Reproducible data analysis
- Scientific documentation
