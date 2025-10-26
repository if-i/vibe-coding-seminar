import streamlit as st
from io import BytesIO

# SVG data for slides
import base64

# Monkey patch st.image to support SVG display
_original_image = st.image

def _patched_image(data, format=None, use_column_width=None):
    if format == "svg":
        b64 = base64.b64encode(data.getvalue()).decode()
        html = f'<img src="data:image/svg+xml;base64,{b64}" style="width:100%;height:auto;" />'
        st.markdown(html, unsafe_allow_html=True)
    else:
        _original_image(data, format=format, use_column_width=use_column_width)

st.image = _patched_image
svg_data = {
    "intro": """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="200" fill="#4B86F4" rx="20" ry="20"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="36" fill="#ffffff" font-family="Arial, sans-serif">Agent-Driven Coding</text>
    </svg>""",
    "why": """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="200" fill="#E5A833" rx="20" ry="20"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="36" fill="#ffffff" font-family="Arial, sans-serif">Why AGENTS.md?</text>
    </svg>""",
    "agents": """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="200" fill="#65C18C" rx="20" ry="20"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="36" fill="#ffffff" font-family="Arial, sans-serif">Agents Roles</text>
    </svg>""",
    "workflow": """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="200" fill="#E96A57" rx="20" ry="20"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="36" fill="#ffffff" font-family="Arial, sans-serif">Workflow</text>
    </svg>""",
    "prompts": """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="200" fill="#6D5ACF" rx="20" ry="20"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="36" fill="#ffffff" font-family="Arial, sans-serif">Prompts</text>
    </svg>""",
    "results": """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="200" fill="#40916C" rx="20" ry="20"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="36" fill="#ffffff" font-family="Arial, sans-serif">Results</text>
    </svg>""",
    "lessons": """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="200" fill="#BB3E03" rx="20" ry="20"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-size="36" fill="#ffffff" font-family="Arial, sans-serif">Lessons</text>
    </svg>""",
}

def get_svg_bytes(key):
    return BytesIO(svg_data[key].encode('utf-8'))

def slide(title, content, subtitle=None):
    st.markdown(f"## {title}")
    if subtitle:
        st.markdown(f"#### {subtitle}")
    st.markdown(content)
    st.markdown("---")

st.set_page_config(page_title="Codex + AGENTS.md", layout="centered")

st.sidebar.title("🎛️ Навигация по слайдам")
slides = ["intro", "why", "agents", "workflow", "prompts", "results", "lessons"]
current_slide = st.sidebar.radio("Перейти к слайду:", slides, index=0)

if current_slide == "intro":
    st.image(get_svg_bytes("intro"), format="svg", use_column_width=True)
    slide(
        "Agent-Driven Coding",
        """
        👋 Привет! Я расскажу, как использую **Codex (OpenAI)** и файл **AGENTS.md**
        как "операционную систему" для вайбкодинга.

        Это не просто промптинг — это **оркестрация контекста, правил и агентских ролей**, 
        чтобы код рождался в потоке, но оставался детерминированным.
        """
    )
elif current_slide == "why":
    st.image(get_svg_bytes("why"), format="svg", use_column_width=True)
    slide(
        "Зачем мне AGENTS.md?",
        """
        - Структурирует "вибрацию" кода: кто, как и зачем пишет.  
        - Хранит **контекст и протоколы взаимодействия** (developer / reviewer / explainer).  
        - Позволяет сохранять *flow* между сессиями Codex или GPT‑5.  

        💡 *Каждый агент = слой мышления*.  
        Это как если бы IDE знала твои привычки, а не просто синтаксис.

        [Подробнее про формат AGENTS.md](https://agents.md) — официальный документ со структурой ролей, примерами и best practices.
        """
    )
elif current_slide == "agents":
    st.image(get_svg_bytes("agents"), format="svg", use_column_width=True)
    slide(
        "Структура AGENTS.md",
        """
        ```markdown
        # AGENTS.md

        ## Architect
        - отвечает за структуру проекта и tech decisions  
        - всегда формулирует цели как API‑границы

        ## Coder
        - реализует минимально работающую версию  
        - ориентируется на DX и читаемость

        ## Reviewer
        - оценивает дифф по 3 параметрам: ясность, композиция, тестируемость
        ```

        💬 Промпты Codex используют эти роли как "персонажи" в кодовой сессии.
        """
    )
elif current_slide == "workflow":
    st.image(get_svg_bytes("workflow"), format="svg", use_column_width=True)
    slide(
        "Workflow: Codex + AGENTS.md",
        """
        1️⃣ Открываю проект → подгружается AGENTS.md  
        2️⃣ Codex считывает роли → контекст синхронизируется с workspace  
        3️⃣ Запускается "агентный цикл":
        - Architect ставит цель
        - Coder пишет
        - Reviewer комментирует  
        4️⃣ Результат — чистый код + trace reasoning в комментариях.

        ⚙️ В итоге Codex превращается не в autocomplete, а в *collaborative teammate*.
        """
    )
elif current_slide == "prompts":
    st.image(get_svg_bytes("prompts"), format="svg", use_column_width=True)
    slide(
        "Рабочие промпты",
        """
        ✅ Хорошо работают:
        - "Act as Reviewer defined in AGENTS.md, critique the diff."
        - "As Architect, refactor for scalability, not performance."
        - "Coder: implement but don’t explain unless asked."

        🚫 Не работают:
        - "Just fix this" без контекста роли.  
        - Слишком общее "improve this code" — Codex теряет целостность агента.
        """
    )
elif current_slide == "results":
    st.image(get_svg_bytes("results"), format="svg", use_column_width=True)
    slide(
        "Результаты",
        """
        📈 Прирост продуктивности:
        - ~2× скорость прототипирования  
        - код становится консистентным между проектами  
        - промпты становятся повторно используемыми (modular reasoning)

        🎯 Итог — вайбкодинг становится **реплицируемой практикой**, а не магией потока.
        """
    )
elif current_slide == "lessons":
    st.image(get_svg_bytes("lessons"), format="svg", use_column_width=True)
    slide(
        "Что я вынес",
        """
        - AGENTS.md — как `.env` для мышления: контекст + границы.  
        - Codex и GPT‑5 могут "чувствовать вайб", если ты формализуешь роли.  
        - Ключ к вайбкодингу — **редуцировать шум и усилить намерение**.

        🧠 *Вайбкодинг = синергия между агентами, кодом и состоянием сознания разработчика.*
        """
    )
