# exhibitA-input.csv


# import pandas as pd

# # Read the CSV file into a pandas DataFrame
# df = pd.read_csv('exhibitA-input.csv', delimiter='\t')

# # Filter the DataFrame to include only the rows with distinct songs
# distinct_songs = df['SONG_ID'].value_counts()
# filtered_df = df[df['SONG_ID'].isin(distinct_songs[distinct_songs == 346].index)]

# # Get the count of unique users
# num_users = filtered_df['CLIENT_ID'].nunique()

# # Print the result
# print("Number of users who played 346 distinct songs:", num_users)



import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('exhibitA-input.csv', delimiter='\t')

# Get the count of distinct songs played for each user
user_song_counts = df.groupby('CLIENT_ID')['SONG_ID'].nunique()

# Get the maximum number of distinct songs played
max_distinct_songs = user_song_counts.max()

# Print the result
print("Maximum number of distinct songs played:", max_distinct_songs)