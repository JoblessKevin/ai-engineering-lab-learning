# ai-engineering-lab-learning
An AI learning project.

# VS code extension
Python, Pylance, Jupyter, GitLens, Remote SSH, Python Debugger, Black Formatter, Ruff (使用需停用 Black Formatter)

# Windows PowerShell
1. 確認 Python 與 pip
python --version
python -m pip --version

2. 建立專案與虛擬環境
cd \ai-engineering-lab-learning

python -m venv .venv

3. 啟用虛擬環境
.\.venv\Scripts\Activate.ps1

4. 驗證 Python 的實際位置 (預期看到 \ai-engineering-lab-learning\.venv\Scripts\python.exe)
python -c "import sys; print(sys.executable)"

# 安裝 pip 套件
1. 安裝 pip 套件
python -m pip install numpy
python -c "import numpy; print(numpy.__version__)"
python -m pip show numpy

2. 安裝 Jupyter lab
python -m pip install jupyterlab ipykernel
python -c "import sys; print(sys.executable)"

# 啟動 Jupyter Lab
python -m jupyter lab

# 檢查 GPU 顯卡
```bash
1. 作業系統資訊
Get-CimInstance Win32_OperatingSystem |
    Select-Object Caption, Version

2. CPU 資訊
Get-CimInstance Win32_Processor |
    Select-Object Name, NumberOfCores, NumberOfLogicalProcessors

3. 系統記憶體（RAM）
Get-CimInstance Win32_ComputerSystem |
    Select-Object @{Name="RAM_GB";Expression={
        [math]::Round($_.TotalPhysicalMemory / 1GB, 2)
    }}

4. 顯示卡資訊
Get-CimInstance Win32_VideoController |
    Select-Object Name, AdapterRAM

5. NVDIA 顯卡專用
nvidia-smi

# 理解 PyTorch 如何判斷 GPU 可用性
check_gpu_cuda.py

# AI API Key
$env:ANTHROPIC_API_KEY = "your-real-key"

# AI API Setting
model：指定模型 ID。模型名稱會變動，正式使用前應查看供應商的模型清單。
max_tokens：限制本次回應可產生的最大 Token 數，不是保證模型一定會用完這個數量。
messages：對話輸入。這裡只有一則 user message。
usage：回傳實際的 Token 用量資訊。
stop_reason：說明模型為什麼停止生成，例如正常完成或達到輸出限制。

# 安裝 uv
1. (Requirement)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
uv --version
uv venv .venv
uv pip install numpy pandas matplotlib

2. 根據 pyproject.toml 直接更新所有 dependency
uv sync

3. (Optional) 可以指定版本安裝
uv python install 3.12
uv venv --python 3.12 .venv

# uv 實際練習
1. 確認專案狀態
git status
uv --version
Test-Path .\pyproject.toml
Test-Path .\uv.lock

2. 建立獨立的 uv 練習環境
mkdir uv-practice
cd uv-practice
uv init --bare --no-workspace
uv python list

3. 用 uv 管理 Python 版本與依賴
uv add numpy
uv add pandas
uv add "google-genai"
Get-Content .\pyproject.toml
uv lock
uv sync


4. 確認 uv 確實在管理環境
uv run python -c "import sys; print(sys.executable)"
uv run python -c "import numpy, pandas; print('NumPy:', numpy.__version__); print('Pandas:', pandas.__version__)"
uv tree

"print('Hello from uv!')" | Set-Content .\hello.py
uv run hello.py

uv remove pandas
uv tree
uv add pandas
uv tree


# pyproject.toml
python 的 pom.xml

## 安裝 Hugging Face Datasets
cd C:\Users\yk.chiu\Documents\GitHub\ai-engineering-lab-learning\uv-practice
uv add datasets huggingface_hub
uv run python -c "import datasets, huggingface_hub; print(datasets.__version__); print(huggingface_hub.__version__)"
uv run python .\data_management.py


## Docker
docker desktop start

