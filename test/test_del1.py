from unittest.mock import patch
import unittest
import pandas as pd
import numpy as np
from io import StringIO
from src.funksjoner import Del1

class TestDel1(unittest.TestCase):
    
    def setUp(self):
        # Lager en fil som ikke eksisterer for å teste filhåndtering
        self.del1 = Del1("dummy.csv")
        # Simulerer en CSV-fil med data
        # Bruker semikolon som separator og norsk desimaltegn for å matche daten i table.csv
        self.sample_csv = "Tid(norsk normaltid);Temp\n01.01.2023 00:00;1,5\n01.01.2023 01:00;2,0"

    # Teste at filen lastes inn riktig
    def test_load_data_success(self):
        with patch("builtins.open", return_value=StringIO(self.sample_csv)), \
             patch("pandas.read_csv", return_value=pd.read_csv(StringIO(self.sample_csv), sep=";")):
            df = self.del1.load_data()
            self.assertIsNotNone(df)
            self.assertIn("Temp", df.columns)
    # Teste at dummy filen ikke finnes
    def test_load_data_file_not_found(self):
        with patch("pandas.read_csv", side_effect=FileNotFoundError()):
            self.assertIsNone(self.del1.load_data())

    # Teste at feil ved tolking av filen håndteres
    def test_clean_data_removes_hidden_chars(self):
        self.del1.data = pd.DataFrame({"Temp ": [1, 2]})
        cleaned = self.del1.clean_data()
        self.assertIn("Temp", cleaned.columns)

    # Teste at funksjonen kalrer å bytte til numerisk format
    def test_convert_to_numerical_success(self):
        self.del1.data = pd.DataFrame({"Temp": ["1,2", "3,4"]})
        df = self.del1.convert_to_numerical("Temp")
        self.assertTrue(np.issubdtype(df["Temp"].dtype, np.floating))

    # Teste at funksjonen håndterer feil ved konvertering
    def test_convert_to_numerical_key_error(self):
        self.del1.data = pd.DataFrame({})
        self.del1.convert_to_numerical("Nonexistent") 

    # Teste at funksjonen konverterer til datetime-format
    def test_convert_to_datetime_success(self):
        self.del1.data = pd.DataFrame({"Tid": ["01.01.2023 00:00"]})
        df = self.del1.convert_to_datetime("Tid")
        self.assertTrue(pd.api.types.is_datetime64_any_dtype(df["Tid"]))

    # Teste at funksjonen håndterer feil ved konvertering til datetime
    def test_convert_to_datetime_key_error(self):
        self.del1.data = pd.DataFrame({})
        self.del1.convert_to_datetime("Nonexistent") 


unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestDel1))
