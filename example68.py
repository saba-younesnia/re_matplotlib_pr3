import matplotlib.pyplot as plt
import numpy as np

names=['apple','pear','orange','strawberry']
amounts=np.array([120,90,560,50])

plt.pie(amounts,labels=names,autopct='%1.0f%%')
plt.show()

plt.pie(amounts,labels=names,autopct='%1.1f%%')
plt.show()

plt.pie(amounts,labels=names,autopct='%1.2f%%')
plt.show()