import streamlit as st

# ==========================================
# TOÀN BỘ DỮ LIỆU TỪ FILE PDF ĐƯỢC SỐ HÓA
# ==========================================
COURSE_DATA = {
    "Unit 1: Social Trends": {
        "theory": """### UNIT 1: SOCIAL TRENDS
**[GRAMMAR FOCUS] - The Present Continuous (Thì hiện tại tiếp diễn)**
*   **Cấu trúc:** Subject + Be (am/is/are) + Verb-ing
*   **Cách dùng:**
    1.  Hành động đang diễn ra ngay lúc nói (Activities happening now).
        *VD: The kids are watching TV. / What are you writing?*
    2.  Hành động xảy ra xung quanh thời điểm nói (Activities happening around now).
        *VD: Sally is studying hard for her exams this week.*
    3.  Dự định trong tương lai gần (Near future, planned events).
        *VD: Polly is coming for dinner tomorrow.*

**[SKILLS FOCUS] - Writing a Topic Sentence (Viết câu chủ đề)**
*   Topic sentence là câu quan trọng nhất, cho biết toàn bộ đoạn văn nói về cái gì.
*   **Các bước:** 
    1. Nghĩ về chủ đề.
    2. Tìm từ khóa. 
    3. Viết một câu hoàn chỉnh giới thiệu ý chính sử dụng từ khóa.""",
        "exercises": [
            {"q": "Sorry, Mum. I (do) ___ my homework.", "a": "am doing"},
            {"q": "What ___ (your sister/do)?", "a": "is your sister doing"},
            {"q": "She (have) ___ a shower.", "a": "is having"},
            {"q": "And what ___ (Gary and Sam/do)?", "a": "are Gary and Sam doing"},
            {"q": "They (play) ___ football.", "a": "are playing"},
            {"q": "But Dad (not do) ___ anything.", "a": "isn't doing"},
            {"q": "Yes, I am. I (read) ___ the paper.", "a": "am reading"}
        ]
    },
    "Unit 2: The World of Colours": {
        "theory": """### UNIT 2: THE WORLD OF COLOURS
**[GRAMMAR FOCUS] - Conjunctions (Liên từ)**
Được dùng để nối các từ hoặc nhóm từ. Phân loại:
1.  **Coordinating (Liên từ kết hợp):** and, but, or, nor, for, so, yet.
    *VD: He can't sing but he can dance very well.*
2.  **Correlative (Liên từ tương quan):** either...or, neither...nor, not only...but also.
    *VD: The house is not only big but also nice.*
3.  **Subordinating (Liên từ phụ thuộc):** after, although, if, because, until, when, where, whether...
    *VD: I will give her the book if I see her.*

**[SKILLS FOCUS] - Free Writing (Viết tự do)**
*   Là cách để động não (brainstorm) trước khi viết.
*   Viết liên tục trong 10-20 phút, không sửa lỗi, viết bất cứ thứ gì nảy ra trong đầu.""",
        "exercises": [
            {"q": "___ pink was thought to be a stronger color, it was best suited for boys. (although/and/if)", "a": "although"},
            {"q": "Blue was more delicate ___ dainty for girls. (so/and/or)", "a": "and"},
            {"q": "Most likely you feel good ___ you wear your favorite color. (when/so/but)", "a": "when"},
            {"q": "People think pink is for girls, ___ it isn't always this way. (so/but/because)", "a": "but"}
        ]
    },
    "Unit 3: Politeness": {
        "theory": """### UNIT 3: POLITENESS
**[GRAMMAR FOCUS] - Subject-Verb Agreement (Sự hòa hợp Chủ - Vị)**
Quy tắc đặc biệt:
*   Nối bằng "or/nor": Động từ chia theo chủ ngữ gần nhất.
*   Nối bằng "either..or/neither..nor": Động từ chia theo chủ ngữ gần nhất.
*   Nối bằng "along with, as well as": Động từ chia theo chủ ngữ ĐẦU TIÊN.
*   Đại từ bất định (each, everyone, someone...): Động từ chia SỐ ÍT.
*   Phần trăm, phân số (percent, fraction...): Xét danh từ sau giới từ "of".
*   "The number of" + V(số ít) / "A number of" + V(số nhiều).
*   Tiền bạc, thời gian, tên sách: Động từ chia SỐ ÍT.

**[SKILLS FOCUS] - Supporting Main Idea with Examples (Hỗ trợ ý chính bằng ví dụ)**
*   Ví dụ cụ thể là bằng chứng mạnh mẽ nhất. 
*   Giúp chứng minh tính hợp lý cho câu luận điểm của bạn.""",
        "exercises": [
            {"q": "Both José and Martha (is/are) ___ on vacation this week.", "a": "are"},
            {"q": "Every student and parent (has/have) ___ received a copy of the honor code.", "a": "has"},
            {"q": "Either the original or a photocopy (is/are) ___ acceptable.", "a": "is"},
            {"q": "Neither you nor she (is/are/am) ___ aware of the implications.", "a": "is"},
            {"q": "The number of people we need to hire (is/are) ___ thirteen.", "a": "is"}
        ]
    },
    "Unit 4: Games": {
        "theory": """### UNIT 4: GAMES
**[GRAMMAR FOCUS] - Modals (Động từ khuyết thiếu)**
*   **Can/Could:** Khả năng, sự cho phép (Could là quá khứ của Can).
*   **Must:** Sự bắt buộc cá nhân, sự chắc chắn (Mustn't = cấm đoán).
*   **May/Might:** Khả năng có thể xảy ra (không chắc chắn).
*   **Can't:** Chắc chắn không thể xảy ra.
*   **Needn't:** Không cần thiết phải làm gì.
*   **Shall:** Dùng trong câu hỏi "Shall I/we...?" để đưa ra lời đề nghị.

**[SKILLS FOCUS] - Writing an Opinion Paragraph (Viết đoạn văn nêu ý kiến)**
Cấu trúc 3 phần:
1.  **Topic Sentence:** Nêu rõ quan điểm Đồng ý/Không đồng ý.
2.  **Reasons + Supporting details:** Đưa ra lý do (First, Secondly...) và chi tiết.
3.  **Concluding Sentence:** Câu kết luận (To sum up, In conclusion...).""",
        "exercises": [
            {"q": "He lost her credit card, so he ___ pay for the meal. (can't/couldn't/shouldn't)", "a": "couldn't"},
            {"q": "They ___ be on holiday but I'm not sure. (must/may/can)", "a": "may"},
            {"q": "You ___ enter the country without a visa. It's prohibited. (mustn't/can't/needn't)", "a": "can't"},
            {"q": "___ you speak Japanese? (May/Could/Can)", "a": "Can"}
        ]
    },
    "Unit 5: Family life": {
        "theory": """### UNIT 5: FAMILY LIFE
**[GRAMMAR FOCUS] - Comparative and Superlative (So sánh hơn & So sánh nhất)**
1.  **Tính từ 1 âm tiết:** 
    *   Hơn: Thêm "-er" (taller)
    *   Nhất: Thêm "-est" (tallest)
    *   *Quy tắc gấp đôi phụ âm: big -> bigger -> biggest.*
2.  **Tính từ 2 âm tiết:**
    *   Thường dùng: more/most (more peaceful)
    *   Tận cùng "y": đổi "y" thành "ier/iest" (happier/happiest).
    *   Tận cùng "er, le, ow": thêm er/est (narrower, gentler).
3.  **Tính từ 3 âm tiết trở lên:** Luôn dùng more/most (more intelligent).

**[SKILLS FOCUS] - Writing a Personal Letter (Viết thư cá nhân)**
Cấu trúc:
1. Địa chỉ người gửi (Góc phải trên)
2. Ngày tháng (Dưới địa chỉ)
3. Lời chào (Dear, Hi...)
4. Nội dung chính
5. Lời kết (Love, Regards...)
6. Chữ ký
7. Tái bút (P/S - nếu có)""",
        "exercises": [
            {"q": "Jeremy is 10. Jenny is 8. Jeremy is (old) ___ than Jenny.", "a": "older"},
            {"q": "The Alps are very high. They are the (high) ___ mountains in Europe.", "a": "highest"},
            {"q": "An ocean is (large) ___ than a sea.", "a": "larger"},
            {"q": "A Rolls Royce is (expensive) ___ than a Twingo.", "a": "more expensive"},
            {"q": "This exercise is not very difficult. It's (easy) ___ than I expected.", "a": "easier"}
        ]
    },
    "Supplementary (Ôn Tập Tổng Hợp)": {
        "theory": """### SUPPLEMENTARY PRACTICE
Phần này tổng hợp các kiến thức nâng cao, đặc biệt tập trung vào:
1. Sự phối hợp thì (Tenses mix).
2. Câu bị động (Passive Voice).
3. Viết lại câu (Sentence Transformation - If, Unless, Wish, Reported Speech).""",
        "exercises": [
            {"q": "What time ___ (the meeting/end)?", "a": "does the meeting end"},
            {"q": "Tomorrow I ___ (visit) my aunt, Sally.", "a": "am visiting"},
            {"q": "Molly ___ (speak) French but right now she is speaking Spanish.", "a": "speaks"},
            {"q": "We ___ (not/finish) our history project yet.", "a": "haven't finished"},
            {"q": "Look! It ___ (rain) so we can't go to the beach.", "a": "is raining"},
            {"q": "When Melanie came into the office yesterday, her eyes were red. I think she ___ (cry).", "a": "had been crying"},
            {"q": "After Larry ___ (see) the film on TV, he decided to buy the book.", "a": "had seen"},
            {"q": "This time next week he ___ (fly) to South Africa.", "a": "will be flying"},
            {"q": "Rewrite: The weather is too terrible for you to go out. -> If the weather ___", "a": "were not terrible, you could go out"},
            {"q": "Passive: Someone made this dress in Spain. -> This dress ___", "a": "was made in Spain"}
        ]
    }
}

# ==========================================
# CẤU HÌNH GIAO DIỆN STREAMLIT
# ==========================================
st.set_page_config(page_title="Writing 1 - English App", layout="wide")

# Khởi tạo biến trạng thái (Session State) để theo dõi bài học và câu hỏi hiện tại
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
if 'current_unit' not in st.session_state:
    st.session_state.current_unit = list(COURSE_DATA.keys())[0]

# --- THANH ĐIỀU HƯỚNG BÊN TRÁI (SIDEBAR) ---
st.sidebar.title("📚 Danh Sách Bài Học")
selected_unit = st.sidebar.radio("Chọn Unit để học:", list(COURSE_DATA.keys()))

# Nếu người dùng đổi Unit, reset lại số thứ tự câu hỏi về 0
if selected_unit != st.session_state.current_unit:
    st.session_state.current_unit = selected_unit
    st.session_state.q_index = 0
    st.rerun()

unit_data = COURSE_DATA[st.session_state.current_unit]
st.header(f"📖 {st.session_state.current_unit}")

# --- TẠO 2 TAB: LÝ THUYẾT VÀ THỰC HÀNH ---
tab1, tab2 = st.tabs(["Lý Thuyết (Theory)", "Thực Hành (Practice)"])

with tab1:
    st.markdown(unit_data["theory"])

with tab2:
    exercises = unit_data.get("exercises", [])
    
    if not exercises:
        st.info("Hiện chưa có bài tập cho phần này.")
    else:
        q_data = exercises[st.session_state.q_index]
        
        # Hiển thị câu hỏi
        st.subheader(f"Câu {st.session_state.q_index + 1} / {len(exercises)}")
        st.markdown(f"**{q_data['q']}**")
        
        # Ô nhập đáp án (dùng form để khi nhấn Enter không bị load lại trang sai cách)
        with st.form(key="answer_form", clear_on_submit=False):
            user_answer = st.text_input("Nhập đáp án của bạn:")
            submit_btn = st.form_submit_button("Kiểm tra ✔")
            
            if submit_btn:
                if user_answer.strip().lower() == q_data["a"].strip().lower():
                    st.success("🎉 Chính xác!")
                else:
                    st.error("❌ Sai rồi, hãy kiểm tra lại nhé!")
        
        st.markdown("---")
        
        # Cụm nút điều hướng
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("⬅ Câu trước"):
                if st.session_state.q_index > 0:
                    st.session_state.q_index -= 1
                    st.rerun()
        
        with col2:
            if st.button("👀 Hiện Đáp Án"):
                st.warning(f"Đáp án đúng: **{q_data['a']}**")
                
        with col3:
            # Khoảng trống để căn chỉnh nút
            pass 
            
        with col4:
            if st.button("Câu sau ➡"):
                if st.session_state.q_index < len(exercises) - 1:
                    st.session_state.q_index += 1
                    st.rerun()
