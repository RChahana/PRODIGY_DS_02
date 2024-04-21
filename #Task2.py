import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
#Data Cleaning
df=pd.read_csv("titles.csv")
print(df.info())
print(df.shape)
df=df.drop_duplicates('id',keep='first')
#EDA
print(df.isnull().sum())
df=df.drop(['description','age_certification','seasons','imdb_id',
    'imdb_votes','tmdb_popularity','tmdb_score'],axis=1)
df['imdb_score'].fillna(df['imdb_score'].mean(),inplace=True)
df=df.dropna()
print(df.isnull().sum())
df1=pd.DataFrame(df.sample(n=20))
#Data Visualization
# Initialize an empty dictionary to store country frequencies
country_freq = {}
for countries in df['production_countries']:
    # Remove brackets and split the string to get individual countries
    countries = countries.strip("[]").replace("'", "").split(", ")
    for country in countries:
        if country in country_freq:
            country_freq[country] += 1
        else:
            country_freq[country] = 1
country_counts = pd.Series(country_freq)

# Plot the Barplot
country_counts.plot(kind='bar')
plt.title('Production Countries Histogram')
plt.xlabel('Country')
plt.ylabel('Frequency')
plt.show()
# Plot the countplot
df2=pd.DataFrame(df)
sns.countplot(x='type',data=df2)
plt.xlabel('Type')
plt.tight_layout()
plt.show()
#Boxplot
df3=pd.DataFrame(df.sample(n=50))
sns.boxplot(x='production_countries',y='imdb_score',hue='type',data=df3)
plt.show()
#Violin plot
sns.violinplot(x='production_countries',y='imdb_score',hue='type',data=df1,palette='pastel')
plt.show()
df4=pd.DataFrame(df.sample(n=55))
#Stripplot
sns.stripplot(x='production_countries',y='imdb_score',jitter=True,hue='type',data=df4)
plt.show()
#Boxen plot
sns.boxenplot(data=df,x='release_year',y='type')
plt.ylabel("Type of Netflix films")
plt.title('Year vs type')
plt.show()
#Pointplot
df=df.drop_duplicates('release_year',keep='first')
flights_wide=df.pivot(index='release_year',columns='production_countries',values='release_year')
sns.pointplot(flights_wide)
plt.title('Year vs Production_Countries')
plt.ylabel('Release year')
plt.show()
#Correlation Matrix
num_col=df.select_dtypes(include=np.number)
corr_matrix=num_col.corr()
sns.heatmap(corr_matrix,annot=True,cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

