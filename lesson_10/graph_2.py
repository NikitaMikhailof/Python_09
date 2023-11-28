import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv('spotify-2023_fixed.csv')
plt.figure(figsize=(10, 6))

title_dict = {'fontsize': 20, 'fontweight': 'bold', 
              'color': '#0E6655', 'family': 'fantasy'}
lable_dict = {'fontsize': '16', 'color': '#BA4A00', 'family': 'fantasy'}

df.loc[df['released_year'] == 2023]

sns.lineplot(data=df, x='artist_count', y='released_month')

plt.title('Количество артистов в релизах 2023 году', fontdict=title_dict)
plt.xlabel('Количество артистов', fontdict=lable_dict)
plt.ylabel('Месяц', fontdict=lable_dict)

plt.show()




