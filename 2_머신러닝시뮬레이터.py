import streamlit as st

if 'logged_in' not in st.session_state or not st.session_state['logged_in']:
    st.warning('🔒 로그인 후 이용 가능한 페이지입니다. 랜딩페이지에서 로그인을 진행해주세요.')
    st.stop()

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.svm import SVC
import numpy as np

st.set_page_config(page_title="붓꽃 품종 예측 시뮬레이터", page_icon="🌸")
st.title("🌸 머신러닝 시뮬레이터: 붓꽃 품종 예측")
st.markdown('''학생들이 직접 4가지 붓꽃의 특징 변수(꽃받침 길이/너비, 꽃잎 길이/너비)를 입력하면, **서포트 벡터 머신(SVM)** 머신러닝 모델이 붓꽃의 3가지 품종 중 하나로 예측해 줍니다.''')

@st.cache_resource
def train_svm_model():
    iris = load_iris()
    model = SVC(kernel='rbf', probability=True, random_state=42)
    model.fit(iris.data, iris.target)
    return model, iris.target_names

model, target_names = train_svm_model()

st.sidebar.header("🔍 붓꽃 특징 입력")
st.sidebar.write("아래 슬라이더를 조절하여 값을 입력해 보세요.")
sepal_length = st.sidebar.slider("꽃받침 길이 (Sepal Length, cm)", 4.0, 8.0, 5.1, step=0.1)
sepal_width = st.sidebar.slider("꽃받침 너비 (Sepal Width, cm)", 2.0, 4.5, 3.5, step=0.1)
petal_length = st.sidebar.slider("꽃잎 길이 (Petal Length, cm)", 1.0, 7.0, 1.4, step=0.1)
petal_width = st.sidebar.slider("꽃잎 너비 (Petal Width, cm)", 0.1, 2.5, 0.2, step=0.1)

st.write("---")
st.subheader("💡 입력된 특징 값")
col1, col2, col3, col4 = st.columns(4)
col1.metric("꽃받침 길이", f"{sepal_length} cm")
col2.metric("꽃받침 너비", f"{sepal_width} cm")
col3.metric("꽃잎 길이", f"{petal_length} cm")
col4.metric("꽃잎 너비", f"{petal_width} cm")

if st.button("🚀 인공지능 예측하기"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)
    pred_prob = model.predict_proba(input_data)[0]
    species_idx = prediction[0]
    species = target_names[species_idx]
    
    st.write("---")
    st.subheader("🎉 머신러닝 예측 결과")
    if species == 'setosa':
        st.success(f"이 붓꽃은 **Setosa (세토사)** 품종으로 예측되었습니다! (확률: {pred_prob[species_idx]*100:.1f}%)")
    elif species == 'versicolor':
        st.info(f"이 붓꽃은 **Versicolor (버시컬러)** 품종으로 예측되었습니다! (확률: {pred_prob[species_idx]*100:.1f}%)")
    else:
        st.warning(f"이 붓꽃은 **Virginica (버지니카)** 품종으로 예측되었습니다! (확률: {pred_prob[species_idx]*100:.1f}%)")
        
    st.write("📊 **품종별 예측 확률:**")
    st.progress(float(pred_prob[0]), text=f"Setosa: {pred_prob[0]*100:.1f}%")
    st.progress(float(pred_prob[1]), text=f"Versicolor: {pred_prob[1]*100:.1f}%")
    st.progress(float(pred_prob[2]), text=f"Virginica: {pred_prob[2]*100:.1f}%")
