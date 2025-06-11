import streamlit as st

st.set_page_config(page_title="스페인의 역사", layout="wide")

st.title("🇪🇸 스페인의 역사")
st.markdown("""
스페인은 수천 년의 역사를 지닌 유럽의 중요한 국가 중 하나입니다. 아래는 시대별로 정리한 스페인의 역사입니다.
""")

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Flag_of_Spain.svg/320px-Flag_of_Spain.svg.png", width=200, caption="스페인 국기")

# 사이드바: 시대 선택
period = st.sidebar.radio("시대 선택", ["전체", "선사시대와 고대", "중세 시대", "근세 시대", "근대와 현대"])

# 각 시대별 콘텐츠 정의
def show_prehistory():
    st.header("🦴 선사시대와 고대")
    st.image("https://upload.wikimedia.org/wikipedia/commons/6/6a/Dama_de_Elche_%28M.A.N._Madrid%29_03.jpg", caption="엘체의 여인(기원전 이베리아 문명)", width=300)
    st.markdown("""
    - 이베리아인, 켈트족 정착  
    - 페니키아, 그리스, 카르타고 식민지  
    - 기원전 218년 로마 제국 정복 → **히스파니아**로 편입  
    """)

def show_medieval():
    st.header("🏰 중세 시대")
    st.image("https://upload.wikimedia.org/wikipedia/commons/9/98/La_Alhambra.jpg", caption="알함브라 궁전 (이슬람 시기)", width=400)
    st.markdown("""
    - 서고트 왕국(5세기 후반)  
    - 711년 무어인 침입 → 알 안달루스 수립  
    - 1492년 그라나다 함락 → 레콩키스타 종료  
    """)

def show_early_modern():
    st.header("⚓ 근세 시대")
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/0c/Christopher_Columbus3.jpg", caption="크리스토퍼 콜럼버스", width=300)
    st.markdown("""
    - 이사벨 1세 & 페르디난드 2세 결혼 → 통일 왕국  
    - 1492년 콜럼버스 항해 → 라틴아메리카 식민지 형성  
    - 16~17세기: 스페인 제국의 황금기  
    """)

def show_modern():
    st.header("🛠️ 근대와 현대")
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/f7/Francisco_Franco.jpg", caption="프란시스코 프랑코", width=250)
    st.markdown("""
    - 19세기: 나폴레옹 전쟁, 라틴아메리카 독립  
    - 1936~1939년: 스페인 내전 → 프랑코 독재  
    - 1975년 민주화 이후 입헌군주제 수립  
    """)

# 선택한 시대에 따라 콘텐츠 출력
if period == "전체" or period == "선사시대와 고대":
    show_prehistory()
if period == "전체" or period == "중세 시대":
    show_medieval()
if period == "전체" or period == "근세 시대":
    show_early_modern()
if period == "전체" or period == "근대와 현대":
    show_modern()

# 타임라인 표
st.markdown("---")
st.subheader("🕰️ 주요 역사 타임라인")
st.markdown("""
| 연도          | 사건                                       |
|---------------|--------------------------------------------|
| 기원전 1100년 | 페니키아인 도착                            |
| 기원전 218년  | 로마 제국 히스파니아 정복 시작             |
| 711년         | 무어인 이베리아 반도 정복                   |
| 1492년        | 그라나다 함락, 콜럼버스 신대륙 도착        |
| 1588년        | 스페인 무적함대 패배 (영국과의 전쟁)        |
| 1808년        | 나폴레옹 침입, 반도 전쟁 시작               |
| 1936년        | 스페인 내전 발발                            |
| 1975년        | 프랑코 사망 → 민주화 시작                  |
| 현재          | 입헌군주제 및 유럽연합(EU) 회원국          |
""")

st.success("시대별 이미지와 함께 스페인의 역사 여정을 살펴보았습니다!")
