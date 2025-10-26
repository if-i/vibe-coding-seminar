import streamlit as st
from io import BytesIO
import base64

# Настройка страницы (самое начало)
st.set_page_config(page_title="Codex + AGENTS.md", layout="centered")

# SVG‑данные для слайдов
svg_data = {
    "intro": """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="200" fill="#4B86F4" rx="20" ry="20"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle"
          font-size="36" fill="#ffffff" font-family="Arial, sans-serif">
      Agent-Driven Coding
    </text>
    </svg>""",
    "what": """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="200" fill="#FF9F1C" rx="20" ry="20"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle"
          font-size="32" fill="#ffffff" font-family="Arial, sans-serif">
      Что это / Когда уместно
    </text>
    </svg>""",
    "why": """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="200" fill="#E5A833" rx="20" ry="20"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle"
          font-size="36" fill="#ffffff" font-family="Arial, sans-serif">
      Why AGENTS.md?
    </text>
    </svg>""",
    "agents": """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="200" fill="#65C18C" rx="20" ry="20"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle"
          font-size="36" fill="#ffffff" font-family="Arial, sans-serif">
      Agents Roles
    </text>
    </svg>""",
    "workflow": """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="200" fill="#E96A57" rx="20" ry="20"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle"
          font-size="36" fill="#ffffff" font-family="Arial, sans-serif">
      Workflow
    </text>
    </svg>""",
    "prompts": """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="200" fill="#6D5ACF" rx="20" ry="20"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle"
          font-size="36" fill="#ffffff" font-family="Arial, sans-serif">
      Prompts
    </text>
    </svg>""",
    "results": """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="200" fill="#40916C" rx="20" ry="20"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle"
          font-size="36" fill="#ffffff" font-family="Arial, sans-serif">
      Results
    </text>
    </svg>""",
    "lessons": """<svg width="800" height="200" xmlns="http://www.w3.org/2000/svg">
    <rect width="800" height="200" fill="#BB3E03" rx="20" ry="20"/>
    <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle"
          font-size="36" fill="#ffffff" font-family="Arial, sans-serif">
      Lessons
    </text>
    </svg>""",
}

# Помощник для отображения SVG с alt + base64
def render_svg(svg: str, alt: str = "slide"):
    if isinstance(svg, str):
        svg_bytes = svg.encode("utf-8")
    else:
        svg_bytes = svg
    b64 = base64.b64encode(svg_bytes).decode()
    st.markdown(
        f'<img src="data:image/svg+xml;base64,{b64}" alt="{alt}" style="max-width:100%;height:auto;">',
        unsafe_allow_html=True,
    )

# Помощник для контента слайда
def slide(title: str, content: str, subtitle: str | None = None) -> None:
    st.markdown(f"## {title}")
    if subtitle:
        st.markdown(f"#### {subtitle}")
    st.markdown(content)
    st.markdown("---")

# Порядок слайдов
slides = ["intro", "what", "why", "agents", "workflow", "prompts", "results", "lessons"]

# Боковая панель и CTA
st.sidebar.title("🎛️ Навигация по слайдам")
if "slide" not in st.session_state:
    st.session_state["slide"] = slides[0]

# Шаблон AGENTS.md для скачивания
AGENTS_MD_TEMPLATE = """# AGENTS.md
## Setup
- Install deps: `pip install -r requirements.txt`
- Run: `streamlit run streamlit_app.py`

## Roles
- Architect: defines scope, stack, and constraints
- Coder: implements tasks in small verifiable steps
- Reviewer: enforces tests, linting, and security checks

## Conventions
- Small PRs with clear intent
- Tests & type hints for non-trivial logic
- Secrets never in code; use env/secret manager
"""
st.sidebar.download_button(
    "Скачать AGENTS.md‑шаблон",
    AGENTS_MD_TEMPLATE,
    file_name="AGENTS.md",
    mime="text/markdown",
)
st.sidebar.markdown(
    "[Открыть репозиторий/слайды](https://github.com/if-i/vibe-coding-seminar)"
)

# Радио для выбора слайда
selected = st.sidebar.radio(
    "Перейти к слайду:", slides, index=slides.index(st.session_state["slide"])
)

# Next/Prev
c1, _, c3 = st.columns([1, 6, 1])
i = slides.index(selected)
with c1:
    if st.button("← Назад", disabled=(i == 0)):
        selected = slides[i - 1]
with c3:
    if st.button("Вперёд →", disabled=(i == len(slides) - 1)):
        selected = slides[i + 1]
st.session_state["slide"] = selected

# Краткие описания (alt/резюме)
summaries = {
    "intro": "Введение: Codex и AGENTS.md как ОС для вайбкодинга.",
    "what": "Что такое vibe coding и когда применять: rapid prototyping, внутренние тулзы; ограничения: нужен тестовый/ревью процесс для прод.",
    "why": "Зачем AGENTS.md: структурирует вибрацию кода, хранит контекст, сохраняет flow.",
    "agents": "Роли: Architect, Coder, Reviewer — отвечают за архитектуру, реализацию, ревью.",
    "workflow": "Рабочий цикл: Architect ставит задачу, Coder пишет, Reviewer проверяет.",
    "prompts": "Промпты: примеры хорошо и плохо работающих запросов.",
    "results": "Результаты: ускорение разработки, единообразие кода, повторяемость.",
    "lessons": "Уроки: AGENTS.md как env для мышления, важность формализованных ролей.",
}

# Рендеринг выбранного слайда
key = selected
if key == "intro":
    render_svg(svg_data["intro"], alt=summaries["intro"])
    st.caption(summaries["intro"])
    slide(
        "Agent-Driven Coding",
        """
        👋 Привет! Я расскажу, как использую **Codex (OpenAI)** и файл **AGENTS.md**
        как "операционную систему" для вайбкодинга.

        Это не просто промптинг — это **оркестрация контекста, правил и агентских ролей**, 
        чтобы код рождался в потоке, но оставался детерминированным.
        """,
    )
elif key == "what":
    render_svg(svg_data["what"], alt=summaries["what"])
    st.caption(summaries["what"])
    slide(
        "Что это / Когда уместно",
        """
        **Преимущества**:
        - ⚡️ Быстрый прототипинг и проверка гипотез
        - 🛠️ Создание внутренних инструментов и MVP
        - 🔁 Повторяемость и структурирование процессов

        **Ограничения**:
        - ✅ Использовать в проде только с тестами и ревью
        - 🧪 Требуется контроль качества и мониторинг
        - 🛑 Не заменяет традиционную инженерию, а дополняет её
        """,
    )
elif key == "why":
    render_svg(svg_data["why"], alt=summaries["why"])
    st.caption(summaries["why"])
    slide(
        "Зачем мне AGENTS.md?",
        """
        - Структурирует "вибрацию" кода: кто, как и зачем пишет.  
        - Хранит **контекст и протоколы взаимодействия** (developer / reviewer / explainer).  
        - Позволяет сохранять *flow* между сессиями Codex или GPT‑5.  

        💡 *Каждый агент = слой мышления*.  
        Это как если бы IDE знала твои привычки, а не просто синтаксис.

        [Подробнее про формат AGENTS.md](https://agents.md) — официальный документ со структурой ролей, примерами и best practices.
        """,
    )
elif key == "agents":
    render_svg(svg_data["agents"], alt=summaries["agents"])
    st.caption(summaries["agents"])
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
        - оценивает дифф по 3 параметрам: ясность, композиция, тестируемость
        ```

        💬 Промпты Codex используют эти роли как "персонажи" в кодовой сессии.
        """,
    )
elif key == "workflow":
    render_svg(svg_data["workflow"], alt=summaries["workflow"])
    st.caption(summaries["workflow"])
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
        """,
    )
elif key == "prompts":
    render_svg(svg_data["prompts"], alt=summaries["prompts"])
    st.caption(summaries["prompts"])
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
        """,
    )
elif key == "results":
    render_svg(svg_data["results"], alt=summaries["results"])
    st.caption(summaries["results"])
    slide(
        "Результаты",
        """
        📈 Прирост продуктивности:
        - ~2× скорость прототипирования  
        - код становится консистентным между проектами  
        - промпты становятся повторно используемыми (modular reasoning)

        🎯 Итог — вайбкодинг становится **реплицируемой практикой**, а не магией потока.
        """,
    )
elif key == "lessons":
    render_svg(svg_data["lessons"], alt=summaries["lessons"])
    st.caption(summaries["lessons"])
    slide(
        "Что я вынес",
        """
        - AGENTS.md — как `.env` для мышления: контекст + границы.  
        - Codex и GPT‑5 могут "чувствовать вайб", если ты формализуешь роли.  
        - Ключ к вайбкодингу — **редуцировать шум и усилить намерение**.

        🧠 *Вайбкодинг = синергия между агентами, кодом и состоянием сознания разработчика.*
        """,
    )
