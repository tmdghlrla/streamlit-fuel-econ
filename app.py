import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def main() :
    st.title('자동차 데이터 분석~')
    st.text('안녕')
    st.subheader('차트 보기')

    df=pd.read_csv('data/fuel_econ.csv')

    if st.checkbox('데이터 프레임 보기') :
         st.dataframe(df)
    else :
        st.text('')

    st.text('컬럼을 선택하면, 중복제거한 데이터의 갯수를 보여줍니다.')

    choice = st.selectbox('컬럼선택', df.columns)
    count=df[choice].dropna().nunique()
    st.text('{} 컬럼의 중복 제거한 데이터의 갯수는 {}개 입니다.'.format(choice, count))

    selected_list=st.multiselect('두개 이상의 컬럼을 선택하세요', options=df.columns[8:],max_selections=2)

    if len(selected_list) == 2 :
        fig1=plt.figure()
        plt.scatter(data=df,x=selected_list[0],y=selected_list[1])
        plt.title('{} Vs {}'.format(selected_list[0],selected_list[1]))
        plt.xlabel(selected_list[0])
        plt.ylabel(selected_list[1])
        st.pyplot(fig1)
        st.text('상관계수')
        st.dataframe(df[selected_list].corr(numeric_only=True))
    else :
        st.text('')


if __name__ == '__main__' :
    main()