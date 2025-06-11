import streamlit as st

st.set_page_config(page_title="스페인의 역사", layout="wide")
st.title("🇪🇸 스페인의 역사")
st.markdown("스페인은 유럽의 문화적, 정치적 중심지 중 하나로, 수천 년 동안 풍부한 역사적 사건을 겪어 왔습니다.")

# 멋진 배경 이미지
st.image("https://upload.wikimedia.org/wikipedia/commons/9/98/Alhambra_Granada_Spain.jpg", 
         caption="알함브라 궁전 (Granada) – 이슬람 건축의 정수", use_column_width=True)

# 사이드바: 시대 선택
period = st.sidebar.radio("시대 선택", ["전체", "선사시대와 고대", "중세 시대", "근세 시대", "근대와 현대"])

# 시대별 섹션 함수
def show_prehistory():
    st.header("🦴 선사시대와 고대")
    st.image("https://upload.wikimedia.org/wikipedia/commons/4/4f/Segovia_Aqueduct_02.jpg", 
             caption="세고비아 로마 수도교 – 로마 제국 시기의 유산", use_column_width=True)
    st.markdown("""
    - 이베리아인, 켈트족 등이 초기 정착함  
    - 기원전 1100년경 페니키아인과 그리스인 도착  
    - 기원전 218년 로마 제국에 정복되어 '히스파니아'로 편입  
    """)

def show_medieval():
    st.header("🏰 중세 시대")
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/1c/Alcazar_Segovia_Spain.jpg", 
             caption="세고비아 알카사르 – 기독교 왕국 시대의 성채", use_column_width=True)
    st.markdown("""
    - 5세기 서고트족이 로마 제국 붕괴 이후 지배  
    - 711년 무어인 침입 → 이슬람 문화 번성  
    - 1492년 그라나다 함락 → 레콩키스타 종료  
    """)

def show_early_modern():
    st.header("⚓ 근세 시대")
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/29/Colon_Espanol.jpg", 
             caption="크리스토퍼 콜럼버스 – 대항해 시대의 상징", use_column_width=True)
    st.markdown("""
    - 카스티야와 아라곤의 통일 → 스페인 왕국 탄생  
    - 1492년 콜럼버스의 항해 → 아메리카 대륙 식민지화  
    - 16~17세기: 스페인 제국의 전성기 (펠리페 2세 시대)  
    """)

def show_modern():
    st.header("🛠️ 근대와 현대")
    st.image("https://upload.wikimedia.org/wikipedia/commons/f/f7/Francisco_Franco.jpg", 
             caption="프란시스코 프랑코 – 스페인 내전과 독재 시대", use_column_width=True)
    st.markdown("""
    - 19세기: 나폴레옹 침공 → 반도 전쟁  
    - 1936~1939년: 스페인 내전 → 프랑코 정권 수립  
    - 1975년 프랑코 사망 후 민주화 진행  
    - 현재: 입헌군주제 및 유럽연합(EU) 회원국  
    """)

# 선택한 시대에 따라 출력
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
| 연도          | 주요 사건                                   |
|---------------|--------------------------------------------|
| 기원전 1100년 | 페니키아인 도착                            |
| 기원전 218년  | 로마 제국 히스파니아 정복 시작             |
| 711년         | 무어인 이베리아 반도 정복                   |
| 1492년        | 그라나다 함락, 콜럼버스 신대륙 도착        |
| 1588년        | 스페인 무적함대 패배 (영국과의 전쟁)        |
| 1808년        | 나폴레옹 침입, 반도 전쟁 시작               |
| 1936년        | 스페인 내전 발발                            |
| 1975년        | 프랑코 사망 → 민주화 시작                  |
| 현재          | 입헌군주제, 유럽연합의 일원                |
""")

st.success("스페인의 역사 여정을 멋진 이미지와 함께 살펴보았습니다.")
st.caption("🔗 이미지 출처: Wikimedia Commons (공용 라이선스)")
