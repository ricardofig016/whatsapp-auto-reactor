# WhatsApp Chat Auto-Reactor

This project is a Python script that runs in the background and scans WhatsApp Web for any messages from a specified chat. It automatically reacts to every message in the chat with the "🙏" emoji.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.10.12
- Selenium (`pip install selenium`)
- WebDriver for Google Chrome ([ChromeDriver](https://sites.google.com/chromium.org/driver/))

## Installation

1. Clone this repository or download the script file.

2. Install the required Python packages using pip:

   ```bash
   pip install selenium
   ```

3. Download ChromeDriver and ensure it is in your system's PATH.

## Usage

1. Open a terminal and navigate to the directory containing the script.

2. Run the script using Python:

   ```bash
   python main.py
   ```

3. You will be prompted to enter the name of the chat you want to monitor. Type the exact name of the chat and press Enter.

4. The script will open WhatsApp Web in your browser. Scan the QR code with your mobile device to log in.

5. The script will start monitoring the chat for new messages and automatically react to each new message with the "🙏" emoji.

## Script Details

1. **Initialization**:

   - The script initializes the Selenium WebDriver and opens WhatsApp Web.
   - It waits for the user to scan the QR code to log in.

2. **Chat Search**:

   - The script searches for the specified chat and opens it.

3. **Message Reaction**:
   - The script continuously monitors the chat for new messages.
   - It reacts to the latest message with the "🙏" emoji if it hasn't already been reacted to.

## Notes

- This script relies on web automation and can break if WhatsApp changes its web interface.
- Be mindful of WhatsApp's terms of service when using automation tools.
- The script waits for elements to be present on the page before interacting with them to avoid errors.

## License

This project is licensed under the [MIT LICENSE](./LICENSE).
