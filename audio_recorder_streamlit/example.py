import streamlit as st

from audio_recorder_streamlit import audio_recorder_ui
import time


state = 'init'
st.subheader("Base audio recorder")
status = audio_recorder_ui(
    key="base3",
    recording_color="red",
    neutral_color="#303030",
    icon_size="6x",
    icon_name="microphone",
    status=state
)
st.text("Click to record : {}".format(status))


st.text("for loop")
for i in range(10):
    if i == 5:
        time.sleep(5)
        state = 'stop'
        st.text("for loop stop")
        st.experimental_rerun()

st.text("for loop end")



# st.subheader("Custom recorder")
# custom_audio_bytes = audio_recorder(
#     text="",
#     recording_color="#e8b62c",
#     neutral_color="#6aa36f",
#     icon_name="user",
#     icon_size="6x",
#     sample_rate=41_000,
#     key="custom",
# )
# st.text("Click to record")
# if custom_audio_bytes:
#     st.audio(custom_audio_bytes, format="audio/wav")

# st.subheader("Fixed length recorder")
# fixed_audio_bytes = audio_recorder(
#     energy_threshold=(-1.0, 1.0),
#     pause_threshold=3.0,
#     key="fixed",
# )
# st.text("Click to record 3 seconds")
# if fixed_audio_bytes:
#     st.audio(fixed_audio_bytes, format="audio/wav")
