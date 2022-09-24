# Soluções parciais

import pandas as pd

# Exs 1.1 e 1.2
tx = pd.read_csv('/home/rodrigo/Workshops/Pandas-Workshop/data/2019_Yellow_Taxi_Trip_Data.csv')
print(tx.head())
print()

# Ex 1.3
print(tx[['fare_amount', 'tip_amount', 'tolls_amount', 'total_amount']].describe())
print()

# Ex 1.4
print(tx.loc[tx.trip_distance.idxmax(), ['fare_amount', 'tip_amount', 'tolls_amount', 'total_amount']])
print()



