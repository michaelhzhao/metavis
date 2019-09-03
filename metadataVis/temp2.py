import pandas as pd
lf = pd.read_csv('C:/Users/mihuz/Documents/metadataVis/data/newdata/VTN106_ADL01_20170929.csv')

lf = lf.drop_duplicates()
lf = lf.dropna(axis=0, subset=['PTID'])

lf.to_csv('data/adccluc.csv')