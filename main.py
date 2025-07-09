import streamlit as st

st.write('---')
st.title('1.버튼')
st.write('---')

if st.button("클릭하세요"):
    st.write("버튼이 눌려졌습니다.")


st.write('---')
st.title('2.체크박스')
st.write('---')

if st.checkbox("약관에 동히하시겠습니까?"):
    agree=st.write("약관에 동이하셨네요")
st.write('---')
st.title('3. 라디오 버튼')
st.write('---')



st.write('---')
st.title('4.셀렉트박스')
st.write('---')

choice = st.selectbox("가장 좋아하는 과일을 선택하세요", ["사과", "바나나", "체리"])
st.write(f"선택한 과일: {choice}")  

st.write('---')
st.title('5.멀티셀렉트')
st.write('---')

fruits =st.multiselect(
    "먹고싶은 과일을 선택하세요",("사과","바나나","체리", "포도"), default=["사과"])
st.write("선택한 과일:" , fruits)

st.write('---')
st.title('6.슬라이더')
st.write('---')


age = st.slider("나이를 선택하세요",
     min_value=0 , max_value=100, value=20
     )
height = st.slider(
    "키 범위 선택", min_value=140.0, max_value=200.0, value=(160.0, 180.0))

st.write('---')
st.title('7.비밀번호')
st.write('---')

name= st.text_input(
    label="이름을 입력하세요",
    placeholder="홍길동"
)
password = st.text_input( label="비밀번호",
    type="비밀번호",
    help="영문,숫자,특수문자 조합 8~16가지",
    max_chars=16 )

st.text_input(
    label="읽기 전용 필드", value="수정불가", disabled=True
)


st.write('---')
st.title('8. 텍스트 영역')
st.write('---')

feedback = st.text_area(
    "자유롭게 의견을 남겨주세요", 
    height=150
)