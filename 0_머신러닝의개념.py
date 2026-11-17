import streamlit as st

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning('🔒 로그인 후 이용 가능한 페이지입니다. 랜딩페이지에서 로그인을 진행해주세요.')
    st.stop()

st.set_page_config(page_title="머신러닝의 개념", page_icon="🧠")
st.markdown('''
<style>
.title-box { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 15px; text-align: center; color: white; margin-bottom: 30px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
.title-box h1 { color: white; margin: 0; }
.content-box { background-color: #f8f9fa; border-left: 5px solid #764ba2; padding: 20px; border-radius: 5px; margin-bottom: 20px; color: #333; }
</style>
''', unsafe_allow_html=True)
st.markdown('<div class="title-box"><h1>🧠 머신러닝(Machine Learning)이란?</h1></div>', unsafe_allow_html=True)
st.markdown('<div class="content-box"><h3>기계가 스스로 학습한다!</h3><p>기존의 프로그램은 개발자가 직접 모든 <b>규칙(Rule)</b>을 코드로 작성해야 했습니다.<br>하지만 머신러닝은 기계에게 수많은 <b>데이터(Data)</b>를 제공하고, 기계가 그 데이터 속에서 <b>스스로 패턴과 규칙을 찾아내도록 학습</b>시키는 인공지능의 한 분야입니다.</p></div>', unsafe_allow_html=True)
st.divider()
st.subheader("💡 머신러닝의 3가지 주요 학습 방법")
st.info("**1. 지도 학습 (Supervised Learning)**\n\n문제와 함께 **정답(Label)**을 알려주고 학습시키는 방법입니다. 새로운 데이터가 주어졌을 때 정답을 예측하는 데 사용됩니다.\n* **예시:** 스팸 메일 분류, 이미지 인식(강아지/고양이 분류)")
st.warning("**2. 비지도 학습 (Unsupervised Learning)**\n\n정답 없이 **데이터만** 주고, 기계가 스스로 데이터의 패턴, 형태, 특징을 찾아 무리를 짓게(군집화) 하는 방법입니다.\n* **예시:** 쇼핑몰 고객 군집 분석, 뉴스 기사 토픽 분류")
st.success("**3. 강화 학습 (Reinforcement Learning)**\n\n기계(에이전트)가 주어진 환경에서 어떤 행동을 했을 때 **보상(Reward)**이나 **벌점(Penalty)**을 주어, 가장 큰 보상을 받는 최적의 행동 순서를 스스로 깨우치게 하는 방법입니다.\n* **예시:** 알파고(바둑 AI), 자율주행 자동차, 로봇 제어")
