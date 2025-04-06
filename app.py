import streamlit as st
import base64

# Page config
st.set_page_config(layout="wide")

# Load the image and convert to base64
def load_image_base64(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Use relative image path
image_path = "image.png"
image_base64 = load_image_base64(image_path)

# HTML, CSS, JS
html = f"""
<style>
.container {{
    position: relative;
    width: 100%;
    max-width: 1000px;
    margin: auto;
}}

.bg-image {{
    width: 100%;
    display: block;
}}

.marker {{
    position: absolute;
    width: 20px;
    height: 20px;
    background-color: red;
    border-radius: 50%;
    cursor: pointer;
    border: 2px solid white;
    z-index: 2;
}}

.info-box {{
    position: absolute;
    background-color: rgba(255, 255, 255, 0.95);
    padding: 12px 16px;
    border-radius: 8px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    display: none;
    z-index: 5;
    max-width: 250px;
}}

.close-btn {{
    margin-top: 10px;
    padding: 5px 10px;
    background-color: #d33;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}}

</style>

<div class="container">
    <img src="data:image/png;base64,{image_base64}" class="bg-image" />

    <!-- Marker 1 -->
    <div class="marker" style="top: 30%; left: 40%;" onclick="showInfo('info1', this)"></div>
    <div class="info-box" id="info1">
        <strong>📍 Point A</strong>
        <p>This is the detail for marker A.</p>
        <button class="close-btn" onclick="hideAll()">Close</button>
    </div>

    <!-- Marker 2 -->
    <div class="marker" style="top: 50%; left: 20%;" onclick="showInfo('info2', this)"></div>
    <div class="info-box" id="info2">
        <strong>📍 Point B</strong>
        <p>This is the detail for marker B.</p>
        <button class="close-btn" onclick="hideAll()">Close</button>
    </div>

    <!-- Marker 3 -->
    <div class="marker" style="top: 65%; left: 60%;" onclick="showInfo('info3', this)"></div>
    <div class="info-box" id="info3">
        <strong>📍 Point C</strong>
        <p>This is the detail for marker C.</p>
        <button class="close-btn" onclick="hideAll()">Close</button>
    </div>
</div>

<script>
function showInfo(id, markerElement) {{
    hideAll();

    const box = document.getElementById(id);
    const top = markerElement.style.top;
    const left = markerElement.style.left;

    const topPercent = parseFloat(top);
    const leftPercent = parseFloat(left);

    // Position slightly below and right of the marker
    box.style.top = (topPercent + 4) + '%';
    box.style.left = (leftPercent + 2) + '%';
    box.style.display = 'block';
}}

function hideAll() {{
    const boxes = document.getElementsByClassName('info-box');
    for (let box of boxes) {{
        box.style.display = 'none';
    }}
}}
</script>
"""

# Render the interactive layout
st.components.v1.html(html, height=800, scrolling=False)