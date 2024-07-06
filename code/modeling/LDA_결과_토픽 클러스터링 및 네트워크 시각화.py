def get_word(word_id):
    # 단어 ID를 받아 실제 단어 반환
    return dictionary.get(word_id)

def get_topic_words(topic_id, top_n=10):
    # 주어진 토픽 ID에 대해 상위 top_n개의 단어 반환
    topic_words = lda_model.get_topic_terms(topic_id, topn=top_n)
    return [get_word(word_id) for word_id, prob in topic_words]

def get_topic_word_dist(lda_model, top_n=10):
    # LDA 모델의 토픽-단어 분포 매트릭스를 생성
    num_topics = lda_model.num_topics
    vocab_size = len(lda_model.id2word)
    topic_word_dist = np.zeros((num_topics, vocab_size))
    for topic_id in range(num_topics):
        top_words = get_topic_words(topic_id, top_n)
        for word in top_words:
            word_id = lda_model.id2word.token2id.get(word, -1)
            if word_id != -1:
                topic_word_dist[topic_id, word_id] = 1
    return topic_word_dist

# 토픽-단어 분포 매트릭스 생성 (상위 10개 단어만 고려)
topic_word_dist = get_topic_word_dist(lda_model, top_n=10)

# k-means 클러스터링 수행
num_clusters = 5  # 클러스터 수 설정
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
cluster_assignments = kmeans.fit_predict(topic_word_dist)

# 클러스터별 토픽 출력
for cluster_id in range(num_clusters):
    cluster_topics = [i for i, c in enumerate(cluster_assignments) if c == cluster_id]
    print(f'Cluster {cluster_id}:')
    for topic_id in cluster_topics:
        top_words = get_topic_words(topic_id, top_n=5)
        print(f'  Topic {topic_id+1}: {", ".join(top_words)}')
    print()

# 클러스터 정보를 딕셔너리로 변환
cluster_dict = {}
for cluster_id in range(num_clusters):
    cluster_topics = [i for i, c in enumerate(cluster_assignments) if c == cluster_id]
    cluster_dict[cluster_id] = cluster_topics

# 네트워크 생성
G = nx.Graph()

# 노드 추가 (토픽 번호 = 노드 번호)
for topic_id in range(lda_model.num_topics):
    for cluster_id, topic_list in cluster_dict.items():
        if topic_id in topic_list:
            G.add_node(topic_id+1, label=f"Topic {topic_id+1}", cluster=cluster_id)
            break

# 엣지 추가 (토픽 간 유사도 기반)
for i in range(lda_model.num_topics):
    for j in range(i+1, lda_model.num_topics):
        similarity = np.dot(topic_word_dist[i], topic_word_dist[j]) / (np.linalg.norm(topic_word_dist[i]) * np.linalg.norm(topic_word_dist[j]))
        G.add_edge(i+1, j+1, weight=similarity)

# 클러스터별 노드 색상 설정
cluster_colors = {0: 'r', 1: 'g', 2: 'b', 3: 'c', 4: 'm'}
node_colors = [cluster_colors[G.nodes[node]['cluster']] for node in G.nodes()]

# 네트워크 시각화
pos = nx.spring_layout(G, k=0.5, iterations=50)
nx.draw(G, pos, with_labels=True, font_size=8, node_color=node_colors)
plt.show()
