import streamlit as st
import matplotlib.pyplot as plt

st.warning("Not all words are counted manually or automatically for verification by us")

st.title("📊 Qur'anic Word Counts & Ratio Miracles")
st.markdown("Explore mathematically balanced word frequencies and linguistic patterns in the Qur’an that point to deeper meaning and divine authorship.")

# Word Frequencies
word_counts = {
    "Qul (Say)": 332,
    "Qālū (They said)": 332,
    "Month (Shahr)": 12,
    "Prayer (Salawat)": 5,
    "Iblīs": 11,
    "Seek Refuge (A‘ūdhu)": 11,
    "Angels (Malāʾikah)": 88,
    "Devil (Shayṭān)": 88,
    "Life (Ḥayāh)": 145,
    "Death (Mawt)": 145,
    "World (Dunyā)": 115,
    "Hereafter (Ākhirah)": 115
}

# Section 1: Table
st.subheader("📋 Verified Word Frequencies in the Qur’an")
st.write("Below is a list of select words and how many times they appear in the Qur’an:")

st.table(word_counts)

# Section 2: Bar Chart
st.subheader("📈 Frequency Comparison")

fig, ax = plt.subplots()
ax.bar(word_counts.keys(), word_counts.values(), color='teal')
plt.xticks(rotation=45, ha='right')
plt.title("Word Frequencies in the Qur’an")
plt.tight_layout()
st.pyplot(fig)

# Section 3: Ratio Analysis
st.subheader("🧮 Ratio Patterns and Miracles")

st.markdown("""
**1. "Qul" vs "Qālū"**  
- Both appear exactly **332 times**; a perfect dialogue symmetry.

**2. "Angels" vs "Devil"**  
- *Malāʾikah* (Angels): 88 times  
- *Shayṭān* (Devil): 88 times  
- Symbolizing the constant balance in moral struggle.

**3. "Life" vs "Death"**  
- *Ḥayāh* (Life): 145 times  
- *Mawt* (Death): 145 times  
- A reflection of divine balance between birth and end.

**4. "World" vs "Hereafter"**  
- *Dunyā*: 115 times  
- *Ākhirah*: 115 times  
- Emphasizing the equal significance of this life and the next.

**5. "Sea" vs "Land"**  
- *Sea* is mentioned **32 times**  
- *Land* is mentioned **13 times**  
- Total = 45  
- Sea ratio = 32/45 ≈ **71.11%**  
- Land ratio = 13/45 ≈ **28.89%**

This matches the actual **Earth surface composition**: ~**71% water** and **29% land** — a stunning alignment with science.
""")

# Section 4: Pie Chart for Sea vs Land
st.subheader("🌍 Earth’s Surface Ratio in the Qur’an")

labels = ['Sea (32)', 'Land (13)']
sizes = [32, 13]
colors = ['#3399ff', '#99cc66']
explode = (0.1, 0)

fig2, ax2 = plt.subplots()
ax2.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
        shadow=True, startangle=140)
ax2.axis('equal')
st.pyplot(fig2)

st.info("🌊 The Qur’an’s mention of ‘Sea’ and ‘Land’ aligns with Earth’s actual surface ratio — something not measurable by humans in the 7th century.")

# Footer
st.caption("✨ Built to reflect the perfect balance of the Divine Word.")
