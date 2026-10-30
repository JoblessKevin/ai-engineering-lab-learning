# Notebook vs Python Script：工程師應該怎麼選？
假設正在開發一個 RAG 系統，需要測試 Chunking 策略

可能會：
1. 載入 100 篇 PDF。
2. 測試不同 Chunk Size。
3. 比較 Embedding 結果。
4. 測量 Retrieval Latency。
5. 比較 Top-K 搜尋結果。
6. 記錄哪種設定效果最好。

這些工作很適合 Notebook，因為你需要不斷觀察、修改與比較。但當實驗完成後，不應該把整個正式系統都留在 Notebook 裡。

# Multiple Environment
| 學習階段 | 可能使用的套件 | 環境需求 |
| :--- | :--- | :--- |
| Phase 0 : Setup | NumPy、Jupyter、Pandas | 輕量 Python |
| Phase 1 : Math | NumPy、SciPy、Matplotlib | 數值運算 |
| Phase 2 : ML | Scikit-learn | 傳統 ML |
| Phase 3 : Deep Learning | PyTorch | GPU / CUDA |
| Phase 7 : Transformers | Transformers、Tokenizers | 可能需要特定 PyTorch 版本 |
| Phase 11 : LLM Engineering | Gemini、OpenAI、Anthropic SDK | API 開發，通常不需要 PyTorch |

# 未來架構的可能型式

ai-engineering-lab-learning/
│
├── .venv/                    # Phase 0-2 共用輕量環境
│
├── notebooks/
│   ├── lesson_05_jupyter.ipynb
│   └── experiments/
│
├── phases/
│   ├── deep-learning/
│   │   └── .venv/            # 專用 PyTorch 環境
│   │
│   ├── transformers/
│   │   └── .venv/            # 需要時建立獨立環境
│   │
│   └── llm-engineering/
│       └── .venv/            # LLM API SDK 環境
│
├── pyproject.toml
├── uv.lock
└── .gitignore


