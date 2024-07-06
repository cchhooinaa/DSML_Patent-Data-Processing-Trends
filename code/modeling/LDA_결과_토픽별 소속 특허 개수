# 문서-토픽 분포 구하기
doc_topic_dist = lda_model.get_document_topics(corpus)

# 토픽별 문서 수 계산
topic_doc_counts = [0] * lda_model.num_topics
for doc_topics in doc_topic_dist:
    for topic_id, prob in doc_topics:
        topic_doc_counts[topic_id] += 1

# 시각화
topics = range(1, lda_model.num_topics+1)
doc_counts = topic_doc_counts

# 토픽별 고유 색상 지정
colors = ['blue', 'orangered', 'gold', 'forestgreen', 'dodgerblue', 'darkviolet', 'deeppink', 'greenyellow', 'aqua', 'sienna']
cmap = ListedColormap(colors)

plt.figure(figsize=(10, 6))
bars = plt.bar(topics, doc_counts, color=colors)

for bar in bars:
    height = bar.get_height()
    plt.gca().annotate('{}'.format(int(height)),
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3),
                       textcoords="offset points",
                       ha='center', va='bottom')

plt.xlabel('Topic', fontsize=12)
plt.ylabel('Document Count', fontsize=12)
plt.title('Topic Distribution', fontsize=16)
plt.show()
