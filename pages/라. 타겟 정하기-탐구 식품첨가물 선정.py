import streamlit as st

with st.sidebar:
    st.caption('위에서부터 순차적으로 클릭해주세요!')

st.title("타겟 정하기- 탐구 식품첨가물 선정")

st.write("")
st.write("")

st.markdown(" ## 내가 조사하고 싶은 식품첨가물은... ## ")

st.write("")
st.markdown('<p style="color:#96582a; font-size:20px;",> 식품 산업과 식품첨가물에 대한 다양한 자료를 살펴보았습니다. 하지만 자료를 그저 살펴보고 만족하기만 해서는 안됩니다. 적절한 지점에서 활용할 수 있어야 시간을 들여 자료를 살펴본 보람도 생기겠죠? </p>', unsafe_allow_html=True)
st.markdown('<p style="color:#96582a; font-size:20px;",> 아직 어떤 식품첨가물에 자신의 관심사를 연결할 수 있을지 모르겠다면, 추가적인 정보나 자료를 더 찾아보아도 좋습니다. </p>', unsafe_allow_html=True)


st.write("")

st.markdown('<p style="color:#96582a; font-size:20px;"><strong><span style="background-color: #fffde7;">살펴본 자료와 추가로 조사한 자료를 바탕으로 탐구 대상을 선정해봅시다. </span></strong></p>', unsafe_allow_html=True)

st.write("")
st.write("")

st.divider()

with st.form("exploration_form"):
        # 1. 탐구하고 싶은 식품첨가물 서술형 입력
        st.markdown("탐구 대상")
        additive_to_explore = st.text_input("탐구하고 싶은 식품첨가물")

        st.write("")

        # 2. 탐구 자료 선택
        st.markdown("탐구하고 싶은 식품첨가물을 정하는 데에 사용한 그래프 혹은 자료")
        selected_graphs = st.multiselect(
            "사용한 자료를 선택하세요", 
            ["식품첨가물 위험성 관련 뉴스","국가별 식품첨가물 규제 기준 수", "식품 유형별 해외 대상 수출액", "기타 자료"]
        )
        other_graph_description = ""
        if "기타 자료" in selected_graphs:
            other_graph_description = st.text_input("기타 자료에 대한 설명을 작성하세요")

        st.write("")

        # 3. 탐구 선정 이유 작성
        st.markdown("탐구 대상 선정 이유")
        exploration_reason = st.text_area(
            "2번에서 답한 그래프 혹은 자료를 바탕으로 해당 식품첨가물을 탐구 대상으로 선정한 이유를 구체적으로 작성해주세요.")

        # 4. 제출 버튼
        submitted = st.form_submit_button("제출")

        if submitted:
            if not additive_to_explore.strip():
                st.warning("탐구하고 싶은 식품첨가물을 작성해주세요.")
            elif not selected_graphs:
                st.warning("사용한 자료를 하나 이상 선택해주세요.")
            elif "기타 자료" in selected_graphs and not other_graph_description.strip():
                st.warning("기타 자료를 선택한 경우, 설명을 작성해주세요.")
            elif not exploration_reason.strip():
                st.warning("탐구 선정 이유를 작성해주세요.")
            else:
                st.success("제출되었습니다!")

st.write("")
st.write("")

st.markdown('<p style="color:#96582a; font-size:20px;"><strong><span style="background-color: #fffde7;">오늘의 수업 끝! 수고했습니다😀 </span></strong></p>', unsafe_allow_html=True)

st.write("")
st.write("")