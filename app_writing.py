import streamlit as st

# ==========================================
# FULL DATABASE: BỐ CỤC CHUẨN THEO PDF
# ==========================================
COURSE_DATA = {
    "Unit 1: Social Trends": {
        "theory": "### UNIT 1: SOCIAL TRENDS\n**The Present Continuous (Thì hiện tại tiếp diễn)**",
        "exercises": [
            {
                "type": "mcq", 
                "instruction": "Put the verbs in the correct form of the Present Continuous.",
                "original": "Jim: Sorry, Mum. I ___ my homework. (DO)", 
                "starter": "",
                "options": ["A. am doing", "B. do", "C. is doing"], 
                "a": "A", 
                "explain": "Diễn tả hành động đang xảy ra tại thời điểm nói. I + am + V-ing."
            }
        ]
    },
    "Supp: Rewrites & Passive Voice": {
        "theory": "### ÔN TẬP TỔNG HỢP: VIẾT LẠI CÂU & CÂU BỊ ĐỘNG\nBố cục đã được tinh chỉnh giống 100% định dạng đề thi trong PDF.",
        "exercises": [
            {
                "type": "rewrite",
                "instruction": "Complete the second sentences without changing the meaning of the first sentences.",
                "original": "1. The weather is too terrible for you to go out.",
                "starter": "→ If the weather...",
                "options": [
                    "A. wasn't terrible, you can go out.",
                    "B. weren't too terrible, you could go out.",
                    "C. is not terrible, you could go out.",
                    "D. had not been terrible, you could have gone out."
                ],
                "a": "B",
                "explain": "Thực tế ở hiện tại (is terrible) -> Dùng Câu điều kiện loại 2 (trái với hiện tại): If + S + V(quá khứ/weren't), S + could/would + V."
            },
            {
                "type": "rewrite",
                "instruction": "Complete the second sentences without changing the meaning of the first sentences.",
                "original": "2. All the students have to take the final exam.",
                "starter": "→ The final exam...",
                "options": [
                    "A. has to be taken by all the students.",
                    "B. have to be taken by all the students.",
                    "C. is taken by all the students.",
                    "D. had to be taken by all the students."
                ],
                "a": "A",
                "explain": "Bị động của động từ khuyết thiếu / have to: S + have/has to be + PII. 'The final exam' là số ít nên dùng 'has to be taken'."
            },
            {
                "type": "rewrite",
                "instruction": "Complete the second sentences without changing the meaning of the first sentences.",
                "original": "3. Please don't repeat what I said.",
                "starter": "→ Would you mind...",
                "options": [
                    "A. not to repeat what I said?",
                    "B. not repeating what I said?",
                    "C. don't repeat what I said?",
                    "D. to not repeat what I said?"
                ],
                "a": "B",
                "explain": "Cấu trúc: Would you mind + (not) + V-ing? (Bạn có phiền nếu không...)."
            },
            {
                "type": "rewrite",
                "instruction": "Complete the second sentences without changing the meaning of the first sentences.",
                "original": "4. I can't swim as well as my friend can.",
                "starter": "→ My friend...",
                "options": [
                    "A. can swim as well as I can.",
                    "B. can't swim better than me.",
                    "C. can swim better than I can.",
                    "D. swims worse than I do."
                ],
                "a": "C",
                "explain": "So sánh không bằng ('can't swim as well as') viết lại thành so sánh hơn ('can swim better than')."
            }
        ]
    }
}

# ==========================================
# STREAMLIT UI CODE - NÂNG CẤP GIAO DIỆN
# ==========================================
st.set_page_config(page_title="HOU - Writing 1 App", page_icon="🎓", layout="wide")

# CSS tùy chỉnh để làm nổi bật câu hỏi
st.markdown("""
<style>
    .instruction-text { font-size: 16px; font-style: italic; color: #555; margin-bottom: 10px;}
    .original-sentence { font-size: 18px; font-weight: bold; color: #1f77b4; padding: 10px; background-color: #e6f2ff; border-radius: 5px; margin-bottom: 10px; border-left: 5px solid #1f77b4;}
    .starter-text { font-size: 18px; font-weight: bold; color: #d62728; margin-bottom: 15px;}
    .stRadio > div { flex-direction: column; }
</style>
""", unsafe_allow_html=True)

if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
if 'current_topic' not in st.session_state:
    st.session_state.current_topic = list(COURSE_DATA.keys())[0]

st.sidebar.title("📚 Tất Cả Bài Học")
selected_topic = st.sidebar.radio("Chọn học phần:", list(COURSE_DATA.keys()))

if selected_topic != st.session_state.current_topic:
    st.session_state.current_topic = selected_topic
    st.session_state.q_index = 0
    st.rerun()

topic_data = COURSE_DATA[st.session_state.current_topic]
st.header(f"📖 {st.session_state.current_topic}")

tab_theory, tab_practice = st.tabs(["📚 Lý Thuyết Cốt Lõi", "✍️ Bài Tập Thực Hành"])

with tab_theory:
    st.markdown(topic_data["theory"])

with tab_practice:
    exercises = topic_data.get("exercises", [])
    if not exercises:
        st.info("Chưa có bài tập cho phần này.")
    else:
        q_data = exercises[st.session_state.q_index]
        st.progress((st.session_state.q_index + 1) / len(exercises))
        st.subheader(f"Câu hỏi {st.session_state.q_index + 1} / {len(exercises)}")
        
        with st.form(key=f"exercise_form_{st.session_state.q_index}"):
            
            # --- KHU VỰC RENDER ĐỀ BÀI THEO BỐ CỤC PDF ---
            if q_data.get("type") == "rewrite":
                st.markdown(f"<div class='instruction-text'>📌 Yêu cầu: {q_data['instruction']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='original-sentence'>{q_data['original']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='starter-text'>{q_data['starter']} __________________</div>", unsafe_allow_html=True)
            else:
                # Dành cho các dạng bài tập khác (như điền từ Unit 1)
                st.markdown(f"<div class='instruction-text'>📌 Yêu cầu: {q_data['instruction']}</div>", unsafe_allow_html=True)
                st.markdown(f"<div class='original-sentence'>{q_data['original']}</div>", unsafe_allow_html=True)
            # ---------------------------------------------
            
            user_choice = st.radio("Chọn vế hoàn thành câu chính xác nhất:", q_data["options"], index=None)
            submit_btn = st.form_submit_button("Kiểm tra ✔")
            
            if submit_btn:
                if user_choice:
                    choice_letter = user_choice.split(".")[0]
                    if choice_letter == q_data["a"]:
                        st.success(f"🎉 Chính xác! Đáp án đúng là {q_data['a']}")
                    else:
                        st.error(f"❌ Sai rồi! Đáp án đúng phải là {q_data['a']}")
                    st.info(f"💡 **Giải thích chi tiết:** {q_data['explain']}")
                else:
                    st.warning("⚠️ Vui lòng chọn 1 đáp án trước!")
        
        st.markdown("---")
        col_prev, col_space, col_next = st.columns([1, 2, 1])
        with col_prev:
            if st.button("⬅ Câu trước") and st.session_state.q_index > 0:
                st.session_state.q_index -= 1
                st.rerun()
        with col_next:
            st.markdown('<div style="text-align: right;">', unsafe_allow_html=True)
            if st.button("Câu sau ➡") and st.session_state.q_index < len(exercises) - 1:
                st.session_state.q_index += 1
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
