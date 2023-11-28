import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

df = pd.read_csv('spotify-2023_fixed.csv')
plt.figure(figsize=(10, 6))

title_dict = {'fontsize': 20, 'fontweight': 'bold', 
              'color': '#cd5700', 'family': 'fantasy'}
lable_dict = {'fontsize': '16', 'color': '#cd5700', 'family': 'fantasy'}

dezzer = len(df[df['mode'] =='Major']['in_deezer_charts'].value_counts()) 
shazam = len(df[df['mode'] =='Major']['in_shazam_charts'].value_counts()) 
apple = len(df[df['mode'] =='Major']['in_apple_charts'].value_counts()) 

plt.title('Количество веселых песен в чартах', fontdict=title_dict)
plt.xlabel('Наименование чартов', fontdict=lable_dict)
plt.ylabel('Количество песен', fontdict=lable_dict)

sns.barplot(x=["deezer_charts", "shazam_charts", "apple_charts"],
            y=[dezzer, shazam, apple])

plt.show()