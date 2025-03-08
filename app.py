import streamlit as st
import re
st.title("Password Strength Checker web app")
password = st.text_input("Enter your Password here" , type="password")
button=st.button("Check")
# list of common passwords
common_passwords = [
    "123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890",
    "qwerty", "abc123", "password1", "123123", "admin", "welcome", "iloveyou",
    "1q2w3e4r", "letmein", "football", "monkey", "sunshine", "1234"
]

if button :
    score = 0
    if password in common_passwords :
        st.text("⚠️ This is a commonly used password. Consider using a stronger one.")
        
    if len(password)>=8 :
        score = score+1
    else :
        st.text("❌Password should be 8 or more characters long")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score=score+1
    else :
        st.text("❌password must contain upper case and lower case letter")

    if re.search(r"\d", password):
        score += 1
    else:
        st.text("❌ Add at least one number (0-9).")
    
    if re.search(r"[!@#$%^&*.]", password):
        score += 1
    else:
        st.text("❌ Include at least one special character (!@#$%^&*).")
    if score == 4:
        st.text("✅ Strong Password!")
    elif score == 3:
        st.text("⚠️ Moderate Password - Consider adding more security features.")
    else:
        st.text("❌ Weak Password - Improve it using the suggestions above.")
