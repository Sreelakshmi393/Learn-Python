import matplotlib.pyplot as plt
import numpy as np

pos = np.arange(6) + 0.5

snames = ['Avi','Jose','Bob','Nick','Zelda','Vicky']
plt.bar(pos,(4,6,2,8,7,9),align = 'center',color = 'green')

plt.ylabel('Height of students',color = 'blue')
plt.xlabel('Students', color = 'blue')
plt.title("Studnet's Physical Data(inches)",color = 'red')

plt.tick_params(axis = 'x',colors = 'brown')
plt.tick_params(axis = 'y',colors = 'brown')

plt.subplots_adjust(left = .11,bottom = .12,right = .94)

plt.xticks(pos,snames)

plt.show()
