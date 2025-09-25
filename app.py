import streamlit as st
import pandas as pd

def main():
    """
    '경제활동_통합.csv' 파일을 읽어 Streamlit으로 서비스하는 메인 함수
    """
    # Streamlit 페이지 설정 (넓은 레이아웃)
    st.set_page_config(layout="wide")

    # 앱 제목
    st.title('📊 경제활동 데이터 대시보드')

    # 데이터 로딩 함수 (캐시 사용으로 성능 향상)
    @st.cache_data
    def load_data(filepath):
        """
        CSV 파일을 로드합니다. 한글 인코딩 문제를 처리합니다.
        """
        try:
            # UTF-8 인코딩으로 먼저 시도
            df = pd.read_csv(filepath, encoding='utf-8')
        except UnicodeDecodeError:
            # 실패 시 CP949(Windows 기본) 인코딩으로 시도
            df = pd.read_csv(filepath, encoding='cp949')
        return df

    file_path = '경제활동_통합.csv'

    try:
        # 데이터 로드
        data = load_data(file_path)

        st.header('📈 데이터 미리보기 (상위 10개)')
        st.dataframe(data.head(10))

        st.header('📄 데이터 기본 정보')
        st.write(f"전체 행: `{data.shape[0]}`개, 전체 열: `{data.shape[1]}`개")

        if st.checkbox('기초 통계량 보기'):
            st.subheader('기초 통계량')
            st.write(data.describe(include='all'))

    except FileNotFoundError:
        st.error(f"'{file_path}' 파일을 찾을 수 없습니다. `app.py`와 같은 폴더에 파일이 있는지 확인해주세요.")

if __name__ == "__main__":
    main()