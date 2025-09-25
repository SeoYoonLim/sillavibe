it_terms = {
    "AI": "인공지능 (Artificial Intelligence)",
    "ML": "머신러닝 (Machine Learning)",
    "DL": "딥러닝 (Deep Learning)",
    "Big Data": "빅데이터",
    "Cloud Computing": "클라우드 컴퓨팅",
    "IoT": "사물 인터넷 (Internet of Things)",
    "Blockchain": "블록체인",
    "Cybersecurity": "사이버 보안",
    "Data Science": "데이터 과학",
    "AR": "증강 현실 (Augmented Reality)",
    "VR": "가상 현실 (Virtual Reality)",
    "Edge Computing": "엣지 컴퓨팅",
    "Quantum Computing": "양자 컴퓨팅",
    "5G": "5세대 이동 통신",
    "API": "응용 프로그래밍 인터페이스 (Application Programming Interface)"
}

def get_it_term_definition(term):
    """IT 용어에 대한 정의를 반환합니다."""
    if term in it_terms:
        return it_terms[term]
    else:
        return "정의를 찾을 수 없습니다."

if __name__ == '__main__':
    while True:
        term = input("IT 용어를 입력하세요 (종료하려면 '종료'를 입력하세요): ")
        if term == "종료":
            break
        definition = get_it_term_definition(term)
        print(f"{term}: {definition}")