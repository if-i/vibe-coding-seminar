import streamlit as st
from itertools import cycle
from PIL import Image

# --- Config ---
st.set_page_config(page_title="Codex + AGENTS.md", layout="centered")

# --- Helper ---
def slide(title, content, subtitle=None):
    st.markdown(f"## {title}")
    if subtitle:
        st.markdown(f"#### {subtitle}")
    st.markdown(content)
    st.markdown("---")

# --- Sidebar ---
st.sidebar.title("🎛️ Навигация по слайдам")
slides = [
    "intro", "why", "agents", "workflow", "prompts", "results", "lessons"
]
current_slide = st.sidebar.radio("Перейти к слайду:", slides, index=0)

# --- Content ---
if current_slide == "intro":
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
    slide(
        "Зачем мне AGENTS.md?",
        """
        - Структурирует "вибрацию" кода: кто, как и зачем пишет.  
        - Хранит **контекст и протоколы взаимодействия** (developer / reviewer / explainer).  
        - Позволяет сохранять *flow* между сессиями Codex или GPT-5.  

        [Подробнее про формат AGENTS.md](https://agents.md) — официальный документ со структурой ролей, примерами и best practices.  

        💡 *Каждый агент = слой мышления*.  
        Это как если бы IDE знала твои привычки, а не просто синтаксис.
        """
    )

elif current_slide == "agents":
    slide(
        "Структура AGENTS.md",
        """
        ```markdown
        # AGENTS.md

        ## Architect
        - отвечает за структуру проекта и tech decisions  
        - всегда формулирует цели как API-границы

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
    slide(
        "Что я вынес",
        """
        - AGENTS.md — как `.env` для мышления: контекст + границы.  
        - Codex и GPT-5 могут "чувствовать вайб", если ты формализуешь роли.  
        - Ключ к вайбкодингу — **редуцировать шум и усилить намерение**.

        🧠 *Вайбкодинг = синергия между агентами, кодом и состоянием сознания разработчика.*
        """
    )
    st.success("Спасибо за внимание! ✨ Вопросы?")
