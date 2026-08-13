import streamlit as st

# ==========================================
# FULL DATABASE: UNIT 1-5 & REWRITES (BỐ CỤC CHUẨN)
# ==========================================
COURSE_DATA = {
    "Unit 1: Social Trends": {
        "theory": "### UNIT 1: SOCIAL TRENDS\n**The Present Continuous (Thì hiện tại tiếp diễn)**\n- Cấu trúc: S + am/is/are + V-ing\n- Cách dùng: Đang diễn ra lúc nói; Xung quanh thời điểm nói; Dự định tương lai gần.",
        "exercises": [
            {"type": "mcq", "instruction": "Put the verbs in the correct form of the Present Continuous.", "original": "1. Jim, can you help me? - Sorry, Mum. I ___ my homework. (DO)", "starter": "", "options": ["A. am doing", "B. do", "C. is doing", "D. have done"], "a": "A", "explain": "Hành động đang xảy ra tại thời điểm nói. I + am + V-ing."},
            {"type": "mcq", "instruction": "Put the verbs in the correct form of the Present Continuous.", "original": "2. What ___ your sister ___? (DO)", "starter": "", "options": ["A. does / do", "B. is / doing", "C. has / done", "D. was / doing"], "a": "B", "explain": "Câu hỏi thì HTTĐ: Tobe + S + V-ing?"},
            {"type": "mcq", "instruction": "Put the verbs in the correct form of the Present Continuous.", "original": "3. She ___ a shower. (HAVE)", "starter": "", "options": ["A. has", "B. have", "C. is having", "D. had"], "a": "C", "explain": "Diễn tả hành động đang tắm ngay thời điểm nói."},
            {"type": "mcq", "instruction": "Put the verbs in the correct form of the Present Continuous.", "original": "4. And what ___ Gary and Sam ___? (DO)", "starter": "", "options": ["A. do / do", "B. are / doing", "C. is / doing", "D. have / done"], "a": "B", "explain": "Chủ ngữ số nhiều (Gary and Sam) dùng 'are'."},
            {"type": "mcq", "instruction": "Put the verbs in the correct form of the Present Continuous.", "original": "5. They ___ football. (PLAY)", "starter": "", "options": ["A. play", "B. played", "C. is playing", "D. are playing"], "a": "D", "explain": "They + are + V-ing."},
            {"type": "mcq", "instruction": "Put the verbs in the correct form of the Present Continuous.", "original": "6. But Dad ___ anything. (NOT DO)", "starter": "", "options": ["A. doesn't do", "B. isn't doing", "C. not doing", "D. hasn't done"], "a": "B", "explain": "Phủ định của HTTĐ: is not + V-ing."},
            {"type": "mcq", "instruction": "Put the verbs in the correct form of the Present Continuous.", "original": "7. Yes, I am. I ___ the paper. (READ)", "starter": "", "options": ["A. read", "B. am reading", "C. is reading", "D. reading"], "a": "B", "explain": "I + am + V-ing."}
        ]
    },
    "Unit 2: The World of Colours": {
        "theory": "### UNIT 2: THE WORLD OF COLOURS\n**Conjunctions (Liên từ)**\n- Coordinating (Kết hợp): and, but, or, so, yet...\n- Subordinating (Phụ thuộc): although, because, if, when...",
        "exercises": [
            {"type": "mcq", "instruction": "Fill in each blank with a conjunction given.", "original": "1. ___ pink was thought to be a stronger color, it was best suited for boys.", "starter": "", "options": ["A. Because", "B. Although", "C. So", "D. If"], "a": "B", "explain": "Dùng 'Although' (Mặc dù) để chỉ sự nhượng bộ, tương phản."},
            {"type": "mcq", "instruction": "Fill in each blank with a conjunction given.", "original": "2. Blue was more delicate ___ dainty for girls.", "starter": "", "options": ["A. and", "B. but", "C. or", "D. so"], "a": "A", "explain": "Dùng 'and' để nối 2 tính từ cùng trường nghĩa tích cực (delicate và dainty)."},
            {"type": "mcq", "instruction": "Fill in each blank with a conjunction given.", "original": "3. Red ___ pink saris are the most popular colors for brides.", "starter": "", "options": ["A. so", "B. because", "C. and", "D. but"], "a": "C", "explain": "Nối 2 danh từ đồng đẳng (Red và pink)."},
            {"type": "mcq", "instruction": "Fill in each blank with a conjunction given.", "original": "4. Most likely you feel good ___ you wear your favorite color.", "starter": "", "options": ["A. when", "B. although", "C. or", "D. but"], "a": "A", "explain": "Dùng 'when' (khi) để chỉ điều kiện thời gian."},
            {"type": "mcq", "instruction": "Fill in each blank with a conjunction given.", "original": "5. ___ black symbolizes death in Western cultures, it is associated with powerful forces.", "starter": "", "options": ["A. Because", "B. So", "C. Although", "D. Or"], "a": "C", "explain": "Mệnh đề chỉ sự tương phản (Mặc dù...)."},
            {"type": "mcq", "instruction": "Fill in each blank with a conjunction given.", "original": "6. ___ you see a young lady in violet, it is her, my mistress.", "starter": "", "options": ["A. If", "B. So", "C. But", "D. Although"], "a": "A", "explain": "Câu điều kiện: NẾU bạn thấy..."},
            {"type": "mcq", "instruction": "Fill in each blank with a conjunction given.", "original": "7. People think pink is for girls, ___ it isn't always this way.", "starter": "", "options": ["A. so", "B. but", "C. and", "D. if"], "a": "B", "explain": "Chỉ sự trái ngược: NGƯỜI TA nghĩ vậy, NHƯNG không phải lúc nào cũng vậy."},
            {"type": "mcq", "instruction": "Fill in each blank with a conjunction given.", "original": "8. She wants to look stylish, ___ she decided to dye her hair blonde.", "starter": "", "options": ["A. but", "B. and", "C. so", "D. if"], "a": "C", "explain": "Dùng 'so' (vì vậy) chỉ kết quả của vế trước."}
        ]
    },
    "Unit 3: Politeness": {
        "theory": "### UNIT 3: POLITENESS\n**Subject-Verb Agreement (Sự hòa hợp Chủ - Vị)**\n- Neither A nor B / Either A or B -> Động từ chia theo B (gần nhất).\n- A along with/as well as B -> Động từ chia theo A (đầu tiên).\n- Every / Each -> Chia SỐ ÍT.",
        "exercises": [
            {"type": "mcq", "instruction": "Choose the correct verb in the parentheses.", "original": "1. Both José and Martha (is, are) ___ on vacation this week.", "starter": "", "options": ["A. is", "B. are"], "a": "B", "explain": "'Both A and B' luôn đi với động từ số nhiều."},
            {"type": "mcq", "instruction": "Choose the correct verb in the parentheses.", "original": "2. Every student and parent (has, have) ___ received a copy of the honor code.", "starter": "", "options": ["A. has", "B. have"], "a": "A", "explain": "Có 'Every' ở đầu câu -> Động từ luôn chia số ít."},
            {"type": "mcq", "instruction": "Choose the correct verb in the parentheses.", "original": "3. What they need (is, are) ___ step-by-step procedures.", "starter": "", "options": ["A. is", "B. are"], "a": "A", "explain": "Mệnh đề danh ngữ 'What they need' đóng vai trò chủ ngữ -> Động từ số ít."},
            {"type": "mcq", "instruction": "Choose the correct verb in the parentheses.", "original": "4. Either the original or a photocopy (is, are) ___ acceptable as proof.", "starter": "", "options": ["A. is", "B. are"], "a": "A", "explain": "Either A or B -> Chia theo B (a photocopy là số ít)."},
            {"type": "mcq", "instruction": "Choose the correct verb in the parentheses.", "original": "5. Neither my paralegal nor my assistant (recalls, recall) ___ receiving a letter.", "starter": "", "options": ["A. recalls", "B. recall"], "a": "A", "explain": "Neither A nor B -> Chia theo B (my assistant là số ít)."},
            {"type": "mcq", "instruction": "Choose the correct verb in the parentheses.", "original": "6. Neither the union leader nor the negotiators (has, have) ___ clearly explained.", "starter": "", "options": ["A. has", "B. have"], "a": "B", "explain": "Chia theo B (the negotiators là SỐ NHIỀU -> have)."},
            {"type": "mcq", "instruction": "Choose the correct verb in the parentheses.", "original": "7. Neither you nor she (is, are, am) ___ aware of all the implications.", "starter": "", "options": ["A. is", "B. are", "C. am"], "a": "A", "explain": "Chia theo B (she -> is)."},
            {"type": "mcq", "instruction": "Choose the correct verb in the parentheses.", "original": "8. The model shown in the recent catalog and advertisements (is, are) ___ not the model I want.", "starter": "", "options": ["A. is", "B. are"], "a": "A", "explain": "Chủ ngữ chính là 'The model' (số ít). Phần 'shown...' chỉ là mệnh đề rút gọn."},
            {"type": "mcq", "instruction": "Choose the correct verb in the parentheses.", "original": "9. The members of the committee (has, have) ___ met to discuss the morale problem.", "starter": "", "options": ["A. has", "B. have"], "a": "B", "explain": "Chủ ngữ chính là 'The members' (số nhiều)."},
            {"type": "mcq", "instruction": "Choose the correct verb in the parentheses.", "original": "10. The committee (has, have) ___ met to discuss the morale problem.", "starter": "", "options": ["A. has", "B. have"], "a": "A", "explain": "Danh từ tập hợp 'The committee' hành động như một thể thống nhất -> số ít."}
        ]
    },
    "Unit 4: Games": {
        "theory": "### UNIT 4: GAMES\n**Modals (Động từ khuyết thiếu)**\n- Must: Sự bắt buộc / Mustn't: Cấm đoán.\n- Can/Could: Khả năng, sự cho phép.\n- May/Might: Khả năng có thể xảy ra nhưng không chắc.",
        "exercises": [
            {"type": "mcq", "instruction": "Circle the best answer.", "original": "1. He lost her credit card, so he ___ pay for the meal.", "starter": "", "options": ["A. shouldn't", "B. couldn't", "C. can't", "D. wouldn't"], "a": "B", "explain": "Hành động 'lost' ở quá khứ -> Dùng couldn't (không thể trong quá khứ)."},
            {"type": "mcq", "instruction": "Circle the best answer.", "original": "2. They ___ be on holiday but I'm not sure.", "starter": "", "options": ["A. can", "B. must", "C. may", "D. should"], "a": "C", "explain": "'but I'm not sure' chỉ sự không chắc chắn -> dùng may/might."},
            {"type": "mcq", "instruction": "Circle the best answer.", "original": "3. You ___ enter the country without a visa.", "starter": "", "options": ["A. can", "B. must", "C. need", "D. can't"], "a": "D", "explain": "Luật pháp cấm nhập cảnh thiếu visa -> can't / mustn't. (Lưu ý: trong các đáp án PDF đưa ra không có mustn't, nên chọn từ mang nghĩa phủ định phù hợp nhất là can't hoặc mustn't nếu có)."},
            {"type": "mcq", "instruction": "Circle the best answer.", "original": "4. ___ you turn it down a bit, please!", "starter": "", "options": ["A. Can", "B. Can't", "C. Should", "D. Shouldn't"], "a": "A", "explain": "Đưa ra lời yêu cầu lịch sự: Can/Could you..."},
            {"type": "mcq", "instruction": "Circle the best answer.", "original": "5. ___ you speak Japanese?", "starter": "", "options": ["A. May", "B. Could", "C. Should", "D. Can"], "a": "D", "explain": "Hỏi về khả năng (ability) -> Can."}
        ]
    },
    "Unit 5: Family life": {
        "theory": "### UNIT 5: FAMILY LIFE\n**Comparative and Superlative (So sánh)**\n- Tính từ 1 âm tiết: +er / +est (taller / tallest).\n- Tính từ 2 âm tiết (tận cùng y, le, ow, er): +er / +est.\n- Tính từ 3 âm tiết trở lên: more / most.",
        "exercises": [
            {"type": "mcq", "instruction": "Complete the sentences with the correct form of the adjective.", "original": "1. Jeremy is 10. Jenny is 8. Jeremy is (old) ___ than Jenny.", "starter": "", "options": ["A. older", "B. oldest", "C. more old", "D. most old"], "a": "A", "explain": "So sánh giữa 2 người (có 'than'). Tính từ ngắn 'old' + đuôi 'er' -> older."},
            {"type": "mcq", "instruction": "Complete the sentences with the correct form of the adjective.", "original": "2. The Alps are very high. They are (high) ___ mountains in Europe.", "starter": "", "options": ["A. higher", "B. high", "C. the highest", "D. most high"], "a": "C", "explain": "So sánh nhất trong một khu vực (in Europe). Tính từ ngắn + est."},
            {"type": "mcq", "instruction": "Complete the sentences with the correct form of the adjective.", "original": "3. An ocean is (large) ___ a sea.", "starter": "", "options": ["A. larger than", "B. the largest", "C. more large", "D. large than"], "a": "A", "explain": "Tính từ kết thúc bằng 'e' (large) -> chỉ thêm 'r' (larger). Có 'than' vì so sánh 2 vật."},
            {"type": "mcq", "instruction": "Complete the sentences with the correct form of the adjective.", "original": "4. A Rolls Royce costs a lot of money. It is (expensive) ___ a Twingo.", "starter": "", "options": ["A. expensiver than", "B. more expensive than", "C. most expensive", "D. expensive than"], "a": "B", "explain": "Tính từ dài (expensive) -> dùng more + adj + than."},
            {"type": "mcq", "instruction": "Complete the sentences with the correct form of the adjective.", "original": "5. John's results were high. Fred's results were (low) ___ John's.", "starter": "", "options": ["A. the lowest", "B. lower than", "C. more low than", "D. low than"], "a": "B", "explain": "So sánh hơn: lower than."},
            {"type": "mcq", "instruction": "Complete the sentences with the correct form of the adjective.", "original": "6. This exercise is not very difficult. It's (easy) ___ I expected.", "starter": "", "options": ["A. easiest", "B. more easy than", "C. easier than", "D. easy than"], "a": "C", "explain": "Tận cùng là 'y' -> đổi thành 'i' rồi thêm 'er' (easier)."},
            {"type": "mcq", "instruction": "Complete the sentences with the correct form of the adjective.", "original": "7. The weather is not good. I hope the weather will be (nice) ___ next week.", "starter": "", "options": ["A. nicest", "B. more nice", "C. nicer", "D. the nicer"], "a": "C", "explain": "Tận cùng bằng 'e' -> thêm 'r' (nicer). Ý ngầm so sánh tuần sau với tuần này."},
            {"type": "mcq", "instruction": "Complete the sentences with the correct form of the adjective.", "original": "8. People are usually (friendly) ___ in small towns.", "starter": "", "options": ["A. friendliest", "B. friendlier", "C. more friendly", "D. B & C đều đúng"], "a": "D", "explain": "'Friendly' là trường hợp đặc biệt, có thể dùng 'friendlier' hoặc 'more friendly' đều được chấp nhận."}
        ]
    },
    "Supp: Rewrites & Passive Voice": {
        "theory": "### ÔN TẬP: VIẾT LẠI CÂU & CÂU BỊ ĐỘNG\nĐã chuyển đổi sang định dạng trắc nghiệm bám sát cấu trúc thi.",
        "exercises": [
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "1. The weather is too terrible for you to go out.", "starter": "→ If the weather...", "options": ["A. wasn't terrible, you can go out.", "B. weren't too terrible, you could go out.", "C. is not terrible, you could go out.", "D. had not been terrible, you could have gone out."], "a": "B", "explain": "Thực tế ở hiện tại (is terrible) -> Dùng Câu điều kiện loại 2 (trái với hiện tại): If + S + weren't, S + could/would + V."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "2. All the students have to take the final exam.", "starter": "→ The final exam...", "options": ["A. has to be taken by all the students.", "B. have to be taken by all the students.", "C. is taken by all the students.", "D. had to be taken by all the students."], "a": "A", "explain": "Bị động của have to: S + have/has to be + PII. 'The final exam' (số ít) -> has to be taken."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "3. Please don't repeat what I said.", "starter": "→ Would you mind...", "options": ["A. not to repeat what I said?", "B. not repeating what I said?", "C. don't repeat what I said?", "D. to not repeat what I said?"], "a": "B", "explain": "Cấu trúc: Would you mind + (not) + V-ing? (Bạn có phiền nếu không...)."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "4. I can't swim as well as my friend can.", "starter": "→ My friend...", "options": ["A. can swim as well as I can.", "B. can't swim better than me.", "C. can swim better than I can.", "D. swims worse than I do."], "a": "C", "explain": "So sánh không bằng ('can't swim as well as') -> viết lại thành so sánh hơn ('can swim better than')."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "5. We lost our way. We didn't arrive on time.", "starter": "→ Unless...", "options": ["A. we had lost our way, we would have arrived on time.", "B. we lost our way, we would arrive on time.", "C. we had not lost our way, we wouldn't have arrived.", "D. we didn't lose our way, we arrived on time."], "a": "A", "explain": "Sự việc ở quá khứ -> Dùng CĐK loại 3. Unless = If... not. Câu gốc: Nếu chúng ta KHÔNG bị lạc (Unless we had lost our way)."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "6. It took me three hours to open the door.", "starter": "→ I spent...", "options": ["A. three hours to open the door.", "B. three hours opening the door.", "C. three hours open the door.", "D. me three hours opening the door."], "a": "B", "explain": "It took + sb + time + to V = S + spent + time + V-ing."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "7. The film was too boring for you to watch.", "starter": "→ The film was so...", "options": ["A. boring that you couldn't watch it.", "B. boring that you can watch it.", "C. boring for you to watch it.", "D. boring that you couldn't watch."], "a": "A", "explain": "Cấu trúc quá... đến nỗi mà: S + be + so + adj + that + S + V. Lưu ý mệnh đề sau 'that' phải có tân ngữ 'it'."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "8. They don't play football any more.", "starter": "→ They used...", "options": ["A. to play football.", "B. to playing football.", "C. play football.", "D. not to play football."], "a": "A", "explain": "Cấu trúc 'used to + V-bare' chỉ thói quen trong quá khứ nay không còn nữa."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "9. It takes Minh 2 hours to do his homework every day.", "starter": "→ Minh spends...", "options": ["A. 2 hours to do his homework every day.", "B. 2 hours doing his homework every day.", "C. 2 hours does his homework every day.", "D. 2 hours do his homework every day."], "a": "B", "explain": "Tương tự câu 6: It takes... to V = spend... V-ing."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "10. We were late for school because of the heavy rain.", "starter": "→ Because it...", "options": ["A. rains heavily, we were late for school.", "B. rained heavily, we were late for school.", "C. was heavy rain, we were late for school.", "D. rained heavy, we were late for school."], "a": "B", "explain": "Chuyển cụm danh từ 'the heavy rain' thành mệnh đề 'it rained heavily'."},
            {"type": "rewrite", "instruction": "Rewrite the sentences in the passive voice.", "original": "11. I have eaten many sweets.", "starter": "→ Many sweets...", "options": ["A. have been eaten by me.", "B. has been eaten by me.", "C. was eaten by me.", "D. had been eaten by me."], "a": "A", "explain": "Bị động thì HT Hoàn Thành: S + have/has + been + PII. (Many sweets số nhiều -> have)."},
            {"type": "rewrite", "instruction": "Rewrite the sentences in the passive voice.", "original": "12. This famous director will produce ten short comedy films.", "starter": "→ Ten short comedy films...", "options": ["A. will produce by this famous director.", "B. will be produced by this famous director.", "C. would be produced by this famous director.", "D. will be producing by this famous director."], "a": "B", "explain": "Bị động của Tương lai đơn (will): S + will be + PII."}
        ]
    }
}

# ==========================================
# STREAMLIT UI CODE - BỐ CỤC CHUẨN PDF
# ==========================================
st.set_page_config(page_title="HOU - Writing 1 App", page_icon="🎓", layout="wide")

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
            
            # --- RENDER BỐ CỤC CHUẨN PDF ---
            st.markdown(f"<div class='instruction-text'>📌 Yêu cầu: {q_data['instruction']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='original-sentence'>{q_data['original']}</div>", unsafe_allow_html=True)
            
            if q_data.get("type") == "rewrite":
                st.markdown(f"<div class='starter-text'>{q_data['starter']} __________________</div>", unsafe_allow_html=True)
            # -------------------------------
            
            user_choice = st.radio("Chọn đáp án chính xác nhất:", q_data["options"], index=None)
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
