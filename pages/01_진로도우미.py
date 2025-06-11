import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 목표 대학/학과 점수 데이터 (간략화 가능, 필요하면 더 추가해줘)
goal_db = {
    "서울대": {
        "컴퓨터공학과": 95,
        "의예과": 98,
        "경영학과": 92,
        "심리학과": 90,
        "전자공학과": 93,
        "간호학과": 89,
        "경제학과": 91,
        "법학과": 92
    },
    "성균관대": {
        "컴퓨터공학과": 90,
        "의예과": 93,
        "경영학과": 88,
        "심리학과": 85,
        "전자공학과": 87,
        "간호학과": 83,
        "경제학과": 86,
        "법학과": 87
    },
    # ... (중략) 다른 대학도 포함
    "이화여대": {
        "컴퓨터공학과": 85,
        "간호학과": 90,
        "경영학과": 82,
        "심리학과": 88,
        "전자공학과": 83,
        "경제학과": 80,
        "법학과": 81
    },
    "숙명여대": {
        "컴퓨터공학과": 80,
        "경영학과": 78,
        "심리학과": 75,
        "간호학과": 79,
        "전자공학과": 77,
        "경제학과": 74,
        "법학과": 76
    },
    "건국대": {
        "컴퓨터공학과": 83,
        "경영학과": 79,
        "심리학과": 76,
        "전자공학과": 80,
        "간호학과": 75,
        "경제학과": 77,
        "법학과": 78
    },
    "홍익대": {
        "컴퓨터공학과": 81,
        "경영학과": 78,
        "심리학과": 74,
        "전자공학과": 79,
        "간호학과": 73,
        "경제학과": 75,
        "법학과": 76
    }
}

# 학과별 중요 과목 및 추천 선택과목
major_subjects = {
    "컴퓨터공학과": {
        "중요과목": ["수학", "과학(물리)"],
        "추천선택과목": ["과학탐구(물리Ⅰ)", "과학탐구(정보과학)"]
    },
    "의예과": {
        "중요과목": ["과학(생물, 화학)", "수학"],
        "추천선택과목": ["과학탐구(생물Ⅰ)", "과학탐구(화학Ⅰ)"]
    },
    "경영학과": {
        "중요과목": ["수학", "사회(경제)"],
        "추천선택과목": ["사회탐구(경제)", "사회탐구(법과정치)"]
    },
    "심리학과": {
        "중요과목": ["과학(생물)", "사회(사회문화)"],
        "추천선택과목": ["과학탐구(생물Ⅰ)", "사회탐구(사회문화)"]
    },
    "전자공학과": {
        "중요과목": ["수학", "과학(물리)"],
        "추천선택과목": ["과학탐구(물리Ⅰ)", "과학탐구(화학Ⅰ)"]
    },
    "간호학과": {
        "중요과목": ["과학(생물)", "수학"],
        "추천선택과목": ["과학탐구(생물Ⅰ)", "과학탐구(화학Ⅰ)"]
    },
}

# 샘플 데이터 생성 (모델 학습용)
def load_sample_data():
    np.random.seed(0)
    study_time = np.random.normal(2.5, 1.0, 100)
    sleep_time = np.random.normal(7.0, 1.0, 100)
    focus_level = np.random.randint(2, 6, 100)
    assignment = np.random.uniform(50, 100, 100)
    phone_use = np.random.uniform(1, 5, 100)
    interest = np.random.randint(1, 6, 100)

    score = (
        10 * study_time +
        3 * focus_level +
        0.5 * assignment -
        4 * phone_use +
        2 * interest +
        np.random.normal(0, 5, 100)
    )
    data = pd.DataFrame({
        'Study Time': study_time,
        'Sleep Time': sleep_time,
        'Focus Level': focus_level,
        'Assignment Completion (%)': assignment,
        'Phone Use Time': phone_use,
        'Interest Level': interest,
        'Score': score
    })
    return data

def train_model(data):
    features = ['Study Time', 'Sleep Time', 'Focus Level', 'Assignment Completion (%)', 'Phone Use Time', 'Interest Level']
    X = data[features]
    y = data['Score']
    model = LinearRegression()
    model.fit(X, y)
    return model

def give_feedback(study, sleep, focus, assignment, phone_use, interest):
    feedback = []
    if study < 2:
        feedback.append("📌 공부 시간이 부족해요. 하루 2시간 이상 추천해요.")
    if sleep < 6:
        feedback.append("💤 수면 시간이 너무 적어요. 최소 6시간은 자야 집중력이 유지돼요.")
    if focus < 3:
        feedback.append("👀 수업 집중도를 높이면 학습 효율이 올라가요.")
    if assignment < 70:
        feedback.append("📎 과제 수행률이 낮아요. 꼼꼼히 챙겨보는 게 좋아요.")
    if phone_use > 3:
        feedback.append("📱 핸드폰 사용 시간이 너무 많아요. 공부 시간에 집중하세요.")
    if interest < 3:
        feedback.append("🤔 과목에 대한 흥미도가 낮네요. 흥미를 가지려고 노력해보세요.")
    if not feedback:
        feedback.append("✅ 전반적으로 좋은 습관이에요! 이대로만 계속 가자!")
    return feedback

# 스트림릿 앱 시작
st.title("📚 성적 예측 & 진로 상담 웹앱")
st.markdown("공부 습관, 지난 학기 성적, 목표 대학/학과 입력 후 맞춤 피드백과 진학 가능성을 확인해보세요!")

# 1. 지난 학기 성적 입력
st.header("📚 지난 학기 성적 입력하기")
semesters = ["1학기", "2학기", "3학기", "4학기"]
subjects = ["국어", "수학", "영어", "과학", "사회"]

score_data = {}
for sem in semesters:
    st.subheader(f"{sem} 성적 입력")
    scores = {}
    for subj in subjects:
        score = st.number_input(f"{sem} {subj} 성적 (0~100)", min_value=0, max_value=100, value=80, key=f"{sem}_{subj}")
        scores[subj] = score
    score_data[sem] = scores

df_scores = pd.DataFrame(score_data).T

st.subheader("📈 학기별 과목별 성적 그래프")
fig, ax = plt.subplots(figsize=(10, 5))
for subj in subjects:
    ax.plot(df_scores.index, df_scores[subj], marker='o', label=subj)
ax.set_ylim(0, 100)
ax.set_ylabel("성적")
ax.set_title("학기별 과목별 성적 추이")
ax.legend()
st.pyplot(fig)

# 2. 공부 습관 입력
st.header("📥 공부 습관 입력하기")
study_time = st.slider("하루 평균 공부 시간 (시간)", 0.0, 8.0, 2.0, 0.5)
sleep_time = st.slider("하루 평균 수면 시간 (시간)", 0.0, 10.0, 7.0, 0.5)
focus = st.slider("수업 집중도 (1~5)", 1, 5, 3)
assignment = st.slider("과제 수행률 (%)", 0, 100, 80)
phone_use = st.slider("하루 핸드폰 사용 시간 (시간)", 0.0, 10.0, 2.0, 0.5)
interest = st.slider("과목에 대한 흥미도 (1~5)", 1, 5, 3)

input_data = pd.DataFrame([{
    'Study Time': study_time,
    'Sleep Time': sleep_time,
    'Focus Level': focus,
    'Assignment Completion (%)': assignment,
    'Phone Use Time': phone_use,
    'Interest Level': interest
}])

# 3. 목표 대학/학과 입력
st.header("🎯 목표 대학 및 학과 입력하기")
goal_univ = st.text_input("목표 대학을 입력하세요 (예: 서울대)")
goal_major = st.text_input("목표 학과를 입력하세요 (예: 컴퓨터공학과)")

# 4. 모델 학습 및 예측
data = load_sample_data()
model = train_model(data)
predicted_score = model.predict(input_data)[0]

st.header("📊 예측 결과")
st.success(f"예상 성적: **{predicted_score:.2f}점**")

# 5. 피드백 메시지
st.subheader("🗒️ 맞춤 피드백")
for msg in give_feedback(study_time, sleep_time, focus, assignment, phone_use, interest):
    st.write(msg)

# 6. 목표 대학/학과 진학 가능성 판단
st.subheader("🎯 목표 대학/학과 진학 가능성")
required_score = None
if goal_univ and goal_major:
    required_score = goal_db.get(goal_univ.strip(), {}).get(goal_major.strip())
    if required_score:
        if predicted_score >= required_score:
            st.success(f"🎉 {goal_univ} {goal_major} 진학 가능성이 높아요! (필요 점수: {required_score})")
        else:
            st.warning(f"📉 {goal_univ} {goal_major} 진학을 위해 점수가 더 필요해요! (필요: {required_score}, 예측: {predicted_score:.2f})")
    else:
        st.info("해당 대학/학과 정보가 없습니다.")

# 7. 학과별 중요 과목 및 선택 과목 안내
if goal_major:
    st.subheader(f"📚 {goal_major} 중요 과목 및 추천 선택과목")
    info = major_subjects.get(goal_major)
    if info:
        st.write("중요 과목:", ", ".join(info["중요과목"]))
        st.write("추천 선택 과목:", ", ".join(info["추천선택과목"]))
    else:
        st.write("해당 학과의 중요 과목 정보가 없습니다.")
