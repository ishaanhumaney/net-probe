# NetProbe

NetProbe is a lightweight, concurrent TCP port scanner written in standard Python. It skips bloated external dependencies, relying on native socket programming and multithreading to audit network endpoints quickly and efficiently.

## Value Proposition

Traditional network scanners can be heavy, require root privileges, or rely on massive third-party packages. NetProbe solves this by using Python's standard library to achieve rapid execution through a pool of worker threads. It’s an ideal script for quick security audits, debugging local network configurations, or integrating into larger automation pipelines where minimal overhead is required.

## Key Features

* **Concurrent Execution:** Uses `ThreadPoolExecutor` with 100 concurrent workers to scan 1,024 ports in seconds.
* **Zero Dependencies:** Built entirely using native Python modules (`socket`, `concurrent.futures`). No `pip install` required.
* **Graceful Error Handling:** Safely resolves hostnames and manages connection timeouts without crashing midway.
* **Clean CLI Interface:** Direct, interactive prompts with explicit status logging for open ports.

## Tech Stack Breakdown

* **Language:** Python 3.x
* **Core Libraries:** * `socket`: Handles low-level TCP stream connections (`socket.AF_INET`, `socket.SOCK_STREAM`).
    * `concurrent.futures`: Powers the `ThreadPoolExecutor` to handle non-blocking asynchronous scanning behavior.

## Quick Start

### Run in GitHub Codespaces (100% Browser)
1. Click the **Code** button at the top right of this repository.
2. Select the **Codespaces** tab and click **Create codespace on main**.
3. Once the terminal loads, run the tool directly:
   ```bash
   python main.py
   ```

### Local Setup
If you prefer running it locally, ensure you have Python 3 installed.
  1. Download main.py or download the repository ZIP file.
  2. Open your terminal in the directory containing the file.
  3. Run the script:
  ```bash
      python main.py
  ```
  4. Enter localhost or a target IP address when prompted.

## Project Structure
 ```bash
net-probe/
├── .github/
│   └── workflows/
│       └── ci.yml      # GitHub Actions linting workflow
├── .gitignore          # Ignores environment files and caches
├── LICENSE             # MIT License
├── README.md           # Documentation
└── main.py             # Main port scanner implementation
 ```

## Roadmap
[ ] Add argument parsing via argparse to support flag-based command inputs (e.g., -t 192.168.1.1 -p 80,443).

[ ] Implement customizable port range selection instead of the hardcoded 1–1024 bracket.

[ ] Add an option to export scan results directly into a structured format like JSON or text logs.

[ ] Support UDP port scanning alongside the current TCP infrastructure.
