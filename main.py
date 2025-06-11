import streamlit as st
import folium
from streamlit_folium import st_folium

# 여행지 정보
destinations = {
    "바르셀로나": {
        "coords": (41.3851, 2.1734),
        "description": "가우디의 건축물과 해변, 축구로 유명한 도시입니다. 사그라다 파밀리아 성당은 꼭 방문해야 할 명소입니다."
    },
    "마드리드": {
        "coords": (40.4168, -3.7038),
        "description": "스페인의 수도로 왕궁, 프라도 미술관, 그란비아 거리 등 다양한 볼거리가 있습니다."
    },
    "세비야": {
        "coords": (37.3891, -5.9845),
        "description": "플라멩코의 본고장이며, 세비야 대성당과 알카사르 궁전이 유명합니다."
    },
    "그라나다": {
        "coords": (37.1773, -3.5986),
        "description": "알함브라 궁전으로 유명하며, 이슬람 문화와 유럽 문화가 혼합된 독특한 분위기를 느낄 수 있습니다."
    },
    "산세바스티안": {
        "coords": (43.3183, -1.9812),
        "description": "아름다운 해변과 미슐랭 레스토랑이 많은 고급 휴양지입니다."
    }
}

st.title("🇪🇸 스페인 여행지 가이드")
st.markdown("스페인의 주요 도시를 선택하면 정보를 제공하고 지도를 표시해드립니다.")

# 여행지 선택
selected = st.selectbox("여행지를 선택하세요:", list(destinations.keys()))

# 선택한 여행지 정보 표시
info = destinations[selected]
st.subheader(f"📍 {selected}")
st.write(info["description"])

# 지도 생성
m = folium.Map(location=info["coords"], zoom_start=6)
folium.Marker(info["coords"], tooltip=selected, popup=info["description"]).add_to(m)

# 지도 출력
st_folium(m, width=700, height=500)
