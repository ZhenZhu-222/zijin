import streamlit as st

# 设置页面标题和图标
st.set_page_config(
    page_title="浪漫相遇",
    page_icon="💘",
    layout="centered",
)

# 使用 HTML 和 CSS 自定义样式
st.markdown(
    """
    <style>
    /* 全局背景 */
    .stApp {
        background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%);
        background-size: cover;
        background-position: center;
        animation: moveBackground 20s linear infinite;
    }
    @keyframes moveBackground {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    /* 气泡效果 */
    .bubbles {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        overflow: hidden;
        z-index: 0;
    }
    .bubbles li {
        position: absolute;
        list-style: none;
        display: block;
        width: 20px;
        height: 20px;
        background: rgba(255, 255, 255, 0.2);
        animation: animate 25s linear infinite;
        bottom: -150px;
    }
    .bubbles li:nth-child(1) {
        left: 25%;
        width: 80px;
        height: 80px;
        animation-delay: 0s;
    }
    .bubbles li:nth-child(2) {
        left: 10%;
        width: 20px;
        height: 20px;
        animation-delay: 2s;
        animation-duration: 12s;
    }
    .bubbles li:nth-child(3) {
        left: 70%;
        width: 20px;
        height: 20px;
        animation-delay: 4s;
    }
    .bubbles li:nth-child(4) {
        left: 40%;
        width: 60px;
        height: 60px;
        animation-delay: 0s;
        animation-duration: 18s;
    }
    .bubbles li:nth-child(5) {
        left: 65%;
        width: 20px;
        height: 20px;
        animation-delay: 0s;
    }
    .bubbles li:nth-child(6) {
        left: 75%;
        width: 110px;
        height: 110px;
        animation-delay: 3s;
    }
    .bubbles li:nth-child(7) {
        left: 35%;
        width: 150px;
        height: 150px;
        animation-delay: 7s;
    }
    .bubbles li:nth-child(8) {
        left: 50%;
        width: 25px;
        height: 25px;
        animation-delay: 15s;
        animation-duration: 45s;
    }
    .bubbles li:nth-child(9) {
        left: 20%;
        width: 15px;
        height: 15px;
        animation-delay: 2s;
        animation-duration: 35s;
    }
    .bubbles li:nth-child(10) {
        left: 85%;
        width: 150px;
        height: 150px;
        animation-delay: 0s;
        animation-duration: 11s;
    }
    @keyframes animate {
        0% {
            transform: translateY(0) rotate(0deg);
            opacity: 1;
            border-radius: 0;
        }
        100% {
            transform: translateY(-1000px) rotate(720deg);
            opacity: 0;
            border-radius: 50%;
        }
    }
    /* 文字内容 */
    .header {
        font-size: 48px;
        font-weight: bold;
        color: #ff6f61;
        text-align: center;
        margin-top: 50px;
        position: relative;
        z-index: 1;
    }
    .subheader {
        font-size: 24px;
        color: #fff;
        text-align: center;
        margin-top: 20px;
        position: relative;
        z-index: 1;
    }
    .quote {
        font-size: 20px;
        font-style: italic;
        color: #fff;
        text-align: center;
        margin-top: 40px;
        position: relative;
        z-index: 1;
    }
    .heart {
        font-size: 100px;
        color: #ff6f61;
        text-align: center;
        margin-top: 50px;
        animation: heartbeat 1.5s infinite;
        position: relative;
        z-index: 1;
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.2); }
        100% { transform: scale(1); }
    }
    .footer {
        font-size: 16px;
        color: #fff;
        text-align: center;
        margin-top: 100px;
        position: relative;
        z-index: 1;
    }
    /* 滚动图片 */
    .scrolling-images {
        display: flex;
        overflow: hidden;
        white-space: nowrap;
        margin-top: 50px;
        position: relative;
        z-index: 1;
    }
    .scrolling-images img {
        height: 150px;
        margin: 0 20px;
        animation: scroll-left 20s linear infinite;
    }
    .scrolling-images.reverse img {
        animation: scroll-right 20s linear infinite;
    }
    @keyframes scroll-left {
        0% { transform: translateX(100%); }
        100% { transform: translateX(-100%); }
    }
    @keyframes scroll-right {
        0% { transform: translateX(-100%); }
        100% { transform: translateX(100%); }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 动态背景
st.markdown(
    """
    <ul class="bubbles">
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
        <li></li>
    </ul>
    """,
    unsafe_allow_html=True,
)

# 网页内容
st.markdown('<div class="header">💘 浪漫相遇 💘</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">在这里，遇见你的另一半</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="quote">"在茫茫人海中，我遇见了你，就像星星遇见了月亮，注定要一起闪耀。"</div>',
    unsafe_allow_html=True,
)
st.markdown('<div class="heart">❤️</div>', unsafe_allow_html=True)

# 三行滚动图片
st.markdown(
    """
    <div class="scrolling-images">
        <img src="https://i.imgur.com/1.jpg" alt="Image 1">
        <img src="https://i.imgur.com/2.jpg" alt="Image 2">
        <img src="https://i.imgur.com/3.jpg" alt="Image 3">
        <img src="https://i.imgur.com/4.jpg" alt="Image 4">
        <img src="https://i.imgur.com/5.jpg" alt="Image 5">
    </div>
    <div class="scrolling-images reverse">
        <img src="https://i.imgur.com/6.jpg" alt="Image 6">
        <img src="https://i.imgur.com/7.jpg" alt="Image 7">
        <img src="https://i.imgur.com/8.jpg" alt="Image 8">
        <img src="https://i.imgur.com/9.jpg" alt="Image 9">
        <img src="https://i.imgur.com/10.jpg" alt="Image 10">
    </div>
    <div class="scrolling-images">
        <img src="https://i.imgur.com/11.jpg" alt="Image 11">
        <img src="https://i.imgur.com/12.jpg" alt="Image 12">
        <img src="https://i.imgur.com/13.jpg" alt="Image 13">
        <img src="https://i.imgur.com/14.jpg" alt="Image 14">
        <img src="https://i.imgur.com/15.jpg" alt="Image 15">
    </div>
    """,
    unsafe_allow_html=True,
)

# 页脚
st.markdown(
    '<div class="footer">© 2023 浪漫相遇 | 让爱从这里开始</div>',
    unsafe_allow_html=True,
)

# 背景音乐（可选）
st.markdown(
    """
    <iframe src="https://www.youtube.com/embed/5qap5aO4i9A?autoplay=1&loop=1&controls=0&mute=1" 
            width="0" height="0" frameborder="0" allow="autoplay"></iframe>
    """,
    unsafe_allow_html=True,
)