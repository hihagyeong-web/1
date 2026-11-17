import sqlite3
from datetime import datetime, timedelta, timezone

def get_db_connection():
    # same_thread를 False로 설정하여 Streamlit 멀티스레딩 환경에서 안전하게 사용
    conn = sqlite3.connect('myproject.db', check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    
    # 사용자 테이블
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id_num INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            username TEXT NOT NULL,
            userid TEXT UNIQUE NOT NULL,
            passwd TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    ''')
    
    # 실태조사 테이블 (inventory)
    c.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            id_number INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            userid TEXT NOT NULL,
            q1 INTEGER, q2 INTEGER, q3 INTEGER, q4 INTEGER, q5 INTEGER,
            q6 INTEGER, q7 INTEGER, q8 INTEGER, q9 INTEGER, q10 INTEGER,
            created_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_kst_time():
    # 한국표준시(KST) 적용
    KST = timezone(timedelta(hours=9))
    return datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')
