from scipy.io import arff
import pandas as pd

data, meta = arff.loadarff('fz.arff')
df = pd.DataFrame(data)
print(data.head())