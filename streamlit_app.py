import random
import streamlit as st

WORDS = [
    ("apple", "사과"),
    ("school", "학교"),
    ("friend", "친구"),
    ("happy", "행복한"),
    ("study", "공부하다"),
    ("library", "도서관"),
    ("travel", "여행하다"),
    ("rain", "비"),
    ("sunny", "화창한"),
    ("music", "음악"),
    ("teacher", "선생님"),
    ("family", "가족"),
    ("beautiful", "아름다운"),
    ("exercise", "운동"),
    ("guitar", "기타"),
    ("computer", "컴퓨터"),
    ("language", "언어"),
    ("favorite", "가장 좋아하는"),
    ("museum", "박물관"),
    ("piano", "피아노"),
]


def reset_game():
    st.session_state.questions = random.sample(WORDS, k=8)
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.feedback = ""
    st.session_state.pop("selected_answer", None)


def next_question():
    st.session_state.current_index += 1
    st.session_state.answered = False
    st.session_state.feedback = ""
    st.session_state.pop("selected_answer", None)
    st.rerun()


if "questions" not in st.session_state:
    reset_game()

st.set_page_config(page_title="영단어 게임", page_icon="📚", layout="centered")
st.title("📚 영어 공부 + BTS")
st.write("영단어 게임과 BTS 소개를 함께 즐겨보세요!")

menu = st.tabs(["영단어 게임", "BTS 소개"])

with menu[0]:
    st.header("📝 영단어 게임")
    st.write("뜻을 보고 알맞은 영어 단어를 고르세요.")

    st.sidebar.header("🎯 게임 정보")
    st.sidebar.write("- 8문제를 풀어요.")
    st.sidebar.write("- 뜻을 보고 영어 단어를 고르면 됩니다.")
    st.sidebar.write("- 정답을 맞히면 점수가 올라갑니다.")

    if st.button("새 게임 시작"):
        reset_game()

    if st.session_state.current_index >= len(st.session_state.questions):
        st.success(f"게임 끝! 총 {len(st.session_state.questions)}문제 중 {st.session_state.score}개 맞혔어요.")
        if st.button("다시 도전하기"):
            reset_game()
        st.stop()

    english_word, korean_meaning = st.session_state.questions[st.session_state.current_index]

    options = [english_word]
    other_words = [word for word, _ in WORDS if word != english_word]
    distractors = random.sample(other_words, k=3)
    options = options + distractors
    random.shuffle(options)

    st.write(f"### 문제 {st.session_state.current_index + 1}/{len(st.session_state.questions)}")
    st.write(f"뜻: {korean_meaning}")

    selected = st.radio("영어 단어를 고르세요.", options, key="selected_answer")

    if not st.session_state.answered:
        if st.button("정답 확인"):
            if selected == english_word:
                st.session_state.score += 1
                st.session_state.feedback = "✅ 정답입니다!"
            else:
                st.session_state.feedback = f"❌ 아쉽습니다. 정답은 {english_word}입니다."
            st.session_state.answered = True
    else:
        st.info(st.session_state.feedback)
        if st.button("다음 문제"):
            next_question()

    st.caption(f"현재 점수: {st.session_state.score}점")

with menu[1]:
    st.header("🎤 BTS 소개")
    st.markdown("BTS는 방탄소년단으로, 한국의 대표적인 보이그룹입니다. 멋진 춤, 감동적인 노래, 그리고 세련된 비주얼로 전 세계 팬들에게 사랑받고 있어요.")

    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/BTS_during_a_press_conference_on_April_25%2C_2019_%28cropped%29.jpg/800px-BTS_during_a_press_conference_on_April_25%2C_2019_%28cropped%29.jpg",
        caption="BTS의 화려한 무대와 세련된 비주얼",
        use_container_width=True,
    )

    st.subheader("🌟 BTS의 매력")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🎵 멋진 음악")
        st.write("다양한 장르의 음악으로 많은 사람들에게 감동을 줍니다.")
    with col2:
        st.info("💃 화려한 퍼포먼스")
        st.write("정교한 안무와 강렬한 무대 매력이 정말 인상적입니다.")
    with col3:
        st.info("🌍 글로벌 인기")
        st.write("전 세계 팬들과 함께하는 특별한 존재입니다.")

    st.subheader("👑 멤버 소개")
    st.write("RM, 진, 슈가, 제이홉, 지민, 뷔, 정국으로 구성된 BTS는 각각 다른 매력을 가지고 있습니다.")

    st.subheader("🎶 좋아하는 BTS 곡")
    st.write("- Dynamite")
    st.write("- Butter")
    st.write("- Spring Day")
