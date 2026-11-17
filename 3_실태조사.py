import streamlit as st

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning('🔒 로그인 후 이용 가능한 페이지입니다. 랜딩페이지에서 로그인을 진행해주세요.')
    st.stop()

import sys
import os
# 상위 디렉토리의 db.py를 임포트하기 위한 경로 추가
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection, get_kst_time

st.set_page_config(page_title="AX 실태조사", page_icon="📋")
st.title("📋 AX(AI 전환)에 따른 학생 인식 실태조사")
st.write("본 설문은 대학 내 인공지능 전환(AI Transformation)에 대한 학생들의 인식을 알아보기 위한 것입니다. 각 문항에 대해 자신의 생각과 가장 가까운 것을 선택해주세요.")

questions = [
    "1. 인공지능(AI) 기술이 내 전공 분야의 미래를 크게 변화시킬 것이라고 생각한다.",
    "2. 나는 AI 도구(ChatGPT 등)를 활용하여 학습 효율을 높일 수 있다고 생각한다.",
    "3. 대학 교육 과정에서 AI 관련 교육이 필수적으로 이루어져야 한다고 생각한다.",
    "4. AX(AI 전환)로 인해 나의 향후 직업 선택이나 진로에 불안감을 느낀다.",
    "5. 나는 스스로 AI 기술을 배우고 활용할 수 있는 충분한 역량을 갖추고 있다.",
    "6. AI 기술이 도입되면 학업 평가(시험, 과제 등) 방식도 바뀌어야 한다고 생각한다.",
    "7. 전공 수업에서 AI를 활용한 프로젝트나 실습이 더 많아지기를 바란다.",
    "8. AI가 제공하는 정보의 정확성이나 윤리적 문제에 대해 비판적으로 판단할 수 있다.",
    "9. 교수님들이 수업에 AI 기술을 적극적으로 활용하기를 기대한다.",
    "10. AX 시대에 대비하기 위해 대학 차원의 지원(인프라, 특강 등)이 충분하다고 생각한다."
]

options = ["1: 전혀 그렇지 않다", "2: 그렇지 않다", "3: 보통이다", "4: 그렇다", "5: 매우 그렇다"]

with st.form("inventory_form"):
    answers = []
    for i, q in enumerate(questions):
        st.write(f"**{q}**")
        ans = st.radio("응답 선택", options, index=2, horizontal=True, key=f"q{i+1}", label_visibility="collapsed")
        # 선택된 문자열에서 숫자 부분만 추출
        answers.append(int(ans.split(":")[0]))
        st.markdown("<hr style='margin: 10px 0;'>", unsafe_allow_html=True)
        
    submitted = st.form_submit_button("설문 제출하기")
    
    if submitted:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute('''
            INSERT INTO inventory (userid, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (st.session_state['userid'], *answers, get_kst_time()))
        conn.commit()
        conn.close()
        st.success("🎉 설문이 성공적으로 제출되었습니다. 참여해 주셔서 감사합니다!")
