import streamlit as st
import streamlit.components.v1 as components


def html_text_area_with_live_byte_counter(label: str, key: str, default: str = "", height: int = 150, max_bytes: int = 2000,):

    html_code = f"""
    <div style="font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin-top: 15px;">
        <label for="{key}" style="font-weight: bold;">{label}</label><br>
        <textarea id="{key}"
                  style="width: calc(100% - 20px);height:{height}px;font-size:16px;padding:8px;
                         border:1px solid #ccc;border-radius:6px;">{default}</textarea>
        <div id="{key}_counter" style="margin-top:6px;">
            <strong>Byte counter:</strong> <span id="{key}_byteCount">0</span> / {max_bytes}
        </div>
        <a id="{key}_download" download="output.txt"
           style="display:inline-block; margin-top:12px; padding:10px 18px; border:none;
                  border-radius:8px; text-decoration:none; background:#4CAF50; color:white;
                  font-weight:600; transition: background 0.3s;">
           ⬇ Download as .txt
        </a>
        <script>
            const box = document.getElementById("{key}");
            const counter = document.getElementById("{key}_byteCount");
            const maxBytes = {max_bytes};
            const dl = document.getElementById("{key}_download");

            function updateUI() {{
                const encoder = new TextEncoder();
                const bytes = encoder.encode(box.value).length;
                counter.textContent = bytes;
                counter.parentElement.style.color = bytes > maxBytes ? "red" : "inherit";

                const blob = new Blob([box.value], {{type: "text/plain;charset=utf-8"}});
                const url = URL.createObjectURL(blob);
                dl.href = url;
            }}

            box.addEventListener("input", updateUI);
            updateUI();
        </script>
    </div>
    """
    components.html(html_code, height=height + 140, scrolling=False)


# Demo app
st.title("Live Byte Counter + Client-side Download")
st.markdown(
    "Type your text below. The byte counter updates in real-time, "
    "and you can download your input as a `.txt` file."
)
html_text_area_with_live_byte_counter("Enter text:", key="mytextarea", default="", max_bytes=2000)
