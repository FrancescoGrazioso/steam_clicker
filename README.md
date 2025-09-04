# Steam Clicker - Hollow Knight Silksong Auto Purchase

A simple Python script to automatically click the Steam cart purchase button and verify the purchase was successful by checking pixel colors.

## 🚀 Quick Setup

### 1. Install Dependencies
```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install pyautogui pynput
```

### 2. Configure Coordinates

Edit `main.py` and update these values:

```python
# ----- CONFIG -----
CLICK_POS = (855, 724)            # where to click (Steam cart purchase button)
CHECK_POS = (297, 332)            # pixel to check (verification area)
TARGET_RGB = (30, 40, 55)       # target color (success indicator)
INTERVAL_SECONDS = 0.5            # main interval
# ------------------
```

**How to find coordinates:**
1. Open Steam and go to your cart with Hollow Knight Silksong
2. Use a tool like [MouseInfo](https://automatetheboringstuff.com/chapter18/) to get exact pixel coordinates
3. Replace `CLICK_POS` with the purchase button coordinates
4. Replace `CHECK_POS` with a pixel that changes color when purchase succeeds
5. Update `TARGET_RGB` with the success color (RGB values)

### 3. Run the Script
```bash
python main.py
```

## 🎮 How It Works

1. **Clicks** the Steam cart purchase button at regular intervals
2. **Checks** a specific pixel color to verify purchase success
3. **Stops** when the target color is detected (purchase successful)
4. **Safety**: Press `5` key or move mouse to top-left corner to stop anytime

## ⚠️ Important Notes

- **Test first**: Run with a cheap item to verify coordinates work correctly
- **Steam must be visible**: The script needs to see the Steam window
- **Don't move mouse**: Keep the mouse away from the top-left corner (failsafe)
- **One purchase only**: The script stops after detecting successful purchase

## 🛑 Emergency Stop

- Press `5` key
- Move mouse to top-left corner of screen
- Close the terminal window

## 📋 Requirements

- Python 3.6+
- Steam client
- Hollow Knight Silksong in cart
- macOS/Windows/Linux

---

**Disclaimer**: Use responsibly. This script is for educational purposes. Make sure you have sufficient funds in your Steam wallet.
