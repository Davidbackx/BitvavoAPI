import matplotlib.pyplot as plt

values = [157.81,3.33,4621.39,1200.40,63.90]
labels = ["1","2","3","4","5"]
print(values)
plt.pie(values,labels=labels)
plt.show()