import streamlit as st
import pandas as pd
from db import init_db, get_db_connection, get_kst_time
import sqlite3

# DB 및 테이블 초기화
init_db()

# 세션 상태 초기화
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title('🚀 앱 랜딩페이지 및 로그인')
    st.write("서비스를 이용하시려면 로그인을 하시거나 신규로 가입해 주세요.")
    
    tab1, tab2 = st.tabs(['🔑 로그인', '📝 신규등록'])
    
    with tab1:
        st.subheader('로그인')
        login_id = st.text_input('아이디', key='login_id')
        login_pw = st.text_input('비밀번호', type='password', key='login_pw')
        
        if st.button('로그인'):
            conn = get_db_connection()
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE userid=? AND passwd=?', (login_id, login_pw))
            user = c.fetchone()
            conn.close()
            
            if user:
                st.session_state['logged_in'] = True
                st.session_state['userid'] = user['userid']
                st.session_state['username'] = user['username']
                st.rerun()
            else:
                st.error('아이디 또는 비밀번호가 일치하지 않습니다.')

    with tab2:
        st.subheader('신규 회원가입')
        reg_name = st.text_input('이름', key='reg_name')
        reg_id = st.text_input('아이디', key='reg_id')
        reg_pw = st.text_input('비밀번호', type='password', key='reg_pw')
        reg_pw2 = st.text_input('비밀번호 확인', type='password', key='reg_pw2')
        
        if st.button('가입하기'):
            if reg_pw != reg_pw2:
                st.error('비밀번호가 일치하지 않습니다.')
            elif not reg_name or not reg_id or not reg_pw:
                st.error('모든 항목을 입력해주세요.')
            else:
                conn = get_db_connection()
                c = conn.cursor()
                try:
                    c.execute('INSERT INTO users (username, userid, passwd, created_at) VALUES (?, ?, ?, ?)', 
                              (reg_name, reg_id, reg_pw, get_kst_time()))
                    conn.commit()
                    st.success('회원가입이 완료되었습니다. [로그인] 탭에서 접속해 주세요.')
                except sqlite3.IntegrityError:
                    st.error('이미 사용 중인 아이디입니다.')
                finally:
                    conn.close()
else:
    # ==========================================
    # 로그인 후 접근 가능한 원본 웹앱 영역
    # ==========================================
    st.sidebar.success(f"환영합니다, {st.session_state['username']}님!")
    if st.sidebar.button('🚪 로그아웃'):
        st.session_state['logged_in'] = False
        st.session_state['userid'] = None
        st.session_state['username'] = None
        st.rerun()

    urls = ['https://www.youtube.com/watch?v=KR8ddnPjCtk', 
            'https://www.youtube.com/watch?v=Z8tZjIOptZI', 
            'https://www.youtube.com/watch?v=cYI85HFgFeg']

    images = ['https://i.ytimg.com/vi/MP8R6kBykzE/sddefault.jpg']

    st.title('This is my first webapp')

    con1, con2 = st.columns((4,1))
    with con1:
        with st.expander('Content...'):
            for i in range(len(urls)):
                st.video(urls[i])
            pass
    with con2:
        with st.expander('Tips...'):
            st.image(images[0])
            pass

    con3, con4 = st.columns((4,1))
    with con3:
        with st.expander('Content...'):
            import pandas as pd
            df = pd.read_csv('./data.csv')
            st.write(df)
    with con4:
        with st.expander('Tips...'):
            with open('./ml.txt', 'r', encoding='utf8') as f:
                    mytxt = f.read()
                    st.markdown(mytxt)

            st.image(images[0])
            pass
