# 10개 토픽별 비율 연도 분포
years = sorted(list(year_topic_dist.keys()))
num_topics = len(year_topic_dist[years[0]])

# 토픽별 고유 색상 지정
colors = ['blue', 'orangered', 'gold', 'forestgreen', 'dodgerblue', 'darkviolet', 'deeppink', 'greenyellow', 'aqua', 'sienna']
cmap = ListedColormap(colors)

plt.figure(figsize=(16, 6))

for i in range(num_topics):
    topic_proportions = [year_topic_dist[year][i] for year in years]
    plt.plot(years, topic_proportions, marker='o', linestyle='-', color=colors[i], label=f'Topic {i+1}')

plt.xlabel('Year')
plt.ylabel('Proportion')
plt.title('Topic Distribution by Year')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
