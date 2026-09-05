# BlogForge

BlogForge is a local AI writing workspace for generating technical blog articles. It uses a Streamlit interface and a LangGraph workflow to route a topic, optionally research current information, create an article plan, write sections in parallel, and assemble the final Markdown article.

The default language model runs locally through Ollama, so the main writing workflow does not require an OpenAI API key.

## Features

- Local LLM generation with Ollama
- Structured planning with Pydantic models
- LangGraph workflow orchestration
- Automatic research routing for current or volatile topics
- Tavily web search support
- Parallel section writing
- Optional technical image planning and Gemini image generation
- Markdown article output
- Streamlit workspace with article history, progress, previews, and downloads
- Downloadable Markdown and ZIP bundles

## Requirements

- Windows 10 or newer
- Python 3.11 or newer
- Ollama
- At least 8 GB RAM for a small local model
- Internet access for package installation and optional Tavily/Gemini features

The default model is `qwen2.5:3b-instruct`, which is a practical starting point for an 8 GB RAM computer. Larger models may require more memory.

## Project Structure

```text
blog_writing_agent/
|-- backend/
|   |-- graph.py                 LangGraph workflow definition
|   |-- llm_initialization.py    Ollama ChatOllama configuration
|   |-- model.py                 Pydantic schemas and graph state
|   |-- orchestrator.py          Article planning node
|   |-- reducer.py               Markdown reducer
|   |-- reducer_with_image.py    Image planning and final assembly
|   |-- router.py                Research decision node
|   |-- tavily_search.py         Tavily research node
|   |-- worker.py                Parallel section writer
|-- frontend/
|   |-- app.py                   Streamlit application entry point
|   |-- markdown_css.py          Custom Streamlit styles
|-- run_app.py                   One-click Python launcher
|-- README.md
```

Generated Markdown files are written to the current project directory. Generated images are written to the `images/` directory when image generation is used.

## Installation

### 1. Install Python

Install Python 3.11 or newer from:

```text
https://www.python.org/downloads/
```

During installation, enable the option to add Python to PATH.

Check the installation:

```powershell
python --version
```

### 2. Create a virtual environment

From the project root:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this once in an elevated PowerShell window or use Command Prompt instead:

```powershell
.venv\Scripts\activate.bat
```

### 3. Install Python packages

```powershell
python -m pip install --upgrade pip
python -m pip install streamlit pandas langgraph langchain-core langchain-ollama langchain-community pydantic python-dotenv tavily-python google-genai
```

`google-genai` is only needed when Gemini image generation is enabled. `tavily-python` is needed for web research when the application routes a topic to research.

### 4. Install and prepare Ollama

Install Ollama from:

```text
https://ollama.com/download/windows
```

Start Ollama, then download the default model:

```powershell
ollama pull qwen2.5:3b-instruct
```

Confirm that the model is available:

```powershell
ollama list
```

You can test it directly:

```powershell
ollama run qwen2.5:3b-instruct
```

Exit the model prompt with `Ctrl+C` after confirming it responds.

Ollama normally serves the API at:

```text
http://localhost:11434
```

## Environment Variables

Create a `.env` file in the project root for optional configuration. Never commit this file or place real API keys in source code.

```dotenv
OLLAMA_MODEL=qwen2.5:3b-instruct
OLLAMA_BASE_URL=http://localhost:11434

# Optional: enables web research when the router requests it.
TAVILY_API_KEY=your_tavily_key_here

# Optional: enables Gemini image generation.
GOOGLE_API_KEY=your_google_api_key_here
```

### Ollama configuration

The application reads these values from the environment:

- `OLLAMA_MODEL`: model name, default `qwen2.5:3b-instruct`
- `OLLAMA_BASE_URL`: Ollama server URL, default `http://localhost:11434`

The code also accepts the older `LM_STUDIO_MODEL` and `LM_STUDIO_BASE_URL` variable names as fallbacks for compatibility, but Ollama variable names are recommended.

### Tavily configuration

Tavily is optional. If `TAVILY_API_KEY` is missing, research returns no web evidence and the rest of the workflow can still run for topics that do not require current sources.

Get a Tavily key from:

```text
https://tavily.com/
```

### Gemini image configuration

The reducer asks the local LLM whether useful visuals are needed. If images are requested, Gemini image generation requires `GOOGLE_API_KEY` and the `google-genai` package. If image generation fails, the article remains usable and includes a failure note in place of the image.

## Running the Application

### One-click launch

After installing Python packages and Ollama, run:

```powershell
python run_app.py
```

The launcher locates the project directory, prefers the local `.venv`, sets `PYTHONPATH`, and starts Streamlit with the correct frontend entry point. You can also double-click `run_app.py` on Windows if `.py` files are associated with Python.

### PowerShell launch

From the project root:

```powershell
$env:PYTHONPATH = "."
python -m streamlit run frontend/app.py
```

Streamlit normally opens the application automatically. If it does not, open:

```text
http://localhost:8501
```

Keep the terminal window open while using the application. Stop the server with `Ctrl+C`.

## How the Workflow Works

1. Enter an article topic in the Streamlit workspace.
2. The router asks the local LLM whether research is required.
3. If research is needed, Tavily searches for relevant evidence.
4. The orchestrator creates a structured article plan.
5. The worker fan-outs the plan tasks and writes sections in parallel.
6. The reducer orders and combines the sections into Markdown.
7. The image reducer asks whether diagrams or visuals improve the article.
8. Optional Gemini image generation creates image files in `images/`.
9. The final article is displayed in Streamlit and can be downloaded as Markdown or a ZIP bundle.

## Output Files

- Markdown articles are written in the project working directory.
- Image assets are written to `images/`.
- The Streamlit article view provides Markdown, bundle, and image download controls.

Use short, descriptive topics because the topic is sent through the router, planner, and section-writing stages. For current events, pricing, model releases, rankings, or weekly roundups, configure Tavily so the article can use fresh evidence.

## Troubleshooting

### `ModuleNotFoundError: No module named 'backend'`

Run Streamlit from the project root and set `PYTHONPATH`:

```powershell
cd D:\WB\blog_writing_agent\blog_writing_agent
$env:PYTHONPATH = "."
python -m streamlit run frontend/app.py
```

The included `run_app.py` already does this automatically.

### `No module named streamlit`

Activate the virtual environment and install the dependencies:

```powershell
.venv\Scripts\Activate.ps1
python -m pip install streamlit
```

### Ollama connection errors

Check that Ollama is installed and running:

```powershell
ollama list
ollama run qwen2.5:3b-instruct
```

If Ollama is running on another address, set `OLLAMA_BASE_URL` in `.env`.

### Research returns no sources

Confirm that `.env` contains a valid `TAVILY_API_KEY`. Research is optional, so the application may continue without sources when the key is missing or a request fails.

### Gemini image generation errors

Install the SDK and configure the key:

```powershell
python -m pip install google-genai
```

Then add `GOOGLE_API_KEY` to `.env`. Image generation is optional; Markdown generation can still complete without it.

### The browser does not open

Open the Streamlit URL manually:

```text
http://localhost:8501
```

If that port is busy, Streamlit will print another local URL in the launcher window.

## Security Notes

- Keep `.env` local and out of Git.
- Do not paste API keys into Python files, README files, screenshots, or commits.
- If a secret was ever committed, rotate the key and remove it from Git history before pushing again.

## Development Checks

Run a syntax and import check from the project root:

```powershell
python -m py_compile backend\*.py frontend\app.py frontend\markdown_css.py
python -c "from backend.graph import app; print('graph import ok')"
```

The main application entry point is `frontend/app.py`; the backend graph is exposed as `backend.graph.app`.
