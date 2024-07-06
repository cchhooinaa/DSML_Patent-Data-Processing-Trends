# pyLDAvis 준비
vis_data = gensimvis.prepare(lda_model, corpus, dictionary)
pyLDAvis.display(vis_data)

# get_word 함수 정의
def get_word(word_id):
    return dictionary.get(word_id)

# 토픽 번호를 실제 단어로 변환하는 함수
def get_topic_words(topic_id, top_n=10):
    topic_words = lda_model.get_topic_terms(topic_id, topn=top_n)
    return [get_word(word_id) for word_id, prob in topic_words]

import matplotlib.pyplot as plt
plt.rc('font', family='NanumBarunGothic')
plt.rcParams['axes.unicode_minus'] =False

# 모든 토픽에 대해 상위 단어들을 리스트로 출력
for topic_id in range(lda_model.num_topics):
    print(f"Topic {topic_id+1}:")
    topic_words = get_topic_words(topic_id)
    print(", ".join(topic_words))
    print()

plt.figure(figsize=(20, 15))
for topic_id in range(lda_model.num_topics):
    topic_words = get_topic_words(topic_id)

    if not topic_words:
        print(f"Skipping Topic {topic_id} (no words assigned)")
        continue

    wordcloud = WordCloud(width=400, height=300, background_color='white', font_path='/content/NanumGothic.otf').generate(' '.join(topic_words))

    plt.subplot(lda_model.num_topics // 3 + 1, 3, topic_id + 1)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Topic {topic_id+1}')

plt.tight_layout()
plt.show()
