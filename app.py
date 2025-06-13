import streamlit as st

st.set_page_config(page_title="محاور", page_icon="💬", layout="centered")

st.title("💬 محاور - مساعدك الذكي في فهم وتوصيل الرسائل")

st.markdown("ابدأ بالإجابة على الأسئلة التالية لتحديد نمط شخصيتك في التواصل، ثم أضف رسالة المدير وسيتم إعادة صياغتها بما يتناسب معك.")

# الأسئلة
q1 = st.radio("1. كيف تفضل أن تُعطى لك المهام؟", ["مباشرة وواضحة", "بشرح وتفصيل", "بلغة هادئة وتحفيزية"])
q2 = st.radio("2. إذا تأخرت في مهمة، كيف تفضل أن يتم تذكيرك؟", ["بتنبيه مباشر", "بشرح أثر التأخير", "بأسلوب داعم ومحفز"])
q3 = st.radio("3. كيف تتخذ قراراتك؟", ["بسرعة ووضوح", "بعد تفكير وتحليل", "حسب الشعور والانطباع"])

# تحديد النمط
if st.button("تحديد شخصيتي"):
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
    st.success(f"🎯 نمط شخصيتك في التواصل هو: **{personality}**")
    st.session_state["personality"] = personality

# إعادة الصياغة
if "personality" in st.session_state:
    st.markdown("---")
    st.subheader("✉️ إعادة صياغة رسالة المدير")

    message = st.text_area("أدخل رسالة المدير هنا")

    if st.button("إعادة الصياغة حسب شخصيتي"):
        personality = st.session_state["personality"]
        if personality == "تنفيذي":
            rewritten = f"📌 {message.strip()}، يُرجى تنفيذه فورًا."
        elif personality == "تحليلي":
            rewritten = f"🔍 {message.strip()}، مع شرح التفاصيل وتأثيرها على المهام."
        else:
            rewritten = f"🌟 {message.strip()}، نثق بك وبقدرتك على إنجازها بإبداع."

        st.write("### ✍️ الرسالة المعدّلة:")
        st.info(rewritten)
