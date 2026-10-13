import streamlit as st

st.set_page_config(
    page_title="RGB Colour Mixer",
    page_icon="🎨",
    layout="centered",
)

st.markdown(
    """
    <style>
    .main {
        background-color: #f5f7fb;
    }
    .title {
        text-align: center;
        color: #263859;
    }
    .subtitle {
        text-align: center;
        color: #596579;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    '<h1 class="title">🎨 RGB Colour Mixer</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="subtitle">Mix Red, Green and Blue to create your own colour!</p>',
    unsafe_allow_html=True,
)

st.divider()


def set_preset(r, g, b):
    st.session_state.red = r
    st.session_state.green = g
    st.session_state.blue = b


def reset_values():
    st.session_state.red = 128
    st.session_state.green = 128
    st.session_state.blue = 128


for channel, default in [
    ("red", 128),
    ("green", 128),
    ("blue", 128),
]:
    if channel not in st.session_state:
        st.session_state[channel] = default

st.subheader("Adjust RGB Values")

red = st.slider("🔴 Red", 0, 255, key="red")
green = st.slider("🟢 Green", 0, 255, key="green")
blue = st.slider("🔵 Blue", 0, 255, key="blue")

hex_color = f"#{red:02X}{green:02X}{blue:02X}"
rgb_color = f"rgb({red}, {green}, {blue})"

st.divider()
st.subheader("Your Mixed Colour")

st.markdown(
    f"""
    <div style="
        width: 100%;
        height: 220px;
        background-color: {hex_color};
        border-radius: 16px;
        border: 2px solid #dddddd;
        box-shadow: 0 4px 12px rgba(0,0,0,0.12);
    "></div>
    """,
    unsafe_allow_html=True,
)

col1, col2 = st.columns(2)
with col1:
    st.metric("RGB Value", f"{red}, {green}, {blue}")
with col2:
    st.metric("HEX Code", hex_color)

st.code(rgb_color, language="css")

st.subheader("Quick Colour Presets")
presets = {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255),
    "Yellow": (255, 255, 0),
    "Cyan": (0, 255, 255),
    "Magenta": (255, 0, 255),
    "White": (255, 255, 255),
    "Black": (0, 0, 0),
}

preset_columns = st.columns(4)
for index, (name, values) in enumerate(presets.items()):
    with preset_columns[index % 4]:
        st.button(
            name,
            key=f"preset_{name}",
            use_container_width=True,
            on_click=set_preset,
            args=values,
        )

st.button(
    "🔄 Reset RGB Values",
    on_click=reset_values,
    use_container_width=True,
)

st.divider()
st.info(
    "RGB is an additive colour model. Red, green and blue light combine "
    "to create different colours. Mixing all three at 255 produces white, "
    "while setting all three to 0 produces black."
)
st.caption("RGB Colour Mixer | Built with Python and Streamlit")
