import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="AI Tutor MVP", layout="wide")

st.title("👨‍🏫 AI Tutor - Hệ thống giảng dạy thông minh")

col1, col2 = st.columns([1, 2])

with col1:
    st.header("Tương tác")
    st.write("Nhấn vào nút bên dưới để nói chuyện với thầy giáo")
    
    # Nhúng Widget của Vapi (Lấy Public Key từ Dashboard Vapi)
    vapi_widget_code = """
    <script>
      var vapiInstance = null;
      const assistant = "7d17a5b8-d627-4224-9ef9-0b404de6edd2"; 
      const apiKey = "99789d88-4ebb-44ee-883c-f616591603f1"; 

      (function (d, s, id) {
        var js, vjs = d.getElementsByTagName(s)[0];
        if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = "https://cdn.jsdelivr.net/gh/VapiAI/html-script-tag@latest/dist/assets/index.js";
        vjs.parentNode.insertBefore(js, vjs);

        js.onload = () => {
          vapiInstance = window.vapiSDK.run({
            apiKey: apiKey,
            assistant: assistant,
            config: {
                display: {
                    position: "bottom-left",
                }
            }
          });
        };
      })(document, "script", "vapi-sdk");
    </script>
    """
    components.html(vapi_widget_code, height=200)

with col2:
    st.header("Bảng viết của thầy")
    # Khu vực hiển thị nội dung bài học
    content = st.text_area("Nội dung bài giảng (AI cập nhật...)", 
                          value="Hệ thống đang sẵn sàng. Hãy đặt câu hỏi!", height=400)
    
    # Hiển thị công thức Toán học nếu có
    st.latex(r'''a^2 + b^2 = c^2''') 
    st.info("Mẹo: AI sẽ tự động vẽ biểu đồ hoặc viết công thức tại đây.")