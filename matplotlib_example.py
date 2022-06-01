import matplotlib.pyplot as plt

x = []
y=[]

readFile = open("coordinate.txt",'r')

data = readFile.read()
print(data)

plt.plot([1,2,3,4],[3,8,10,25])
plt.title('Rain in December')
plt.xlabel('Days in December')
plt.ylabel('Inches of rain')
plt.show()
