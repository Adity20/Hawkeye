import streamlit as st
import new11

# Title of the application
st.title("HawkEye - Navigation Aid for the Blind")

# Button to start/stop the camera feed
if "camera_started" not in st.session_state:
    st.session_state.camera_started = False

if st.button("Start Camera"):
    st.session_state.camera_started = not st.session_state.camera_started
    if st.session_state.camera_started:
        st.success("Camera started. Processing...")
    else:
        st.warning("Camera stopped.")

# If camera is started, show the camera feed and process the data
if st.session_state.camera_started:
    # Get the frame and process it to detect objects and calculate distances
    frame, results = new11.process_camera_feed()

    # Display the camera feed
    st.image(frame, caption="Live Camera Feed", channels="RGB")

    # Display the results from the object detection
    if results:
        for obj, distance in results.items():
            st.write(f"Object: {obj}, Distance: {distance} meters")

        # Audio feedback logic here (play audio for distance)
        new11.play_audio_feedback(results)
    else:
        st.warning("No objects detected.")
