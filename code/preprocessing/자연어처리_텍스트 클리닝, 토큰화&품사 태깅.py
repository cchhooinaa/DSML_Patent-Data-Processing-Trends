def clean_text(text):
    text = re.sub(r'[^가-힣\s]', '', text)  # 한글과 공백을 제외한 모든 문자 제거
    return text

cleaned_patents = []
for title, abstract in patents:
    cleaned_title = clean_text(title)
    cleaned_abstract = clean_text(abstract)
    cleaned_patents.append((cleaned_title, cleaned_abstract))

okt = Okt()
tokenized_patents = [[token for token, pos in okt.pos(title + ' ' + abstract) if pos.startswith(('N', 'V', 'A'))] for title, abstract in cleaned_patents]
