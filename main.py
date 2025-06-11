import streamlit as st
import folium
from streamlit_folium import st_folium

# 여행지 정보
destinations = {
    "바르셀로나": {
        "coords": (41.3851, 2.1734),
        "description": "가우디의 건축물과 해변, 축구로 유명한 도시입니다.",
        "attractions": [
            {
                "name": "사그라다 파밀리아",
                "desc": "가우디가 설계한 상징적인 성당",
                "coords": (41.4036, 2.1744),
                "img": "https://upload.wikimedia.org/wikipedia/commons/7/7e/Sagrada_Familia_01.jpg"
            },
            {
                "name": "구엘 공원",
                "desc": "모자이크와 독특한 건축 양식의 공원",
                "coords": (41.4145, 2.1527),
                "img": "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/Park_G%C3%BCell_Barcelona_Spain.jpg/800px-Park_G%C3%BCell_Barcelona_Spain.jpg"
            }
        ],
        "itinerary": "3일 일정: 1일차 - 사그라다 파밀리아, 구엘 공원, 2일차 - 바르셀로네타 해변, 3일차 - 고딕 지구 탐방"
    },
    "마드리드": {
        "coords": (40.4168, -3.7038),
        "description": "스페인의 수도로 왕궁, 미술관, 쇼핑 거리로 유명합니다.",
        "attractions": [
            {
                "name": "마드리드 왕궁",
                "desc": "스페인 국왕의 공식 거처",
                "coords": (40.4170, -3.7143),
                "img": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Palacio_Real_de_Madrid_01.jpg"
            },
            {
                "name": "프라도 미술관",
                "desc": "유럽 최고의 미술관 중 하나",
                "coords": (40.4138, -3.6921),
                "img": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Madrid_-_Museo_del_Prado_3.jpg"
            }
        ],
        "itinerary": "2일 일정: 1일차 - 왕궁, 프라도 미술관, 2일차 - 그란비아 거리 쇼핑, 레티로 공원"
    },
    "세비야": {
        "coords": (37.3891, -5.9845),
        "description": "플라멩코와 역사적 유산으로 가득한 도시입니다.",
        "attractions": [
            {
                "name": "세비야 대성당",
                "desc": "세계에서 가장 큰 고딕 양식 성당 중 하나",
                "coords": (37.3891, -5.9844),
                "img": "https://upload.wikimedia.org/wikipedia/commons/e/e9/Catedral_de_Sevilla_11.jpg"
            },
            {
                "name": "알카사르 궁전",
                "desc": "이슬람과 기독교 문화가 혼합된 궁전",
                "coords": (37.3829, -5.9902),
                "img": "https://upload.wikimedia.org/wikipedia/commons/4/41/Sevilla_Real_Alcazar_Garten.jpg"
            }
        ],
        "itinerary": "2일 일정: 1일차 - 세비야 대성당, 알카사르 궁전, 2일차 - 플라멩코 공연, 스페인 광장"
    },
    "그라나다": {
        "coords": (37.1773, -3.5986),
        "description": "알함브라 궁전과 언덕 위 전망으로 유명합니다.",
        "attractions": [
            {
                "name": "알함브라 궁전",
                "desc": "이슬람 예술의 정수",
                "coords": (37.1760, -3.5881),
                "img": "https://upload.wikimedia.org/wikipedia/commons/9/94/Alhambra_palace.jpg"
            },
            {
                "name": "알바이신 지구",
                "desc": "그라나다의 전통 마을, 언덕 위에서의 멋진 경관",
                "coords": (37.1782, -3.5905),
                "img": "https://upload.wikimedia.org/wikipedia/commons/4/4c/Albaicin-view.jpg"
            }
        ],
        "itinerary": "2일 일정: 1일차 - 알함브라 궁전, 2일차 - 알바이신 지구, 그라나다 성당"
    },
    "산세바스티안": {
        "coords": (43.3183, -1.9812),
        "description": "아름다운 해변과 미식 문화가 공존하는 도시입니다.",
        "attractions": [
            {
                "name": "라 콘차 해변",
                "desc": "스페인 최고의 해변 중 하나",
                "coords": (43.3187, -1.9861),
                "img": "https://upload.wikimedia.org/wikipedia/commons/7/7f/La_Concha_Bay%2C_San_Sebasti%C3%A1n.jpg"
            },
            {
                "name": "몬테 이겔도",
                "desc": "전망대에서 도시 전경 감상",
                "coords": (43.3201, -1.9775),
                "img": "https://upload.wikimedia.org/wikipedia/commons/b/bd/San_Sebastian_view_from_Igeldo.jpg"
            }
        ],
        "itinerary": "3일 일정: 1일차 - 라 콘차 해변, 2일차 - 몬테 이겔도, 3일차 - 올드타운"
    }
}

st.set_page_config(page_title="스페인 여행 가이드", layout="wide")
st.title("🇪🇸 스페인 여행지 가이드")
st.markdown("스페인의 주요 도시를 선택하면 관광 명소와 지도를 함께 보여드립니다.")

# 여행지 선택
selected = st.selectbox("여행지를 선택하세요:", list(destinations.keys()))
info = destinations[selected]

# 여행지 정보
st.subheader(f"📍 {selected}")
st.write(info["description"])

# 여행 일정 추천
st.markdown("### 📅 추천 여행 일정")
st.write(info["itinerary"])

# 지도 표시
m = folium.Map(location=info["coords"], zoom_start=6)

# 여행지 마커
folium.Marker(info["coords"], tooltip=selected, popup=info["description"]).add_to(m)

# 관광지 마커 추가
for attr in info["attractions"]:
    folium.Marker(
        location=attr["coords"],
        popup=f"{attr['name']} - {attr['desc']}",
        tooltip=attr["name"]
    ).add_to(m)

st_folium(m, width=700, height=500)

# 관광명소 출력
st.markdown("### 🌟 주요 관광명소")
for attr in info["attractions"]:
    with st.container():
        st.image(attr["img"], width=600, caption=attr["name"])
        st.write(f"**{attr['name']}**: {attr['desc']}")
        st.markdown("---")

# 사용자 평가 기능 (별점)
st.markdown("### ⭐ 사용자 평가")
rating = st.slider("이 여행지를 평가해 주세요", 1, 5, 3)
st.write(f"당신의 평점: {rating}성급")
