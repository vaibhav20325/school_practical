import matplotlib.pyplot as plt

labels=['Uttar Pradesh', 'Madhya Pradesh','Bihar','Arunachal Pradesh',
        'Goa','Sikkim','Nagaland','Tripura','Haryana','Punjab']
pnp=[828,236,1102,17,394,86,119,350,573,550]

plt.pie(pnp,labels=labels)
plt.show()
