# IPL Data Analysis - Simple Summary

import pandas as pd
import matplotlib.pyplot as plt

# Load data
ipl = pd.read_csv("IPL_Matches.csv")

# Count wins by team
wins = ipl['winner'].value_counts()

print("Match Wins by Team:")
print(wins)

# Plot bar chart of wins
wins.plot(kind='bar', title='IPL Match Wins by Team')
plt.xlabel('Team')
plt.ylabel('Number of Wins')
plt.show()
