import matplotlib.pyplot as plt

sizes = [23,15,5,34,22]

labels = ['Android','Apple','Windows','Blackberry','Xiaomi']
colors = ['yellow','orange','cyan','magenta','red']

plt.pie(sizes,colors = colors,startangle = 90,labels = labels)
plt.title('Popularity in phones')
plt.legend(title='Legend',loc = 'center right')
plt.axis('equal')
plt.show()
