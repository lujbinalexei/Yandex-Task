import pandas as pd
import numpy as np

data = pd.read_csv('data_task4_old.txt', sep = '\t')
data[:5]

delta = pd.to_datetime(data.closed_ts.values) - pd.to_datetime(data.assigned_ts.values)
sec = delta.seconds.values / data.Microtasks.values
data['sec'] = sec

login = list(set(data.login))
metric = []
for i in login:
    assessor = data[data.login == i]
    metric.append(sum(assessor.sec.values) / assessor.shape[0])
    
print('Справедливый норматив времени для выполнения асессором одного микрозадания: {:.1f} сек.'.format(np.median(metric)))