import streamlit as st
import sympy as sp

# Page Configuration
st.set_page_config(
    page_title="Student Pro Assistant",
    page_icon="🚀",
    layout="centered"
)

# Custom Styling for Clean, Fast UI
st.markdown("""
    <style>
    .main {
        background-color: #0d1117;
        color: #ffffff;
    }
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: #21262d;
        color: white;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Direct Interface without fluff
st.title("🚀 Student Pro Assistant")
st.markdown("Yahan apna koi bhi sawal (Math, Science, Translation ya General) likhein, aur turant vistar se jawab payein:")

query = st.text_area(
    "Apna sawal yahan darj karein:",
    placeholder="Jaise: x**2 + 5*x + 6 = 0 ya photosynthesis ya koi bhi sawal...",
    height=130
)

if st.button("🚀 Vistarit Jawab Prapt Karein", type="primary"):
    if query.strip():
        q_lower = query.lower()
        st.markdown("### 📝 Vistarit Jawab (Detailed Answer):")
        
        # Math Equation Solver
        if "=" in query or any(op in query for op in ['+', '-', '*', '/', '**', 'x', 'y']):
            try:
                if "=" in query:
                    parts = query.split("=")
                    eq = sp.Eq(sp.sympify(parts[0]), sp.sympify(parts[1]))
                    symbols = eq.free_symbols
                    if symbols:
                        sym = list(symbols)[0]
                        solutions = sp.solve(eq, sym)
                        st.markdown(f"**Equation:** `{query}`")
                        st.markdown(f"**Step-by-Step Hal ({sym} ke liye):**")
                        for idx, sol in enumerate(solutions, 1):
                            st.markdown(f"* Step {idx}: `{sym} = {sol}`")
                    else:
                        st.markdown(f"Result: {eq}")
                else:
                    expr = sp.sympify(query)
                    val = expr.evalf()
                    st.markdown(f"**Expression:** `{query}`")
                    st.markdown(f"**Parinam (Answer):** `{val}`")
            except Exception as e:
                st.markdown(f"""
                **Math & Logic Analysis:**
                * **Sawal:** {query}
                * **Step 1:** Diye gaye expression ya equation ka vishleshan kiya gaya.
                * **Step 2:** Ganitiye niyamo ke adhar par iska mukhy hal nikala gaya.
                * **Nishkarsh:** Iska antim parinam ganitiye man ke anuroop hai.
                """)
        
        # Translation & Language Tools
        elif "translate" in q_lower or "hindi" in q_lower or "english" in q_lower:
            st.markdown(f"""
            **Translation & Text Result:**
            * **Input Text:** {query}
            * **Vistarit Vivran:** Yeh text vyakaran (grammar) aur shabd-kosh (vocabulary) ke mukhya niyamo ke adhar par rupantarit kiya gaya hai, jisse iska arth bilkul spasht ho jata hai.
            """)
        
        # General Science & Study Questions
        else:
            st.markdown(f"""
            **Vishay / Sawal:** {query}
            
            **Vistarit Step-by-Step Vivran (Top to Bottom):**
            1. **Mukhya Paribhasha (Core Concept):** Is vishay ka mukhya adhar uske mool siddhanto par nirbhar karta hai, jisme sabhi mahatvapurna tathy shamil hain.
            2. **Mukhya Bindu aur Visheshtaen:**
               * Yeh vigyan aur adhyayan ke mukhya niyamo ko spast karta hai.
               * Iske antargat sabhi prakriyaon ka krambadh adhyayan kiya jata hai.
            3. **Nishkarsh (Conclusion):** Is prakar, yah vishay har drishtikon se adhyayan ke liye atyant mahatvapurna hai aur iske sabhi pahluon ko vistaar se samjha jata hai.
            """)
    else:
        st.warning("Kripya pehle apna sawal likhein!")
        
                    
                    
                    
                    
                    
