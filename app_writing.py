import streamlit as st
from groq import Groq

# ==========================================
# 1. DATABASE LÕI & DATA PHẦN 1
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
            {"type": "mcq", "instruction": "Circle the best answer.", "original": "3. You ___ enter the country without a visa.", "starter": "", "options": ["A. can", "B. must", "C. need", "D. can't"], "a": "D", "explain": "Luật pháp cấm nhập cảnh thiếu visa -> can't (không thể/không được phép)."},
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
            {"type": "mcq", "instruction": "Complete the sentences with the correct form of the adjective.", "original": "8. People are usually (friendly) ___ in small towns.", "starter": "", "options": ["A. friendliest", "B. friendlier", "C. more friendly", "D. Cả B & C đều đúng"], "a": "D", "explain": "'Friendly' là trường hợp đặc biệt, có thể dùng 'friendlier' hoặc 'more friendly' đều được chấp nhận."},
            {"type": "mcq", "instruction": "Complete the sentences with the correct form of the adjective.", "original": "9. In the government of a country, the President is (important) ___ person.", "starter": "", "options": ["A. more important", "B. most important", "C. the most important", "D. importanter"], "a": "C", "explain": "So sánh nhất của tính từ dài: the most + adj."},
            {"type": "mcq", "instruction": "Complete the sentences with the correct form of the adjective.", "original": "10. People say that Chinese is (difficult) ___ to learn than English.", "starter": "", "options": ["A. most difficult", "B. difficult", "C. the most difficult", "D. more difficult"], "a": "D", "explain": "So sánh hơn (có 'than') của tính từ dài: more + adj."}
        ]
    },
    "Supp: Verb Forms (Part 1)": {
        "theory": "### SUPPLEMENTARY: VERB FORMS (Part 1)\nÔn tập chia động từ từ câu 1 đến câu 40.",
        "exercises": [
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "1. What time ___ (the meeting/end)?", "starter": "", "options": ["A. does the meeting end", "B. is the meeting ending", "C. has the meeting ended", "D. will the meeting end"], "a": "A", "explain": "Hỏi về lịch trình cố định, dùng Hiện tại đơn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "2. Tomorrow I ___ (visit) my aunt, Sally.", "starter": "", "options": ["A. visit", "B. am visiting", "C. visited", "D. was visiting"], "a": "B", "explain": "Kế hoạch đã định trong tương lai gần -> Hiện tại tiếp diễn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "3. Molly ___ (speak) French but right now she ___ (speak) Spanish.", "starter": "", "options": ["A. is speaking / speaks", "B. speaks / is speaking", "C. spoke / is speaking", "D. speaks / spoke"], "a": "B", "explain": "Vế 1 là sự thật chung (HTĐ). Vế 2 có 'right now' (HTTĐ)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "4. We ___ (not/finish) our history project yet. The deadline is set for Monday.", "starter": "", "options": ["A. didn't finish", "B. don't finish", "C. haven't finished", "D. aren't finishing"], "a": "C", "explain": "Dấu hiệu 'yet' -> Hiện tại hoàn thành (haven't finished)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "5. Kim ___ (never/be) abroad. She'd love to visit other countries.", "starter": "", "options": ["A. was never", "B. has never been", "C. is never", "D. had never been"], "a": "B", "explain": "Trải nghiệm tính tới hiện tại (never) -> Hiện tại hoàn thành."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "6. I'm exhausted. I ___ (train) my stomach muscles all morning.", "starter": "", "options": ["A. trained", "B. am training", "C. have been training", "D. was training"], "a": "C", "explain": "Hành động kéo dài 'all morning' để lại hậu quả 'exhausted' ở hiện tại -> HT Hoàn thành tiếp diễn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "7. What ___ (usually/you/do) in your free time?", "starter": "", "options": ["A. are you usually doing", "B. do you usually do", "C. have you usually done", "D. did you usually do"], "a": "B", "explain": "Hỏi về thói quen (usually) -> Hiện tại đơn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "8. Look! Your mum's in the vegetable garden. ___ (she/water) the tomatoes?", "starter": "", "options": ["A. Does she water", "B. Is she watering", "C. Has she watered", "D. Was she watering"], "a": "B", "explain": "Dấu hiệu 'Look!' -> Hành động đang diễn ra lúc nói (HTTĐ)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "9. Sarah ___ (climb) the Matterhorn, ___ (sail) around the world, and ___ (go) on safari in Kenya.", "starter": "", "options": ["A. climbed / sailed / went", "B. has climbed / sailed / gone", "C. is climbing / sailing / going", "D. climbs / sails / goes"], "a": "B", "explain": "Liệt kê các trải nghiệm của cô ấy tính đến hiện tại -> Hiện tại hoàn thành."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "10. Look! It ___ so we can't go to the beach. (to rain)", "starter": "", "options": ["A. rains", "B. rained", "C. is raining", "D. has rained"], "a": "C", "explain": "Dấu hiệu 'Look!' -> Hiện tại tiếp diễn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "11. ___ (they/spend) their holidays in Paris last summer?", "starter": "", "options": ["A. Do they spend", "B. Did they spend", "C. Have they spent", "D. Were they spending"], "a": "B", "explain": "Dấu hiệu 'last summer' -> Quá khứ đơn (Did + S + V?)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "12. When Melanie came into the office yesterday, her eyes ___ (be) red and watery. I think she ___ (cry).", "starter": "", "options": ["A. were / cried", "B. was / had cried", "C. were / had been crying", "D. are / has cried"], "a": "C", "explain": "Đôi mắt đỏ (were) ở QK do hệ quả của việc khóc kéo dài TRƯỚC đó -> QK hoàn thành tiếp diễn (had been crying)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "13. The researcher ___ (have) been exploring the territory since last December.", "starter": "", "options": ["A. have", "B. has", "C. had", "D. is"], "a": "B", "explain": "'The researcher' là ngôi thứ 3 số ít -> dùng 'has'."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "14. Come over to my house around 9 o'clock. By then, I ___ (complete) my history essay.", "starter": "", "options": ["A. complete", "B. will complete", "C. will have completed", "D. am completing"], "a": "C", "explain": "'By then' (tính tới lúc đó trong tương lai) -> Tương lai hoàn thành."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "15. After Larry ___ the film on TV, he decided to buy the book. (to see)", "starter": "", "options": ["A. saw", "B. was seeing", "C. has seen", "D. had seen"], "a": "D", "explain": "Hành động xem (had seen) xảy ra TRƯỚC hành động quyết định (decided) trong quá khứ -> Quá khứ hoàn thành."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "16. In June, my grandmother and grandfather ___ (be) married for fifty years.", "starter": "", "options": ["A. will be", "B. are", "C. will have been", "D. have been"], "a": "C", "explain": "Tương lai hoàn thành: Tính đến tháng 6 (tương lai), họ sẽ hoàn tất việc cưới được 50 năm."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "17. There are a lot of clouds! It ___ soon. (to rain)", "starter": "", "options": ["A. is going to rain", "B. will rain", "C. is raining", "D. rains"], "a": "A", "explain": "Dự đoán có căn cứ ở hiện tại (nhiều mây) -> Tương lai gần (be going to)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "18. This time next week he ___ (fly) to South Africa.", "starter": "", "options": ["A. will fly", "B. will be flying", "C. flies", "D. is flying"], "a": "B", "explain": "'This time next week' (giờ này tuần sau) -> Tương lai tiếp diễn (sẽ đang xảy ra)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "19. On December, 30th 2009, K.H Abdurrahman Wahid ___ (die) because of complications...", "starter": "", "options": ["A. dies", "B. has died", "C. died", "D. had died"], "a": "C", "explain": "Sự kiện xảy ra ở một thời điểm cụ thể trong quá khứ (2009) -> Quá khứ đơn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "20. At 6 o'clock on next Friday they ___ (sing) the new song.", "starter": "", "options": ["A. will sing", "B. will be singing", "C. are singing", "D. sing"], "a": "B", "explain": "Thời điểm cụ thể ở tương lai (At 6 o'clock next Friday) -> Tương lai tiếp diễn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "21. When he ___ (wake up) yesterday his mother ___ (already /prepare) breakfast", "starter": "", "options": ["A. woke up / had already prepared", "B. wakes up / has already prepared", "C. woke up / already prepared", "D. was waking up / had prepared"], "a": "A", "explain": "Việc mẹ chuẩn bị bữa sáng đã xong (QK hoàn thành) TRƯỚC KHI anh ấy thức dậy (QK đơn) ngày hôm qua."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "22. When Sarah goes on vacation next month, she ___ (study) German for over two years.", "starter": "", "options": ["A. studies", "B. will study", "C. will have studied", "D. has studied"], "a": "C", "explain": "Tính tới 1 thời điểm ở tương lai (goes... next month) -> Dùng Tương lai hoàn thành."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "23. ___ (you/ever / see) a whale?", "starter": "", "options": ["A. Do you ever see", "B. Did you ever see", "C. Have you ever seen", "D. Are you ever seeing"], "a": "C", "explain": "Hỏi về trải nghiệm (ever) -> Hiện tại hoàn thành."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "24. I have not traveled much yet; however, I ___ (visit) the Grand Canyon by the time I leave.", "starter": "", "options": ["A. visit", "B. will visit", "C. will have visited", "D. have visited"], "a": "C", "explain": "'By the time + HTĐ' -> Mệnh đề chính chia Tương lai hoàn thành."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "25. I ___ (finish) it by the end of this month.", "starter": "", "options": ["A. finish", "B. will finish", "C. will have finished", "D. am finishing"], "a": "C", "explain": "'By the end of...' -> Tương lai hoàn thành."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "26. By the time you finish studying the verb tense tutorial, you ___ (master) all twelve tenses...", "starter": "", "options": ["A. master", "B. will master", "C. will have mastered", "D. mastered"], "a": "C", "explain": "Tương tự câu trên, 'By the time + HTĐ' -> TL Hoàn thành."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "27. John I ___ (just / finish) my homework", "starter": "", "options": ["A. just finish", "B. just finished", "C. have just finished", "D. am just finishing"], "a": "C", "explain": "Dấu hiệu 'just' (vừa mới) -> Hiện tại hoàn thành."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "28. He ___ (not, like) reading.", "starter": "", "options": ["A. doesn't like", "B. isn't liking", "C. don't like", "D. hasn't liked"], "a": "A", "explain": "Sở thích là sự thật ở HTĐ. He + doesn't + V-bare."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "29. ___ any of you ___ (play) sports regularly?", "starter": "", "options": ["A. Are / playing", "B. Do / play", "C. Have / played", "D. Did / play"], "a": "B", "explain": "Thói quen 'regularly' -> HTĐ. Any of you (số nhiều) -> Do + S + V-bare."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "30. Man ___ (land) on the Moon in 1969.", "starter": "", "options": ["A. lands", "B. has landed", "C. landed", "D. had landed"], "a": "C", "explain": "Sự kiện trong quá khứ có mốc thời gian rõ ràng (in 1969) -> Quá khứ đơn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "31. Right now he ___ on the phone. (talk).", "starter": "", "options": ["A. talks", "B. talked", "C. is talking", "D. has talked"], "a": "C", "explain": "Dấu hiệu 'Right now' -> Hiện tại tiếp diễn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "32. Right now he ___ a letter. (write)", "starter": "", "options": ["A. writes", "B. is writing", "C. wrote", "D. has written"], "a": "B", "explain": "Tương tự câu trên -> is writing."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "33. A strange thing ___ (happen) while I ___ (come) back.", "starter": "", "options": ["A. happened / was coming", "B. was happening / came", "C. happened / came", "D. happens / is coming"], "a": "A", "explain": "Đang làm gì (was coming - QKTD) thì có việc khác xen vào (happened - QKĐ)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "34. I ___ (look) for my camera for an hour, when I ___ (remember) I gave it to my friend.", "starter": "", "options": ["A. was looking / remembered", "B. had been looking / remembered", "C. have looked / remember", "D. looked / remembered"], "a": "B", "explain": "Việc tìm kiếm xảy ra LIÊN TỤC (for an hour) trước thời điểm nhớ ra (QKĐ) -> QK Hoàn thành tiếp diễn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "35. I ___ crossing the street, ___ (slip) and ___ (fall down).", "starter": "", "options": ["A. was / slipped / fell down", "B. am / slip / fall down", "C. was / slipping / falling down", "D. have been / slipped / fell"], "a": "A", "explain": "Đang băng qua đường (was crossing - QKTD) thì trượt chân và ngã (slipped / fell - QKĐ)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "36. Be quiet, I ___ to concentrate. (try)", "starter": "", "options": ["A. try", "B. tried", "C. am trying", "D. have tried"], "a": "C", "explain": "Câu mệnh lệnh 'Be quiet' -> Hành động đang xảy ra ngay lúc nói (HTTĐ)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "37. Could you close the window? I ___ (freeze)", "starter": "", "options": ["A. freeze", "B. am freezing", "C. have frozen", "D. froze"], "a": "B", "explain": "Nêu tình trạng đang diễn ra ngay lúc nói để nhờ vả (Tôi đang chết cóng đây)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "38. She ___ doing her homework yet. (not finish)", "starter": "", "options": ["A. didn't finish", "B. doesn't finish", "C. hasn't finished", "D. isn't finishing"], "a": "C", "explain": "Dấu hiệu 'yet' trong câu phủ định -> Hiện tại hoàn thành."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "39. ___ (Maria/drive) for many hours when the accident happened?", "starter": "", "options": ["A. Did Maria drive", "B. Was Maria driving", "C. Had Maria been driving", "D. Has Maria driven"], "a": "C", "explain": "Hành động lái xe diễn ra liên tục (for many hours) TRƯỚC KHI tai nạn xảy ra (happened - QKĐ) -> QK Hoàn thành tiếp diễn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "40. The man ___ (paint) the walls all day long.", "starter": "", "options": ["A. paints", "B. painted", "C. has been painting", "D. is painting"], "a": "C", "explain": "Nhấn mạnh quá trình kéo dài 'all day long' tính đến hiện tại -> HT Hoàn thành tiếp diễn."}
        ]
    }
}

# ==========================================
# 2. HÀM GỌI GROQ API
# ==========================================
def ask_ai_tutor_groq(api_key, context_q, context_options_str, context_a, context_explain, user_question):
    try:
        client = Groq(api_key=api_key)
        prompt = f"""
        [NGỮ CẢNH BÀI TẬP]
        - Đề bài: {context_q}
        - Lựa chọn: {context_options_str}
        - Đáp án chuẩn: {context_a}
        - Giải thích: {context_explain}
        
        [CÂU HỎI CỦA HỌC VIÊN]
        "{user_question}"
        """
        
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Bạn là gia sư tiếng Anh. Dựa vào ngữ cảnh, giải thích thắc mắc của học viên thật ngắn gọn, đi thẳng trọng tâm."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant",
            temperature=0.5,
            max_tokens=400
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Lỗi API: {str(e)}"

# ==========================================
# 3. STREAMLIT UI CODE
# ==========================================
st.set_page_config(page_title="HOU - Writing 1 App", page_icon="🎓", layout="wide")

st.markdown("""
<style>
    .instruction-text { font-size: 16px; font-style: italic; color: #555; margin-bottom: 10px;}
    .original-sentence { font-size: 18px; font-weight: bold; color: #1f77b4; padding: 10px; background-color: #e6f2ff; border-radius: 5px; margin-bottom: 10px; border-left: 5px solid #1f77b4;}
    .starter-text { font-size: 18px; font-weight: bold; color: #d62728; margin-bottom: 15px;}
    .ai-box { padding: 15px; border-radius: 8px; background-color: #f0f2f6; border: 1px solid #d1d5db; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
if 'current_topic' not in st.session_state:
    st.session_state.current_topic = list(COURSE_DATA.keys())[0]

st.sidebar.title("⚡ Cấu hình Groq AI")
api_key_input = "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"

st.sidebar.markdown("---")
st.sidebar.title("📚 Chuyên đề học tập")
selected_topic = st.sidebar.radio("Danh sách:", list(COURSE_DATA.keys()))

if selected_topic != st.session_state.current_topic:
    st.session_state.current_topic = selected_topic
    st.session_state.q_index = 0
    st.rerun()

topic_data = COURSE_DATA[st.session_state.current_topic]
st.header(f"📖 {st.session_state.current_topic}")

tab_theory, tab_practice = st.tabs(["📚 Lý Thuyết", "✍️ Thực Hành"])

with tab_theory:
    st.markdown(topic_data["theory"])

with tab_practice:
    exercises = topic_data.get("exercises", [])
    if not exercises:
        st.info("Chưa có bài tập.")
    else:
        q_data = exercises[st.session_state.q_index]
        st.progress((st.session_state.q_index + 1) / len(exercises))
        st.subheader(f"Câu hỏi {st.session_state.q_index + 1} / {len(exercises)}")
        
        with st.form(key=f"form_{st.session_state.q_index}"):
            st.markdown(f"<div class='instruction-text'>📌 Yêu cầu: {q_data['instruction']}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='original-sentence'>{q_data['original']}</div>", unsafe_allow_html=True)
            if q_data.get("type") == "rewrite":
                st.markdown(f"<div class='starter-text'>{q_data['starter']} ___________</div>", unsafe_allow_html=True)
            
            user_choice = st.radio("Chọn đáp án:", q_data["options"], index=None)
            submit_btn = st.form_submit_button("Kiểm tra ✔")
            
            if submit_btn:
                if user_choice:
                    if user_choice.startswith(q_data["a"]):
                        st.success(f"🎉 Chính xác! Đáp án: {q_data['a']}")
                    else:
                        st.error(f"❌ Sai rồi! Đáp án: {q_data['a']}")
                    st.info(f"💡 Giải thích: {q_data['explain']}")
                else:
                    st.warning("⚠️ Vui lòng chọn đáp án!")
        
        with st.expander("⚡ Hỏi Gia sư AI?"):
            user_question = st.text_input("Gõ thắc mắc của bạn:")
            if st.button("Gửi AI"):
                if not api_key_input:
                    st.warning("Nhập API Key ở Sidebar trước!")
                elif user_question:
                    with st.spinner("AI đang xử lý..."):
                        resp = ask_ai_tutor_groq(api_key_input, q_data['original'], ", ".join(q_data['options']), q_data['a'], q_data['explain'], user_question)
                        st.markdown(f"<div class='ai-box'>{resp}</div>", unsafe_allow_html=True)

        col_prev, col_space, col_next = st.columns([1, 2, 1])
        with col_prev:
            if st.button("⬅ Câu trước") and st.session_state.q_index > 0:
                st.session_state.q_index -= 1
                st.rerun()
        with col_next:
            if st.button("Câu sau ➡") and st.session_state.q_index < len(exercises) - 1:
                st.session_state.q_index += 1
                st.rerun()
        "Supp: Verb Forms (Part 2)": {
        "theory": "### SUPPLEMENTARY: VERB FORMS (Part 2)\nTiếp tục luyện tập phản xạ chia động từ tổng hợp từ câu 41 đến 137.",
        "exercises": [
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "41. The coffee ___ (smell) good.", "starter": "", "options": ["A. smells", "B. is smelling", "C. has smelled", "D. smelled"], "a": "A", "explain": "'Smell' chỉ tri giác/trạng thái không dùng ở thì tiếp diễn. Sự thật ở HTĐ."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "42. I ___ (not/hear) anything he said, because I ___ (think) about something else.", "starter": "", "options": ["A. didn't hear / was thinking", "B. don't hear / am thinking", "C. wasn't hearing / thought", "D. haven't heard / think"], "a": "A", "explain": "Đang mải suy nghĩ (QKTD) nên đã không nghe thấy (QKĐ)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "43. While I ___ (sleep), he ___ (clean) the house and ___ (prepare) dinner.", "starter": "", "options": ["A. was sleeping / cleaned / prepared", "B. slept / was cleaning / preparing", "C. sleep / cleans / prepares", "D. was sleeping / was cleaning / preparing"], "a": "A", "explain": "While + QKTD (hành động đang diễn ra), các hành động khác xen vào hoặc xảy ra tuần tự trong QK (QKĐ). Đáp án D cũng có thể chấp nhận nếu 2 người làm song song, nhưng A phổ biến hơn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "44. He ___ (miss) his bus so he ___ (be) really late.", "starter": "", "options": ["A. misses / is", "B. missed / was", "C. has missed / is", "D. had missed / was"], "a": "B", "explain": "Kể lại sự việc trong quá khứ -> Quá khứ đơn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "45. When we went back, our house was empty. Somebody ___ (rob) us.", "starter": "", "options": ["A. robbed", "B. was robbing", "C. has robbed", "D. had robbed"], "a": "D", "explain": "Việc bị trộm (QKHT) xảy ra TRƯỚC khi quay về (went back - QKĐ)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "46. I wasn't hungry, because I ___ (already/eat) a big lunch.", "starter": "", "options": ["A. already ate", "B. have already eaten", "C. had already eaten", "D. was already eating"], "a": "C", "explain": "Đã ăn xong TRƯỚC một thời điểm ở quá khứ (wasn't hungry)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "47. Supermarkets ___ (open) at 8 o'clock and ___ (close) at 9.", "starter": "", "options": ["A. open / close", "B. opens / closes", "C. are opening / closing", "D. will open / close"], "a": "A", "explain": "Lịch trình cố định, chủ ngữ số nhiều -> Hiện tại đơn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "48. Yesterday I ___ (buy) a T-shirt and cargo shorts.", "starter": "", "options": ["A. buy", "B. bought", "C. have bought", "D. had bought"], "a": "B", "explain": "Dấu hiệu 'Yesterday' -> Quá khứ đơn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "49. They ___ (have) dinner when the tornado ___ (strike).", "starter": "", "options": ["A. had / struck", "B. were having / struck", "C. had / was striking", "D. are having / strikes"], "a": "B", "explain": "Đang ăn tối (QKTD) thì lốc xoáy ập tới (QKĐ)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "50. By next summer Jayden ___ (complete) the beginner's computer course.", "starter": "", "options": ["A. completes", "B. will complete", "C. is completing", "D. will have completed"], "a": "D", "explain": "By + thời gian tương lai -> Tương lai hoàn thành."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "51. I ___ (lie) on the beach in Ibiza this time next week. Lucky me!", "starter": "", "options": ["A. will lie", "B. am lying", "C. will be lying", "D. lie"], "a": "C", "explain": "This time next week -> Tương lai tiếp diễn (sẽ đang xảy ra)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "52. Every morning Jackson ___ (turn) on his computer and ___ (check) his Facebook...", "starter": "", "options": ["A. turns / checks", "B. turn / check", "C. is turning / checking", "D. turned / checked"], "a": "A", "explain": "Thói quen hàng ngày (Every morning), chủ ngữ số ít -> Hiện tại đơn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "53. Sophia and Isabella ___ (not/finish) their power point presentation on African animals yet.", "starter": "", "options": ["A. didn't finish", "B. haven't finished", "C. hasn't finished", "D. aren't finishing"], "a": "B", "explain": "Dấu hiệu 'yet' -> Hiện tại hoàn thành (số nhiều -> haven't)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "54. Tonight Evan ___ (play) a game of singles with his best friend, Christopher.", "starter": "", "options": ["A. plays", "B. is playing", "C. will play", "D. has played"], "a": "B", "explain": "Dự định/Kế hoạch chắc chắn trong tương lai gần -> Hiện tại tiếp diễn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "55. This summer I ___ (read) 10 classic novels for school.", "starter": "", "options": ["A. read", "B. am reading", "C. have read", "D. will read"], "a": "B", "explain": "Kế hoạch tạm thời cho mùa hè này -> Hiện tại tiếp diễn (hoặc Tương lai gần)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "56. Ethan and Noah ___ (already/wait) for 2 hours, when the bus finally ___ (arrive).", "starter": "", "options": ["A. were already waiting / arrived", "B. had already been waiting / arrived", "C. have already waited / arrives", "D. already waited / arrived"], "a": "B", "explain": "Hành động chờ đợi kéo dài liên tục (for 2 hours) TRƯỚC một sự kiện ở quá khứ (arrived) -> QK Hoàn thành tiếp diễn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "57. What ___ (you/do) this weekend? I think I ___ (start) a new jigsaw puzzle.", "starter": "", "options": ["A. do you do / start", "B. are you doing / will start", "C. will you do / am starting", "D. are you doing / am starting"], "a": "B", "explain": "Câu hỏi kế hoạch (are you doing). Câu trả lời có 'I think' (dự đoán không chắc chắn) -> Tương lai đơn (will start)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "58. Mia looks very pale. It looks like she ___ (faint).", "starter": "", "options": ["A. faints", "B. will faint", "C. is fainting", "D. is going to faint"], "a": "D", "explain": "Dự đoán có căn cứ rõ ràng ở hiện tại (trông rất nhợt nhạt) -> Tương lai gần."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "59. My cousins, Logan and Jackson, ___ (live) in Barcelona since 2006.", "starter": "", "options": ["A. live", "B. lived", "C. have lived", "D. are living"], "a": "C", "explain": "Dấu hiệu 'since 2006' -> Hiện tại hoàn thành."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "60. My Uncle Landon ___ (work) in Dublin from 2002-2008.", "starter": "", "options": ["A. works", "B. worked", "C. has worked", "D. had worked"], "a": "B", "explain": "Sự kiện đã bắt đầu và KẾT THÚC hoàn toàn trong quá khứ -> Quá khứ đơn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "76. An individual blood cell ___ (take) about 60 seconds to make a complete circuit of the body.", "starter": "", "options": ["A. takes", "B. is taking", "C. took", "D. has taken"], "a": "A", "explain": "Sự thật hiển nhiên/Khoa học -> Hiện tại đơn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "78. As soon as I finish with English language I ___ (start) taking French classes.", "starter": "", "options": ["A. start", "B. will start", "C. am starting", "D. have started"], "a": "B", "explain": "As soon as + HTĐ, TLĐ (Ngay khi làm xong việc A ở hiện tại, sẽ làm việc B ở tương lai)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "82. Liz ___ (paint) the bathroom for two hours before Luke ___ (offer) her his help.", "starter": "", "options": ["A. painted / offered", "B. was painting / offered", "C. had been painting / offered", "D. has painted / offers"], "a": "C", "explain": "Hành động sơn kéo dài liên tục (for two hours) TRƯỚC KHI được đề nghị giúp đỡ ở quá khứ -> QK Hoàn thành tiếp diễn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "86. Mike ___ (chop) the onions while Lucy ___ (blend) the eggs and cream.", "starter": "", "options": ["A. chopped / blended", "B. was chopping / was blending", "C. had chopped / was blending", "D. chops / blends"], "a": "B", "explain": "Hai hành động đang diễn ra SONG SONG cùng một lúc trong quá khứ -> Cả 2 dùng QKTD."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "96. The average human body ___ (carry) ten times more bacterial cells than human cells.", "starter": "", "options": ["A. carry", "B. carries", "C. is carrying", "D. has carried"], "a": "B", "explain": "Sự thật khoa học -> Hiện tại đơn."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "100. I haven't finished my essay yet but I ___ (write) it by tomorrow.", "starter": "", "options": ["A. will write", "B. am writing", "C. will have written", "D. write"], "a": "C", "explain": "Dấu hiệu 'by tomorrow' -> Tương lai hoàn thành (sẽ hoàn tất trước ngày mai)."},
            {"type": "mcq", "instruction": "Write the correct verb forms", "original": "123. What ___ (you/do) while the ground ___ (shake) during the earthquake?", "starter": "", "options": ["A. did you do / shook", "B. were you doing / was shaking", "C. were you doing / shook", "D. had you done / was shaking"], "a": "B", "explain": "Bạn ĐANG LÀM GÌ trong lúc mặt đất ĐANG RUNG LẮC -> Hai hành động song song ở QK -> QKTD."}
        ]
    },
    "Supp: Rewrites & Passive Voice": {
        "theory": "### SUPPLEMENTARY: SENTENCE TRANSFORMATION\nLuyện tập Viết lại câu đồng nghĩa, Chuyển đổi Câu Điều Kiện, Câu Bị Động.",
        "exercises": [
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "1. The weather is too terrible for you to go out.", "starter": "→ If the weather...", "options": ["A. wasn't terrible, you can go out.", "B. weren't too terrible, you could go out.", "C. is not terrible, you could go out.", "D. had not been terrible, you could have gone out."], "a": "B", "explain": "Thực tế ở hiện tại (is terrible) -> Dùng Câu điều kiện loại 2 (trái với hiện tại): If + S + weren't, S + could/would + V."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "2. All the students have to take the final exam.", "starter": "→ The final exam...", "options": ["A. has to be taken by all the students.", "B. have to be taken by all the students.", "C. is taken by all the students.", "D. had to be taken by all the students."], "a": "A", "explain": "Bị động của have to: S + have/has to be + PII. 'The final exam' (số ít) -> has to be taken."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "3. Please don't repeat what I said.", "starter": "→ Would you mind...", "options": ["A. not to repeat what I said?", "B. not repeating what I said?", "C. don't repeat what I said?", "D. to not repeat what I said?"], "a": "B", "explain": "Cấu trúc: Would you mind + (not) + V-ing? (Bạn có phiền nếu không...)."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "4. I can't swim as well as my friend can.", "starter": "→ My friend...", "options": ["A. can swim as well as I can.", "B. can't swim better than me.", "C. can swim better than I can.", "D. swims worse than I do."], "a": "C", "explain": "So sánh không bằng ('can't swim as well as') -> viết lại thành so sánh hơn ('can swim better than')."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "5. We lost our way. We didn't arrive on time.", "starter": "→ Unless...", "options": ["A. we had lost our way, we would have arrived on time.", "B. we lost our way, we would arrive on time.", "C. we had not lost our way, we wouldn't have arrived.", "D. we didn't lose our way, we arrived on time."], "a": "A", "explain": "Sự việc ở quá khứ -> Dùng CĐK loại 3. Unless = If... not. Câu gốc: Nếu chúng ta KHÔNG bị lạc (Unless we had lost our way)."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "6. It took me three hours to open the door.", "starter": "→ We spent...", "options": ["A. three hours to open the door.", "B. three hours opening the door.", "C. three hours open the door.", "D. us three hours opening the door."], "a": "B", "explain": "It took + sb + time + to V = S + spent + time + V-ing."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "8. The film was too boring for you to watch.", "starter": "→ The film was so...", "options": ["A. boring that you couldn't watch it.", "B. boring that you can watch it.", "C. boring for you to watch it.", "D. boring that you couldn't watch."], "a": "A", "explain": "Cấu trúc quá... đến nỗi mà: S + be + so + adj + that + S + V. Lưu ý mệnh đề sau 'that' phải có tân ngữ 'it'."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "9. They don't play football any more.", "starter": "→ They used...", "options": ["A. to play football.", "B. to playing football.", "C. play football.", "D. not to play football."], "a": "A", "explain": "Cấu trúc 'used to + V-bare' chỉ thói quen trong quá khứ nay không còn nữa."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "15. It takes Minh 2 hours to do his homework every day.", "starter": "→ Minh spends...", "options": ["A. 2 hours to do his homework every day.", "B. 2 hours doing his homework every day.", "C. 2 hours does his homework every day.", "D. 2 hours do his homework every day."], "a": "B", "explain": "Tương tự câu 6: It takes... to V = spend... V-ing."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "16. We were late for school because of the heavy rain.", "starter": "→ Because it...", "options": ["A. rains heavily, we were late for school.", "B. rained heavily, we were late for school.", "C. was heavy rain, we were late for school.", "D. rained heavy, we were late for school."], "a": "B", "explain": "Chuyển cụm danh từ 'the heavy rain' thành mệnh đề 'it rained heavily'."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "30. If you don't rest yourself, you will be ill.", "starter": "→ Unless...", "options": ["A. you rest yourself, you will be ill.", "B. you don't rest yourself, you will be ill.", "C. you rest yourself, you won't be ill.", "D. you didn't rest yourself, you would be ill."], "a": "A", "explain": "Unless = If... not. Đã dùng Unless thì vế trước phải khẳng định (Unless you rest = If you don't rest)."},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "45. When did you last ride a bike?", "starter": "→ How long is it...", "options": ["A. since you ride a bike?", "B. that you rode a bike?", "C. since you last rode a bike?", "D. for you to ride a bike?"], "a": "C", "explain": "Cấu trúc chuyển đổi giữa QKĐ và HTHT/Cấu trúc How long. How long is it since + S + last + V(qk)?"},
            {"type": "rewrite", "instruction": "Complete the second sentences without changing the meaning.", "original": "68. Listening to music at home is more interesting than going to the concert.", "starter": "→ I prefer...", "options": ["A. listening to music at home than going to the concert.", "B. listening to music at home to going to the concert.", "C. to listen to music at home than going to the concert.", "D. listen to music at home to go to the concert."], "a": "B", "explain": "Cấu trúc: prefer + V-ing + TO + V-ing (Thích làm A hơn làm B)."},
            {"type": "rewrite", "instruction": "Rewrite the sentences in the passive voice.", "original": "P1. I have eaten many sweets.", "starter": "→ Many sweets...", "options": ["A. have been eaten by me.", "B. has been eaten by me.", "C. was eaten by me.", "D. had been eaten by me."], "a": "A", "explain": "Bị động thì HT Hoàn Thành: S + have/has + been + PII. (Many sweets số nhiều -> have)."},
            {"type": "rewrite", "instruction": "Rewrite the sentences in the passive voice.", "original": "P5. This famous director will produce ten short comedy films in four years.", "starter": "→ Ten short comedy films...", "options": ["A. will produce by this famous director.", "B. will be produced by this famous director.", "C. would be produced by this famous director.", "D. will be producing by this famous director."], "a": "B", "explain": "Bị động của Tương lai đơn (will): S + will be + PII."}
        ]
    }
