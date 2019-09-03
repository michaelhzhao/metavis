import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_csv('to_transform.csv')

print(df['rate'])

copy = df.copy()

def BDPT(df, theta=0, delta=[2, 2], scale=[1, 1]):
    # print(df['rate'].hasnans)
    y_tran = df['rate'].copy()
    power_neg = delta[0]
    power_pos = delta[1]
    if (y_tran.hasnans):
        inds = y_tran.notnull()
        y_obs = y_tran.loc[inds]
    else:
        y_obs = y_tran
    # print(y_obs)
    y_obs = y_obs - theta
    y_tran.loc[y_tran < 0] = (-(y_obs.loc[y_obs < 0] / y_obs.loc[y_obs < 0].median()) ** power_neg) * scale[0]
    y_tran.loc[y_tran >= 0] = ((y_obs.loc[y_obs >= 0] / y_obs.loc[y_obs >= 0].median()) ** power_pos) * scale[1]
    return y_tran

rate = BDPT(df, 0, [2, 2], [1, 1])
print(rate)

# plt.hist(copy[copy['rate'].notnull()]['rate'])

# plt.hist(rate[rate['rate'].notnull()]['rate'])
# plt.show()