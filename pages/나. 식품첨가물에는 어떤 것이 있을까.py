import streamlit as st

with st.sidebar:
    st.sidebar.caption('위에서부터 순차적으로 클릭해주세요!')

st.title("식품첨가물에는 어떤 것이 있을까")

st.write("")
st.write("")

st.markdown(" ## 식품첨가물의 유형 ## ")

st.write("")

st.markdown('<p style="color:#96582a; font-size:24px;",> <strong> 맛있는 음식을 하나 만들더라도 여러 가지 요소를 고려해야 한답니다. </strong> </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> 색도 먹음직스럽게 바꿔야 하고, 맛도 심심하지 않게 유지해야 하고, 배송하고 보관하면서 오래 둬도 상하지 않도록 해야 하고... </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> 식품첨가물은 구체적으로 어떤 역할들을 수행할까요? 또 각각의 유형에 해당하는 식품첨가물로 어떤 것들이 있을까요?</p>', unsafe_allow_html=True)

st.write("")

st.markdown('<p style="color:#96582a; font-size:20px;"><strong><span style="background-color: #fffde7;">식품첨가물의 유형에 대해서 상세히 알아봅시다. </span></strong></p>', unsafe_allow_html=True)
st.write("")
st.write("")


st.divider()


st.markdown(" ### :stew: 향미증진제 ### ")

st.write("")

st.image("향미증진제.jpg")
st.write("")
st.markdown('<p style="color:#96582a; font-size:20px;",> 식품의 맛이나 풍미를 증진시키기 위해 사용되는 식품 첨가물.</span> </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> 대표적으로 <span style="background-color: #fffde7;">조미료, 냉동어묵</span> 등에 사용된다. </p>', unsafe_allow_html=True)
st.write("")
st.markdown('<p style="color:#96582a; font-size:20px;"><strong>▶ MSG, 5-이노신산이나트륨 등</span></strong></p>', unsafe_allow_html=True)

st.write("")
st.write("")


st.divider()


st.markdown(" ### :lollipop: 감미료 ### ")

st.write("")

st.image("감미료.jpg")
st.write("")
st.markdown('<p style="color:#96582a; font-size:20px;",> 식품에 단맛을 부여하는 식품첨가물. </span> </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> 대표적으로 <span style="background-color: #fffde7;">청량음료, 유산균음료, 발효유, 잼, 과자, 빙과류</span> 등에 사용된다. </p>', unsafe_allow_html=True)
st.write("")
st.markdown('<p style="color:#96582a; font-size:20px;"><strong>▶ 아스파탐, 사카린나트륨, 자일리톨 등</span></strong></p>', unsafe_allow_html=True)

st.write("")
st.write("")


st.divider()


st.markdown(" ### :glass_of_milk: 표백제 ### ")

st.write("")

st.image("표백제.jpg")
st.write("")
st.markdown('<p style="color:#96582a; font-size:20px;",> 식품이 가지고 있는 기존의 색을 제거하기 위해 사용되는 식품첨가물. </span> </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> 대표적으로 <span style="background-color: #fffde7;">와인, 말린 과일, 과자, 빵, 빙과류</span> 등에 사용된다. </p>', unsafe_allow_html=True)
st.write("")
st.markdown('<p style="color:#96582a; font-size:20px;"><strong>▶ 아황산나트륨, 차아황산나트륨, 무수아황산 등</span></strong></p>', unsafe_allow_html=True)

st.write("")
st.write("")


st.divider()


st.markdown(" ### :meat_on_bone: 발색제 ### ")

st.write("")

st.image("발색제.jpg")
st.write("")
st.markdown('<p style="color:#96582a; font-size:20px;",> 식품의 색을 안정화시키거나, 유지 또는 강화시키는 식품첨가물. </span> </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> 대표적으로 <span style="background-color: #fffde7;">햄, 소시지, 어류 제품</span> 등에 사용된다. </p>', unsafe_allow_html=True)
st.write("")
st.markdown('<p style="color:#96582a; font-size:20px;"><strong>▶ 아질산나트륨, 질산칼륨, 질산나트륨 등</span></strong></p>', unsafe_allow_html=True)

st.write("")
st.write("")


st.divider()


st.markdown(" ### :art: 착색료 ### ")

st.write("")

st.image("착색료.jpg")
st.write("")
st.markdown('<p style="color:#96582a; font-size:20px;",> 식품에 색을 부여하거나 복원시키는 식품 첨가물. </span> </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> 대표적으로 <span style="background-color: #fffde7;">치즈, 버터, 과자, 빙과류, 소세지, 통조림 육류</span> 등에 사용된다. </p>', unsafe_allow_html=True)
st.write("")
st.markdown('<p style="color:#96582a; font-size:20px;"><strong>▶ 캐러멜 색소, 타르색소 등 식용 색소</span></strong></p>', unsafe_allow_html=True)

st.write("")
st.write("")


st.divider()


st.markdown(" ### :ice_cube: 보존료 ### ")

st.write("")

st.image("보존료.jpg")
st.write("")
st.markdown('<p style="color:#96582a; font-size:20px;",> 식품이 품질 저하되는 것을 방지하고 보존 기간을 연장하는 식품 첨가물. </span> </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> 대표적으로 <span style="background-color: #fffde7;">빵, 소세지, 치즈, 어묵, 단무지, 오이지</span> 등에 사용된다. </p>', unsafe_allow_html=True)
st.write("")
st.markdown('<p style="color:#96582a; font-size:20px;"><strong>▶ 프로피온산, 소르빈산, 데히드로초산, 안식향산 등</span></strong></p>', unsafe_allow_html=True)

st.write("")
st.write("")


st.divider()


st.markdown(" ### :ice_cream: 유화제 ### ")

st.write("")

st.image("유화제.jpg")
st.write("")
st.markdown('<p style="color:#96582a; font-size:20px;",> 물과 기름처럼 섞이지 않는 재료를 균질하게 섞어주는 식품첨가물. </span> </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> 대표적으로 <span style="background-color: #fffde7;">마가린, 쇼트닝, 케이크, 껌, 초콜릿, 빙과류, 두부, 케첩</span> 등에 사용된다. </p>', unsafe_allow_html=True)
st.write("")
st.markdown('<p style="color:#96582a; font-size:20px;"><strong>▶ 카제인나트륨, 글리세린지방산에스테르, 레시틴 등</span></strong></p>', unsafe_allow_html=True)

st.write("")
st.write("")


st.divider()

st.markdown(" ## 식품첨가물의 위험성 ## ")

st.write("")

st.markdown('<p style="color:#96582a; font-size:24px;",> <strong> 우리가 먹는 음식에 쓰이는 식품첨가물은 안전할까요? </strong> </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> 물론, 식품첨가물은 개발 과정에서 그 유해성을 엄격하게 테스트해요. 자연에서 유래된 천연먹거리라고 해서 사람이 먹기에 다 안전한 것도 아니죠. 자연에도 독을 가진 동식물들이 있으니까요. </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> 그렇지만 사람들이 오랜 시간 동안 소비하며 안전성을 몸으로 검증해온 천연먹거리와 달리 식품첨가물이 사용된 가공 식품은 최근 들어 개발되고 판매되기 시작한 것이 많아요. </p>', unsafe_allow_html=True)

st.write("")

st.markdown('<p style="color:#96582a; font-size:20px;"><strong><span style="background-color: #fffde7;"> 식품첨가물의 위험성에 대한 기사를 읽으며, 탐구 대상 선정에 참고해봅시다. </span></strong></p>', unsafe_allow_html=True)
st.write("")
st.write("")

st.divider()

st.markdown(" ### 식품첨가물 위험성 관련 뉴스 ### ")

st.write("")

st.write("각 뉴스 제목을 클릭하면 뉴스를 읽을 수 있답니다.")

st.write("")
st.write("")

st.markdown(
    '<a href="https://www.medicaltimes.com/Main/News/NewsView.html?ID=1160037" style="text-decoration: none; color: #c9a537; font-size: 24px;"><strong> ▶인공감미료 수난... 발암 논란 이어 혈전증 위험 부상</strong></a>',
    unsafe_allow_html=True)
st.markdown(
    '<a href="https://www.assemblyinsider.com/news/articleView.html?idxno=1359" style="text-decoration: none; color: #c9a537; font-size: 24px;"><strong> ▶[칼럼] 햄·소시지 첨가물 ‘아질산나트륨’, 자살위해물건에 등재된다고?</strong></a>',
    unsafe_allow_html=True)
st.markdown(
    '<a href="https://www.donga.com/news/Society/article/all/20241010/130190014/1" style="text-decoration: none; color: #c9a537; font-size: 24px;"><strong> ▶아이들은 사달라 조르는데… 젤리 70%, "타르색소" 사용 </strong></a>',
    unsafe_allow_html=True)

st.write("")
st.write("")
