import streamlit as st
import pandas as pd
import plotly.express as px

def main():
    """
    '경제활동_통합.csv' 파일을 읽어 Streamlit으로 서비스하는 메인 함수
    """
    # Streamlit 페이지 설정 (넓은 레이아웃)
    st.set_page_config(layout="wide")

    # 앱 제목
    st.title('📊 경제활동 데이터 대시보드')
    st.markdown("---")

    # 데이터 로딩 함수 (캐시 사용으로 성능 향상)
    @st.cache_data
    def load_data(filepath):
        """
        CSV 파일을 로드합니다. 한글 인코딩 문제를 처리합니다.
        """
        try:
            # BOM(Byte Order Mark)이 있는 CSV 파일을 위해 'utf-8-sig' 사용
            df = pd.read_csv(filepath, encoding='utf-8-sig')
        except UnicodeDecodeError:
            # 실패 시 CP949(Windows 기본) 인코딩으로 시도
            df = pd.read_csv(filepath, encoding='cp949')
        return df

    file_path = '경제활동_통합.csv'
    try:
        # 데이터 로드
        data = load_data(file_path)

        # --- 데이터 시각화 ---
        st.header("📈 데이터 시각화")

        # 연도 선택
        year_options = sorted(data['년도'].unique())
        selected_year = st.selectbox('확인할 연도를 선택하세요:', year_options, index=len(year_options)-1)

        # 선택된 연도의 데이터 필터링 ('계' 행 제외)
        yearly_data = data[(data['년도'] == selected_year) & (data['지역'] != '계')]

        # 1. 막대 그래프
        st.subheader(f"📊 {selected_year}년 지역별 취업자 및 실업자 수 (막대 그래프)")
        # 시각화를 위해 '지역'을 인덱스로 설정
        chart_data = yearly_data.set_index('지역')[['취업자 (천명)', '실업자 (천명)']]
        st.bar_chart(chart_data)

        # 2. 원형 그래프
        st.subheader(f"🌐 {selected_year}년 지역별 경제활동인구 비율 (원형 그래프)")
        if not yearly_data.empty:
            fig_pie = px.pie(yearly_data,
                             names='지역',
                             values='경제활동인구 (천명)',
                             title=f'{selected_year}년 지역별 경제활동인구 분포',
                             hole=.3) # 도넛 모양으로 만들기
            fig_pie.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig_pie, use_container_width=True)
        else:
            st.warning("해당 연도의 데이터가 없습니다.")

        # --- 상세 데이터 보기 ---
        st.markdown("---")
        if st.checkbox('상세 데이터 보기'):
            st.subheader('📄 상세 데이터')
            st.dataframe(data)
            st.info(f"전체 행: `{data.shape[0]}`개, 전체 열: `{data.shape[1]}`개")
            if st.checkbox('기초 통계량 보기'):
                st.write(data.describe(include='all'))

    except FileNotFoundError:
        st.error(f"'{file_path}' 파일을 찾을 수 없습니다. `app.py`와 같은 폴더에 파일이 있는지 확인해주세요.")

if __name__ == "__main__":
    main()