import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import random

with st.sidebar:
    st.caption('위에서부터 순차적으로 클릭해주세요!')

# CSV 파일 불러오기
data = pd.read_csv("국가별 기준 수.csv")
data2 = pd.read_csv("수출액.csv")

# 폰트 설정
font_path = "NanumGothic.ttf"  # Windows의 일반적인 경로
font_manager.fontManager.addfont(font_path)
rc('font', family='NanumGothic')


st.title("식품첨가물을 더 자세히 알아보자")

st.write("")
st.write("")

st.markdown(" ## 더 많은 자료가 필요해요! ## ")

st.write("")
st.markdown('<p style="color:#96582a; font-size:24px;",> <strong> 그렇다면 우리는 어떤 식품첨가물에 주목해야 할까요? </strong> </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> 앞선 페이지에서, 우리는 다양한 식품첨가물들에 대해 알아보았습니다. 몇몇 식품첨가물은 위험성이 제기되기도 했다는 것까지 확인해보았습니다. </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> 각각의 식품첨가물이 어떤 맥락에서 사용되는지, 세계의 식품 산업에서 어떤 식품들이 주목받고 있는지 추가적인 정보를 더 알고 나면 자신만의 관심 있는 식품첨가물을 골라보기에도 좋겠죠? </p>', unsafe_allow_html=True)


st.write("")

st.markdown('<p style="color:#96582a; font-size:20px;"><strong><span style="background-color: #fffde7;">식품 산업과 식품첨가물에 대한 그래프를 살펴보고 필요한 정보를 탐색해봅시다. </span></strong></p>', unsafe_allow_html=True)

st.write("")
st.write("")

st.divider()

st.markdown(" ## 1. 국가별 식품첨가물 규제 기준 수 ## ")

st.write("")

st.markdown('<p style="color:#96582a; font-size:20px;",> 이 그래프는 세계 각 국가에서 다양한 유형의 식품에 부여하는 식품첨가물 규제기준의 수를 보여줍니다. 국가를 선택하면, 어떤 식품첨가물을 규제기준으로 엄격히 관리하는지 살펴볼 수 있습니다. </p>', unsafe_allow_html=True)

st.write("")
st.write("")

# 국가 선택
countries = data['나라'].unique()
selected_country = st.selectbox("보고 싶은 국가를 선택하세요:", countries)


# 선택한 국가의 데이터 필터링
filtered_data = data[data['나라'] == selected_country]

# 식품첨가물 종류별 데이터 개수 세기
additive_counts = filtered_data['식품첨가물'].value_counts()

# 그래프 생성
fig, ax = plt.subplots(figsize=(10, 6))

# 막대 그래프 색상을 랜덤으로 지정
colors = ["#%06x" % random.randint(0, 0xFFFFFF) for _ in range(len(additive_counts))]
ax.bar(additive_counts.index, additive_counts.values, color=colors)

# 그래프 범주 설정
ax.set_title(f"{selected_country}의 식품첨가물 규제 수 분포", fontsize=16)
ax.set_xlabel("식품첨가물 종류", fontsize=12)
ax.set_ylabel("규제 개수", fontsize=12)
ax.tick_params(axis='x', rotation=45)

# 그래프 표시
st.pyplot(fig)

st.divider()

st.markdown(" ## 2. 식품 유형별 해외 대상 수출액 ## ")

st.write("")

st.markdown('<p style="color:#96582a; font-size:20px;",> 이 그래프는 우리나라에서 해외로 수출하는 식품의 수출액을 식품의 종류에 따라서 보여줍니다. 식품 유형과 국가를 선택하면, 2017년부터 2022년까지 수출액의 변동을 살펴볼 수 있습니다. </p>', unsafe_allow_html=True)

st.write("")
st.write("")

# 산업 분류 선택
industries = data2['산업분류'].unique()
selected_industry = st.selectbox("식품 유형을 선택하세요: ", industries)

# 국가 선택 (다중 선택 가능)
countries = data2['국가'].unique()
selected_countries = st.multiselect("국가를 선택하세요: ", countries)


# 선택한 산업 분류와 국가에 따른 데이터 필터링
filtered_data = data2[(data2['산업분류'] == selected_industry) & (data2['국가'].isin(selected_countries))]

# 선택한 열들 (년도별 값) 추출
years = ['2017', '2018', '2019', '2020', '2021', '2022']

# 그래프 생성
fig, ax = plt.subplots(figsize=(10, 6))

# 국가별로 꺾은 선 그래프 그리기
for country in selected_countries:
    country_data = filtered_data[filtered_data['국가'] == country]
    if not country_data.empty:
        ax.plot(years, country_data[years].values.flatten(), label=country)

# 그래프 범주 설정
ax.set_title(f"{selected_industry} - 국가별 년도별 숫자 값", fontsize=16)
ax.set_xlabel("년도", fontsize=12)
ax.set_ylabel("숫자 값", fontsize=12)
ax.legend(title="국가")

# 그래프 표시
st.pyplot(fig)

st.divider()

st.markdown(" ## 생각해볼 질문 ## ")

st.write("")

st.markdown("### Q1. 국가 별 식품첨가물 규제 기준 수 ### ")

st.markdown('<p style="color:#96582a; font-size:18px;",> ▶ 우리나라에서 가장 규제 기준이 많은 식품첨가물에는 어떤 것이 있나요? </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:18px;",> ▶ 규제 기준의 수가 많다는 것은 어떤 의미로 해석할 수 있을까요? </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> <strong> ▶ 이 자료를 탐구 대상 선정에 어떻게 활용하면 좋을까요?</strong> </p>', unsafe_allow_html=True)

st.write("")
st.write("")

st.markdown("### Q2. 식품 유형별 해외 대상 수출액 ### ")

st.markdown('<p style="color:#96582a; font-size:18px;",> ▶ 수출액 규모가 가장 큰 나라는 어디인가요? </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:18px;",> ▶ 식품첨가물 유형의 수출액은 최근에 가까워질수록 어떻게 변하고 있나요?  </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> <strong> ▶ 이 자료를 탐구 대상 선정에 어떻게 활용하면 좋을까요?</strong> </p>', unsafe_allow_html=True)

st.write("")
st.write("")