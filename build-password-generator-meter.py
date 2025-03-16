import re
import streamlit as st

# Page Styling
st.set_page_config(page_title="Password Strength Checker by SanoberShahid", page_icon="🌘", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        .main { text-align: center; }
        .stTextInput { width: 60% !important; margin: auto; }
        .stButton button { 
            width: 50%; 
            background-color: blue; 
            color: white; 
            font-size: 18px;  
            border-radius: 8px;
            padding: 10px;
        } 
        .stButton button:hover { background-color: red; color: white; }      
    </style>
""", unsafe_allow_html=True)

# Page Title and Description
st.title("🌘 Password Strength Checker")
st.write("Enter your password below to check its security level! 🔍")

# Function to Check Password Strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be **at least 8 characters long**.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one number (0-9)**.")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Password should include **at least one special character (!@#$%^&*)**.")

    # Display password strength results
    if score == 4:
        st.success("✅ **Strong password** - Your password is secure.")
    elif score == 3:
        st.info("⚠️ **Moderate password** - Consider improving security by adding more features.")
    else:
        st.error("❌ **Weak password** - Follow the suggestions below to strengthen it.")

    # Display improvement suggestions
    if feedback:
        with st.expander("🔍 **Improve Your Password**"):
            for item in feedback:
                st.write(item)

# Password Input Field
password = st.text_input("🔐 Enter Your Password:", type="password", help="Ensure your password is strong.")

# Button Functionality
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")



# import re
# import streamlit as st


# #page styling

# st.set_page_config(page_title="Password strengh checker by SanoberShahid",page_icon="🌘", layout="centered")

# #custom css
# st.markdown("""
# <style>
#     .main {text-align: center; }
#     .stTextInput {width: 60% !important; margin: auto; }
#     .stButton button {width: 50%; background-color: blue; color: white; font-size: 18pxl; } 
#     .stButton button:hover { background-color: red; color: white;}      
# </style>           

# """, unsafe_allow_html=True)


# #page title and discription
# st.title("🌘 Password Strength Generator")
# st.write("Enter your password blow to check its security level!🔍")

# # function to check password strength
# def check_password_strength(password):
#     score = 0
#     feedback = []

#     if len(password) >= 8:
#         score += 1 # increased score by 1
#     else:
#         feedback.append("❌ Password should be **atleast 8 charactor long **. ")
#     if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
#         score += 1
#     else:
#         feedback.append("❌ Password should include **both upper (A-Z) and lover case (a-z) letters **. ")

#     if re.search(r"\d", password):
#         score += 1
#     else:
#         feedback.append("❌ Password should include **atleast one number (0-9) **. ")

# #specail charactures
#     if re.search(r"[!@#$%^&*]", password):
#         score += 1
#     else:
#         feedback.append("❌ include **atleast one specail charactor (!@#$%^&*)**. ")


# # display password strength results
    
#     if score == 4:
#         st.success("✅ ** Strong password** - your password is secure..")
#     elif score == 3:
#         st.info("⚠️ **Moderate password** - consider improving security by adding more feature")
#     else:
#         st.error("❌ **Weeked password** - follow the suggetion blow to strength it.")


# # feedback         
#     if feedback:
#         with st.expander("🔍 ** Improve your password ** "):
#             for item in feedback:
#                 st.write(item)
# password = st.text_input("Enter Your Password:", type="password", help="Ensure your password is strong 🔐")

# # button working

# if st.button("Checked Strength"):
#     if password:
#         check_password_strength(password)
#     else:
#         st.warning("⚠️ Please Enter a Password First!")# show warning if password is empyty