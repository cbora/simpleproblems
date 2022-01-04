import pandas as pd

header_list = ['state', 'year', 'quarter', 'hpi']
df = pd.read_csv('https://www.fhfa.gov/DataTools/Downloads/Documents/HPI/HPI_AT_state.csv', names=header_list)

# mean by state, year
mean_by_state_year = df.groupby(['state', 'year'])['hpi'].mean()

print(f'Mean by State, Year\n {mean_by_state_year}\n\n')


# mean by state
mean_by_state = df.groupby('state')['hpi'].mean()
print(f'Mean by State\n {mean_by_state}\n\n')


# Adding column to calculate the running mean for each state
df['Running Mean'] = df.groupby('state', as_index=False).rolling(2)['hpi'].mean().reset_index(level=0, drop=True)
print('DF with Running Mean\n {} \n\n'.format(df))
