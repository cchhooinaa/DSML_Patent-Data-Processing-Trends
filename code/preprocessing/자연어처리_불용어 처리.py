from collections import defaultdict

# 전체 코퍼스에서 단어 빈도수 계산
word_counts = defaultdict(int)
for tokens in tokenized_patents:
    for token in tokens:
        word_counts[token] += 1

# 상위 N개 고빈도 단어 출력
top_n = 100
frequent_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:top_n]
frequent_words = [word for word, count in frequent_words]
print(frequent_words)

# 고빈도 단어 결과 참고하여 불용어 추가 선정
stopwords = ['본', '발명', '은', '는', '이', '가', '의', '에', '을', '를', '것', '에서', '수', '등', '된', '및',
             '종', '와', '한', '하기', '위한', '경우', '있는', '있다', '대한', '하다', '되다', '하는', '대해', '되는', '위해', '관련',
             '상기', '제', '하여', '포함', '단계', '본', '것', '한다', '할', '생', '하나', '된다', '위', '관', '복수', '부', '또는', '적어도', '로부터',
             '될', '중', '통해', '예', '되어', '이상', '다',  '그', '함', '일', '층', '상', '출', '검', '점', '의해', '되고', '성하는']

# 도메인 특화된 불용어 사전 추가
domain_stopwords = ['특허', '기술', '장치', '방법', '시스템', '구성', '이용',  '기반', '순서도', '도면', '예시', '실시', '다양', '적용',
                    '데이터', '값', '하우', '징', '획득', '결과', '제공', '정보']
stopwords.extend(domain_stopwords)

filtered_patents = []
for tokens in tokenized_patents:
    filtered_tokens = [token for token in tokens if token not in stopwords]
    filtered_patents.append(filtered_tokens)

corpus = [' '.join(tokens) for tokens in filtered_patents]
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(corpus)

dictionary = corpora.Dictionary(filtered_patents)
corpus = [dictionary.doc2bow(text) for text in filtered_patents]
