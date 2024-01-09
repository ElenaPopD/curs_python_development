##am importat Pandas pt a incarca si manipula setul de date
import pandas as pd

# Incarc setului de date
file_path = 'C:/Users/elena/Desktop/Python_DevCourse/Sesiunea_16/Tema/Motor_Crashes.csv'
df = pd.read_csv(file_path)


# determin identificarea coloanelor pentru tipurile de vehicule
vehicle_type_columns = [col for col in df.columns if 'VEHICLE TYPE CODE' in col]

#Creez un generator pentru a filtra accidentele cu taxiuri
def taxi_accidents(dataframe):
    for index, row in dataframe.iterrows():
        if any('TAXI' in str(row[col]).upper() for col in vehicle_type_columns):
            yield row

# Utilizarea generatorului pentru a obtine accidentele cu taxiuri
taxi_accident_data = list(taxi_accidents(df))

# Conversia datelor filtrate inapoi intr-un DataFrame
taxi_accidents_df = pd.DataFrame(taxi_accident_data)

# Afisarea primelor cateva randuri
print(taxi_accidents_df.head())
