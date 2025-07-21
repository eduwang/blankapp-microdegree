import streamlit as st
import pandas as pd
import numpy as np
import time

st.title("📊 데이터 시각화 예시 모음")

# 1. 지도 기반 위치 시각화 예시
st.header("1. 지도 기반 위치 시각화")
# 임의의 위도/경도 데이터 생성
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.5665, 126.9780],  # 서울 중심 좌표 근처
    columns=['lat', 'lon']
)
st.map(map_data)  # 지도에 데이터 표시

st.divider()  # 구분선

# 2. CSV 파일 업로드 및 시각화 예시
st.header("2. CSV 파일 업로드 및 시각화")
uploaded_file = st.file_uploader("CSV 파일을 업로드하세요.", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)  # CSV 파일 읽기
    st.write("데이터 미리보기:")
    st.dataframe(df)  # 데이터프레임 표시
    # 컬럼이 2개 이상이면 간단한 차트도 표시
    if df.shape[1] >= 2:
        st.line_chart(df)  # 라인 차트로 시각화

st.divider()

# 3. 난수 스트리밍을 시뮬레이션한 실시간 라인 차트
st.header("3. 실시간 난수 스트리밍 라인 차트")
chart_placeholder = st.empty()  # 차트가 표시될 자리
data = pd.DataFrame(np.random.randn(1, 3), columns=["가", "나", "다"])  # 초기 데이터

for i in range(50):  # 50번 반복(실시간처럼 보이게)
    new_row = pd.DataFrame(np.random.randn(1, 3), columns=["가", "나", "다"])
    data = pd.concat([data, new_row], ignore_index=True)  # 데이터 추가
    chart_placeholder.line_chart(data)  # 차트 업데이트
    time.sleep(0.1)  # 0.1초 대기

st.caption("각 예시는 주석과 함께 제공됩니다.")  # 각 예시 옆에 주석 추가