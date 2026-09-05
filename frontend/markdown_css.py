css = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        --bg: #f7f7f5;
        --surface: #ffffff;
        --surface-soft: #f2f2ef;
        --border: #e7e7e2;
        --text: #181816;
        --muted: #77776f;
        --accent: #171717;
    }

    .stApp {
        background: var(--bg);
        color: var(--text);
        font-family: "DM Sans", sans-serif;
    }

    .stApp > header {
        background: transparent;
    }

    [data-testid="stSidebar"] {
        background: #111110;
        border-right: 0;
    }

    [data-testid="stSidebar"] * {
        color: #f5f5f0;
    }

    [data-testid="stSidebar"] .stButton button {
        background: #f5f5f0 !important;
        color: #111110 !important;
        border: 0;
        border-radius: 10px;
        font-weight: 700;
    }

    [data-testid="stSidebar"] .stButton button * {
        color: #111110 !important;
    }

    [data-testid="stSidebar"] .stButton button:hover {
        background: #ffffff;
        color: #111110;
    }

    .brand {
        font-family: "Space Grotesk", sans-serif;
        font-size: 23px;
        font-weight: 700;
        letter-spacing: -0.7px;
        margin-bottom: 30px;
    }

    .brand-mark {
        display: inline-flex;
        width: 30px;
        height: 30px;
        align-items: center;
        justify-content: center;
        border-radius: 9px;
        background: #f5f5f0;
        color: #111110;
        margin-right: 8px;
        font-size: 16px;
    }

    .sidebar-label {
        color: #888880 !important;
        text-transform: uppercase;
        letter-spacing: 1.2px;
        font-size: 10px;
        font-weight: 700;
        margin: 24px 0 10px;
    }

    .sidebar-blog {
        padding: 9px 10px;
        border-radius: 8px;
        color: #c8c8c2 !important;
        font-size: 13px;
        margin-bottom: 2px;
    }

    .sidebar-blog:hover {
        background: #20201e;
    }

    .hero {
        padding: 52px 0 24px;
        max-width: 880px;
    }

    .eyebrow {
        color: var(--muted);
        text-transform: uppercase;
        letter-spacing: 1.8px;
        font-size: 11px;
        font-weight: 700;
        margin-bottom: 14px;
    }

    .hero h1 {
        font-family: "Space Grotesk", sans-serif;
        font-size: clamp(40px, 5vw, 64px);
        line-height: 0.98;
        letter-spacing: -3px;
        margin: 0;
        max-width: 780px;
    }

    .hero p {
        color: var(--muted);
        font-size: 17px;
        line-height: 1.6;
        margin-top: 18px;
        max-width: 650px;
    }

    .input-card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 22px;
        box-shadow: 0 8px 30px rgba(0,0,0,.035);
    }

    .input-label {
        font-size: 12px;
        color: var(--muted);
        font-weight: 600;
        margin-bottom: 7px;
    }

    .chip {
        display: inline-block;
        background: var(--surface-soft);
        border: 1px solid var(--border);
        padding: 7px 11px;
        border-radius: 999px;
        font-size: 12px;
        color: #55554e;
        margin: 4px 4px 0 0;
    }

    .section-title {
        font-family: "Space Grotesk", sans-serif;
        font-size: 23px;
        font-weight: 700;
        letter-spacing: -0.7px;
        margin: 40px 0 14px;
    }

    .article-shell {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 36px 44px;
        box-shadow: 0 8px 30px rgba(0,0,0,.035);
    }

    .article-shell h1 {
        font-family: "Space Grotesk", sans-serif;
        font-size: 42px;
        line-height: 1.08;
        letter-spacing: -1.8px;
    }

    .article-shell h2 {
        font-family: "Space Grotesk", sans-serif;
        margin-top: 36px;
        letter-spacing: -.7px;
    }

    .article-shell p,
    .article-shell li {
        font-size: 16px;
        line-height: 1.8;
        color: #30302c;
    }

    .meta-card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 15px 16px;
        margin-bottom: 10px;
    }

    .meta-label {
        color: var(--muted);
        font-size: 10px;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 700;
    }

    .meta-value {
        font-size: 14px;
        font-weight: 600;
        margin-top: 4px;
    }

    .progress-card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 20px;
    }

    .step {
        padding: 9px 0;
        font-size: 14px;
        border-bottom: 1px solid var(--border);
    }

    .step:last-child {
        border-bottom: 0;
    }

    .step-done {
        color: #33332f;
    }

    .step-active {
        font-weight: 700;
    }

    .step-muted {
        color: #a1a19a;
    }

    div[data-testid="stTextArea"] textarea {
        border-radius: 12px;
        border: 1px solid var(--border);
        background: #fbfbfa;
        font-size: 16px;
        line-height: 1.6;
    }

    div[data-testid="stTextArea"] textarea:focus {
        border-color: #999991;
        box-shadow: none;
    }

    .stButton > button {
        border-radius: 10px;
        min-height: 42px;
        font-weight: 600;
    }

    .stButton > button[kind="primary"] {
        background: #171717 !important;
        border-color: #171717 !important;
        color: #ffffff !important;
    }

    .stButton > button[kind="primary"] * {
        color: #ffffff !important;
    }

    .library-card {
        background: white;
        border: 1px solid var(--border);
        border-radius: 15px;
        padding: 18px;
        min-height: 125px;
    }

    .library-title {
        font-family: "Space Grotesk", sans-serif;
        font-size: 17px;
        font-weight: 700;
        letter-spacing: -.3px;
    }

    .library-meta {
        color: var(--muted);
        font-size: 12px;
        margin-top: 10px;
    }

    .small-muted {
        color: var(--muted);
        font-size: 12px;
    }

    .topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 8px 0 22px;
        border-bottom: 1px solid var(--border);
        margin-bottom: 28px;
    }

    .topbar-title {
        font-family: "Space Grotesk", sans-serif;
        font-size: 20px;
        font-weight: 700;
    }

    .source-item {
        padding: 12px 0;
        border-bottom: 1px solid var(--border);
    }

    .source-title {
        font-weight: 600;
        font-size: 14px;
    }

    .source-url {
        color: var(--muted);
        font-size: 11px;
        overflow-wrap: anywhere;
        margin-top: 4px;
    }

    /* Hide Streamlit chrome that makes the app feel like a prototype. */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""
   