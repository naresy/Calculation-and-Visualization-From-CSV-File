import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from Formula_Monk_assessment import calculate_statistics, data_processing, data_visualization, data_analysis

def test_compute_statistics():
    data = pd.DataFrame({'AAPL.Close': [100, 200, 300]})
    max_val, min_val, avg_val = calculate_statistics.compute_statistics(data)
    assert max_val == 300
    assert min_val == 100
    assert avg_val == 200
