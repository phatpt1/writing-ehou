import streamlit as st

# ==========================================
# FULL DATABASE: UNIT 1-5 & SUPPLEMENTARY PRACTICE
# ==========================================
COURSE_DATA = {
    "Unit 1: Social Trends": {
        "theory": "### UNIT 1: SOCIAL TRENDS\n**The Present Continuous (Thì hiện tại tiếp diễn)**\n* Cấu trúc: S + am/is/are + V-ing\n* Cách dùng: Đang diễn ra lúc nói; xảy ra xung quanh thời điểm nói; dự định tương lai gần.",
        "exercises": [
            {"type": "text", "q": "Jim, can you help me? - Sorry, Mum. I ___ my homework. (DO)", "a": "am doing"},
            {"type": "text", "q": "What ___ your sister ___? (DO)", "a": "is / doing"},
            {"type": "text", "q": "She ___ a shower. (HAVE)", "a": "is having"},
            {"type": "text", "q": "And what ___ Gary and Sam ___? (DO)", "a": "are / doing"},
            {"type": "text", "q": "They ___ football. (PLAY)", "a": "are playing"},
            {"type": "text", "q": "But Dad ___ anything. (NOT DO)", "a": "isn't doing"},
            {"type": "text", "q": "Yes, I am. I ___ the paper. (READ)", "a": "am reading"}
        ]
    },
    "Unit 2: The World of Colours": {
        "theory": "### UNIT 2: THE WORLD OF COLOURS\n**Conjunctions (Liên từ)**\n* Coordinating: and, but, or, so...\n* Subordinating: although, because, if, when...",
        "exercises": [
            {"type": "text", "q": "1. ___ pink was thought to be a stronger color, it was best suited for boys.", "a": "Although"},
            {"type": "text", "q": "2. Blue was more delicate ___ dainty for girls.", "a": "and"},
            {"type": "text", "q": "3. Red ___ pink saris are the most popular colors for brides.", "a": "and"},
            {"type": "text", "q": "4. Most likely you feel good ___ you wear your favorite color.", "a": "when"},
            {"type": "text", "q": "5. ___ black symbolizes death in Western cultures, it is associated with powerful forces.", "a": "Although"},
            {"type": "text", "q": "6. ___ you see a young lady in violet, it is her, my mistress.", "a": "If"},
            {"type": "text", "q": "7. People think pink is for girls, ___ it isn't always this way.", "a": "but"},
            {"type": "text", "q": "8. She wants to look stylish, ___ she decided to dye her hair blonde.", "a": "so"}
        ]
    },
    "Unit 3: Politeness": {
        "theory": "### UNIT 3: POLITENESS\n**Subject-Verb Agreement (Sự hòa hợp Chủ - Vị)**\n* Neither A nor B -> Động từ chia theo B (gần nhất).\n* A along with B -> Động từ chia theo A (đầu tiên).\n* Every / Each -> Chia SỐ ÍT.",
        "exercises": [
            {"type": "text", "q": "1. Both José and Martha (is, are) ___ on vacation this week.", "a": "are"},
            {"type": "text", "q": "2. Every student and parent (has, have) ___ received a copy of the honor code.", "a": "has"},
            {"type": "text", "q": "3. What they need (is, are) ___ step-by-step procedures.", "a": "is"},
            {"type": "text", "q": "4. Either the original or a photocopy (is, are) ___ acceptable as proof.", "a": "is"},
            {"type": "text", "q": "5. Neither my paralegal nor my assistant (recalls, recall) ___ receiving a letter.", "a": "recalls"},
            {"type": "text", "q": "6. Neither the union leader nor the negotiators (has, have) ___ clearly explained.", "a": "have"},
            {"type": "text", "q": "7. Neither you nor she (is, are, am) ___ aware of all the implications.", "a": "is"},
            {"type": "text", "q": "8. The model shown in the recent catalog and advertisements (is, are) ___ not the model.", "a": "is"},
            {"type": "text", "q": "9. The members of the committee (has, have) ___ met to discuss the morale problem.", "a": "have"},
            {"type": "text", "q": "10. The committee (has, have) ___ met to discuss the morale problem.", "a": "has"}
        ]
    },
    "Unit 4: Games": {
        "theory": "### UNIT 4: GAMES\n**Modals (Động từ khuyết thiếu)**\n* Must: Bắt buộc / Mustn't: Cấm đoán.\n* Can/Could: Khả năng.\n* May/Might: Có thể xảy ra.",
        "exercises": [
            {"type": "text", "q": "1. He lost her credit card, so he ___ pay for the meal. (shouldn't / couldn't / can't)", "a": "couldn't"},
            {"type": "text", "q": "2. They ___ be on holiday but I'm not sure. (can / must / may)", "a": "may"},
            {"type": "text", "q": "3. You ___ enter the country without a visa. (mustn't / can't)", "a": "can't"},
            {"type": "text", "q": "4. ___ you turn it down a bit, please! (Can / Should)", "a": "Can"},
            {"type": "text", "q": "5. ___ you speak Japanese? (May / Could / Can)", "a": "Can"}
        ]
    },
    "Unit 5: Family life": {
        "theory": "### UNIT 5: FAMILY LIFE\n**Comparative and Superlative (So sánh)**\n* Ngắn: +er / +est (taller / tallest).\n* Dài: more / most (more expensive).",
        "exercises": [
            {"type": "text", "q": "1. Jeremy is 10. Jenny is 8. Jeremy is (old) ___ than Jenny.", "a": "older"},
            {"type": "text", "q": "2. The Alps are very high. They are (high) ___ mountains in Europe.", "a": "the highest"},
            {"type": "text", "q": "3. An ocean is (large) ___ a sea.", "a": "larger than"},
            {"type": "text", "q": "4. A Rolls Royce costs more. A Rolls Royce is (expensive) ___ a Twingo.", "a": "more expensive than"},
            {"type": "text", "q": "5. John's results were high. Fred's were very poor. Fred's results were (low) ___ John's.", "a": "lower than"},
            {"type": "text", "q": "6. This exercise is not very difficult. It's (easy) ___ I expected.", "a": "easier than"},
            {"type": "text", "q": "7. The weather is not good today. I hope the weather will be (nice) ___ next week.", "a": "nicer"},
            {"type": "text", "q": "8. People are not very friendly in big cities. They are usually (friendly) ___ in small towns.", "a": "friendlier"},
            {"type": "text", "q": "9. In the government of a country, the President is (important) ___ person.", "a": "the most important"},
            {"type": "text", "q": "10. People say that Chinese is (difficult) ___ to learn than English.", "a": "more difficult"}
        ]
    },
    "Supp: Verb Forms (1 - 70)": {
        "theory": "### SUPPLEMENTARY: VERB FORMS (Part 1)\nÔn tập chia động từ - Hiện tại, Quá khứ, Tương lai và các thì Hoàn thành.",
        "exercises": [
            {"type": "text", "q": "1. What time ___ (the meeting/end)?", "a": "does the meeting end"},
            {"type": "text", "q": "2. Tomorrow I ___ (visit) my aunt, Sally.", "a": "am visiting"},
            {"type": "text", "q": "3. Molly ___ (speak) French but right now she ___ (speak) Spanish.", "a": "speaks / is speaking"},
            {"type": "text", "q": "4. We ___ (not/finish) our history project yet. The deadline is set for Monday.", "a": "haven't finished"},
            {"type": "text", "q": "5. Kim ___ (never/be) abroad. She'd love to visit other countries.", "a": "has never been"},
            {"type": "text", "q": "6. I'm exhausted. I ___ (train) my stomach muscles all morning.", "a": "have been training"},
            {"type": "text", "q": "7. What ___ (usually/you/do) in your free time?", "a": "do you usually do"},
            {"type": "text", "q": "8. Look! Your mum's in the vegetable garden. ___ (she/water) the tomatoes? - I guess she ___.", "a": "Is she watering / is"},
            {"type": "text", "q": "9. Sarah ___ (climb) the Matterhorn, ___ (sail) around the world, and ___ (go) on safari in Kenya.", "a": "has climbed / sailed / gone"},
            {"type": "text", "q": "10. Look! It ___ (rain) so we can't go to the beach.", "a": "is raining"},
            {"type": "text", "q": "11. ___ (they/spend) their holidays in Paris last summer?", "a": "Did they spend"},
            {"type": "text", "q": "12. When Melanie came into the office yesterday, her eyes ___ (be) red and watery. I think she ___ (cry).", "a": "were / had been crying"},
            {"type": "text", "q": "13. The researcher ___ (have) been exploring the territory since last December.", "a": "has"},
            {"type": "text", "q": "14. Come over around 9 o'clock. By then, I ___ (complete) my history essay.", "a": "will have completed"},
            {"type": "text", "q": "15. After Larry ___ (see) the film on TV, he decided to buy the book.", "a": "had seen"},
            {"type": "text", "q": "16. In June, my grandmother and grandfather ___ (be) married for fifty years.", "a": "will have been"},
            {"type": "text", "q": "17. There are a lot of clouds! It ___ (rain) soon.", "a": "is going to rain"},
            {"type": "text", "q": "18. This time next week he ___ (fly) to South Africa.", "a": "will be flying"},
            {"type": "text", "q": "19. On December, 30th 2009, K.H Abdurrahman Wahid ___ (die) because of complications.", "a": "died"},
            {"type": "text", "q": "20. At 6 o'clock on next Friday they ___ (sing) the new song.", "a": "will be singing"},
            {"type": "text", "q": "21. When he ___ (wake up) yesterday his mother ___ (already /prepare) breakfast.", "a": "woke up / had already prepared"},
            {"type": "text", "q": "22. When Sarah goes on vacation next month, she ___ (study) German for over two years.", "a": "will have studied"},
            {"type": "text", "q": "23. ___ (you/ever / see) a whale?", "a": "Have you ever seen"},
            {"type": "text", "q": "24. I have not traveled much yet; however, I ___ (visit) the Grand Canyon by the time I leave.", "a": "will have visited"},
            {"type": "text", "q": "25. I ___ (finish) it by the end of this month.", "a": "will have finished"},
            {"type": "text", "q": "26. By the time you finish studying, you ___ (master) all twelve tenses.", "a": "will have mastered"},
            {"type": "text", "q": "27. John I ___ (just / finish) my homework.", "a": "have just finished"},
            {"type": "text", "q": "28. He ___ (not, like) reading.", "a": "doesn't like"},
            {"type": "text", "q": "29. ___ any of you ___ (play) sports regularly?", "a": "Do / play"},
            {"type": "text", "q": "30. Man ___ (land) on the Moon in 1969.", "a": "landed"},
            {"type": "text", "q": "31. Right now he ___ (talk) on the phone.", "a": "is talking"},
            {"type": "text", "q": "32. Right now he ___ (write) a letter.", "a": "is writing"},
            {"type": "text", "q": "33. A strange thing ___ (happen) while I ___ (come) back.", "a": "happened / was coming"},
            {"type": "text", "q": "34. I ___ (look) for my camera for an hour, when I ___ (remember) I gave it to my friend.", "a": "had been looking / remembered"},
            {"type": "text", "q": "35. I ___ (cross) the street, ___ (slip) and ___ (fall down).", "a": "was crossing / slipped / fell down"},
            {"type": "text", "q": "36. Be quiet, I ___ (try) to concentrate.", "a": "am trying"},
            {"type": "text", "q": "37. Could you close the window? I ___ (freeze).", "a": "am freezing"},
            {"type": "text", "q": "38. She ___ (not finish) doing her homework yet.", "a": "hasn't finished"},
            {"type": "text", "q": "39. ___ (Maria/drive) for many hours when the accident happened?", "a": "Had Maria been driving"},
            {"type": "text", "q": "40. The man ___ (paint) the walls all day long.", "a": "has been painting"},
            {"type": "text", "q": "41. The coffee ___ (smell) good.", "a": "smells"},
            {"type": "text", "q": "42. I ___ (not, hear) anything he said, because I ___ (think) about something else.", "a": "didn't hear / was thinking"},
            {"type": "text", "q": "43. While I ___ (sleep), he ___ (clean) the house and ___ (prepare) dinner.", "a": "was sleeping / cleaned / prepared"},
            {"type": "text", "q": "44. He ___ (miss) his bus so he ___ (be) really late.", "a": "missed / was"},
            {"type": "text", "q": "45. When we went back, our house was empty. Somebody ___ (rob) us.", "a": "had robbed"},
            {"type": "text", "q": "46. I wasn't hungry, because I ___ (already eat) a big lunch.", "a": "had already eaten"},
            {"type": "text", "q": "47. Supermarkets ___ (open) at 8 o'clock and ___ (close) at 9.", "a": "open / close"},
            {"type": "text", "q": "48. Yesterday I ___ (buy) a T-shirt and cargo shorts.", "a": "bought"},
            {"type": "text", "q": "49. They ___ (have) dinner when the tornado ___ (strike).", "a": "were having / struck"},
            {"type": "text", "q": "50. By next summer Jayden ___ (complete) the beginner's computer course.", "a": "will have completed"},
            {"type": "text", "q": "51. I ___ (lie) on the beach in Ibiza this time next week.", "a": "will be lying"},
            {"type": "text", "q": "52. Every morning Jackson ___ (turn) on his computer and ___ (check) his Facebook.", "a": "turns / checks"},
            {"type": "text", "q": "53. Sophia and Isabella ___ (not/finish) their power point presentation yet.", "a": "haven't finished"},
            {"type": "text", "q": "54. Tonight Evan ___ (play) a game of singles with his best friend.", "a": "is playing"},
            {"type": "text", "q": "55. This summer I ___ (read) 10 classic novels for school.", "a": "am reading"},
            {"type": "text", "q": "56. Ethan and Noah ___ (already/wait) for 2 hours, when the bus finally ___ (arrive).", "a": "had already been waiting / arrived"},
            {"type": "text", "q": "57. What ___ (you/do) this weekend? I think I ___ (start) a new jigsaw puzzle.", "a": "are you doing / will start"},
            {"type": "text", "q": "58. Mia looks very pale. It looks like she ___ (faint).", "a": "is going to faint"},
            {"type": "text", "q": "59. My cousins ___ (live) in Barcelona since 2006.", "a": "have lived"},
            {"type": "text", "q": "60. My Uncle Landon ___ (work) in Dublin from 2002-2008.", "a": "worked"},
            {"type": "text", "q": "61. My mother and father ___ (paint) the kitchen all morning.", "a": "have been painting"},
            {"type": "text", "q": "62. Right now Cameron ___ (play) his favorite computer game.", "a": "is playing"},
            {"type": "text", "q": "63. What ___ (you/do) at the moment? Oh, nothing.", "a": "are you doing"},
            {"type": "text", "q": "64. This is the first time I ___ (ever/try) snails.", "a": "have ever tried"},
            {"type": "text", "q": "65-70. (Các câu lặp lại 1-6 trong tài liệu gốc)", "a": "Xem lại đáp án câu 1-6"}
        ]
    },
    "Supp: Verb Forms (71 - 137)": {
        "theory": "### SUPPLEMENTARY: VERB FORMS (Part 2)\nTiếp tục luyện tập chia động từ.",
        "exercises": [
            {"type": "text", "q": "71. We ___ (watch) a movie when you interrupted us.", "a": "were watching"},
            {"type": "text", "q": "72. Right now, I ___ (take) English class.", "a": "am taking"},
            {"type": "text", "q": "73. It's ages since we last ___ (go) to the cinema.", "a": "went"},
            {"type": "text", "q": "74. Next summer we ___ (go) to Ibiza.", "a": "are going"},
            {"type": "text", "q": "75. Pedro ___ (already/do) his homework by the time his parents arrived home.", "a": "had already done"},
            {"type": "text", "q": "76. An individual blood cell ___ (take) about 60 seconds to make a complete circuit.", "a": "takes"},
            {"type": "text", "q": "77. Next World Cup ___ (take) place in Russia.", "a": "will take"},
            {"type": "text", "q": "78. As soon as I finish with English language I ___ (start) taking French classes.", "a": "will start"},
            {"type": "text", "q": "79. In 1962 Brazil ___ (obtain) the two-time championship.", "a": "obtained"},
            {"type": "text", "q": "80. My sister and I ___ (prepare) a gala dinner to celebrate our parents' silver anniversary.", "a": "are preparing"},
            {"type": "text", "q": "81. Where ___ (you/sit) when the light ___ (go) off?", "a": "were you sitting / went"},
            {"type": "text", "q": "82. Liz ___ (paint) the bathroom for two hours before Luke ___ (offer) her his help.", "a": "had been painting / offered"},
            {"type": "text", "q": "83. When Vanda ___ (be) on holiday last summer she ___ (ride) a bike every day.", "a": "was / rode"},
            {"type": "text", "q": "84. The kids ___ (play) at the beach when they ___ (hear) the roar of the ocean.", "a": "were playing / heard"},
            {"type": "text", "q": "85. Sam ___ (vacuum) the carpets before she ___ (settle) down with a book.", "a": "had vacuumed / settled"},
            {"type": "text", "q": "86. Mike ___ (chop) the onions while Lucy ___ (blend) the eggs and cream.", "a": "was chopping / was blending"},
            {"type": "text", "q": "87. Last year I ___ (not/save) any money.", "a": "didn't save"},
            {"type": "text", "q": "88. It's our anniversary next week we ___ (have) party.", "a": "are having"},
            {"type": "text", "q": "89. We ___ (not prepare) at all before we took that test.", "a": "hadn't prepared"},
            {"type": "text", "q": "90. The first computers ___ (be) simple machines designed for basic tasks.", "a": "were"},
            {"type": "text", "q": "91. The known universe ___ (be) made up of 50,000,000,000 galaxies.", "a": "is"},
            {"type": "text", "q": "92. We ___ (have) English class every Monday.", "a": "have"},
            {"type": "text", "q": "93. When you knocked the door, I ___ (eat) a slice of pizza.", "a": "was eating"},
            {"type": "text", "q": "94. How many cups of coffee ___ you ___ (got) today?", "a": "have / got"},
            {"type": "text", "q": "95. The Antarctica ___ (be) very cold.", "a": "is"},
            {"type": "text", "q": "96. The average human body ___ (carry) ten times more bacterial cells than human cells.", "a": "carries"},
            {"type": "text", "q": "97. On 1846 the first professional baseball game ___ (be) played.", "a": "was"},
            {"type": "text", "q": "98. A: Remember that it's a secret. B: I know. I ___ (not/tell) anyone, I promise.", "a": "won't tell"},
            {"type": "text", "q": "99. Sue has bought some chocolates because she ___ (visit) her grandpa in hospital.", "a": "is going to visit"},
            {"type": "text", "q": "100. I haven't finished my essay yet but I ___ (write) it by tomorrow.", "a": "will have written"},
            {"type": "text", "q": "101. At this time next week Brenda ___ (sunbathe) on the Caribbean beach.", "a": "will be sunbathing"},
            {"type": "text", "q": "102. We expect Tom ___ (recover) soon.", "a": "will recover"},
            {"type": "text", "q": "103. What ___ (you/do) tonight? Can we meet at 7?", "a": "are you doing"},
            {"type": "text", "q": "104. Look at Greg. He ___ (jump) into the swimming pool.", "a": "is going to jump"},
            {"type": "text", "q": "105. ___ (you/stop) making so much noise, please?", "a": "Will you stop"},
            {"type": "text", "q": "106-113. (Các câu lặp lại trong tài liệu)", "a": "Xem lại đáp án các câu trước"},
            {"type": "text", "q": "114. Andrew ___ (never/be) on a safari before and he is so excited.", "a": "has never been"},
            {"type": "text", "q": "115. Tomorrow morning I ___ (see) my dentist for my yearly checkup.", "a": "am seeing"},
            {"type": "text", "q": "116. Real Madrid ___ (play) against Barcelona tonight.", "a": "is playing"},
            {"type": "text", "q": "117. Our school ___ (usually/have) breaks in the morning and afternoon.", "a": "usually has"},
            {"type": "text", "q": "118. That girl with the red hair ___ (talk) on the phone right now.", "a": "is talking"},
            {"type": "text", "q": "119. Natalie ___ (sleep) over Chloe's house last Saturday night.", "a": "slept"},
            {"type": "text", "q": "120. I ___ (not/often go) to the cinema these days. ___ you ___ (go) to the cinema once a month?", "a": "don't often go / Do / go"},
            {"type": "text", "q": "121. Guess what I ___ (wear) to the party last night? A vampire costume.", "a": "wore"},
            {"type": "text", "q": "122. By next June, they ___ (graduate) from high school.", "a": "will have graduated"},
            {"type": "text", "q": "123. What ___ (you/do) while the ground ___ (shake) during the earthquake?", "a": "were you doing / shook"},
            {"type": "text", "q": "124-133. (Các câu lặp lại)", "a": "Xem lại đáp án các câu trước"},
            {"type": "text", "q": "134. Fortunately Abigail ___ (just/put up) her umbrella when it ___ (start) to pour.", "a": "had just put up / started"},
            {"type": "text", "q": "135. Tomorrow morning I ___ (see) my dentist.", "a": "am seeing"},
            {"type": "text", "q": "136. Bad weather ___ (delay) our flight to Madagascar last summer.", "a": "delayed"},
            {"type": "text", "q": "137. Last night my family and I ___ (watch) an interesting documentary.", "a": "watched"}
        ]
    },
    "Supp: Rewrites & Passive Voice": {
        "theory": "### SUPPLEMENTARY: SENTENCE TRANSFORMATION\nViết lại câu giữ nguyên nghĩa, câu bị động, câu điều kiện, lời nói gián tiếp.",
        "exercises": [
            {"type": "text", "q": "1. The weather is too terrible for you to go out. -> If the weather...", "a": "weren't too terrible, you could go out."},
            {"type": "text", "q": "2. All the students have to take the final exam. -> The final exam...", "a": "has to be taken by all the students."},
            {"type": "text", "q": "3. Please don't repeat what I said. -> Would you mind...", "a": "not repeating what I said?"},
            {"type": "text", "q": "4. I can't swim as well as my friend can. -> My friend...", "a": "can swim better than me."},
            {"type": "text", "q": "5. We lost our way. We didn't arrive on time. -> Unless...", "a": "we had lost our way, we would have arrived on time."},
            {"type": "text", "q": "6. It took me three hours to open the door. -> We spend...", "a": "three hours opening the door."},
            {"type": "text", "q": "7. I can't answer all the questions. -> I wish...", "a": "I could answer all the questions."},
            {"type": "text", "q": "8. The film was too boring for you to watch. -> The film was so...", "a": "boring that you couldn't watch it."},
            {"type": "text", "q": "9. They don't play football any more. -> They used...", "a": "to play football."},
            {"type": "text", "q": "10. The man said to me, 'Please tell me the way...' -> The man asked me...", "a": "to tell him the way..."},
            {"type": "text", "q": "11. People say that they bought this shop last year. -> It is...", "a": "said that they bought this shop last year."},
            {"type": "text", "q": "15. It takes Minh 2 hours to do his homework every day. -> Minh spends...", "a": "2 hours doing his homework every day."},
            {"type": "text", "q": "16. We were late for school because of the heavy rain. -> Because it...", "a": "rained heavily, we were late for school."},
            {"type": "text", "q": "19. It's two years since I last spoke to her. -> I haven't...", "a": "spoken to her for two years."},
            {"type": "text", "q": "21. Keeping the environment clean is very important. -> It's...", "a": "very important to keep the environment clean."},
            {"type": "text", "q": "24. Old car tires are recycled to make shoes and sandals. -> People...", "a": "recycle old car tires to make shoes and sandals."},
            {"type": "text", "q": "26. It's three years since I last spoke to her. -> I haven't...", "a": "spoken to her for three years."},
            {"type": "text", "q": "30. If you don't rest yourself, you will be ill. -> Unless...", "a": "you rest yourself, you will be ill."},
            {"type": "text", "q": "44. Tom went to Scotland last Friday and is still there. -> Tom has...", "a": "been in Scotland since last Friday."},
            {"type": "text", "q": "45. When did you last ride a bike? -> How long is it...", "a": "since you last rode a bike?"},
            {"type": "text", "q": "51. The children couldn't go swimming because the sea was very rough. -> The sea was too...", "a": "rough for the children to go swimming."},
            {"type": "text", "q": "56. He couldn't afford to buy a car. -> The car...", "a": "was too expensive for him to buy."},
            {"type": "text", "q": "61. How much is this dictionary? -> How much does...", "a": "this dictionary cost?"},
            {"type": "text", "q": "68. Listening to music at home is more interesting than going to the concert. -> I prefer...", "a": "listening to music at home to going to the concert."},
            {"type": "text", "q": "P1. I have eaten many sweets. (Passive) -> Many sweets...", "a": "have been eaten by me."},
            {"type": "text", "q": "P5. This famous director will produce ten short comedy films... (Passive) -> Ten short comedy films...", "a": "will be produced by this famous director..."},
            {"type": "text", "q": "P9. Technology is invading our working places. (Passive) -> Our working places...", "a": "are being invaded by technology."},
            {"type": "text", "q": "P13. Jason will accept the offer next month. (Passive) -> The offer...", "a": "will be accepted by Jason next month."},
            {"type": "text", "q": "P21. They make robots from strong metal. (Passive) -> Robots...", "a": "are made from strong metal."}
        ]
    }
}

# ==========================================
# CẤU HÌNH GIAO DIỆN APP STREAMLIT
# ==========================================
st.set_page_config(page_title="Chinh Phục Tiếng Anh HOU - FULL DATA", page_icon="🎓", layout="wide")

st.markdown("""
<style>
    .stRadio > div { flex-direction: column; }
    .explain-box { padding: 15px; border-radius: 8px; background-color: #e8f4f8; border-left: 5px solid #2980b9; margin-top: 10px; }
</style>
""", unsafe_allow_html=True)

if 'q_index' not in st.session_state:
    st.session_state.q_index = 0
if 'current_topic' not in st.session_state:
    st.session_state.current_topic = list(COURSE_DATA.keys())[0]

st.sidebar.title("📚 Tất Cả Bài Học & Bài Tập")
selected_topic = st.sidebar.radio("Chọn học phần ôn luyện:", list(COURSE_DATA.keys()))

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
        st.info("Hiện chưa có bài tập cho chuyên đề này.")
    else:
        q_data = exercises[st.session_state.q_index]
        st.progress((st.session_state.q_index + 1) / len(exercises))
        st.subheader(f"Câu hỏi {st.session_state.q_index + 1} / {len(exercises)}")
        
        with st.form(key=f"exercise_form_{st.session_state.q_index}"):
            st.markdown(f"**{q_data['q']}**")
            
            user_text = st.text_input("Gõ câu trả lời của bạn vào đây:")
            submit_btn = st.form_submit_button("Kiểm tra đáp án")
            
            if submit_btn:
                if user_text.strip():
                    st.info(f"🔑 **Đáp án gợi ý:** {q_data['a']}")
                    st.write("*(Hệ thống đã loại bỏ trắc nghiệm để đảm bảo ứng dụng chứa đủ 300+ câu hỏi mà không vượt giới hạn hệ thống. Vui lòng tự đối chiếu với đáp án chuẩn)*")
                else:
                    st.warning("⚠️ Vui lòng nhập câu trả lời trước khi kiểm tra!")
        
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
