import unittest
import pandas as pd
from sklearn.linear_model import LinearRegression
from funksjoner import Del1, Del2


class TestDel1(unittest.TestCase):
    def setUp(self):
        self.del1 = Del1("../data/table.csv")
        self.data = self.del1.load_data()
        self.cleaned = self.del1.clean_data()
        self.no_file = Del1("non_existent_file.csv")
        

    def test_load_data(self):
        self.assertIsInstance(self.data, pd.DataFrame)
        self.assertFalse(self.data.empty)
        self.assertRaises(FileNotFoundError, self.no_file.load_data())
           
  
    def test_clean_data(self):
        self.assertIsInstance(self.cleaned, pd.DataFrame)
        self.assertIn("Tid(norsk normaltid)", self.cleaned.columns)
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(self.cleaned["Tid(norsk normaltid)"]))
        self.assertTrue(pd.api.types.is_float_dtype(self.cleaned["Høyeste vindkast (1 t)"]))
        self.assertTrue(pd.api.types.is_float_dtype(self.cleaned["Lufttemperatur"]))        
      


class TestDel2(unittest.TestCase):
    def setUp(self):
        self.del1 = Del1("table.csv")
        self.data = self.del1.clean_data()
        self.del2 = Del2(self.data)
        

    def test_compute_mean(self):
        mean = self.del2.compute_mean("Høyeste vindkast (1 t)")
        self.assertIsInstance(mean, float)

    def test_compute_stdv(self):
        std = self.del2.compute_stdv("Høyeste vindkast (1 t)")
        self.assertIsInstance(std, float)

    def test_compute_median(self):
        median = self.del2.compute_median("Høyeste vindkast (1 t)")
        self.assertIsInstance(median, float)

    def test_moving_average(self):
        ma = self.del2.moving_average("Høyeste vindkast (1 t)", 3)
        self.assertIsInstance(ma, pd.Series)
        self.assertIn("Høyeste vindkast (1 t)_moving_avg", self.del2.data.columns)

    def test_train_linear_regression_and_predict(self):
        model, start_time = self.del2.train_linear_regression("Høyeste vindkast (1 t)")
        self.assertIsInstance(model, LinearRegression)
        pred = self.del2.predict(model, 0)
        self.assertIsInstance(pred, float)

unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestDel1))
unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestDel2))