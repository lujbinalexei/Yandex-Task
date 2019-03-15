'''
Можно вывести пять наихудших асессоров,
а можно весь список (в нужном порядке).
'''

import pandas as pd
import numpy as np

data = pd.read_csv('data_task3.csv', sep = '\t')

login = list(set(data.login))
metric = []
for i in login:
    assessor = data[data.login == i]
    diff = assessor.cjud.values - assessor.jud.values
    diff_0 = diff[diff == 0]
    metric.append((len(diff_0) / len(diff)) * np.log(assessor.shape[0]))

assess = sorted(list(zip(login, metric)), key = lambda f: f[1])
print('Пять наихудших асессоров:\n{}'.format([assess[i][0] for i in range(len(assess))][:5]))