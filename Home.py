import streamlit as st

st.set_page_config(page_title="GoPhish", layout="wide")

st.markdown(
    """
        <style>div[data-testid="stToolbar"] { display: none;}</style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <style>
        .hero {
            background-color: #0d1117;
            padding: 50px;
            text-align: center;
            border-radius: 10px;
        }
        .hero h1 {
            font-size: 3em;
        }
        .cards {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 20px;
            margin-top: 30px;
        }
        .card {
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #f5f5f5; 
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 20px;
            width: 200px;
            text-align: center;
        }
        .card .head {
            height: 4rem;
            color: turquoise; /* Turquoise heading color */
            font-size: 1.4em;
            font-weight: bold;
            line-height: 1.2em;
        }
        .card p:not(.head) {
            padding-top: 1rem;
            border-top: 1px groove #ccc;
            color: #666;
            line-height: 1.2em;
        }
        .tip {
            padding-top: 1rem;
        }
    </style>
    <div class="hero">
        <h1>🎣 Welcome to <span style="color:turquoise;">Go</span>Phish!</h1>
        <p>GoPhish is your interactive phishing simulation tool designed to train employees on cybersecurity awareness.</p>
        <p>Track phishing engagement, register employees, and analyze results—all in one platform.</p>
        <div class="cards">
            <div class="card">
                <p class="head">📊 Dashboard</p>
                <p>View click rates and key stats</p>
            </div>
            <div class="card">
                <p class="head">👥 Employee Registration</p>
                <p>Add new employees to the system</p>
            </div>
            <div class="card">
                <p class="head">📈 Results</p>
                <p>See who passed or failed the phishing drill</p>
            </div>
            <div class="card">
                <p class="head">🤖 Chatbot</p>
                <p>Get real-time guidance on cybersecurity threats</p>
            </div>
        </div>
        <p class="tip">Use the <strong>sidebar</strong> to navigate between pages.</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
        <style>div[class="_profileContainer_gzau3_53"] { display: none;}</style>
        <style>div[class="_container_gzau3_1 _viewerBadge_nim44_23"] { display: none;}</style>
    """,
    unsafe_allow_html=True,
)
