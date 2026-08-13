import tkinter as tk
from tkinter import ttk, messagebox

# ==========================================
# TOÀN BỘ DỮ LIỆU TỪ FILE PDF ĐƯỢC SỐ HÓA
# ==========================================
COURSE_DATA = {
    "Unit 1: Social Trends": {
        "theory": """UNIT 1: SOCIAL TRENDS
[GRAMMAR FOCUS] - The Present Continuous (Thì hiện tại tiếp diễn)
Cấu trúc: Subject + Be (am/is/are) + Verb-ing

Cách dùng:
1. Hành động đang diễn ra ngay lúc nói (Activities happening now).
   VD: The kids are watching TV. / What are you writing?
2. Hành động xảy ra xung quanh thời điểm nói (Activities happening around now).
   VD: Sally is studying hard for her exams this week.
3. Dự định trong tương lai gần (Near future, planned events).
   VD: Polly is coming for dinner tomorrow.

[SKILLS FOCUS] - Writing a Topic Sentence (Viết câu chủ đề)
- Topic sentence là câu quan trọng nhất, cho biết toàn bộ đoạn văn nói về cái gì.
- Các bước: 
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
        "theory": """UNIT 2: THE WORLD OF COLOURS
[GRAMMAR FOCUS] - Conjunctions (Liên từ)
Được dùng để nối các từ hoặc nhóm từ. Phân loại:
1. Coordinating (Liên từ kết hợp): and, but, or, nor, for, so, yet.
   VD: He can't sing but he can dance very well.
2. Correlative (Liên từ tương quan): either...or, neither...nor, not only...but also.
   VD: The house is not only big but also nice.
3. Subordinating (Liên từ phụ thuộc): after, although, if, because, until, when, where, whether...
   VD: I will give her the book if I see her.

[SKILLS FOCUS] - Free Writing (Viết tự do)
- Là cách để động não (brainstorm) trước khi viết.
- Viết liên tục trong 10-20 phút, không sửa lỗi, viết bất cứ thứ gì nảy ra trong đầu.""",
        "exercises": [
            {"q": "___ pink was thought to be a stronger color, it was best suited for boys. (although/and/if)", "a": "although"},
            {"q": "Blue was more delicate ___ dainty for girls. (so/and/or)", "a": "and"},
            {"q": "Most likely you feel good ___ you wear your favorite color. (when/so/but)", "a": "when"},
            {"q": "People think pink is for girls, ___ it isn't always this way. (so/but/because)", "a": "but"}
        ]
    },
    "Unit 3: Politeness": {
        "theory": """UNIT 3: POLITENESS
[GRAMMAR FOCUS] - Subject-Verb Agreement (Sự hòa hợp Chủ - Vị)
Quy tắc đặc biệt:
- Nối bằng "or/nor": Động từ chia theo chủ ngữ gần nhất.
- Nối bằng "either..or/neither..nor": Động từ chia theo chủ ngữ gần nhất.
- Nối bằng "along with, as well as": Động từ chia theo chủ ngữ ĐẦU TIÊN.
- Đại từ bất định (each, everyone, someone...): Động từ chia SỐ ÍT.
- Phần trăm, phân số (percent, fraction...): Xét danh từ sau giới từ "of".
- "The number of" + V(số ít) / "A number of" + V(số nhiều).
- Tiền bạc, thời gian, tên sách: Động từ chia SỐ ÍT.

[SKILLS FOCUS] - Supporting Main Idea with Examples (Hỗ trợ ý chính bằng ví dụ)
- Ví dụ cụ thể là bằng chứng mạnh mẽ nhất. 
- Giúp chứng minh tính hợp lý cho câu luận điểm của bạn.""",
        "exercises": [
            {"q": "Both José and Martha (is/are) ___ on vacation this week.", "a": "are"},
            {"q": "Every student and parent (has/have) ___ received a copy of the honor code.", "a": "has"},
            {"q": "Either the original or a photocopy (is/are) ___ acceptable.", "a": "is"},
            {"q": "Neither you nor she (is/are/am) ___ aware of the implications.", "a": "is"},
            {"q": "The number of people we need to hire (is/are) ___ thirteen.", "a": "is"}
        ]
    },
    "Unit 4: Games": {
        "theory": """UNIT 4: GAMES
[GRAMMAR FOCUS] - Modals (Động từ khuyết thiếu)
- Can/Could: Khả năng, sự cho phép (Could là quá khứ của Can).
- Must: Sự bắt buộc cá nhân, sự chắc chắn (Mustn't = cấm đoán).
- May/Might: Khả năng có thể xảy ra (không chắc chắn).
- Can't: Chắc chắn không thể xảy ra.
- Needn't: Không cần thiết phải làm gì.
- Shall: Dùng trong câu hỏi "Shall I/we...?" để đưa ra lời đề nghị.

[SKILLS FOCUS] - Writing an Opinion Paragraph (Viết đoạn văn nêu ý kiến)
Cấu trúc 3 phần:
1. Topic Sentence: Nêu rõ quan điểm Đồng ý/Không đồng ý.
2. Reasons + Supporting details: Đưa ra lý do (First, Secondly...) và chi tiết.
3. Concluding Sentence: Câu kết luận (To sum up, In conclusion...).""",
        "exercises": [
            {"q": "He lost her credit card, so he ___ pay for the meal. (can't/couldn't/shouldn't)", "a": "couldn't"},
            {"q": "They ___ be on holiday but I'm not sure. (must/may/can)", "a": "may"},
            {"q": "You ___ enter the country without a visa. It's prohibited. (mustn't/can't/needn't)", "a": "can't"},
            {"q": "___ you speak Japanese? (May/Could/Can)", "a": "Can"}
        ]
    },
    "Unit 5: Family life": {
        "theory": """UNIT 5: FAMILY LIFE
[GRAMMAR FOCUS] - Comparative and Superlative (So sánh hơn & So sánh nhất)
1. Tính từ 1 âm tiết: 
   - Hơn: Thêm "-er" (taller)
   - Nhất: Thêm "-est" (tallest)
   *Quy tắc gấp đôi phụ âm: big -> bigger -> biggest.
2. Tính từ 2 âm tiết:
   - Thường dùng: more/most (more peaceful)
   - Tận cùng "y": đổi "y" thành "ier/iest" (happier/happiest).
   - Tận cùng "er, le, ow": thêm er/est (narrower, gentler).
3. Tính từ 3 âm tiết trở lên: Luôn dùng more/most (more intelligent).

[SKILLS FOCUS] - Writing a Personal Letter (Viết thư cá nhân)
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
        "theory": """SUPPLEMENTARY PRACTICE
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

class EnglishApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Writing 1 - Full Course & Exercises App")
        self.geometry("900x600")
        self.configure(bg="#2E3440")
        self.current_unit = list(COURSE_DATA.keys())[0]
        self.current_q_index = 0

        self.create_widgets()
        self.load_unit(self.current_unit)

    def create_widgets(self):
        # Sidebar (Danh sách bài học)
        sidebar = tk.Frame(self, bg="#3B4252", width=250)
        sidebar.pack(side=tk.LEFT, fill=tk.Y)
        
        tk.Label(sidebar, text="DANH SÁCH BÀI HỌC", fg="#ECEFF4", bg="#3B4252", font=("Helvetica", 13, "bold")).pack(pady=20)
        
        for unit in COURSE_DATA.keys():
            btn = tk.Button(sidebar, text=unit, bg="#4C566A", fg="white", font=("Helvetica", 11),
                            relief=tk.FLAT, command=lambda u=unit: self.load_unit(u))
            btn.pack(fill=tk.X, padx=10, pady=5)

        # Khu vực chính
        main_area = tk.Frame(self, bg="#ECEFF4")
        main_area.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Tabs (Lý thuyết / Thực hành)
        self.notebook = ttk.Notebook(main_area)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Tab 1: Lý Thuyết
        self.theory_tab = tk.Frame(self.notebook, bg="white")
        self.notebook.add(self.theory_tab, text="📚 Lý Thuyết (Theory)")
        
        self.theory_text = tk.Text(self.theory_tab, wrap=tk.WORD, font=("Consolas", 12), bg="#FAFAFA", fg="#2E3440")
        self.theory_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Tab 2: Thực Hành (Interactive Quiz)
        self.practice_tab = tk.Frame(self.notebook, bg="#E5E9F0")
        self.notebook.add(self.practice_tab, text="✍️ Thực Hành (Practice)")

        self.lbl_question = tk.Label(self.practice_tab, text="", font=("Helvetica", 14, "bold"), bg="#E5E9F0", fg="#3B4252", wraplength=550, justify="center")
        self.lbl_question.pack(pady=40)

        self.answer_var = tk.StringVar()
        self.entry_answer = tk.Entry(self.practice_tab, textvariable=self.answer_var, font=("Helvetica", 14), width=30)
        self.entry_answer.pack(pady=10)
        self.entry_answer.bind('<Return>', lambda event: self.check_answer())

        self.lbl_feedback = tk.Label(self.practice_tab, text="", font=("Helvetica", 12, "italic"), bg="#E5E9F0")
        self.lbl_feedback.pack(pady=10)

        btn_frame = tk.Frame(self.practice_tab, bg="#E5E9F0")
        btn_frame.pack(pady=20)

        tk.Button(btn_frame, text="⬅ Câu trước", command=self.prev_question, bg="#81A1C1", fg="white", font=("Arial", 11)).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Kiểm tra ✔", command=self.check_answer, bg="#A3BE8C", fg="white", font=("Arial", 11, "bold")).pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Câu sau ➡", command=self.next_question, bg="#81A1C1", fg="white", font=("Arial", 11)).pack(side=tk.LEFT, padx=10)
        
        tk.Button(self.practice_tab, text="👀 Hiện Đáp Án", command=self.show_answer, bg="#BF616A", fg="white", font=("Arial", 10)).pack(pady=10)

    def load_unit(self, unit_name):
        self.current_unit = unit_name
        self.current_q_index = 0
        
        # Load Lý thuyết
        self.theory_text.config(state=tk.NORMAL)
        self.theory_text.delete(1.0, tk.END)
        self.theory_text.insert(tk.END, COURSE_DATA[unit_name]["theory"])
        self.theory_text.config(state=tk.DISABLED)
        
        # Load Câu hỏi đầu tiên
        self.notebook.select(0) # Mặc định chuyển về tab lý thuyết khi đổi bài
        self.load_question()

    def load_question(self):
        exercises = COURSE_DATA[self.current_unit]["exercises"]
        if not exercises:
            self.lbl_question.config(text="Không có bài tập cho phần này.")
            self.entry_answer.pack_forget()
            return
            
        self.entry_answer.pack(pady=10)
        q_data = exercises[self.current_q_index]
        self.lbl_question.config(text=f"Câu {self.current_q_index + 1}/{len(exercises)}: {q_data['q']}")
        self.answer_var.set("")
        self.lbl_feedback.config(text="")

    def check_answer(self):
        exercises = COURSE_DATA[self.current_unit]["exercises"]
        if not exercises: return
        
        correct_answer = exercises[self.current_q_index]["a"].lower().strip()
        user_answer = self.answer_var.get().lower().strip()
        
        if user_answer == correct_answer:
            self.lbl_feedback.config(text="Chính xác! 🎉", fg="#A3BE8C")
        else:
            self.lbl_feedback.config(text="Sai rồi, thử lại nhé!", fg="#BF616A")

    def show_answer(self):
        exercises = COURSE_DATA[self.current_unit]["exercises"]
        if not exercises: return
        correct_answer = exercises[self.current_q_index]["a"]
        self.lbl_feedback.config(text=f"Đáp án đúng: {correct_answer}", fg="#EBCB8B")

    def next_question(self):
        exercises = COURSE_DATA[self.current_unit]["exercises"]
        if self.current_q_index < len(exercises) - 1:
            self.current_q_index += 1
            self.load_question()

    def prev_question(self):
        if self.current_q_index > 0:
            self.current_q_index -= 1
            self.load_question()

if __name__ == "__main__":
    app = EnglishApp()
    app.mainloop()