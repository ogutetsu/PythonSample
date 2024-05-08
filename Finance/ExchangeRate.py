import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cufflinks as cf
import plotly.offline as plyo


raw = pd.read_csv('../SampleData/OANDA_XAUUSD.csv', index_col=0, parse_dates=True)
print(raw.info())
print(raw.tail())

qf = cf.QuantFig(raw,
                 title='OANDA XAUUSD',
                 legend='top',
                 name='XAUUSD')

plyo.iplot(qf.iplot(asFigure=True),
           image='png',
           filename='qf_01')






