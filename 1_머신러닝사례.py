import streamlit as st

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning('🔒 로그인 후 이용 가능한 페이지입니다. 랜딩페이지에서 로그인을 진행해주세요.')
    st.stop()

st.set_page_config(page_title="머신러닝의 사례", page_icon="🌟")
st.title("🌟 우리 일상 속 머신러닝 사례")
st.write("머신러닝 기술은 이미 우리 생활 곳곳에서 편리함을 제공하고 있습니다. 다양한 활용 사례를 알아보겠습니다.")
st.divider()
col1, col2 = st.columns(2)
with col1:
    st.header("🛒 1. 맞춤형 추천 시스템")
    st.image("https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?w=400", use_container_width=True)
    st.write("유튜브, 넷플릭스, 쇼핑몰 등에서 사용자의 과거 시청 및 구매 데이터를 분석하여 **사용자 취향에 딱 맞는 콘텐츠나 상품을 추천**합니다.")
    st.header("🗣️ 2. 음성 인식 및 인공지능 비서")
    st.image("https://images.unsplash.com/photo-1589254065878-42c9da997008?w=400", use_container_width=True)
    st.write("스마트폰의 Siri, Bixby와 같이 사람의 음성을 텍스트로 변환하고 그 의미를 파악하여 **사용자의 명령을 수행하거나 대화**합니다.")
with col2:
    st.header("🚗 3. 자율주행 자동차")
    st.image("https://images.unsplash.com/photo-1469854523086-cc02fe5d8800?w=400", use_container_width=True)
    st.write("수많은 센서와 카메라로 수집된 주행 데이터를 학습하여, 사람의 개입 없이 기계 스스로 장애물을 피하고 **안전한 주행 경로를 결정**합니다.")
    st.header("🩺 4. 의료 진단 보조")
    st.image("https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=400", use_container_width=True)
    st.write("X-ray, MRI, CT 등의 수만 장의 의료 영상을 학습하여, 의사의 육안으로 발견하기 힘든 **미세한 질병(예: 암 종양)을 빠르고 정확하게 진단**하도록 돕습니다.")
st.divider()
st.info("이 외에도 번역기, 스팸 필터링, 주가 예측, 챗봇(ChatGPT 등) 수많은 분야에서 머신러닝이 핵심 기술로 활약하고 있습니다.")
