import pandas as pd

data = pd.read_csv('data/pollution_data.csv')
data.when = pd.to_datetime(data.when)

temp_dict = {}

for key, group in data[
        (data.station == 'Cuatro Caminos') &\
        (data.when.dt.year == 2015)].groupby('magnitude'):
    temp_dict[key] = pd.Series(group.measurement.values,
                               index=group.when.values)

tocorr = pd.DataFrame(temp_dict)
print(tocorr.corr())
