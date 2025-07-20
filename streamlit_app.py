import streamlit as st

st.title("🎈 My new app")  # 1. 페이지 제목

st.header("1. 헤더(Header)")  # 2. 헤더
st.subheader("1-1. 서브헤더(Subheader)")  # 3. 서브헤더
st.text("2. 일반 텍스트(Text)")  # 4. 일반 텍스트

st.markdown("3. **마크다운(Markdown)** _지원_")  # 5. 마크다운

st.code("print('Hello, Streamlit!')", language="python")  # 6. 코드 블록

st.latex(r"4. \LaTeX\ 수식: E=mc^2")  # 7. LaTeX 수식

st.write("5. write() 함수로 다양한 객체 출력")  # 8. write 함수

st.success("6. 성공 메시지(success)")  # 9. 성공 메시지
st.info("7. 정보 메시지(info)")  # 10. 정보 메시지
st.warning("8. 경고 메시지(warning)")  # 11. 경고 메시지
st.error("9. 에러 메시지(error)")  # 12. 에러 메시지
st.exception(Exception("10. 예외(exception)"))  # 13. 예외 메시지

st.image("https://streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", caption="11. 이미지(image) 예시")  # 14. 이미지

st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")  # 15. 오디오

st.video("https://www.youtube.com/watch?v=R2nr1uZ8ffc")  # 16. 비디오

st.checkbox("12. 체크박스(checkbox)")  # 17. 체크박스
st.radio("13. 라디오 버튼(radio)", ["옵션 1", "옵션 2"])  # 18. 라디오 버튼
st.selectbox("14. 셀렉트박스(selectbox)", ["A", "B", "C"])  # 19. 셀렉트박스
st.multiselect("15. 멀티셀렉트(multiselect)", ["Python", "Java", "C++"])  # 20. 멀티셀렉트

st.slider("16. 슬라이더(slider)", 0, 100, 50)  # 21. 슬라이더
st.number_input("17. 숫자 입력(number_input)", min_value=0, max_value=10, value=5)  # 22. 숫자 입력
st.text_input("18. 텍스트 입력(text_input)", "기본값")  # 23. 텍스트 입력
st.text_area("19. 텍스트 영역(text_area)", "여러 줄 입력")  # 24. 텍스트 영역
st.date_input("20. 날짜 입력(date_input)")  # 25. 날짜 입력
st.time_input("21. 시간 입력(time_input)")  # 26. 시간 입력
st.file_uploader("22. 파일 업로더(file_uploader)")  # 27. 파일 업로더
st.color_picker("23. 색상 선택(color_picker)", "#00f900")  # 28. 색상 선택

if st.button("24. 버튼(button)"):  # 29. 버튼
    st.write("버튼이 눌렸어요!")

st.progress(0.5)  # 30. 진행 바(progress)

import pandas as pd
df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6]
})
st.dataframe(df)  # 31. 데이터프레임(dataframe)
st.table(df)  # 32. 테이블(table)
st.json({"key": "value", "number": 123})  # 33. JSON

import numpy as np
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)  # 34. 선 그래프(line_chart)
st.area_chart(chart_data)  # 35. 영역 그래프(area_chart)
st.bar_chart(chart_data)  # 36. 막대 그래프(bar_chart)

st.sidebar.title("37. 사이드바(sidebar) 예시")  # 37. 사이드바

st.caption("각 요소 옆의 주석이 해당 요소의 이름입니다.")  # 38. 캡션

# 각주 예시
st.markdown("""
---
**각주**
1. 페이지 제목: st.title
2. 헤더: st.header
3. 서브헤더: st.subheader
4. 일반 텍스트: st.text
5. 마크다운: st.markdown
6. 코드 블록: st.code
7. LaTeX 수식: st.latex
8. write 함수: st.write
9. 성공 메시지: st.success
10. 정보 메시지: st.info
11. 경고 메시지: st.warning
12. 에러 메시지: st.error
13. 예외 메시지: st.exception
14. 이미지: st.image
15. 오디오: st.audio
16. 비디오: st.video
17. 체크박스: st.checkbox
18. 라디오 버튼: st.radio
19. 셀렉트박스: st.selectbox
20. 멀티셀렉트: st.multiselect
21. 슬라이더: st.slider
22. 숫자 입력: st.number_input
23. 텍스트 입력: st.text_input
24. 텍스트 영역: st.text_area
25. 날짜 입력: st.date_input
26. 시간 입력: st.time_input
27. 파일 업로더: st.file_uploader
28. 색상 선택: st.color_picker
29. 버튼: st.button
30. 진행 바: st.progress
31. 데이터프레임: st.dataframe
32. 테이블: st.table
33. JSON: st.json
34. 선 그래프: st.line_chart
35. 영역 그래프: st.area_chart
36. 막대 그래프: st.bar_chart
37. 사이드바: st.sidebar
38. 캡션: st.caption
""")