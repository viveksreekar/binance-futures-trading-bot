# Simplified Crypto Trading Bot (Binance Futures)

A robust Python-based trading bot built for the Binance Futures Testnet. This project was developed as part of the Junior Python Developer application task. It supports automated order execution with comprehensive logging and error handling.

## 🚀 Features
* **Market Orders**: Instant execution at current market prices.
* **Limit Orders**: Precise entry/exit at specified price targets.
* **Stop-Limit Orders (Bonus)**: Advanced risk management with trigger-based execution.
* **Robust Logging**: All API requests, responses, and errors are tracked in `bot_activity.log`.
* **Interactive CLI**: Simple command-line interface for user-driven trading.
* **Futures Optimized**: Configured specifically for the USDT-M Futures Testnet environment.

## 🛠️ Tech Stack
* **Language**: Python 3.13+
* **API Wrapper**: `python-binance`
* **Environment**: Binance Futures Testnet

## 📋 Prerequisites
1.  Python installed on your machine.
2.  Install the required library:
    ```bash
    pip install python-binance
    ```
3.  Binance Futures Testnet API Key and Secret.

## ⚙️ Configuration & Setup
1.  Clone the repository or download the source code.
2.  Navigate to the project directory.
3.  Run the bot:
    ```bash
    python bot.py
    ```
4.  Enter your API credentials when prompted (Note: For production, use environment variables).

## 📊 Usage Example
* **Select Symbol**: `BTCUSDT`
* **Market Buy**: Option `1`, Side `BUY`, Quantity `0.001`
* **Limit Sell**: Option `2`, Side `SELL`, Quantity `0.001`, Limit Price `95000`
* **Stop-Limit**: Option `3`, Side `SELL`, Quantity `0.001`, Stop Price `89000`, Limit Price `88950`

## 🛡️ Error Handling
The bot includes a custom exception handling wrapper that catches:
* `BinanceAPIException`: Handles invalid symbols, insufficient balance, and API downtime.
* `BinanceOrderException`: Manages malformed order parameters.
* **Connection Errors**: Gracefully handles 502 Bad Gateway and networking issues.

## 📂 Project Structure
* `bot.py`: Main application logic and CLI.
* `bot_activity.log`: Generated log file containing execution history.
* `README.md`: Documentation.

## ✉️ Submission Info
**Name**: C V Vivek Sreekar
**Role**: Junior Python Developer – Crypto Trading Bot
