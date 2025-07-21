import streamlit as st
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
import numpy as np

# NanumGothic 폰트 경로 지정 및 설정
font_path = './fonts/NanumGothic-Regular.ttf'
fontprop = font_manager.FontProperties(fname=font_path)
matplotlib.rc('font', family=fontprop.get_name())
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지

# 데이터 예시
과일 = ['사과', '바나나', '포도', '딸기']
수량 = [10, 15, 7, 12]

# Streamlit 제목
st.title("과일 판매량 그래프")

# Matplotlib 그래프
fig, ax = plt.subplots()
bars = ax.bar(과일, 수량, color='skyblue')
ax.set_ylabel('판매 수량', fontproperties=fontprop)
ax.set_title('과일별 판매량', fontproperties=fontprop)
ax.set_xticklabels(과일, fontproperties=fontprop) 



# 값 표시
for bar, qty in zip(bars, 수량):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), str(qty),
            ha='center', va='bottom', fontsize=12, fontproperties=fontprop)

# Streamlit에 그래프 출력
st.pyplot(fig)