import streamlit as st

# ==========================================
# NGÂN HÀNG DỮ LIỆU: LÝ THUYẾT, BÀI TẬP, ĐÁP ÁN & GIẢI THÍCH
# Hỗ trợ 2 dạng: "mcq" (Trắc nghiệm) và "text" (Tự luận/Viết lại câu)
# ==========================================
COURSE_DATA = {
    "Unit 1: Social Trends": {
        "theory": """### UNIT 1: SOCIAL TRENDS
**[GRAMMAR FOCUS] - The Present Continuous (Thì hiện tại tiếp diễn)**
*   **Cấu trúc:** Subject + am/is/are + V-ing
*   **Cách dùng:**
    1. Đang diễn ra lúc nói. *(The kids are watching TV)*
    2. Xảy ra xung quanh thời điểm nói. *(Sally is studying hard this week)*
    3. Dự định tương lai gần. *(Polly is coming for dinner tomorrow)*""",
        "exercises": [
            {"type": "mcq", "q": "Jim: Sorry, Mum. I ___ my homework. (DO)", "options": ["A. do", "B. am doing", "C. have done"], "a": "B", "explain": "Hành động đang diễn ra lúc nói. Dùng am + V-ing."},
            {"type": "mcq", "q": "Mum: What ___ your sister ___? (DO)", "options": ["A. does / do", "B. is / doing", "C. has / done"], "a": "B", "explain": "Câu hỏi thì HTTĐ: Tobe + S + V-ing? (Cô ấy đang làm gì lúc này)."},
            {"type": "mcq", "q": "Jim: She ___ a shower. (HAVE)", "options": ["A. has", "B. is having", "C. had"], "a": "B", "explain": "Diễn tả hành động đang tắm ngay thời điểm nói."},
            {"type": "mcq", "q": "Jim: They ___ football. (PLAY)", "options": ["A. are playing", "B. play", "C. played"], "a": "A", "explain": "Hành động đang diễn ra, 'They' đi với 'are' + V-ing."},
            {"type": "mcq", "q": "Mum: But Dad ___ anything. (NOT DO)", "options": ["A. doesn't do", "B. isn't doing", "C. hasn't done"], "a": "B", "explain": "Phủ định của HTTĐ: is not + V-ing."},
            {"type": "mcq", "q": "Dad: Yes, I am. I ___ the paper. (READ)", "options": ["A. read", "B. am reading", "C. reading"], "a": "B", "explain": "Bố đính chính là ông đang đọc báo ngay lúc này."}
        ]
    },
    "Unit 2: The World of Colours": {
        "theory": """### UNIT 2: THE WORLD OF COLOURS
**[GRAMMAR FOCUS] - Conjunctions (Liên từ)**
*   **Coordinating (Kết hợp):** and, but, or, so...
*   **Subordinating (Phụ thuộc):** although, because, if, when...""",
        "exercises": [
            {"type": "mcq", "q": "___ pink was thought to be a stronger color, it was best suited for boys.", "options": ["A. Because", "B. Although", "C. So"], "a": "B", "explain": "Dùng 'Although' (Mặc dù) để chỉ sự nhượng bộ, tương phản giữa quan niệm xưa và nay."},
            {"type": "mcq", "q": "Blue was more delicate ___ dainty for girls.", "options": ["A. and", "B. but", "C. or"], "a": "A", "explain": "Dùng 'and' để nối 2 tính từ cùng trường nghĩa (delicate và dainty)."},
            {"type": "mcq", "q": "Most likely you feel good ___ you wear your favorite color.", "options": ["A. when", "B. so", "C. although"], "a": "A", "explain": "Dùng 'when' (khi) để chỉ điều kiện thời gian."},
            {"type": "mcq", "q": "She wants to look stylish, ___ she decided to dye her hair blonde.", "options": ["A. but", "B. so", "C. if"], "a": "B", "explain": "Dùng 'so' (vì vậy) chỉ kết quả của mệnh đề trước."}
        ]
    },
    "Unit 3: Politeness": {
        "theory": """### UNIT 3: POLITENESS
**[GRAMMAR FOCUS] - Subject-Verb Agreement (Sự hòa hợp Chủ - Vị)**
*   Neither A nor B / Either A or B -> Động từ chia theo B (gần nhất).
*   A along with/as well as B -> Động từ chia theo A (đầu tiên).
*   Every / Each / Someone -> Chia SỐ ÍT.""",
        "exercises": [
            {"type": "mcq", "q": "Both José and Martha ___ on vacation this week.", "options": ["A. is", "B. are", "C. was"], "a": "B", "explain": "'Both A and B' luôn đi với động từ số nhiều."},
            {"type": "mcq", "q": "Every student and parent ___ received a copy of the honor code.", "options": ["A. has", "B. have"], "a": "A", "explain": "Có 'Every' ở đầu câu -> Động từ luôn chia số ít."},
            {"type": "mcq", "q": "Neither my paralegal nor my assistant ___ receiving a letter.", "options": ["A. recalls", "B. recall"], "a": "A", "explain": "Cấu trúc Neither A nor B -> chia theo B (my assistant - số ít)."},
            {"type": "mcq", "q": "The politician, along with the newsmen, ___ expected shortly.", "options": ["A. is", "B. are"], "a": "A", "explain": "Cấu trúc 'A along with B' -> chia theo A (The politician - số ít)."}
        ]
    },
    "Unit 4: Games": {
        "theory": """### UNIT 4: GAMES
**[GRAMMAR FOCUS] - Modals (Động từ khuyết thiếu)**
*   **Must:** Bắt buộc / **Mustn't:** Cấm đoán.
*   **Can/Could:** Khả năng.
*   **May/Might:** Có thể xảy ra (không chắc chắn).""",
        "exercises": [
            {"type": "mcq", "q": "He lost her credit card, so he ___ pay for the meal.", "options": ["A. shouldn't", "B. couldn't", "C. can't"], "a": "B", "explain": "Hành động ở quá khứ (lost), nên dùng 'couldn't' (không thể trong quá khứ)."},
            {"type": "mcq", "q": "They ___ be on holiday but I'm not sure.", "options": ["A. must", "B. may", "C. should"], "a": "B", "explain": "'I'm not sure' chỉ sự không chắc chắn -> dùng may/might."},
            {"type": "mcq", "q": "You ___ enter the country without a visa.", "options": ["A. needn't", "B. mustn't", "C. can't"], "a": "C", "explain": "Luật pháp cấm/không cho phép nhập cảnh thiếu visa -> can't / mustn't đều được, nhưng can't phổ biến hơn để chỉ sự không thể về mặt quy định."}
        ]
    },
    "Unit 5: Family life": {
        "theory": """### UNIT 5: FAMILY LIFE
**[GRAMMAR FOCUS] - Comparative and Superlative (So sánh)**
*   **Ngắn:** +er / +est (taller / tallest).
*   **Dài:** more / most (more expensive / most expensive).""",
        "exercises": [
            {"type": "mcq", "q": "Jeremy is 10. Jenny is 8. Jeremy is ___ than Jenny.", "options": ["A. older", "B. oldest", "C. more old"], "a": "A", "explain": "So sánh hơn của tính từ ngắn 'old' là 'older'."},
            {"type": "mcq", "q": "The Alps are very high. They are ___ mountains in Europe.", "options": ["A. higher", "B. the highest", "C. most high"], "a": "B", "explain": "So sánh nhất trong một tập hợp (châu Âu). Dùng the + adj-est."},
            {"type": "mcq", "q": "A Rolls Royce is ___ than a Twingo.", "options": ["A. expensiver", "B. more expensive", "C. most expensive"], "a": "B", "explain": "So sánh hơn của tính từ dài 'expensive'."}
        ]
    },
    "Supplementary: Tenses (Chia Động Từ)": {
        "theory": "### ÔN TẬP TỔNG HỢP: THÌ TRONG TIẾNG ANH\nLuyện tập khả năng phản xạ và nhận diện dấu hiệu các thì (hiện tại, quá khứ, tương lai hoàn thành...).",
        "exercises": [
            {"type": "mcq", "q": "What time ___ (the meeting/end)?", "options": ["A. does the meeting end", "B. is the meeting ending", "C. has the meeting ended"], "a": "A", "explain": "Hỏi về lịch trình (timetable), dùng thì Hiện tại đơn."},
            {"type": "mcq", "q": "Tomorrow I ___ (visit) my aunt, Sally.", "options": ["A. visit", "B. am visiting", "C. have visited"], "a": "B", "explain": "Kế hoạch đã được sắp xếp từ trước trong tương lai gần -> Hiện tại tiếp diễn mang nghĩa tương lai."},
            {"type": "mcq", "q": "Molly ___ (speak) French but right now she ___ (speak) Spanish.", "options": ["A. is speaking / speaks", "B. speaks / is speaking"], "a": "B", "explain": "Vế 1 là khả năng chung (HT Đơn), vế 2 có 'right now' (HT Tiếp diễn)."},
            {"type": "mcq", "q": "We ___ (not/finish) our history project yet.", "options": ["A. didn't finish", "B. haven't finished", "C. don't finish"], "a": "B", "explain": "Dấu hiệu 'yet' -> Thì Hiện tại hoàn thành."},
            {"type": "mcq", "q": "I'm exhausted. I ___ (train) my stomach muscles all morning.", "options": ["A. trained", "B. have been training", "C. am training"], "a": "B", "explain": "Hành động kéo dài liên tục (all morning) để lại hậu quả hiện tại (exhausted) -> Hiện tại hoàn thành tiếp diễn."},
            {"type": "mcq", "q": "When Melanie came into the office yesterday, her eyes were red and watery. I think she ___ (cry).", "options": ["A. cried", "B. had cried", "C. had been crying"], "a": "C", "explain": "Quá khứ hoàn thành tiếp diễn: hành động khóc kéo dài liên tục TRƯỚC thời điểm quá khứ (came), để lại kết quả mắt đỏ ở quá khứ."},
            {"type": "mcq", "q": "By the time you finish studying, you ___ (master) all twelve tenses.", "options": ["A. will master", "B. will have mastered", "C. mastered"], "a": "B", "explain": "'By the time + HT Đơn' -> Vế chính dùng Tương lai hoàn thành (will have PII)."},
            {"type": "mcq", "q": "A strange thing ___ (happen) while I ___ (come) back.", "options": ["A. happened / came", "B. happened / was coming", "C. was happening / came"], "a": "B", "explain": "Hành động đang diễn ra (was coming) thì hành động khác xen vào (happened)."}
        ]
    },
    "Supplementary: Transformations (Viết lại câu)": {
        "theory": "### ÔN TẬP TỔNG HỢP: VIẾT LẠI CÂU & BỊ ĐỘNG\nBiến đổi cấu trúc câu: Câu điều kiện, Câu bị động, Cấu trúc 'It takes / Spend', Câu gián tiếp.",
        "exercises": [
            {
                "type": "text", 
                "q": "The weather is too terrible for you to go out.\n-> If the weather...", 
                "a": "If the weather weren't too terrible, you could go out. (Hoặc: If the weather were better, you could go out)", 
                "explain": "Tình huống ở hiện tại (is). Viết lại bằng Câu điều kiện loại 2 (trái với hiện tại). Cấu trúc: If S + V(quá khứ), S + would/could + V."
            },
            {
                "type": "text", 
                "q": "They don't play football any more.\n-> They used...", 
                "a": "They used to play football.", 
                "explain": "Cấu trúc 'used to + V': Đã từng làm gì trong quá khứ nhưng nay không còn làm nữa."
            },
            {
                "type": "text", 
                "q": "Someone made this dress in Spain. (Passive Voice)\n-> This dress...", 
                "a": "This dress was made in Spain.", 
                "explain": "Bị động quá khứ đơn: S + was/were + PII. Bỏ 'by someone'."
            },
            {
                "type": "text", 
                "q": "It takes Minh 2 hours to do his homework every day.\n-> Minh spends...", 
                "a": "Minh spends 2 hours doing his homework every day.", 
                "explain": "Cấu trúc tương đương: It takes + sb + time + TO DO sth = S + spend(s) + time + DOING sth."
            },
            {
                "type": "text", 
                "q": "We were late for school because of the heavy rain.\n-> Because it...", 
                "a": "Because it rained heavily, we were late for school.", 
                "explain": "Biến đổi từ cụm danh từ 'because of + N/V-ing' sang mệnh đề 'because + S + V'."
            },
            {
                "type": "text", 
                "q": "He has sent a Christmas postcard. (Passive Voice)\n-> A Christmas postcard...", 
                "a": "A Christmas postcard has been sent by him.", 
                "explain": "Bị động của Hiện tại hoàn thành: S + have/has + BEEN + PII."
            },
            {
                "type": "text", 
                "q": "The children couldn't go swimming because the sea was very rough.\n-> The sea was too...", 
                "a": "The sea was too rough for the children to go swimming.", 
                "explain": "Cấu trúc 'too ... to': S + be + too + adj + (for sb) + to V (quá... đến nỗi không thể làm gì)."
            }
        ]
    }
}

# ==========================================
# CẤU HÌNH GIAO DIỆN APP STREAMLIT
# ==========================================
st.set_page_config(page_title="Chinh Phục Tiếng Anh HOU", page_icon="🎓", layout="wide")

st.markdown("""
<style>
    .stRadio > div { flex-direction: column; }
    .explain-box { padding: 15px; border-radius: 8px; background-color: #e8f4f8; border-left: 5px solid #2980b9; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

# Khởi tạo Session State
if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
if 'current_topic' not in st.session_state:
    st.session_state.current_topic = list(COURSE_DATA.keys())[0]

# --- SIDEBAR NAV ---
st.sidebar.title("🎓 Chuyên Đề HOU - Writing 1")
selected_topic = st.sidebar.radio("Chọn học phần ôn luyện:", list(COURSE_DATA.keys()))

if selected_topic != st.session_state.current_topic:
    st.session_state.current_topic = selected_topic
    st.session_state.q_index = 0
    st.rerun()

topic_data = COURSE_DATA[st.session_state.current_topic]
st.header(f"📖 {st.session_state.current_topic}")

# --- TẠO TABS ---
tab_theory, tab_practice = st.tabs(["📚 Lý Thuyết Cốt Lõi", "✍️ Bài Tập Thực Hành"])

with tab_theory:
    st.markdown(topic_data["theory"])

with tab_practice:
    exercises = topic_data.get("exercises", [])
    
    if not exercises:
        st.info("Hiện chưa có bài tập cho chuyên đề này.")
    else:
        q_data = exercises[st.session_state.q_index]
        
        # Thanh tiến trình
        st.progress((st.session_state.q_index + 1) / len(exercises))
        st.subheader(f"Câu hỏi {st.session_state.q_index + 1} / {len(exercises)}")
        
        # --- XỬ LÝ THEO LOẠI BÀI TẬP (Trắc nghiệm hoặc Tự luận) ---
        with st.form(key=f"exercise_form_{st.session_state.q_index}"):
            st.markdown(f"**{q_data['q']}**")
            
            if q_data["type"] == "mcq":
                # Render Trắc nghiệm
                user_answer = st.radio("Chọn đáp án đúng nhất:", q_data["options"], index=None)
                submit_btn = st.form_submit_button("Nộp bài & Xem giải thích")
                
                if submit_btn:
                    if user_answer:
                        choice_letter = user_answer.split(".")[0]
                        if choice_letter == q_data["a"]:
                            st.success(f"🎉 Rất xuất sắc! Đáp án chuẩn: {q_data['a']}")
                        else:
                            st.error(f"❌ Rất tiếc! Đáp án đúng là: {q_data['a']}")
                        st.markdown(f"<div class='explain-box'>💡 <b>Giải thích chi tiết:</b><br>{q_data['explain']}</div>", unsafe_allow_html=True)
                    else:
                        st.warning("⚠️ Bạn chưa chọn đáp án!")
                        
            elif q_data["type"] == "text":
                # Render Tự luận / Viết lại câu
                user_text = st.text_input("Gõ câu trả lời của bạn vào đây:")
                submit_btn = st.form_submit_button("Kiểm tra đáp án")
                
                if submit_btn:
                    if user_text.strip():
                        st.info(f"🔑 **Đáp án gợi ý:** {q_data['a']}")
                        st.markdown(f"<div class='explain-box'>💡 <b>Cấu trúc sử dụng:</b><br>{q_data['explain']}</div>", unsafe_allow_html=True)
                        st.write("*(Với dạng tự luận, hệ thống chỉ đưa ra đáp án chuẩn và cấu trúc để bạn tự đối chiếu, vì cách diễn đạt có thể linh hoạt)*")
                    else:
                        st.warning("⚠️ Vui lòng nhập câu trả lời trước khi kiểm tra!")
        
        st.markdown("---")
        
        # --- NÚT ĐIỀU HƯỚNG ---
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
