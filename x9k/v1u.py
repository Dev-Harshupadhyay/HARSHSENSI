#!/usr/bin/env python3
"""
HARSH SENSI - Terminal UI & Colors
===================================
Colorful ASCII art logo, WELCOME banner aur exit par JAI SHREE RAM.
Pure ASCII art - har terminal / font me perfect render hota hai.
"""
from __future__ import annotations

# --- ANSI Colors ---
_RESET = "\033[0m"
_BOLD = "\033[1m"
_CYAN = "\033[96m"
_GREEN = "\033[92m"
_YELLOW = "\033[93m"
_MAGENTA = "\033[95m"
_RED = "\033[91m"
_BLUE = "\033[94m"
_WHITE = "\033[97m"
_ORANGE = "\033[38;5;208m"   # Saffron / Bhagwa
_SAFFRON = "\033[33m"

# --- ASCII Art : HARSH ---
_ART_HARSH = r"""
  _   _    _    ____  ____  _____
 | | | |  / \  |  _ \|  _ \/ ____|
 | |_| | / _ \ | |_) | |_) \___ \
 |  _  |/ ___ \|  _ <|  _ < |___) |
 |_| |_/_/   \_\_| \_\|_| \_\____/
"""

# --- ASCII Art : SENSI ---
_ART_SENSI = r"""
  ____  _____ _   _ ____  _____
 / ___|| ____| \ | |/ ___||_   _|
 \___ \| _|   | \| |\___ \ | |
  ___) | |___ | |\  |___) || |
 |____/|_____||_| |____/ |_|
"""

# --- Small Logo Mark ---
_LOGO_SMALL = r"""
      +----------------------+
      |  _   _    _    ____  |
      |  | | |  / \  |  _ \   |
      |  |_| | / _ \ | |_)   |
      |  |  |/ ___ \|  _ <   |
      |  |_|/_/   \_\_| \_\  |
      +----------------------+
         HARSH SENSI  -  FF
"""

_RAINBOW = ["\033[91m", "\033[93m", "\033[92m", "\033[96m", "\033[94m", "\033[95m"]


def rainbow(text: str) -> str:
    """Har character ko alag rang do - colourful text."""
    out, idx = [], 0
    for ch in text:
        if ch == " ":
            out.append(" ")
        else:
            out.append(f"{_RAINBOW[idx % len(_RAINBOW)]}{ch}{_RESET}")
            idx += 1
    return "".join(out)


def colorful(text: str) -> str:
    """Cyan -> Magenta gradient colourful text."""
    return f"{_CYAN}{_BOLD}{text}{_MAGENTA}{_RESET}"


def logo() -> None:
    """HARSH SENSI ka bada colourful ASCII logo."""
    print(f"{_ORANGE}{_BOLD}{_ART_HARSH}{_RESET}")
    print(f"{_CYAN}{_BOLD}{_ART_SENSI}{_RESET}")
    print(f"{_YELLOW}{_BOLD}  ** HARSH SENSI **  {_RESET}{_GREEN}Free Fire Sensitivity Engine{_RESET}")
    print(f"{_MAGENTA}{'=' * 54}{_RESET}")


def welcome() -> None:
    """WELCOME HARSH SENSI - colourful welcome banner."""
    print()
    logo()
    print(f"{_GREEN}{_BOLD}  * WELCOME HARSH SENSI *{_RESET}")
    print(f"  {rainbow('WELCOME TO HARSH SENSI - YOUR PERSONAL SENSI ENGINE')}")
    print(f"  {_WHITE}Made with love for the Free Fire Community{_RESET}")
    print(f"  {_YELLOW}Developer : HARSH{_RESET}  {_CYAN}|{_RESET}  {_MAGENTA}Tool : HARSH SENSI{_RESET}")
    print(f"{_MAGENTA}{'=' * 54}{_RESET}")
    print()


def goodbye() -> None:
    """Exit par badhiya JAI SHREE RAM."""
    print()
    print(f"{_ORANGE}{_BOLD}+{'=' * 52}+{_RESET}")
    print(f"{_ORANGE}{_BOLD}|{_RESET}  {_SAFFRON}{_BOLD}  J A I   S H R E E   R A M  {_RESET}  {_ORANGE}{_BOLD}|{_RESET}")
    print(f"{_ORANGE}{_BOLD}+{'=' * 52}+{_RESET}")
    print(f"  {_GREEN}Thanks for using {_BOLD}HARSH SENSI{_RESET}{_GREEN}! Headshot lagao, Booyah karo!{_RESET}")
    print(f"  {_CYAN}HARSH SENSI{_RESET} {_WHITE}- Harsh ka tool, har player ke liye.{_RESET}")
    print()


# --- Compatibility layer (z_run.py inhe import karta hai) ---

def _u0() -> None:
    """Startup banner - logo + welcome."""
    welcome()


def _u1(t: str) -> None:
    print(f"\n{_MAGENTA}{_BOLD}>> {t}{_RESET}\n")


def _u2(m: str) -> None:
    print(f"{_GREEN}[+]{_RESET} {_WHITE}{m}{_RESET}")


def _u3(m: str) -> None:
    print(f"{_YELLOW}[!]{_RESET} {_WHITE}{m}{_RESET}")
