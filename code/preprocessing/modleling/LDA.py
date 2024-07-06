# LDA 토픽 모델링 (토픽 수 범위 지정)
topic_range = range(10, 16)  # 토픽 수 범위 (10부터 15까지)
coherence_scores = []

for num_topics in topic_range:
    lda_model = LdaModel(corpus, num_topics=num_topics, id2word=dictionary)

    # 코히어런스 스코어 계산
    coherence_model = CoherenceModel(model=lda_model, texts=filtered_patents, dictionary=dictionary, coherence='c_v')
    coherence_score = coherence_model.get_coherence()
    coherence_scores.append(coherence_score)

    print(f"Number of Topics: {num_topics}, Coherence Score: {coherence_score:.4f}")

dictionary = corpora.Dictionary(filtered_patents)
corpus = [dictionary.doc2bow(text) for text in filtered_patents]

# LDA 모델 생성 시 랜덤 시드 설정
lda_model = LdaModel(corpus, num_topics=10, id2word=dictionary, random_state=42)

# 토픽 출력
num_topics = 10  # 출력할 토픽의 수
num_words = 10  # 각 토픽에서 출력할 단어의 수

for idx, topic in lda_model.print_topics(num_topics=num_topics, num_words=num_words):
    print(f"Topic {idx+1}: {topic}")

# 모델 성능 평가
from gensim.models import CoherenceModel

# 코히어런스 모델 초기화
coherence_model = CoherenceModel(model=lda_model, texts=filtered_patents, dictionary=dictionary, coherence='c_v')

# 코히어런스 점수 계산
coherence_score = coherence_model.get_coherence()

print(f'Coherence Score: {coherence_score:.4f}')
