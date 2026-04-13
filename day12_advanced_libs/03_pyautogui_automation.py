#!/usr/bin/env python3
"""Day 12, Lesson 3: PyAutoGUI - GUI Automation & Scripting

Learn to automate repetitive GUI tasks:
- Mouse movements and clicks
- Keyboard input
- Screen detection
- Click patterns and delays
"""

from pyautogui import *
import time

print("=== PyAutoGUI: Automate GUI Tasks ===\n")

# Important: Run this in a safe environment!
# To stop a script: Move mouse to corner or press Ctrl+C

# 1. Get screen size
print("1. Screen Information:")
width, height = size()
print(f"   Screen size: {width}x{height}")
print(f"   Current mouse position: {position()}")

# 2. Safe moves (with safety pause)
print("\n2. Mouse Movements:")
PAUSE = 0.5  # Safety pause between actions
setAutoClickRepeatRate(0.5)

# Move to position (safe demo - top-left corner)
write("✓ Can move mouse to any screen position\n", interval=0.05)
write("✓ moveTo(x, y) - instant movement\n", interval=0.05)
write("✓ move(dx, dy) - relative movement\n", interval=0.05)

# 3. Mouse buttons
print("\n3. Mouse Actions:")
write("✓ click() - left click at position\n", interval=0.05)
write("✓ rightClick() - right click\n", interval=0.05)
write("✓ doubleClick() - double click\n", interval=0.05)
write("✓ drag(dx, dy) - click and drag\n", interval=0.05)

# 4. Keyboard input
print("\n4. Keyboard Actions:")
write("✓ typewrite('hello') - type text\n", interval=0.05)
write("✓ press('returnKey') - press key\n", interval=0.05)
write("✓ hotkey('ctrl', 'c') - key combos\n", interval=0.05)

# 5. Image detection
print("\n5. Image Recognition:")
write("✓ Can locate images on screen\n", interval=0.05)
write("✓ locateOnScreen('image.png')\n", interval=0.05)
write("✓ Returns (x, y) position or None\n", interval=0.05)

# 6. Real-world examples (commented for safety)
print("\n6. Real-world Automation (Examples):")

# Example: Auto-fill form
"""
# Click on name field, type name
click(100, 200)
typewrite('John Doe', interval=0.1)

# Tab to next field
press('tab')
typewrite('john@example.com', interval=0.1)

# Click submit button
click(500, 300)
"""

# Example: Repetitive clicking
"""
for i in range(5):
    click(300, 300)  # Click position
    time.sleep(0.5)  # Wait between clicks
"""

print("\n⚠️  SAFETY BEST PRACTICES:")
print("  1. Always set PAUSE delay between actions")
print("  2. Add time.sleep() between rapid actions")
print("  3. Test with print() before running automations")
print("  4. Keep mouse in corner to interrupt script")
print("  5. Use try-except for error handling")

print("\n🎯 USE CASES:")
print("  • Automated testing")
print("  • Form filling")
print("  • Repetitive file operations")
print("  • Game automation")
print("  • Screenshot processing")

print("\n✅ PyAutoGUI lesson complete!")
print("\n⚠️  DISCLAIMER: Use automation responsibly.")
print("   Don't use for malicious purposes.")
