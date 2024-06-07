

import streamlit as st
from streamlit_mic_recorder import speech_to_text

# Initialize session state variable if it doesn't exist
if 'STT_output' not in st.session_state:
    st.session_state['STT_output'] = ''

# Call the speech_to_text function
text = speech_to_text(language='en', use_container_width=True, just_once=True, key='STT')

#st.write(f"Session state key: {'STT_output'}")
st.write(f"{st.session_state.get('STT_output', 'Not set')}")

# Use the session state variable
# st.write(st.session_state['STT_output'])
