import matplotlib.pyplot as plt
from bitvavo_api import data
values = [157.81,3.33,4621.39,1200.40,63.90]
labels = ["1","2","3","4","5"]
print(values)
plt.pie(values,labels=labels)
plt.show()
chart = data.draw_pie_chart_of_all_currencys()
print(chart)