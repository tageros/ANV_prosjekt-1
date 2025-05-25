import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

class Del1():

    def __init__(self, file_path: str) -> None:
        self.data = None
        self.file_path = file_path

    def load_data(self):
        try:
            # Laste inn data
            self.data = pd.read_csv(self.file_path, sep=";", engine='python')

            return self.data

        except FileNotFoundError:
            print(f"Filen {self.file_path} ble ikke funnet.")
            return None
        except pd.errors.ParserError as e:
            print(f"Feil ved tolking av filen: {e}")
        except Exception as e:
            print(f"Uventet feil: {e}")
    
    def clean_data(self):
        try:
            # Fjerne eventuelle skjulte tegn
            self.data.columns = self.data.columns.str.replace("\ufeff", "").str.strip()

            return self.data

        except pd.errors.ParserError as e:
            print(f"Feil ved tolking av filen: {e}")
        except Exception as e:
            print(f"Uventet feil: {e}")

    # Konvertere relevante kolonner til numerisk format
    def convert_to_numerical(self, kolonne: str):
        try:
            self.data[kolonne] = [
                float(x.replace(",", ".")) if isinstance(x, str) else x 
                for x in self.data[kolonne]
            ]
            return self.data 

        except ValueError as e:
            print(f"Feil ved konvertering av kolonner til numerisk format: {e}")
        except KeyError as e:
            print(f"Kolonnen finnes ikke i data: {e}")
        except Exception as e:
            print(f"Uventet feil under konvertering til numerisk format: {e}")


    # Konvertere 'Tid(norsk normaltid)' til datetime-format
    def convert_to_datetime(self, kolonne: str):
        try:
            self.data[kolonne] = [pd.to_datetime(t, format="%d.%m.%Y %H:%M") for t in self.data[kolonne]]
            return self.data
        
        except ValueError as e:
            print(f"Feil ved konvertering av tid: {e}")
        except KeyError as e:   
            print(f"Kolonnen finnes ikke i data: {e}")
        except Exception as e:
            print(f"Uventet feil under konvertering til datetime: {e}")

    
class Del2():

    def __init__(self, data: pd.DataFrame) -> None:
        self.data = data

    # Beregne Gjnnomsnitt
    def compute_mean(self, kolonne: str):
        try:
            gjennomsnitt = self.data[kolonne].mean()
            print(f"Gjennomsnitt for '{kolonne}': {gjennomsnitt:.2f}")
            return gjennomsnitt
        except KeyError:
            print(f"Kolonnen '{kolonne}' finnes ikke i datasettet.")
        except Exception as e:
            print(f"Feil under gjennomsnittsberegning: {e}")
    
    # Beregne Standardavvik
    def compute_stdv(self, kolonne: str):
        try:
            varians = self.data[kolonne].std()
            print(f"Varians for '{kolonne}': {varians:.2f}")
            return varians
        except KeyError:
            print(f"Kolonnen '{kolonne}' finnes ikke i datasettet.")
        except Exception as e:
            print(f"Feil under variansberegning: {e}")
    
    # Beregne Median
    def compute_median(self, kolonne: str):
        try:
            median = self.data[kolonne].median()
            print(f"Median for '{kolonne}': {median:.2f}")
            return median
        except KeyError:
            print(f"Kolonnen '{kolonne}' finnes ikke i datasettet.")
        except Exception as e:
            print(f"Feil under medianberegning: {e}")
    
    # Enkel analyse av data
    def simple_analysis(self, kolonne: str):
        try:
            self.data[kolonne].describe()
        except Exception as e:
            print(f"Feil under enkel analyse: {e}")

    def moving_average(self, kolonne: str, vindu: int):
        try:
            self.data[f"{kolonne}_moving_avg"] = self.data[kolonne].rolling(window=vindu).mean()
            return self.data[f"{kolonne}_moving_avg"]
        except KeyError:
            print(f"Kolonnen '{kolonne}' finnes ikke i datasettet.")
        except Exception as e:
            print(f"Feil under beregning av glidende gjennomsnitt: {e}")

    
    def train_linear_regression(self, target: str, time_column = "Tid(norsk normaltid)"):
        try:
            # Lager kopier av dataene for å unngå å endre originaldataene og fionner starttidspunktet
            self.data = self.data.copy()
            start_time = self.data[time_column].min()
            
            # Konverterer tid til timer fra starttidspunktet
            self.data["medgått_tid"] = (self.data[time_column] - start_time).dt.total_seconds() / 3600 
            
            # Rydder data ved å fjerne rader med NaN-verdier i de relevante kolonnene som er nødvendig 
            cleaned_data = self.data.dropna(subset=[target, "medgått_tid"])
            
            # Trener Modellen
            model = LinearRegression()
            model.fit(cleaned_data[["medgått_tid"]], cleaned_data[target])

            return model, start_time
        
        except KeyError:
            print(f"En eller flere kolonner finnes ikke i datasettet.")
        except Exception as e:
            print(f"Feil under trening av lineær regresjon: {e}")

    def predict(self, model, time: float):
        try:
            return model.intercept_ + model.coef_[0] * time
        
        except Exception as e:
            print(f"Feil under prediksjon: {e}")

    
    def correlation_analysis(self, kolonne1: str, kolonne2: str, method: str = "pearson"):
        if method not in ["pearson", "spearman", "kendall"]:
            print(f"Ugyldig metode '{method}'. Bruk 'pearson', 'spearman' eller 'kendall'.")
            return None
        try:
            # Beregner korrelasjon mellom de to kolonnene for den metoden som er valgt
            if method == "pearson":
                correlation = self.data[kolonne1].corr(self.data[kolonne2], method='pearson')
            elif method == "spearman":
                correlation = self.data[kolonne1].corr(self.data[kolonne2], method='spearman')
            elif method == "kendall":
                correlation = self.data[kolonne1].corr(self.data[kolonne2], method='kendall')
            correlation = self.data[kolonne1].corr(self.data[kolonne2])
            
            print(f"Korrelasjon mellom '{kolonne1}' og '{kolonne2}' ({method}): {correlation:.2f}")
            return correlation
        except KeyError:
            print(f"En eller begge kolonner finnes ikke i datasettet.")
        except Exception as e:
            print(f"Feil under korrelasjonsanalyse: {e}")
    
    