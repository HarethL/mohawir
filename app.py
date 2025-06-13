import streamlit as st

st.set_page_config(page_title="محاور - واجهة تفاعلية", page_icon="💬", layout="wide")

st.title("💬 محاور - تجربة تواصل ذكي بين المدير والموظف")

# ====== تسجيل الأسماء ======
st.sidebar.header("🧾 تسجيل الأسماء")
manager_name = st.sidebar.text_input("اسم المدير")
employee_name = st.sidebar.text_input("اسم الموظف")

if manager_name and employee_name:
    st.success(f"تم تسجيل الأسماء بنجاح: 👨‍💼 {manager_name} ↔️ 👨‍💻 {employee_name}")

    st.markdown("---")
    st.header("🧠 تحديد نمط شخصية الموظف")

    # ====== استبيان تحليل الشخصية ======
    q1 = st.radio("1. كيف تفضل أن تُعطى لك المهام؟", ["مباشرة وواضحة", "بشرح وتفصيل", "بلغة هادئة ومحفّزة"], key="q1")
    q2 = st.radio("2. إذا تأخرت في مهمة، كيف تفضل أن يتم تذكيرك؟", ["بتنبيه مباشر", "بشرح أثر التأخير", "بأسلوب داعم ومحفّز"], key="q2")
    q3 = st.radio("3. كيف تتخذ قراراتك؟", ["بسرعة ووضوح", "بعد تفكير وتحليل", "حسب الشعور والانطباع"], key="q3")

    if st.button("تحليل الشخصية"):
        scores = {"تنفيذي": 0, "تحليلي": 0, "عاطفي": 0}

        if q1 == "مباشرة وواضحة": scores["تنفيذي"] += 1
        elif q1 == "بشرح وتفصيل": scores["تحليلي"] += 1
        else: scores["عاطفي"] += 1

        if q2 == "بتنبيه مباشر": scores["تنفيذي"] += 1
        elif q2 == "بشرح أثر التأخير": scores["تحليلي"] += 1
        else: scores["عاطفي"] += 1

        if q3 == "بسرعة ووضوح": scores["تنفيذي"] += 1
        elif q3 == "بعد تفكير وتحليل": scores["تحليلي"] += 1
        else: scores["عاطفي"] += 1

        personality = max(scores, key=scores.get)
        st.session_state["personality"] = personality
        st.success(f"🎯 نمط شخصية الموظف هو: **{personality}**")

    # ====== واجهة الدردشة ======
    if "personality" in st.session_state:
        st.markdown("---")
        col1, col2 = st.columns(2)

        with col1:
            st.subheader(f"🗣️ رسالة من المدير ({manager_name})")
            message = st.text_area("اكتب رسالتك هنا", key="manager_message")
            if st.button("إرسال إلى الموظف"):
                personality = st.session_state["personality"]
                if personality == "تنفيذي":
                    rewritten = f"📌 {message.strip()}، يُرجى تنفيذه فورًا."
                elif personality == "تحليلي":
                    rewritten = f"🔍 {message.strip()}، مع شرح التفاصيل وتأثيرها على المهام."
                else:
                    rewritten = f"🌟 {message.strip()}، نثق بك وبقدرتك على إنجازها بإبداع."

                st.session_state["last_message"] = rewritten

        with col2:
            st.subheader(f"📥 الرسالة للموظف ({employee_name})")
            if "last_message" in st.session_state:
                st.info(st.session_state["last_message"])
            else:
                st.write("لم يتم إرسال رسالة بعد.")

else:
    st.warning("يرجى إدخال اسم المدير واسم الموظف أولاً لبدء التجربة.")
