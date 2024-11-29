
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

#load data
df= pd.read_csv("https://raw.githubusercontent.com/nabilahrahmawati/Bike_Dsb/refs/heads/main/hour_bikeshare.csv")
df['dateday'] = pd.to_datetime(df['dateday'])


st.set_page_config(page_title="Bike-Rent Dashboard",
                   page_icon="sparkles:",
                   layout="wide")

# Menghapus kolom yang tidak dipakai
drop_col = ['windspeed']

for i in df.columns:
  if i in drop_col:
    df.drop(labels=i, axis=1, inplace=True)

# Menyiapkan season_rent_df
def create_season_rent_df(df):
    season_rent_df = df.groupby(by='season')[['registered', 'casual']].sum().reset_index()
    return season_rent_df

# Menyiapkan monthly_rent_df
def create_monthly_rent_df(df):
    monthly_rent_df = df.resample(rule='M', on='dateday').agg({
        "casual": "sum",
        "registered": "sum",
        "count": "sum"
    })
    monthly_rent_df.index = monthly_rent_df.index.strftime('%b-%y')
    monthly_rent_df = monthly_rent_df.reset_index()
    
    return monthly_rent_df

# Menyiapkan weekday_rent_df
def create_weekday_rent_df(df):
    weekday_rent_df = df.groupby(by='weekday').agg({
        'count': 'sum'
    }).reset_index()
    return weekday_rent_df

# Menyiapkan workingday_rent_df
def create_workingday_rent_df(df):
    workingday_rent_df = df.groupby(by='workingday').agg({
        'count': 'sum'
    }).reset_index()
    return workingday_rent_df

# Menyiapkan holiday_rent_df
def create_holiday_rent_df(df):
    holiday_rent_df = df.groupby(by='holiday').agg({
        'count': 'sum'
    }).reset_index()
    return holiday_rent_df

# Menyiapkan weather_rent_df
def create_weather_rent_df(df):
    weather_rent_df = df.groupby(by='weathersit').agg({
        'count': 'sum'
    })
    return weather_rent_df


# Membuat komponen filter
min_date = pd.to_datetime(df['dateday']).dt.date.min()
max_date = pd.to_datetime(df['dateday']).dt.date.max()

#Mengatur Sidebar
with st.sidebar:
    # add capital bikeshare logo
    st.image("https://st2.depositphotos.com/1000384/10218/v/950/depositphotos_102186472-stock-illustration-bike-rent-red-stamp.jpg")

    # mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label="Date Filter", min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

#menguhubungkan filter dengan main_df
main_df = df[(df['dateday'] >= str(start_date)) & 
            (df['dateday'] <= str(end_date))]


# Menyiapkan dataframe
season_rent_df = create_season_rent_df(main_df)
monthly_rent_df = create_monthly_rent_df(main_df)
weekday_rent_df = create_weekday_rent_df(main_df)
workingday_rent_df = create_workingday_rent_df(main_df)
holiday_rent_df = create_holiday_rent_df(main_df)
weather_rent_df = create_weather_rent_df(main_df)   


#Mengatur Mainpage
st.title(":sparkles: Bike-Rent Dashboard")
st.markdown("##")

col1, col2, col3 = st.columns(3)

with col1:
    total_all_rides = main_df['count'].sum()
    st.metric("Total Rides", value=total_all_rides)
with col2:
    total_casual_rides = main_df['casual'].sum()
    st.metric("Total Casual Rides", value=total_casual_rides)
with col3:
    total_registered_rides = main_df['registered'].sum()
    st.metric("Total Registered Rides", value=total_registered_rides)

st.markdown("---")

#Chart Sewa Bulanan
st.subheader('Monthly Rentals')
fig, ax = plt.subplots(figsize=(16, 8))

# Create a line plot using the sns.lineplot() function
sns.lineplot(
    x="dateday", 
    y="count", 
    data=monthly_rent_df, 
    label='Count',
    ax=ax
    )

sns.lineplot(
    x="dateday", 
    y="casual", 
    data=monthly_rent_df, 
    label='Casual',
    ax=ax
    )

sns.lineplot(
    x="dateday", 
    y="registered", 
    data=monthly_rent_df, 
    label='Registered',
    ax=ax
    )

ax.set_ylabel("Total Rides", fontsize=20)
ax.set_xlabel(None)
ax.tick_params(axis='x', labelsize=20, rotation=45)
ax.tick_params(axis='y', labelsize=20,)

st.pyplot(fig)

#Chart Sewa setiap Musim (Season)
st.subheader('Seasonly Rentals')

fig, ax = plt.subplots(figsize=(16, 8))
colors1=["tab:gray", "tab:gray", "tab:blue", "tab:gray"]
colors2=["tab:gray", "tab:gray", "tab:olive", "tab:gray"]

sns.barplot(
    x='season',
    y='registered',
    data=season_rent_df,
    label='Registered',
    palette=colors1,
    ax=ax
)

sns.barplot(
    x='season',
    y='casual',
    data=season_rent_df,
    label='Casual',
    palette=colors2,
    ax=ax
)

for index, row in season_rent_df.iterrows():
    ax.text(index, row['registered'], str(row['registered']), ha='center', va='bottom', fontsize=12)
    ax.text(index, row['casual'], str(row['casual']), ha='center', va='bottom', fontsize=12)

ax.set_xlabel(None)
ax.set_ylabel("Total Rides", fontsize=20)
ax.tick_params(axis='x', labelsize=15, rotation=0)
ax.tick_params(axis='y', labelsize=15)
st.pyplot(fig)

# Chart rent berdasarkan weekday, working dan holiday
st.subheader('Weekday, Workingday, and Holiday Rentals')

fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(30,38))

colors3=["tab:gray", "tab:blue"]
colors4=["tab:blue", "tab:gray"]
colors5=["tab:blue", "tab:gray", "tab:gray", "tab:gray", "tab:gray", "tab:gray", "tab:gray"]

# Berdasarkan workingday
sns.barplot(
    x='workingday',
    y='count',
    data=workingday_rent_df,
    palette=colors3,
    ax=axes[0])

for index, row in enumerate(workingday_rent_df['count']):
    axes[0].text(index, row + 1, str(row), ha='center', va='bottom', fontsize=20)

axes[0].set_title('Number of Rents based on Working Day', fontsize=25)
axes[0].set_ylabel(None)
axes[0].set_xlabel("0= Not Rent, 1= Rent", fontsize=20)
axes[0].tick_params(axis='x', labelsize=15)
axes[0].tick_params(axis='y', labelsize=15)

# Berdasarkan holiday
sns.barplot(
  x='holiday',
  y='count',
  data=holiday_rent_df,
  palette=colors4,
  ax=axes[1])

for index, row in enumerate(holiday_rent_df['count']):
    axes[1].text(index, row + 1, str(row), ha='center', va='bottom', fontsize=20)

axes[1].set_title('Number of Rents based on Holiday', fontsize=25)
axes[1].set_ylabel(None)
axes[1].set_xlabel("0= Not Rent, 1= Rent", fontsize=20)
axes[1].tick_params(axis='x', labelsize=15)
axes[1].tick_params(axis='y', labelsize=15)

# Berdasarkan weekday
sns.barplot(
  x='weekday',
  y='count',
  data=weekday_rent_df,
  palette=colors5,
  ax=axes[2])

for index, row in enumerate(weekday_rent_df['count']):
    axes[2].text(index, row + 1, str(row), ha='center', va='bottom', fontsize=20)

axes[2].set_title('Number of Rents based on Weekday', fontsize=25)
axes[2].set_ylabel(None)
axes[2].set_xlabel('Weekday', fontsize=20)
axes[2].tick_params(axis='x', labelsize=20)
axes[2].tick_params(axis='y', labelsize=15)

plt.tight_layout()
st.pyplot(fig)



 
st.caption('Copyright (c) Nab 2023')
