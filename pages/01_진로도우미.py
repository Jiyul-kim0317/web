import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# 1. 목표 대학-학과별 내신 합격선 데이터 (예시)
goal_db = {
    "서울대": {
        "컴퓨터공학과": 95,
        "의예과": 97,
        "경영학과": 92,
        "심리학과": 90
    },
    "성균관대": {
        "컴퓨터공학과": 90,
        "의예과": 93,
        "경영학과": 88,
        "심리학과": 85
    },
    "이화여대": {
        "컴퓨터공학과": 85,
        "간호학과": 90,
        "경영학과": 82,
        "심리학과": 88
    }
}

# 2. 과목별 평균 내신 점수 (예시)
subject_averages = {
    "국어": 80,
    "수학": 78,
    "영어": 82,
    "과학": 75,
    "사회": 77
}

# ----------------------------
st.title("📊 내신 성적 분석 & 목표 대학 내신 비교")

# 학기 및 과목 설정
semesters = ["1학기", "2학기", "3학기", "4학기"]
subjects = list(subject_averages.keys())

# 사용자 내신 점수 입력
st.header("📥 학기별 과목별 내신 점수 입력 (0~100)")

score_data = {}
for sem in semesters:
    st.subheader(f"{sem} 내신 점수 입력")
    scores = {}
    for subj in subjects:
        val = st.number_input(f"{sem} {subj} 성적", min_value=0, max_value=100, value=0, key=f"{sem}_{subj}")
        scores[subj] = val
    score_data[sem] = scores

# 데이터프레임 변환
df_scores = pd.DataFrame(score_data).T

# 상대 점수 계산 함수
def calculate_relative_scores(user_scores, subject_avg):
    relative = {}
    for subj, score in user_scores.items():
        avg = subject_avg.get(subj, 75)
        relative[subj] = score - avg
    return relative

# 학기별 상대 점수 데이터프레임 만들기
df_relative = df_scores.apply(lambda row: calculate_relative_scores(row, subject_averages), axis=1, result_type='expand')

# 시각화: 학기별 과목별 내신 점수 추이
st.subheader("📈 학기별 과목별 내신 점수 변화 추이")
fig, ax = plt.subplots(figsize=(10, 6))
for subj in subjects:
    ax.plot(df_scores.index, df_scores[subj], marker='o', label=subj)
ax.set_ylim(0, 100)
ax.set_ylabel("내신 점수")
ax.set_title("학기별 과목별 내신 점수 추이")
ax.legend()
st.pyplot(fig)

# 상대 점수 표 보여주기
st.subheader("📊 학기별 과목별 상대 점수 (평균 대비 차이)")
st.dataframe(df_relative)

# 목표 대학/학과 선택
st.header("🎯 목표 대학 및 학과 내신 합격선 비교")
goal_univ = st.selectbox("목표 대학 선택", options=list(goal_db.keys()))
goal_major = st.selectbox("목표 학과 선택", options=list(goal_db[goal_univ].keys()))

required_score = goal_db[goal_univ][goal_major]

# 평균 내신 점수 (4학기 평균)
avg_score = df_scores.mean().mean()

st.write(f"목표 대학: **{goal_univ}**, 학과: **{goal_major}**")
st.write(f"목표 내신 합격선 점수 (예시): **{required_score}점**")
st.write(f"입력한 내신 평균 점수: **{avg_score:.2f}점**")

# 5단계 차이에 따른 맞춤 조언
diff = avg_score - required_score

if diff >= 10:
    st.success("🎉 내신 점수가 목표 합격선보다 매우 높습니다! 합격이 확실합니다!")
    st.write("✅ 추천 조언:")
    st.write("1. 현재 학습 방법을 꾸준히 유지하세요.")
    st.write("2. 심화 과목 및 선택과목에서도 우수한 성적을 유지하세요.")
    st.write("3. 모의고사 대비도 게을리 하지 마세요.")
    st.write("4. 동아리나 봉사활동 등 비교과 활동에도 신경 쓰세요.")
    st.write("5. 목표 대학에 대한 자세한 입시 정보도 꾸준히 확인하세요.")

elif 5 <= diff < 10:
    st.success("👍 내신 점수가 목표 합격선보다 약간 높아, 합격 가능성이 높습니다.")
    st.write("✅ 추천 조언:")
    st.write("1. 중요한 과목에 집중하여 점수를 유지하세요.")
    st.write("2. 최근 학기 성적 하락을 주의하세요.")
    st.write("3. 선택과목도 신중하게 골라 내신에 반영되도록 하세요.")
    st.write("4. 꾸준한 모의고사 준비로 실전 감각을 키우세요.")
    st.write("5. 진로 상담이나 선생님 조언도 적극 활용하세요.")

elif 0 <= diff < 5:
    st.info("⚠️ 내신 점수가 목표 합격선과 근접합니다. 세심한 관리가 필요합니다.")
    st.write("⚠️ 개선 조언:")
    st.write("1. 부족한 과목을 집중 관리하세요.")
    st.write("2. 시험 준비 계획을 세우고 실천력을 높이세요.")
    st.write("3. 학기별 성적 변동에 민감하게 대응하세요.")
    st.write("4. 선택과목을 전략적으로 결정하세요.")
    st.write("5. 전문가 상담을 통해 학습 방법을 점검하세요.")

elif -5 <= diff < 0:
    st.warning("⚠️ 내신 점수가 목표 합격선보다 약간 낮습니다. 집중 보완이 필요합니다.")
    st.write("⚠️ 집중 보완 조언:")
    st.write("1. 약한 과목을 집중적으로 보완하는 계획을 세우세요.")
    st.write("2. 시간 관리 및 공부 습관을 개선하세요.")
    st.write("3. 모의고사 성적과 내신 차이를 줄이기 위해 노력하세요.")
    st.write("4. 선택과목을 재검토해 내신 향상에 도움이 되는 과목을 선택하세요.")
    st.write("5. 선생님, 상담사와 상담해 맞춤형 전략을 수립하세요.")

else:
    st.error("❗ 내신 점수가 목표 합격선보다 크게 낮습니다. 대책 마련이 시급합니다!")
    st.write("❗ 긴급 대책 조언:")
    st.write("1. 부족한 과목 위주로 학습 계획을 재구성하세요.")
    st.write("2. 공부 시간과 방법을 근본적으로 점검하고 개선하세요.")
    st.write("3. 학습 동기 부여를 위해 목표와 계획을 다시 설정하세요.")
    st.write("4. 입시 전문가, 진로 상담사의 도움을 반드시 받으세요.")
    st.write("5. 필요시 대학 선택이나 진로 계획을 재검토하는 것도 고려하세요.")
