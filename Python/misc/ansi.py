# --- Define the variables ---
RESET = '\033[0m'

BOLD = '\033[1m'
DIM = '\033[2m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
BLINK_SLOW = '\033[5m'
BLINK_FAST = '\033[6m'
REVERSE = '\033[7m'
HIDDEN = '\033[8m'
STRIKETHROUGH = '\033[9m'

RESET_BOLD_DIM = '\033[22m'
RESET_ITALIC = '\033[23m'
RESET_UNDERLINE = '\033[24m'
RESET_BLINK = '\033[25m'
RESET_REVERSE = '\033[27m'
RESET_HIDDEN = '\033[28m'
RESET_STRIKETHROUGH = '\033[29m'

BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
DEFAULT_FG = '\033[39m'

BRIGHT_BLACK = '\033[90m'
BRIGHT_RED = '\033[91m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_MAGENTA = '\033[95m'
BRIGHT_CYAN = '\033[96m'
BRIGHT_WHITE = '\033[97m'

BG_BLACK = '\033[40m'
BG_RED = '\033[41m'
BG_GREEN = '\033[42m'
BG_YELLOW = '\033[43m'
BG_BLUE = '\033[44m'
BG_MAGENTA = '\033[45m'
BG_CYAN = '\033[46m'
BG_WHITE = '\033[47m'
DEFAULT_BG = '\033[49m'

BG_BRIGHT_BLACK = '\033[100m'
BG_BRIGHT_RED = '\033[101m'
BG_BRIGHT_GREEN = '\033[102m'
BG_BRIGHT_YELLOW = '\033[103m'
BG_BRIGHT_BLUE = '\033[104m'
BG_BRIGHT_MAGENTA = '\033[105m'
BG_BRIGHT_CYAN = '\033[106m'
BG_BRIGHT_WHITE = '\033[107m'

CLEAR_SCREEN = '\033[2J'
CLEAR_LINE = '\033[K'
CURSOR_HOME = '\033[H'

# ==============================================================================
# EXAMPLES
# ==============================================================================

print("=== 1. TEXT STYLES & MODIFIERS ===")
print(f"{BOLD}This text is bold.{RESET}")
print(f"{DIM}This text is dim / faint.{RESET}")
print(f"{ITALIC}This text is italicized.{RESET} (Not supported by all terminals)")
print(f"{UNDERLINE}This text is underlined.{RESET}")
print(f"{BLINK_SLOW}This text flashes slowly.{RESET}")
print(f"{BLINK_FAST}This text flashes rapidly.{RESET} (Rarely supported)")
print(f"{REVERSE}This text has inverted foreground and background.{RESET}")
print(f"Hidden text next: [{HIDDEN}SecretPassword{RESET}] (Highlight the text box to reveal it)")
print(f"{STRIKETHROUGH}This text has a line through it.{RESET}")
print()

print("=== 2. INDIVIDUAL STYLE RESETS ===")
# These turn off one specific style without resetting the color or other styles
print(f"{BOLD}{RED}Bold Red {RESET_BOLD_DIM}Still Red but Normal Weight{RESET}")
print(f"{ITALIC}{UNDERLINE}{GREEN}Italic Underline Green {RESET_ITALIC}Still Underline Green{RESET}")
print()

print("=== 3. STANDARD FOREGROUND COLORS (3-Bit) ===")
print(f"{BLACK}Black text{RESET} (Might be invisible on dark backgrounds)")
print(f"{RED}Red text{RESET}")
print(f"{GREEN}Green text{RESET}")
print(f"{YELLOW}Yellow text{RESET}")
print(f"{BLUE}Blue text{RESET}")
print(f"{MAGENTA}Magenta text{RESET}")
print(f"{CYAN}Cyan text{RESET}")
print(f"{WHITE}White / Gray text{RESET}")
print(f"{RED}Red text changed back to {DEFAULT_FG}default foreground color{RESET}")
print()

print("=== 4. HIGH-INTENSITY BRIGHT FOREGROUND COLORS (4-Bit) ===")
print(f"{BRIGHT_BLACK}Bright Black / Dark Gray text{RESET}")
print(f"{BRIGHT_RED}Bright Red text{RESET}")
print(f"{BRIGHT_GREEN}Bright Green text{RESET}")
print(f"{BRIGHT_YELLOW}Bright Yellow text{RESET}")
print(f"{BRIGHT_BLUE}Bright Blue text{RESET}")
print(f"{BRIGHT_MAGENTA}Bright Magenta text{RESET}")
print(f"{BRIGHT_CYAN}Bright Cyan text{RESET}")
print(f"{BRIGHT_WHITE}Bright White text{RESET}")
print()

print("=== 5. STANDARD BACKGROUND COLORS ===")
print(f"{BG_BLACK}{WHITE} White text on Black background {RESET}")
print(f"{BG_RED} Text on Red background {RESET}")
print(f"{BG_GREEN} Text on Green background {RESET}")
print(f"{BG_YELLOW}{BLACK} Black text on Yellow background {RESET}")
print(f"{BG_BLUE} Text on Blue background {RESET}")
print(f"{BG_MAGENTA} Text on Magenta background {RESET}")
print(f"{BG_CYAN}{BLACK} Black text on Cyan background {RESET}")
print(f"{BG_WHITE}{BLACK} Black text on White background {RESET}")
print()

print("=== 6. HIGH-INTENSITY BRIGHT BACKGROUND COLORS ===")
print(f"{BG_BRIGHT_BLACK} Text on Bright Black background {RESET}")
print(f"{BG_BRIGHT_RED} Text on Bright Red background {RESET}")
print(f"{BG_BRIGHT_GREEN}{BLACK} Black text on Bright Green background {RESET}")
print(f"{BG_BRIGHT_YELLOW}{BLACK} Black text on Bright Yellow background {RESET}")
print(f"{BG_BRIGHT_BLUE} Text on Bright Blue background {RESET}")
print(f"{BG_BRIGHT_MAGENTA} Text on Bright Magenta background {RESET}")
print(f"{BG_BRIGHT_CYAN}{BLACK} Black text on Bright Cyan background {RESET}")
print(f"{BG_BRIGHT_WHITE}{BLACK} Black text on Bright White background {RESET}")
print()

print("=== 7. MIXING EVERYTHING TOGETHER ===")
print(f"{BOLD}{UNDERLINE}{BRIGHT_GREEN}{BG_BLUE}Bold Underline Bright Green text on a Blue background!{RESET}")
print()

print("=== 8. UTILITIES (Wipes output right after showing) ===")
input("Press Enter to test the CLEAR_SCREEN utility sequence...")
print(CLEAR_SCREEN + CURSOR_HOME)
print("The screen was cleared and the cursor was moved to the top left corner!")