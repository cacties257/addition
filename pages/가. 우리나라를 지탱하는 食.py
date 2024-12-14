import streamlit as st
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

with st.sidebar:
    st.caption('위에서부터 순차적으로 클릭해주세요!')

# 폰트 설정
font_path = "NanumGothic.ttf"  # Windows의 일반적인 경로
font_manager.fontManager.addfont(font_path)
rc('font', family='NanumGothic')

# CSV 파일 불러오기
data = pd.read_csv("국내 시장 실적 추이.csv")

st.title('우리나라를 지탱하는 食')

st.write("")
st.write("")

st.markdown(" ## 식품 산업, 얼마나 대단하길래? ## ")

st.write("")

st.markdown('<p style="color:#96582a; font-size:24px;",> <strong> 우리나라 사람들이 특히 밥에 열광한다고들 해요. </strong> </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> 인사할 때는 "밥은 먹었냐?" 헤어질 때는 "나중에 밥이나 한 번 먹자"... </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> 식품은, 식품 산업은 우리나라에서 어느 정도의 의미를 가질까요? 그리고, 그것을 앞으로 수행할 식품첨가물 탐구와 어떻게 연결할 수 있을까요?</p>', unsafe_allow_html=True)

st.write("")

st.markdown('<p style="color:#96582a; font-size:20px;"><strong><span style="background-color: #fffde7;">우리나라의 식품 산업에 대해 알아볼 수 있는 그래프를 확인해봅시다.</span></strong></p>', unsafe_allow_html=True)
st.write("")
st.write("")


st.divider()


st.markdown(" ## 국내 식품시장 실적 그래프 ## ")

st.write("")

# 옵션 선택
option = st.selectbox('보고 싶은 데이터를 선택하세요:', ['생산량(T)', '생산액(억)', '매출액(억)'])
year_range = st.slider('보고 싶은 연도 범위를 선택하세요:', 2002, 2021, (2002, 2021))

# 선택한 범위로 데이터 필터링
filtered_data = data[(data['연도'] >= year_range[0]) & (data['연도'] <= year_range[1])]

# 색상 설정
def get_color(option):
    if option == '생산량(T)':
        return 'gold'
    elif option == '생산액(억)':
        return 'orange'
    elif option == '매출액(억)':
        return 'darkorange'

# 그래프 생성
chart = alt.Chart(filtered_data).mark_bar(color=get_color(option)).encode(
    x=alt.X('연도:O', title='연도'),
    y=alt.Y(option, title=option),
    tooltip=['연도', option]
).properties(
    title=f'국내 식품시장 실적 ({option})',
    width=700,
    height=400
)

# 그래프 출력
st.altair_chart(chart, use_container_width=True)


st.divider()


st.write("")

st.markdown(" ## 생각해볼 질문 ## ")

st.write("")

st.markdown("### Q1. 그래프에서 최근의 연도로 갈수록... ### ")

st.markdown('<p style="color:#96582a; font-size:18px;",> ▶ 생산량은 어떻게 변화하는 경향을 보였나요?</p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:18px;",> ▶ 생산액은 어떻게 변화하는 경향을 보였나요? </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:18px;",> ▶ 매출액은 어떻게 변화하는 경향을 보였나요?</p>', unsafe_allow_html=True)

st.write("")
st.write("")

st.markdown("### Q2. 식품 시장의 중요성 ### ")

st.markdown('<p style="color:#96582a; font-size:20px;",> <strong> ▶ Q1에서 답변한 내용을 참고하여, 우리나라의 식품 시장에서 어떤 일이 벌어지는지 주의 깊게 살펴보아야 하는 이유를 생각해 보고 한 문장으로 표현해봅시다.</strong> </p>', unsafe_allow_html=True)


st.write("")
st.write("")