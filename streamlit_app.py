import streamlit as st

server = st.server.Server.get_current()

st.title("Streamlit Survey")
st.markdown("""
<style>
    .st-emotion-cache-zq5wmm.ezrtsby0
    {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

st.header("Welcome to this survey of how dumb is Elliot")


def get_iq_message(iq):
    if iq <= 24:
        return "This points out to Elliot having a profound mental disability, sounds about right."
    elif 25 <= iq <= 39:
        return "This points out to Elliot having a severe mental disability, looks accurate."
    elif 40 <= iq <= 54:
        return "This points out to Elliot having a moderate mental disability. Must admit this is most probably true."
    elif 55 <= iq <= 69:
        return "This points out to Elliot having a mild mental disability. You don't have to feel pity for the guy."
    elif 70 <= iq <= 84:
        return "This points out to Elliot having a borderline mental disability, you're just being generous at this point."
    elif 85 <= iq <= 114:
        return "This points out to Elliot having an average intelligence, who are you kidding ?"
    elif 115 <= iq <= 129:
        return "This points out to Elliot being above average or bright, as if XD."
    elif 130 <= iq <= 144:
        return "This points out to Elliot being moderately gifted, you are lowering the bar so much."
    elif 145 <= iq <= 159:
        return "This points out to Elliot being highly gifted. I get it, you feel pity for the guy."
    elif 160 <= iq <= 179:
        return "This points out to Elliot being exceptionally gifted. Just get yourself checked out at this point."
    else:
        return "This points out to Elliot being profoundly gifted, well you just lowered that makes the rest of humanity geniouses by default."

username = st.text_input("Enter your username:")

iq = st.slider("Select Elliot's IQ:", 1, 180, 1)
st.write(get_iq_message(iq))

submitted = st.button("Submit")

if 'shared_data' not in st.session_state:
    st.session_state.shared_data = {'messages': []}
    
def add_message(message):
    st.session_state.shared_data['messages'].append(message)
    
st.markdown("---")

if submitted:
    if username:
        add_message(f"{username} assigned Elliot an IQ of: {iq}")
        st.write("\n\n".join(st.session_state.messages))
        server.broadcast_message({'type': 'update_shared_data', 'data': st.session_state.shared_data})
    else:
        st.warning("Username is required.")
