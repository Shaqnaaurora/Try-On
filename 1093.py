import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# dokumentasi
data = {'kategori': ['A', 'B', 'C', 'D', 'E'],
        'nilai': [20, 35, 30, 25, 40],
         'bebas': [0, 1, 2, 3, 4]}
df = pd.DataFrame(data)
print(df)

plt.figure(figsize=(8,8)) 
plt.pie(df['nilai'], labels=df['kategori'], autopct='%1.1f%%')
plt.title('Grafik')
plt.axis('equal') #supaya lingkaran terlihat bulat
plt.show() 