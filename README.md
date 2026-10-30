# ai-engineering-lab-learning
An AI learning project.

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

# 學習 uv
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


# pyproject.toml
python 的 pom.xml