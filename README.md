# Calculation-and-Visualization-From-CSV-File Using wheel Package

This package provides functionalities to analyze Apple time series data. It includes modules for data processing, statistical calculations, visualization, and analysis.



## Modules and Their Functionalities

1. **data_processing.py**: Functions to load and clean data, filter data based on average volume, and aggregate data weekly.
2. **calculate_statistics.py**: Functions to compute max, min, and average values of the stock prices.
3. **data_visualization.py**: Functions to visualize the processed data, including generating candlestick charts.
4. **data_analysis.py**: Placeholder for advanced analysis methods on the data.
5. **Main.py**: Main script to demonstrate usage of the package functionalities.

## Usage

Example usage:

```python
from Formula_Monk_assessment import calculate_statistics, data_processing, data_visualization

# Load and clean data
data = data_processing.load_data('url.csv')
clean_data = data_processing.clean_data(data)

# Compute statistics
calculate_statistics.compute_statistics(clean_data)

# Filter data based on average volume
average_volume = clean_data['AAPL.Volume'].mean()
filtered_data = data_processing.filter_data(clean_data, average_volume)

# Aggregate data to weekly level
weekly_data = data_processing.aggregate_weekly(clean_data)

# Visualize the data
data_visualization.plot_candlestick_chart(weekly_data)
```

## Testing

To run tests for the package:

```bash
python3 -m unittest discover -s tests -p "test_*.py"
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

     


##  How to Run the Code?
Clone the repository to your local machine:
git clone https://github.com/naresy/FormulaMonk_Updated.git
Navigate to the project directory:
cd Formulamonk_updated/formula_monk_assessment
Run the main Python script:
python Main.py
## Run Wheel
# Navigate to the project root
cd /path/to/FormulaMonk_Updated

# Install build tools if not already installed
pip install build setuptools wheel

# Build the package
python -m build --wheel
