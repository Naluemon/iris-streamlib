import streamlit as st

# 1. ตั้งค่าหน้ากระดาษ
st.set_page_config(page_title="Calculator ML", page_icon=":material/calculate:", layout="centered")

# 2. ปรับแต่งดีไซน์ด้วย CSS
st.markdown("""
    <style>
    div.stButton > button:first-child {
        background-color: #007bff;
        color: white;
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #0056b3;
        border: none;
    }
    .stNumberInput, .stSelectbox {
        margin-bottom: 20px;
    }
    /* ปรับแต่งกล่องผลลัพธ์ */
    .result-card {
        background-color: #d4edda;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. ส่วนหัว (ตัด st.write ออกตามที่แจ้ง)
st.title(":material/calculate: Simple Calculator")

# 4. ส่วนอินพุตและคำนวณ
with st.container(border=True):
    col1, col2 = st.columns(2)
    
    with col1:
        num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
    with col2:
        num2 = st.number_input("Enter second number", value=0.0, format="%.2f")

    operation = st.selectbox(
        "Select Operation",
        ["➕ Add", "➖ Subtract", "✖️ Multiply", "➗ Divide"]
    )

    if st.button("Calculate Now"):
        with st.spinner('Calculating...'):
            result = None
            
            if "Add" in operation:
                result = num1 + num2
            elif "Subtract" in operation:
                result = num1 - num2
            elif "Multiply" in operation:
                result = num1 * num2
            elif "Divide" in operation:
                if num2 == 0:
                    st.error("🚨 Error: Cannot divide by zero")
                else:
                    result = num1 / num2

            if result is not None:
                st.balloons()
                st.markdown(f"""
                    <div class="result-card">
                        <h2 style="color:#155724; margin:0; font-size: 1.2rem;">Result</h2>
                        <h1 style="color:#155724; margin:0; font-size: 2.5rem;">{result:,.2f}</h1>
                    </div>
                """, unsafe_allow_html=True)