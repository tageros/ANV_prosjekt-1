from unittest.mock import patch
import unittest
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from io import StringIO
from src.funksjoner import Del2


class TestDel2(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame({
            "Temp": [1, 2, 3, 4, 5],
            "Tid(norsk normaltid)": pd.date_range("2023-01-01", periods=5, freq="H"),
            "Vind": [5, 4, 3, 2, 1]
        })
        self.del2 = Del2(self.df)

    def test_compute_mean(self):
        result = self.del2.compute_mean("Temp")
        self.assertEqual(result, 3.0)

    def test_compute_stdv(self):
        result = self.del2.compute_stdv("Temp")
        expected = np.std(self.df["Temp"], ddof=1)
        self.assertAlmostEqual(result, expected)

    def test_compute_median(self):
        self.assertEqual(self.del2.compute_median("Temp"), 3)

    def test_moving_average_with_self_data(self):
        result = self.del2.moving_average('Temp', vindu=3)
        self.assertIsInstance(result, pd.Series)
        self.assertIn('Temp_moving_avg', self.del2.data.columns)
        self.assertAlmostEqual(result.iloc[2], 2.0)  # (1+2+3)/3

    def test_moving_average_with_explicit_df(self):
        df_missing = self.df.copy()
        df_missing.loc[1, 'Temp'] = np.nan  # Sett én verdi til NaN
        result = self.del2.moving_average('Temp', vindu=3, df=df_missing)
        self.assertIn('Temp_moving_avg', df_missing.columns)
        self.assertTrue(np.isnan(result.iloc[1]) or result.iloc[1] == 1.0)

    def test_train_linear_regression(self):
        model, start_time = self.del2.train_linear_regression("Temp")
        self.assertTrue(hasattr(model, "coef_"))
        self.assertEqual(start_time, self.df["Tid(norsk normaltid)"].min())

    def test_predict_value(self):
        model, _ = self.del2.train_linear_regression("Temp")
        prediction = self.del2.predict(model, 2.0)
        self.assertIsInstance(prediction, float)

    def test_invalid_column_analysis(self):
        self.del2.simple_analysis("Nonexistent")

    def test_correlation_pearson(self):
        correlation = self.del2.correlation_analysis("Temp", "Vind", method="pearson")
        self.assertAlmostEqual(correlation, -1.0)
    
    def test_correlation_spearman(self):
        correlation = self.del2.correlation_analysis("Temp", "Vind", method="spearman")
        self.assertAlmostEqual(correlation, -1.0)
    
    def test_correlation_kendall(self):
        correlation = self.del2.correlation_analysis("Temp", "Vind", method="kendall")
        self.assertAlmostEqual(correlation, -1.0)
    
    def test_correlation_invalid_column(self):
        result = self.del2.correlation_analysis("Temp", "Vind", method="invalid")
        self.assertIsNone(result)
        
    
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestDel2))