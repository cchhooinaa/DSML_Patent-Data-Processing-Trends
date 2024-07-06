# 추출한 10개 토픽별 연도 분포_개별플롯
years = sorted(year_topic_dist.keys())
num_topics = len(year_topic_dist[years[0]])

# 토픽별 고유 색상 지정
colors = ['blue', 'orangered', 'gold', 'forestgreen', 'dodgerblue', 'darkviolet', 'deeppink', 'greenyellow', 'aqua', 'sienna']
cmap = ListedColormap(colors)

fig, axes = plt.subplots(nrows=num_topics, ncols=1, figsize=(12, num_topics*4), sharey=True)

for topic_id, ax in enumerate(axes.flat):
    values = [year_topic_dist[year][topic_id] for year in years]
    ax.plot(years, values, marker='o', color=colors[topic_id], label=f"Topic {topic_id+1}")
    ax.set_ylim(0, 1600)  # y축 범위 설정
    ax.set_xlabel('Year', fontsize=12)
    ax.set_ylabel('Proportion', fontsize=12)
    ax.set_title(f'Topic {topic_id+1} Evolution', fontsize=14)
    ax.legend(loc='upper left', fontsize=10)

    # x축 틱 라벨 설정
    ax.set_xticks(range(len(years)))
    ax.set_xticklabels(years, rotation=45, ha='right', fontsize=10)

plt.subplots_adjust(hspace=0.5)  # 서브플롯 간격 조정
plt.tight_layout()
plt.show()
