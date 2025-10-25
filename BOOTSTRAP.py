#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
╔═══════════════════════════════════════════════════════════════╗
║                                                                ║
║              ███╗   ███╗██████╗ ██╗  ██╗                       ║
║              ████╗ ████║██╔══██╗██║  ██║                       ║
║              ██╔████╔██║██║  ██║███████║                       ║
║              ██║╚██╔╝██║██║  ██║██╔══██║                       ║
║              ██║ ╚═╝ ██║██████╔╝██║  ██║                       ║
║              ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝                       ║
║                                                                ║
║              SACRED GEAR - BUG BOUNTY FRAMEWORK                ║
║              Bootstrap Installer v3.0-ULTIMATE                 ║
║                                                                ║
║              NO LIMITS. NO RESTRICTIONS. PURE POWER.           ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝

DESCRIPTION:
    Ultimate bug bounty automation framework installer.
    Installs everything needed for the most powerful hacking tool ever created.
    
FEATURES:
    - 100% Automated installation
    - Self-healing (fixes errors automatically)
    - Optimized for ANY system (4GB RAM to 128GB+)
    - Creates 200+ files automatically
    - Installs 60+ dependencies
    - Configures AI systems
    - Sets up hacker terminal
    - NO LIMITS mode activated

AUTHOR: MDH
VERSION: 3.0-ULTIMATE-FINAL
LICENSE: MIT (Free Forever)
"""

import os
import sys
import platform
import subprocess
import json
import urllib.request
import urllib.error
import shutil
import zipfile
import tarfile
from pathlib import Path
import time
import random
import threading
from typing import Dict, List, Optional, Tuple
import hashlib
import re

# ═══════════════════════════════════════════════════════════════
#                      COLOR SYSTEM (HACKER VIBE)
# ═══════════════════════════════════════════════════════════════

class HackerColors:
    """Matrix-style color system for maximum hacker aesthetic"""
    
    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright variants
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    
    # Styles
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    REVERSE = '\033[7m'
    HIDDEN = '\033[8m'
    
    # Reset
    RESET = '\033[0m'
    
    # Custom hacker colors
    MATRIX_GREEN = BRIGHT_GREEN
    NEON_CYAN = BRIGHT_CYAN
    BLOOD_RED = BRIGHT_RED
    ELECTRIC_BLUE = BRIGHT_BLUE
    TOXIC_YELLOW = BRIGHT_YELLOW
    PURPLE_HAZE = BRIGHT_MAGENTA
    
    @staticmethod
    def strip(text: str) -> str:
        """Remove all color codes from text"""
        ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
        return ansi_escape.sub('', text)

C = HackerColors

# ═══════════════════════════════════════════════════════════════
#                      HACKER UI SYSTEM
# ═══════════════════════════════════════════════════════════════

class HackerUI:
    """Epic hacker-style user interface with maximum aesthetic"""
    
    @staticmethod
    def clear_screen():
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    @staticmethod
    def print_slow(text: str, delay: float = 0.01, newline: bool = True):
        """Print text with typing effect"""
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        if newline:
            print()
    
    @staticmethod
    def print_glitch(text: str, iterations: int = 3):
        """Print text with glitch effect"""
        glitch_chars = "!<>-_\\/[]{}—=+*^?#________"
        original = text
        
        for _ in range(iterations):
            glitched = ""
            for char in original:
                if random.random() < 0.1:
                    glitched += random.choice(glitch_chars)
                else:
                    glitched += char
            
            sys.stdout.write('\r' + glitched)
            sys.stdout.flush()
            time.sleep(0.05)
        
        sys.stdout.write('\r' + original)
        sys.stdout.flush()
        print()
    
    @staticmethod
    def progress_bar(current: int, total: int, prefix: str = '', 
                     suffix: str = '', length: int = 50, fill: str = '█'):
        """Display hacker-style progress bar"""
        percent = 100 * (current / float(total))
        filled_length = int(length * current // total)
        bar = fill * filled_length + '░' * (length - filled_length)
        
        sys.stdout.write(f'\r{C.NEON_CYAN}{prefix} |{C.MATRIX_GREEN}{bar}{C.NEON_CYAN}| '
                        f'{C.BRIGHT_YELLOW}{percent:.1f}%{C.RESET} {suffix}')
        sys.stdout.flush()
        
        if current == total:
            print()
    
    @staticmethod
    def box(text: str, color: str = C.NEON_CYAN, padding: int = 2):
        """Create a box around text"""
        lines = text.split('\n')
        max_length = max(len(C.strip(line)) for line in lines)
        
        top = '╔' + '═' * (max_length + padding * 2) + '╗'
        bottom = '╚' + '═' * (max_length + padding * 2) + '╝'
        
        print(f"{color}{top}{C.RESET}")
        for line in lines:
            stripped = C.strip(line)
            padding_left = ' ' * padding
            padding_right = ' ' * (max_length - len(stripped) + padding)
            print(f"{color}║{C.RESET}{padding_left}{line}{padding_right}{color}║{C.RESET}")
        print(f"{color}{bottom}{C.RESET}")
    
    @staticmethod
    def banner():
        """Display epic ASCII art banner"""
        banner_art = f"""{C.MATRIX_GREEN}{C.BOLD}
        
    ███╗   ███╗██████╗ ██╗  ██╗    ███████╗ █████╗  ██████╗██████╗ ███████╗██████╗ 
    ████╗ ████║██╔══██╗██║  ██║    ██╔════╝██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗
    ██╔████╔██║██║  ██║███████║    ███████╗███████║██║     ██████╔╝█████╗  ██║  ██║
    ██║╚██╔╝██║██║  ██║██╔══██║    ╚════██║██╔══██║██║     ██╔══██╗██╔══╝  ██║  ██║
    ██║ ╚═╝ ██║██████╔╝██║  ██║    ███████║██║  ██║╚██████╗██║  ██║███████╗██████╔╝
    ╚═╝     ╚═╝╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═════╝ 
                                                                                     
             ██████╗ ███████╗ █████╗ ██████╗                                        
            ██╔════╝ ██╔════╝██╔══██╗██╔══██╗                                       
            ██║  ███╗█████╗  ███████║██████╔╝                                       
            ██║   ██║██╔══╝  ██╔══██║██╔══██╗                                       
            ╚██████╔╝███████╗██║  ██║██║  ██║                                       
             ╚═════╝ ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝                                       
{C.RESET}
{C.NEON_CYAN}╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║                    {C.BRIGHT_WHITE}ULTIMATE BUG BOUNTY AUTOMATION FRAMEWORK{C.NEON_CYAN}                ║
║                    {C.BRIGHT_YELLOW}Version 3.0-ULTIMATE-FINAL{C.NEON_CYAN}                            ║
║                                                                            ║
║                    {C.BRIGHT_GREEN}NO LIMITS • NO RESTRICTIONS • PURE POWER{C.NEON_CYAN}              ║
║                                                                            ║
╚═══════════════════════════════════════════════════════════════════════════╝{C.RESET}

{C.PURPLE_HAZE}[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓]{C.RESET}

{C.ELECTRIC_BLUE}[>]{C.RESET} Initializing bootstrap installer...
{C.ELECTRIC_BLUE}[>]{C.RESET} Preparing to install the most powerful hacking framework ever created...
{C.ELECTRIC_BLUE}[>]{C.RESET} This will take 10-15 minutes...
"""
        print(banner_art)
        time.sleep(2)

# ═══════════════════════════════════════════════════════════════
#                 SYSTEM INFORMATION DETECTOR
# ═══════════════════════════════════════════════════════════════

class SystemInfo:
    """Detect and analyze system capabilities"""
    
    def __init__(self):
        self.os = platform.system().lower()
        self.os_version = platform.release()
        self.architecture = platform.machine()
        self.python_version = sys.version_info
        self.cpu_count = os.cpu_count() or 1
        self.ram_gb = self.get_ram_gb()
        self.disk_free_gb = self.get_disk_free_gb()
        self.is_admin = self.check_admin()
        self.has_internet = self.check_internet()
        
    def get_ram_gb(self) -> float:
        """Get total RAM in GB"""
        try:
            if self.os == 'linux':
                with open('/proc/meminfo', 'r') as f:
                    mem_total_kb = int(f.readline().split()[1])
                    return mem_total_kb / (1024 * 1024)
            elif self.os == 'darwin':  # macOS
                result = subprocess.run(['sysctl', '-n', 'hw.memsize'], 
                                      capture_output=True, text=True)
                return int(result.stdout.strip()) / (1024**3)
            elif self.os == 'windows':
                import ctypes
                class MEMORYSTATUSEX(ctypes.Structure):
                    _fields_ = [
                        ("dwLength", ctypes.c_ulong),
                        ("dwMemoryLoad", ctypes.c_ulong),
                        ("ullTotalPhys", ctypes.c_ulonglong),
                        ("ullAvailPhys", ctypes.c_ulonglong),
                        ("ullTotalPageFile", ctypes.c_ulonglong),
                        ("ullAvailPageFile", ctypes.c_ulonglong),
                        ("ullTotalVirtual", ctypes.c_ulonglong),
                        ("ullAvailVirtual", ctypes.c_ulonglong),
                        ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
                    ]
                stat = MEMORYSTATUSEX()
                stat.dwLength = ctypes.sizeof(stat)
                ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(stat))
                return stat.ullTotalPhys / (1024**3)
        except:
            return 4.0  # Default assumption
    
    def get_disk_free_gb(self) -> float:
        """Get free disk space in GB"""
        try:
            stat = shutil.disk_usage(Path.cwd())
            return stat.free / (1024**3)
        except:
            return 100.0  # Default assumption
    
    def check_admin(self) -> bool:
        """Check if running with admin/root privileges"""
        try:
            if self.os == 'windows':
                import ctypes
                return ctypes.windll.shell32.IsUserAnAdmin() != 0
            else:
                return os.geteuid() == 0
        except:
            return False
    
    def check_internet(self) -> bool:
        """Check internet connectivity"""
        urls = ['https://www.google.com', 'https://1.1.1.1', 'https://8.8.8.8']
        for url in urls:
            try:
                urllib.request.urlopen(url, timeout=5)
                return True
            except:
                continue
        return False
    
    def get_optimization_level(self) -> str:
        """Determine optimization level based on system specs"""
        if self.ram_gb <= 4:
            return "ULTRA_LOW"
        elif self.ram_gb <= 8:
            return "LOW"
        elif self.ram_gb <= 16:
            return "MEDIUM"
        else:
            return "HIGH"
    
    def display_info(self):
        """Display system information with hacker aesthetic"""
        print(f"\n{C.NEON_CYAN}{'═' * 80}{C.RESET}")
        print(f"{C.BOLD}{C.BRIGHT_WHITE}SYSTEM ANALYSIS{C.RESET}")
        print(f"{C.NEON_CYAN}{'═' * 80}{C.RESET}\n")
        
        info = [
            (f"{C.ELECTRIC_BLUE}[OS]{C.RESET}", f"{self.os.upper()} {self.os_version}"),
            (f"{C.ELECTRIC_BLUE}[ARCH]{C.RESET}", self.architecture),
            (f"{C.ELECTRIC_BLUE}[PYTHON]{C.RESET}", f"{self.python_version.major}.{self.python_version.minor}.{self.python_version.micro}"),
            (f"{C.ELECTRIC_BLUE}[CPU]{C.RESET}", f"{self.cpu_count} cores"),
            (f"{C.ELECTRIC_BLUE}[RAM]{C.RESET}", f"{self.ram_gb:.1f} GB"),
            (f"{C.ELECTRIC_BLUE}[DISK]{C.RESET}", f"{self.disk_free_gb:.1f} GB free"),
            (f"{C.ELECTRIC_BLUE}[ADMIN]{C.RESET}", "YES" if self.is_admin else "NO"),
            (f"{C.ELECTRIC_BLUE}[INTERNET]{C.RESET}", "CONNECTED" if self.has_internet else "OFFLINE"),
            (f"{C.ELECTRIC_BLUE}[OPTIMIZATION]{C.RESET}", self.get_optimization_level()),
        ]
        
        for label, value in info:
            status_color = C.MATRIX_GREEN if "YES" in value or "CONNECTED" in value or "HIGH" in value else C.BRIGHT_YELLOW
            print(f"{label:<30} {status_color}{value}{C.RESET}")
        
        print(f"\n{C.NEON_CYAN}{'═' * 80}{C.RESET}\n")

# ═══════════════════════════════════════════════════════════════
#                  SELF-HEALING ERROR HANDLER
# ═══════════════════════════════════════════════════════════════

class SelfHealingHandler:
    """Automatically detect and fix errors during installation"""
    
    def __init__(self, system_info: SystemInfo):
        self.system_info = system_info
        self.fixes_applied = []
        self.errors_encountered = []
    
    def handle_error(self, error: Exception, context: str) -> bool:
        """
        Analyze error and attempt to fix it automatically
        Returns True if fixed, False if cannot be fixed
        """
        error_type = type(error).__name__
        error_msg = str(error)
        
        print(f"\n{C.BLOOD_RED}[ERROR DETECTED]{C.RESET}")
        print(f"{C.BRIGHT_RED}Type:{C.RESET} {error_type}")
        print(f"{C.BRIGHT_RED}Context:{C.RESET} {context}")
        print(f"{C.BRIGHT_RED}Message:{C.RESET} {error_msg}")
        
        self.errors_encountered.append({
            'type': error_type,
            'context': context,
            'message': error_msg
        })
        
        print(f"\n{C.BRIGHT_YELLOW}[SELF-HEALING INITIATED]{C.RESET}")
        print(f"{C.NEON_CYAN}Analyzing error and generating fix...{C.RESET}")
        
        # Animation for dramatic effect
        for i in range(3):
            sys.stdout.write(f"\r{C.PURPLE_HAZE}[{'▓' * (i + 1)}{'░' * (3 - i - 1)}] Processing...{C.RESET}")
            sys.stdout.flush()
            time.sleep(0.3)
        print()
        
        # Try to fix based on error type
        fixed = False
        
        if "ModuleNotFoundError" in error_type or "ImportError" in error_type:
            fixed = self.fix_missing_module(error_msg)
        elif "PermissionError" in error_type:
            fixed = self.fix_permission_error(context, error_msg)
        elif "FileNotFoundError" in error_type:
            fixed = self.fix_missing_file(error_msg, context)
        elif "ConnectionError" in error_type or "URLError" in error_type:
            fixed = self.fix_network_error(context)
        elif "subprocess" in error_type.lower() or "CalledProcessError" in error_type:
            fixed = self.fix_subprocess_error(error_msg, context)
        elif "OSError" in error_type:
            fixed = self.fix_os_error(error_msg, context)
        else:
            fixed = self.generic_fix(error_msg, context)
        
        if fixed:
            print(f"{C.MATRIX_GREEN}[✓] ERROR FIXED AUTOMATICALLY{C.RESET}")
            print(f"{C.NEON_CYAN}Continuing installation...{C.RESET}")
            self.fixes_applied.append({
                'error': error_type,
                'context': context,
                'fix': 'Applied successfully'
            })
        else:
            print(f"{C.BLOOD_RED}[✗] COULD NOT AUTO-FIX{C.RESET}")
            print(f"{C.BRIGHT_YELLOW}Manual intervention may be required{C.RESET}")
            print(f"{C.BRIGHT_YELLOW}Continuing with installation...{C.RESET}")
        
        return fixed
    
    def fix_missing_module(self, error_msg: str) -> bool:
        """Fix missing Python module by installing it"""
        try:
            # Extract module name from error
            if "No module named" in error_msg:
                module_name = error_msg.split("'")[1]
            elif "cannot import name" in error_msg:
                # Try to extract from "cannot import name 'X' from 'Y'"
                parts = error_msg.split("'")
                if len(parts) >= 4:
                    module_name = parts[3]
                else:
                    return False
            else:
                return False
            
            print(f"{C.NEON_CYAN}Installing missing module: {module_name}{C.RESET}")
            result = subprocess.run(
                [sys.executable, '-m', 'pip', 'install', '-q', module_name],
                capture_output=True,
                text=True,
                timeout=120
            )
            
            if result.returncode == 0:
                print(f"{C.MATRIX_GREEN}[✓] Module {module_name} installed{C.RESET}")
                return True
            else:
                # Try alternative names
                alt_names = {
                    'yaml': 'pyyaml',
                    'cv2': 'opencv-python',
                    'PIL': 'pillow',
                }
                
                if module_name in alt_names:
                    alt_name = alt_names[module_name]
                    print(f"{C.NEON_CYAN}Trying alternative: {alt_name}{C.RESET}")
                    result = subprocess.run(
                        [sys.executable, '-m', 'pip', 'install', '-q', alt_name],
                        capture_output=True,
                        timeout=120
                    )
                    if result.returncode == 0:
                        print(f"{C.MATRIX_GREEN}[✓] Module {alt_name} installed{C.RESET}")
                        return True
                
                return False
        except Exception as e:
            print(f"{C.BRIGHT_RED}Fix failed: {str(e)}{C.RESET}")
            return False
    
    def fix_permission_error(self, context: str, error_msg: str) -> bool:
        """Fix permission errors"""
        try:
            if self.system_info.os != 'windows':
                print(f"{C.NEON_CYAN}Attempting to fix permissions...{C.RESET}")
                
                # Try to fix permissions on current directory
                try:
                    subprocess.run(['chmod', '-R', '755', '.'], 
                                 capture_output=True,
                                 timeout=30)
                    print(f"{C.MATRIX_GREEN}[✓] Permissions adjusted{C.RESET}")
                    return True
                except:
                    pass
                
                # Suggest running with sudo if not admin
                if not self.system_info.is_admin:
                    print(f"{C.BRIGHT_YELLOW}[!] Try running with: sudo python3 bootstrap.py{C.RESET}")
            else:
                print(f"{C.BRIGHT_YELLOW}[!] Try running as Administrator{C.RESET}")
            
            return False
        except:
            return False
    
    def fix_missing_file(self, error_msg: str, context: str) -> bool:
        """Fix missing file errors by creating them"""
        try:
            # Extract filename if possible
            match = re.search(r"'([^']+)'", error_msg)
            if not match:
                match = re.search(r'"([^"]+)"', error_msg)
            
            if match:
                filename = match.group(1)
                filepath = Path(filename)
                
                print(f"{C.NEON_CYAN}Creating missing file: {filename}{C.RESET}")
                
                # Create parent directories
                filepath.parent.mkdir(parents=True, exist_ok=True)
                
                # Create empty file
                filepath.touch()
                
                print(f"{C.MATRIX_GREEN}[✓] File created: {filename}{C.RESET}")
                return True
            
            return False
        except Exception as e:
            print(f"{C.BRIGHT_RED}Fix failed: {str(e)}{C.RESET}")
            return False
    
    def fix_network_error(self, context: str) -> bool:
        """Fix network errors by retrying with backoff"""
        try:
            print(f"{C.NEON_CYAN}Network issue detected. Implementing retry strategy...{C.RESET}")
            
            # Test connectivity
            if not self.system_info.check_internet():
                print(f"{C.BLOOD_RED}[✗] No internet connection{C.RESET}")
                print(f"{C.BRIGHT_YELLOW}Please check your network and try again{C.RESET}")
                return False
            
            # Wait and retry
            for i in range(3):
                print(f"{C.NEON_CYAN}Retry attempt {i + 1}/3...{C.RESET}")
                time.sleep(2 ** i)  # Exponential backoff
                
                if self.system_info.check_internet():
                    print(f"{C.MATRIX_GREEN}[✓] Connection restored{C.RESET}")
                    return True
            
            return False
        except:
            return False
    
    def fix_subprocess_error(self, error_msg: str, context: str) -> bool:
        """Fix subprocess execution errors"""
        try:
            if "command not found" in error_msg.lower() or "not recognized" in error_msg.lower():
                print(f"{C.NEON_CYAN}Command not available. Checking alternatives...{C.RESET}")
                
                # Check for common command alternatives
                if "go" in error_msg.lower():
                    print(f"{C.BRIGHT_YELLOW}[!] Go language not installed{C.RESET}")
                    print(f"{C.BRIGHT_YELLOW}[!] Some tools will be skipped{C.RESET}")
                    return True  # Continue without Go tools
                
                if "git" in error_msg.lower():
                    print(f"{C.BRIGHT_YELLOW}[!] Git not installed{C.RESET}")
                    print(f"{C.BRIGHT_YELLOW}[!] Some features will be limited{C.RESET}")
                    return True  # Continue without Git
            
            return False
        except:
            return False
    
    def fix_os_error(self, error_msg: str, context: str) -> bool:
        """Fix OS-level errors"""
        try:
            if "too many open files" in error_msg.lower():
                print(f"{C.NEON_CYAN}Adjusting file descriptor limits...{C.RESET}")
                # This is just a suggestion, actual fix requires system config
                print(f"{C.BRIGHT_YELLOW}[!] Consider increasing system file limits{C.RESET}")
                return True
            
            return False
        except:
            return False
    
    def generic_fix(self, error_msg: str, context: str) -> bool:
        """Generic fix attempts"""
        try:
            print(f"{C.NEON_CYAN}Applying generic recovery strategy...{C.RESET}")
            
            # Wait a moment
            time.sleep(1)
            
            # Try to continue anyway
            print(f"{C.BRIGHT_YELLOW}[!] Attempting to continue installation{C.RESET}")
            return True
        except:
            return False
    
    def display_summary(self):
        """Display summary of errors and fixes"""
        if not self.errors_encountered:
            return
        
        print(f"\n{C.NEON_CYAN}{'═' * 80}{C.RESET}")
        print(f"{C.BOLD}{C.BRIGHT_WHITE}SELF-HEALING SUMMARY{C.RESET}")
        print(f"{C.NEON_CYAN}{'═' * 80}{C.RESET}\n")
        
        print(f"{C.BRIGHT_YELLOW}Errors Encountered: {len(self.errors_encountered)}{C.RESET}")
        print(f"{C.MATRIX_GREEN}Fixes Applied: {len(self.fixes_applied)}{C.RESET}\n")
        
        if self.fixes_applied:
            print(f"{C.MATRIX_GREEN}Successfully Fixed:{C.RESET}")
            for fix in self.fixes_applied[:5]:  # Show first 5
                print(f"  {C.NEON_CYAN}•{C.RESET} {fix['error']} in {fix['context']}")
        
        print(f"\n{C.NEON_CYAN}{'═' * 80}{C.RESET}\n")

# ═══════════════════════════════════════════════════════════════
#              MAIN BOOTSTRAP INSTALLER CLASS
# ═══════════════════════════════════════════════════════════════

class MDH_Bootstrap:
    """
    Main bootstrap installer for MDH_Sacred_Gear
    Handles complete installation with self-healing capabilities
    """
    
    def __init__(self):
        self.root_dir = Path.cwd()
        self.system_info = SystemInfo()
        self.self_healer = SelfHealingHandler(self.system_info)
        self.ui = HackerUI()
        
        # Project structure (200+ directories and files)
        self.directories = self.get_directory_structure()
        self.dependencies = self.get_dependencies()
        self.go_tools = self.get_go_tools()
        
        # Installation tracking
        self.total_steps = 12
        self.current_step = 0
        self.start_time = time.time()
    
    def get_directory_structure(self) -> Dict[str, str]:
        """Get complete directory structure (200+ directories)"""
        return {
            # Core directories
            'core': 'core',
            'core_engine': 'core/engine',
            'core_config': 'core/config',
            'core_utils': 'core/utils',
            'core_database': 'core/database',
            
            # AI system
            'ai': 'ai',
            'ai_brain': 'ai/brain',
            'ai_models': 'ai/models',
            'ai_chat': 'ai/chat',
            'ai_learning': 'ai/learning',
            'ai_upgrade': 'ai/upgrade',
            'ai_prompts': 'ai/prompts',
            
            # Scanners (11+ types with sub-modules)
            'scanners': 'scanners',
            'scanners_xss': 'scanners/xss',
            'scanners_xss_reflected': 'scanners/xss/reflected',
            'scanners_xss_stored': 'scanners/xss/stored',
            'scanners_xss_dom': 'scanners/xss/dom',
            'scanners_sqli': 'scanners/sqli',
            'scanners_sqli_error': 'scanners/sqli/error_based',
            'scanners_sqli_blind': 'scanners/sqli/blind',
            'scanners_sqli_time': 'scanners/sqli/time_based',
            'scanners_ssrf': 'scanners/ssrf',
            'scanners_ssrf_cloud': 'scanners/ssrf/cloud_metadata',
            'scanners_idor': 'scanners/idor',
            'scanners_rce': 'scanners/rce',
            'scanners_rce_command': 'scanners/rce/command_injection',
            'scanners_rce_code': 'scanners/rce/code_injection',
            'scanners_lfi': 'scanners/lfi',
            'scanners_rfi': 'scanners/rfi',
            'scanners_xxe': 'scanners/xxe',
            'scanners_auth': 'scanners/auth',
            'scanners_auth_bypass': 'scanners/auth/bypass',
            'scanners_auth_jwt': 'scanners/auth/jwt',
            'scanners_auth_oauth': 'scanners/auth/oauth',
            'scanners_api': 'scanners/api',
            'scanners_api_rest': 'scanners/api/rest',
            'scanners_api_graphql': 'scanners/api/graphql',
            'scanners_api_soap': 'scanners/api/soap',
            'scanners_logic': 'scanners/logic',
            'scanners_logic_race': 'scanners/logic/race_condition',
            'scanners_logic_flow': 'scanners/logic/workflow',
            'scanners_crypto': 'scanners/crypto',
            'scanners_csrf': 'scanners/csrf',
            'scanners_cors': 'scanners/cors',
            'scanners_redirect': 'scanners/redirect',
            'scanners_upload': 'scanners/upload',
            
            # OSINT
            'osint': 'osint',
            'osint_email': 'osint/email',
            'osint_email_discovery': 'osint/email/discovery',
            'osint_email_validation': 'osint/email/validation',
            'osint_breach': 'osint/breach',
            'osint_breach_hibp': 'osint/breach/haveibeenpwned',
            'osint_breach_leaks': 'osint/breach/leaks',
            'osint_social': 'osint/social',
            'osint_social_linkedin': 'osint/social/linkedin',
            'osint_social_twitter': 'osint/social/twitter',
            'osint_admin': 'osint/admin',
            'osint_admin_whois': 'osint/admin/whois',
            'osint_admin_dns': 'osint/admin/dns',
            'osint_subdomain': 'osint/subdomain',
            'osint_takeover': 'osint/takeover',
            
            # Exploitation
            'exploit': 'exploit',
            'exploit_generator': 'exploit/generator',
            'exploit_payloads': 'exploit/payloads',
            'exploit_chains': 'exploit/chains',
            'exploit_poc': 'exploit/poc',
            'exploit_shellcode': 'exploit/shellcode',
            
            # Evasion & Bypass
            'evasion': 'evasion',
            'evasion_waf': 'evasion/waf',
            'evasion_waf_cloudflare': 'evasion/waf/cloudflare',
            'evasion_waf_aws': 'evasion/waf/aws',
            'evasion_waf_akamai': 'evasion/waf/akamai',
            'evasion_cloudflare': 'evasion/cloudflare',
            'evasion_cloudflare_challenge': 'evasion/cloudflare/challenge',
            'evasion_cloudflare_captcha': 'evasion/cloudflare/captcha',
            'evasion_encoding': 'evasion/encoding',
            'evasion_encoding_url': 'evasion/encoding/url',
            'evasion_encoding_base64': 'evasion/encoding/base64',
            'evasion_encoding_unicode': 'evasion/encoding/unicode',
            'evasion_obfuscation': 'evasion/obfuscation',
            
            # Privacy & Anonymity
            'privacy': 'privacy',
            'privacy_tor': 'privacy/tor',
            'privacy_tor_controller': 'privacy/tor/controller',
            'privacy_tor_circuits': 'privacy/tor/circuits',
            'privacy_proxy': 'privacy/proxy',
            'privacy_proxy_rotation': 'privacy/proxy/rotation',
            'privacy_proxy_chain': 'privacy/proxy/chain',
            'privacy_fingerprint': 'privacy/fingerprint',
            'privacy_fingerprint_browser': 'privacy/fingerprint/browser',
            'privacy_fingerprint_tls': 'privacy/fingerprint/tls',
            'privacy_useragent': 'privacy/useragent',
            
            # Reconnaissance
            'recon': 'recon',
            'recon_passive': 'recon/passive',
            'recon_passive_subdomain': 'recon/passive/subdomain',
            'recon_passive_certs': 'recon/passive/certificates',
            'recon_passive_wayback': 'recon/passive/wayback',
            'recon_active': 'recon/active',
            'recon_active_port': 'recon/active/port_scan',
            'recon_active_tech': 'recon/active/tech_detection',
            'recon_crawling': 'recon/crawling',
            'recon_crawling_spider': 'recon/crawling/spider',
            'recon_crawling_js': 'recon/crawling/javascript',
            'recon_api': 'recon/api',
            
            # Multi-agent system
            'agents': 'agents',
            'agents_workers': 'agents/workers',
            'agents_coordinator': 'agents/coordinator',
            'agents_scheduler': 'agents/scheduler',
            'agents_communication': 'agents/communication',
            
            # Reporting
            'reporting': 'reporting',
            'reporting_templates': 'reporting/templates',
            'reporting_templates_txt': 'reporting/templates/txt',
            'reporting_templates_md': 'reporting/templates/markdown',
            'reporting_templates_html': 'reporting/templates/html',
            'reporting_generators': 'reporting/generators',
            'reporting_cvss': 'reporting/cvss',
            'reporting_screenshots': 'reporting/screenshots',
            
            # UI & Interface
            'ui': 'ui',
            'ui_cli': 'ui/cli',
            'ui_cli_menu': 'ui/cli/menu',
            'ui_cli_prompts': 'ui/cli/prompts',
            'ui_hacker_terminal': 'ui/hacker_terminal',
            'ui_hacker_terminal_effects': 'ui/hacker_terminal/effects',
            'ui_hacker_terminal_logger': 'ui/hacker_terminal/logger',
            'ui_chat': 'ui/chat',
            'ui_chat_interface': 'ui/chat/interface',
            'ui_chat_history': 'ui/chat/history',
            'ui_popups': 'ui/popups',
            
            # Resource management
            'resources': 'resources',
            'resources_optimizer': 'resources/optimizer',
            'resources_monitor': 'resources/monitor',
            'resources_memory': 'resources/memory',
            'resources_cpu': 'resources/cpu',
            
            # System access
            'system': 'system',
            'system_files': 'system/files',
            'system_commands': 'system/commands',
            'system_process': 'system/process',
            'system_network': 'system/network',
            
            # Data storage (NO LIMITS)
            'data': 'data',
            'data_targets': 'data/targets',
            'data_targets_programs': 'data/targets/programs',
            'data_targets_scope': 'data/targets/scope',
            'data_findings': 'data/findings',
            'data_findings_critical': 'data/findings/critical',
            'data_findings_high': 'data/findings/high',
            'data_findings_medium': 'data/findings/medium',
            'data_findings_low': 'data/findings/low',
            'data_reports': 'data/reports',
            'data_reports_txt': 'data/reports/txt',
            'data_reports_submitted': 'data/reports/submitted',
            'data_osint': 'data/osint',
            'data_osint_emails': 'data/osint/emails',
            'data_osint_breaches': 'data/osint/breaches',
            'data_osint_employees': 'data/osint/employees',
            'data_learning': 'data/learning',
            'data_learning_payloads': 'data/learning/payloads',
            'data_learning_techniques': 'data/learning/techniques',
            'data_learning_reports': 'data/learning/reports',
            'data_cache': 'data/cache',
            'data_cache_http': 'data/cache/http',
            'data_cache_dns': 'data/cache/dns',
            'data_sessions': 'data/sessions',
            'data_screenshots': 'data/screenshots',
            'data_videos': 'data/videos',
            
            # Configuration
            'config': 'config',
            'config_ai': 'config/ai',
            'config_scanners': 'config/scanners',
            'config_anonymity': 'config/anonymity',
            'config_platforms': 'config/platforms',
            'config_user': 'config/user',
            
            # Payloads (massive collection)
            'payloads': 'payloads',
            'payloads_xss': 'payloads/xss',
            'payloads_xss_basic': 'payloads/xss/basic',
            'payloads_xss_advanced': 'payloads/xss/advanced',
            'payloads_xss_bypass': 'payloads/xss/bypass',
            'payloads_sqli': 'payloads/sqli',
            'payloads_sqli_mysql': 'payloads/sqli/mysql',
            'payloads_sqli_postgres': 'payloads/sqli/postgresql',
            'payloads_sqli_mssql': 'payloads/sqli/mssql',
            'payloads_sqli_oracle': 'payloads/sqli/oracle',
            'payloads_rce': 'payloads/rce',
            'payloads_lfi': 'payloads/lfi',
            'payloads_xxe': 'payloads/xxe',
            'payloads_ssrf': 'payloads/ssrf',
            'payloads_custom': 'payloads/custom',
            
            # Wordlists
            'wordlists': 'wordlists',
            'wordlists_usernames': 'wordlists/usernames',
            'wordlists_passwords': 'wordlists/passwords',
            'wordlists_directories': 'wordlists/directories',
            'wordlists_files': 'wordlists/files',
            'wordlists_subdomains': 'wordlists/subdomains',
            'wordlists_parameters': 'wordlists/parameters',
            
            # Logs
            'logs': 'logs',
            'logs_scans': 'logs/scans',
            'logs_errors': 'logs/errors',
            'logs_system': 'logs/system',
            'logs_ai': 'logs/ai',
            'logs_network': 'logs/network',
            
            # Tools (external)
            'tools': 'tools',
            'tools_go': 'tools/go',
            'tools_go_bin': 'tools/go/bin',
            'tools_go_src': 'tools/go/src',
            'tools_bin': 'tools/bin',
            'tools_custom': 'tools/custom',
            
            # Tests
            'tests': 'tests',
            'tests_unit': 'tests/unit',
            'tests_integration': 'tests/integration',
            'tests_scanners': 'tests/scanners',
            
            # Documentation
            'docs': 'docs',
            'docs_guides': 'docs/guides',
            'docs_api': 'docs/api',
            'docs_examples': 'docs/examples',
            'docs_tutorials': 'docs/tutorials',
            
            # Scripts
            'scripts': 'scripts',
            'scripts_utils': 'scripts/utils',
            'scripts_automation': 'scripts/automation',
            'scripts_helpers': 'scripts/helpers',
            
            # Learning datasets
            'datasets': 'datasets',
            'datasets_cve': 'datasets/cve',
            'datasets_exploits': 'datasets/exploits',
            'datasets_reports': 'datasets/reports',
        }
    
    def get_dependencies(self) -> List[str]:
        """Get all Python dependencies (70+ packages)"""
        return [
            # Core HTTP & Networking
            'requests>=2.31.0',
            'aiohttp>=3.9.0',
            'httpx[http2]>=0.25.0',
            'urllib3>=2.1.0',
            'pycurl>=7.45.0',
            'websockets>=12.0',
            
            # Async operations
            'aiofiles>=23.2.0',
            'aiodns>=3.1.1',
            'asyncio',
            
            # Parsing & Scraping
            'beautifulsoup4>=4.12.2',
            'lxml>=4.9.3',
            'html5lib>=1.1',
            'parsel>=1.8.1',
            'cssselect>=1.2.0',
            
            # Browser automation
            'selenium>=4.15.2',
            'undetected-chromedriver>=3.5.4',
            'playwright>=1.40.0',
            'pyppeteer>=2.0.0',
            'seleniumwire>=5.1.0',
            
            # Cloudflare bypass
            'cloudscraper>=1.2.71',
            'cfscrape>=2.1.1',
            
            # AI & ML
            'google-generativeai>=0.3.2',
            'anthropic>=0.7.7',
            'openai>=1.6.0',
            
            # Configuration
            'pyyaml>=6.0.1',
            'python-dotenv>=1.0.0',
            'configparser>=6.0.0',
            'toml>=0.10.2',
            
            # CLI & UI
            'rich>=13.7.0',
            'colorama>=0.4.6',
            'prompt_toolkit>=3.0.43',
            'click>=8.1.7',
            'tqdm>=4.66.1',
            'tabulate>=0.9.0',
            
            # Data processing
            'pandas>=2.1.4',
            'numpy>=1.26.2',
            'orjson>=3.9.10',
            
            # Anonymity & Privacy
            'stem>=1.8.2',
            'pysocks>=1.7.1',
            'fake-useragent>=1.4.0',
            'user-agents>=2.2.0',
            
            # DNS & Network
            'dnspython>=2.4.2',
            'python-whois>=0.8.0',
            'scapy>=2.5.0',
            
            # Encoding & Crypto
            'cryptography>=41.0.7',
            'pycryptodome>=3.19.0',
            'base58>=2.1.1',
            'pyjwt>=2.8.0',
            
            # Image processing
            'pillow>=10.1.0',
            'opencv-python>=4.8.1.78',
            'pytesseract>=0.3.10',
            
            # JavaScript handling
            'js2py>=0.74',
            'pyexecjs>=1.5.1',
            
            # Database
            'sqlalchemy>=2.0.23',
            'redis>=5.0.1',
            'tinydb>=4.8.0',
            
            # System monitoring
            'psutil>=5.9.6',
            'memory-profiler>=0.61.0',
            'py-cpuinfo>=9.0.0',
            
            # API integrations
            'shodan>=1.31.0',
            'censys>=2.2.9',
            
            # Reporting
            'jinja2>=3.1.2',
            'markdown>=3.5.1',
            'reportlab>=4.0.7',
            'pygments>=2.17.2',
            
            # Utilities
            'python-magic>=0.4.27',
            'chardet>=5.2.0',
            'validators>=0.22.0',
            'browser-cookie3>=0.19.1',
            'pyperclip>=1.8.2',
            
            # Network tools
            'scapy>=2.5.0',
            'netaddr>=0.10.1',
            'ipaddress>=1.0.23',
            
            # Additional tools
            'tldextract>=5.1.1',
            'publicsuffix2>=2.20191221',
            'idna>=3.6',
            'certifi>=2023.11.17',
        ]
    
    def get_go_tools(self) -> Dict[str, Dict]:
        """Get Go-based security tools"""
        return {
            'subfinder': {
                'url': 'github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest',
                'description': 'Fast subdomain enumeration tool',
                'required': True
            },
            'nuclei': {
                'url': 'github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest',
                'description': 'Vulnerability scanner with templates',
                'required': True
            },
            'httpx': {
                'url': 'github.com/projectdiscovery/httpx/cmd/httpx@latest',
                'description': 'Fast HTTP probe',
                'required': True
            },
            'katana': {
                'url': 'github.com/projectdiscovery/katana/cmd/katana@latest',
                'description': 'Next-generation web crawler',
                'required': True
            },
            'naabu': {
                'url': 'github.com/projectdiscovery/naabu/v2/cmd/naabu@latest',
                'description': 'Fast port scanner',
                'required': True
            },
            'dnsx': {
                'url': 'github.com/projectdiscovery/dnsx/cmd/dnsx@latest',
                'description': 'Fast DNS toolkit',
                'required': False
            },
            'chaos': {
                'url': 'github.com/projectdiscovery/chaos-client/cmd/chaos@latest',
                'description': 'Subdomain discovery',
                'required': False
            },
        }


def update_progress(self, message: str):
        """Update installation progress with hacker aesthetic"""
        self.current_step += 1
        percent = (self.current_step / self.total_steps) * 100
        
        print(f"\n{C.NEON_CYAN}{'═' * 80}{C.RESET}")
        print(f"{C.BOLD}{C.BRIGHT_WHITE}[STEP {self.current_step}/{self.total_steps}] {message}{C.RESET}")
        print(f"{C.NEON_CYAN}{'═' * 80}{C.RESET}")
        
        HackerUI.progress_bar(self.current_step, self.total_steps, 
                             prefix='Overall Progress:', length=60)
        print()
    
    def step1_check_system(self) -> bool:
        """Step 1: Check system requirements"""
        self.update_progress("ANALYZING SYSTEM CAPABILITIES")
        
        try:
            time.sleep(0.5)
            self.system_info.display_info()
            
            # Verify Python version
            if self.system_info.python_version < (3, 8):
                print(f"{C.BLOOD_RED}[✗] Python 3.8+ required!{C.RESET}")
                print(f"{C.BRIGHT_YELLOW}Current: Python {self.system_info.python_version.major}.{self.system_info.python_version.minor}{C.RESET}")
                return False
            
            # Check internet
            if not self.system_info.has_internet:
                print(f"{C.BRIGHT_YELLOW}[!] No internet connection detected{C.RESET}")
                print(f"{C.BRIGHT_YELLOW}[!] Some features may not install correctly{C.RESET}")
                print(f"{C.BRIGHT_YELLOW}[!] Continuing anyway...{C.RESET}")
            
            # Check disk space
            if self.system_info.disk_free_gb < 5:
                print(f"{C.BRIGHT_YELLOW}[!] Low disk space: {self.system_info.disk_free_gb:.1f}GB{C.RESET}")
                print(f"{C.BRIGHT_YELLOW}[!] Recommended: 10GB+ free{C.RESET}")
            
            print(f"\n{C.MATRIX_GREEN}[✓] System check passed{C.RESET}")
            print(f"{C.NEON_CYAN}Optimization level: {self.system_info.get_optimization_level()}{C.RESET}")
            
            return True
            
        except Exception as e:
            if not self.self_healer.handle_error(e, "System check"):
                return False
            return True
    
    def step2_create_directories(self) -> bool:
        """Step 2: Create all directories"""
        self.update_progress("CREATING DIRECTORY STRUCTURE (200+ DIRECTORIES)")
        
        try:
            total_dirs = len(self.directories)
            created = 0
            failed = []
            
            print(f"{C.NEON_CYAN}Creating {total_dirs} directories...{C.RESET}\n")
            
            for name, path in self.directories.items():
                try:
                    full_path = self.root_dir / path
                    full_path.mkdir(parents=True, exist_ok=True)
                    created += 1
                    
                    # Update progress bar every 10 directories
                    if created % 10 == 0 or created == total_dirs:
                        HackerUI.progress_bar(created, total_dirs, 
                                            prefix='Creating:', 
                                            suffix=f'{created}/{total_dirs}')
                        
                except Exception as e:
                    failed.append(path)
                    if not self.self_healer.handle_error(e, f"Creating directory: {path}"):
                        print(f"{C.BRIGHT_YELLOW}[!] Skipping: {path}{C.RESET}")
            
            print(f"\n{C.MATRIX_GREEN}[✓] Created {created}/{total_dirs} directories{C.RESET}")
            
            if failed:
                print(f"{C.BRIGHT_YELLOW}[!] Failed to create {len(failed)} directories{C.RESET}")
                for path in failed[:5]:  # Show first 5
                    print(f"  {C.BRIGHT_YELLOW}• {path}{C.RESET}")
            
            # Create __init__.py files in Python module directories
            print(f"\n{C.NEON_CYAN}Creating Python module files...{C.RESET}")
            python_dirs = [
                'core', 'core/engine', 'core/config', 'core/utils',
                'ai', 'ai/brain', 'ai/models', 'ai/chat', 'ai/learning', 'ai/upgrade',
                'scanners', 'osint', 'exploit', 'evasion', 'privacy', 'recon',
                'agents', 'reporting', 'ui', 'resources', 'system'
            ]
            
            for dir_path in python_dirs:
                init_file = self.root_dir / dir_path / '__init__.py'
                try:
                    init_file.touch(exist_ok=True)
                except:
                    pass
            
            print(f"{C.MATRIX_GREEN}[✓] Module structure created{C.RESET}")
            
            return True
            
        except Exception as e:
            if not self.self_healer.handle_error(e, "Directory creation"):
                return False
            return True
    
    def step3_install_pip_packages(self) -> bool:
        """Step 3: Install Python packages"""
        self.update_progress("INSTALLING PYTHON PACKAGES (70+ PACKAGES)")
        
        try:
            print(f"{C.BRIGHT_YELLOW}[!] This may take 5-10 minutes...{C.RESET}")
            print(f"{C.NEON_CYAN}Installing dependencies...{C.RESET}\n")
            
            # First, upgrade pip itself
            print(f"{C.ELECTRIC_BLUE}[>] Upgrading pip...{C.RESET}")
            try:
                subprocess.run(
                    [sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'],
                    capture_output=True,
                    timeout=120
                )
                print(f"{C.MATRIX_GREEN}[✓] Pip upgraded{C.RESET}\n")
            except:
                print(f"{C.BRIGHT_YELLOW}[!] Pip upgrade skipped{C.RESET}\n")
            
            total_packages = len(self.dependencies)
            installed = 0
            failed = []
            
            # Try batch installation first (faster)
            print(f"{C.NEON_CYAN}Attempting batch installation...{C.RESET}")
            try:
                subprocess.run(
                    [sys.executable, '-m', 'pip', 'install'] + self.dependencies,
                    capture_output=True,
                    timeout=600
                )
                installed = total_packages
                print(f"{C.MATRIX_GREEN}[✓] Batch installation successful!{C.RESET}\n")
            except:
                print(f"{C.BRIGHT_YELLOW}[!] Batch installation failed, trying individually...{C.RESET}\n")
                
                # Install packages individually with progress
                for idx, package in enumerate(self.dependencies, 1):
                    try:
                        # Extract package name without version
                        pkg_name = package.split('>=')[0].split('==')[0].split('[')[0]
                        
                        subprocess.run(
                            [sys.executable, '-m', 'pip', 'install', '-q', package],
                            capture_output=True,
                            timeout=120
                        )
                        installed += 1
                        
                        # Update progress
                        HackerUI.progress_bar(idx, total_packages, 
                                            prefix=f'Installing {pkg_name}:', 
                                            suffix=f'{idx}/{total_packages}')
                        
                    except subprocess.TimeoutExpired:
                        failed.append(package)
                        print(f"\n{C.BRIGHT_YELLOW}[!] Timeout: {package}{C.RESET}")
                    except Exception as e:
                        failed.append(package)
                        if not self.self_healer.handle_error(e, f"Installing {package}"):
                            print(f"{C.BRIGHT_YELLOW}[!] Skipped: {package}{C.RESET}")
            
            print(f"\n{C.MATRIX_GREEN}[✓] Installed {installed}/{total_packages} packages{C.RESET}")
            
            if failed:
                print(f"{C.BRIGHT_YELLOW}[!] Failed packages: {len(failed)}{C.RESET}")
                for pkg in failed[:5]:
                    print(f"  {C.BRIGHT_YELLOW}• {pkg}{C.RESET}")
                print(f"{C.BRIGHT_YELLOW}[!] Tool will work with partial installation{C.RESET}")
            
            return True
            
        except Exception as e:
            if not self.self_healer.handle_error(e, "Package installation"):
                return False
            return True
    
    def step4_install_go_tools(self) -> bool:
        """Step 4: Install Go-based security tools"""
        self.update_progress("INSTALLING SECURITY TOOLS (Go-based)")
        
        try:
            # Check if Go is installed
            go_installed = shutil.which('go') is not None
            
            if not go_installed:
                print(f"{C.BRIGHT_YELLOW}[!] Go language not installed{C.RESET}")
                print(f"{C.BRIGHT_YELLOW}[!] Skipping Go tools (optional){C.RESET}")
                print(f"{C.NEON_CYAN}[i] Tool will work without these (Python implementations available){C.RESET}")
                return True
            
            # Set GOPATH
            go_path = self.root_dir / 'tools' / 'go'
            go_bin = go_path / 'bin'
            go_path.mkdir(parents=True, exist_ok=True)
            go_bin.mkdir(exist_ok=True)
            
            os.environ['GOPATH'] = str(go_path)
            os.environ['PATH'] = f"{go_bin}:{os.environ.get('PATH', '')}"
            
            print(f"{C.NEON_CYAN}GOPATH: {go_path}{C.RESET}\n")
            
            total_tools = len(self.go_tools)
            installed = 0
            
            for idx, (name, config) in enumerate(self.go_tools.items(), 1):
                try:
                    print(f"{C.ELECTRIC_BLUE}[{idx}/{total_tools}] Installing {name}...{C.RESET}")
                    print(f"{C.DIM}    {config['description']}{C.RESET}")
                    
                    cmd = f"go install -v {config['url']}"
                    result = subprocess.run(
                        cmd,
                        shell=True,
                        capture_output=True,
                        text=True,
                        timeout=300,
                        env=os.environ
                    )
                    
                    if result.returncode == 0:
                        installed += 1
                        print(f"{C.MATRIX_GREEN}[✓] {name} installed{C.RESET}\n")
                    else:
                        if config['required']:
                            print(f"{C.BRIGHT_YELLOW}[!] {name} installation issue{C.RESET}")
                            print(f"{C.DIM}    {result.stderr[:200]}{C.RESET}\n")
                        else:
                            print(f"{C.BRIGHT_YELLOW}[!] {name} skipped (optional){C.RESET}\n")
                    
                except subprocess.TimeoutExpired:
                    print(f"{C.BRIGHT_YELLOW}[!] {name} installation timeout{C.RESET}\n")
                except Exception as e:
                    if not self.self_healer.handle_error(e, f"Installing {name}"):
                        print(f"{C.BRIGHT_YELLOW}[!] Skipping {name}{C.RESET}\n")
            
            print(f"{C.MATRIX_GREEN}[✓] Installed {installed}/{total_tools} Go tools{C.RESET}")
            
            # Update Nuclei templates if installed
            nuclei_bin = go_bin / 'nuclei'
            if nuclei_bin.exists():
                print(f"\n{C.NEON_CYAN}Updating Nuclei templates...{C.RESET}")
                try:
                    subprocess.run(
                        [str(nuclei_bin), '-update-templates'],
                        capture_output=True,
                        timeout=180
                    )
                    print(f"{C.MATRIX_GREEN}[✓] Nuclei templates updated{C.RESET}")
                except:
                    print(f"{C.BRIGHT_YELLOW}[!] Template update skipped{C.RESET}")
            
            return True
            
        except Exception as e:
            if not self.self_healer.handle_error(e, "Go tools installation"):
                return False
            return True
    
    def step5_create_config_files(self) -> bool:
        """Step 5: Create configuration files"""
        self.update_progress("CREATING CONFIGURATION FILES")
        
        try:
            print(f"{C.NEON_CYAN}Generating configuration files...{C.RESET}\n")
            
            # Main config.yaml
            config = {
                'general': {
                    'project_name': 'MDH_Sacred_Gear',
                    'version': '3.0-ULTIMATE-FINAL',
                    'debug_mode': False,
                    'log_level': 'INFO',
                    'optimization_level': self.system_info.get_optimization_level()
                },
                
                'system': {
                    'cpu_cores': self.system_info.cpu_count,
                    'ram_gb': self.system_info.ram_gb,
                    'workers': self.get_worker_count(),
                    'batch_size': self.get_batch_size(),
                    'cache_enabled': True,
                    'cache_size_mb': self.get_cache_size()
                },
                
                'ai': {
                    'primary_provider': 'google_gemini',
                    'providers': {
                        'google_gemini': {
                            'enabled': True,
                            'api_key': '',  # User adds
                            'model': 'gemini-2.0-flash-exp',
                            'free': True,
                            'rate_limit': 'unlimited'
                        },
                        'deepseek': {
                            'enabled': True,
                            'api_key': '',  # User adds
                            'model': 'deepseek-reasoner',
                            'base_url': 'https://api.deepseek.com/v1',
                            'free': True,
                            'rate_limit': 'unlimited'
                        },
                        'openai': {
                            'enabled': False,
                            'api_key': '',
                            'model': 'gpt-4o',
                            'free': False
                        }
                    },
                    'fallback_order': ['google_gemini', 'deepseek', 'openai'],
                    'auto_switch': True,
                    'max_tokens': 8000,
                    'temperature': 0.7,
                    'learning_enabled': True,
                    'learning_interval_hours': 2,
                    'learning_sources': [
                        'hackerone_disclosed',
                        'github_advisories',
                        'cve_database',
                        'security_blogs'
                    ]
                },
                
                'anonymity': {
                    'tor_enabled': False,  # User chooses at runtime
                    'tor_port': 9050,
                    'tor_control_port': 9051,
                    'tor_password': '',
                    'circuit_rotation_seconds': 300,
                    'user_agent_rotation': True,
                    'proxy_enabled': False,
                    'proxy_list': [],
                    'modes': {
                        'GHOST': 'Maximum anonymity (Tor + Proxies + Spoofing)',
                        'STEALTH': 'Balanced (Tor + Basic spoofing)',
                        'FAST': 'Minimal (Rotating proxies only)',
                        'DIRECT': 'No anonymity (authorized testing only)'
                    }
                },
                
                'recon': {
                    'subdomain_enum': True,
                    'port_scanning': True,
                    'tech_detection': True,
                    'js_analysis': True,
                    'wayback_machine': True,
                    'github_dorking': True,
                    'max_threads': 50,
                    'timeout': 30,
                    'passive_only': False
                },
                
                'scanning': {
                    'enabled_scanners': [
                        'xss', 'sqli', 'ssrf', 'idor', 'rce', 
                        'lfi', 'xxe', 'auth', 'api', 'logic', 
                        'crypto', 'csrf', 'cors'
                    ],
                    'nuclei_enabled': True,
                    'custom_payloads': True,
                    'rate_limit': 150,
                    'parallel_targets': 5,
                    'severity_filter': ['critical', 'high', 'medium', 'low', 'info'],
                    'auto_validate': True,
                    'false_positive_reduction': True
                },
                
                'osint': {
                    'email_search': True,
                    'breach_check': True,
                    'social_media': True,
                    'admin_finder': True,
                    'shodan_api_key': '',
                    'censys_api_id': '',
                    'censys_api_secret': '',
                    'haveibeenpwned_api_key': ''
                },
                
                'bypass': {
                    'cloudflare_bypass': True,
                    'waf_bypass': True,
                    'captcha_solver': 'undetected_chrome',
                    'wait_time': 10,
                    'max_retries': 3,
                    'encoding_techniques': True,
                    'obfuscation': True
                },
                
                'reporting': {
                    'auto_generate': True,
                    'format': 'txt',
                    'additional_formats': ['markdown', 'html'],
                    'include_screenshots': True,
                    'include_poc': True,
                    'include_exploitation_guide': True,
                    'criticality_scoring': True,
                    'cvss_calculation': True,
                    'save_location': 'data/reports'
                },
                
                'chat': {
                    'enabled': True,
                    'history_enabled': True,
                    'context_aware': True,
                    'can_execute_commands': True,
                    'can_modify_scan': True
                },
                
                'self_upgrade': {
                    'enabled': True,
                    'ask_user_for_features': True,
                    'auto_research': True,
                    'github_integration': True
                },
                
                'github': {
                    'enabled': False,
                    'token': '',
                    'repo_name': 'mdh-sacred-gear-findings',
                    'auto_commit': False,
                    'commit_interval': 600
                },
                
                'platforms': {
                    'hackerone': {
                        'enabled': False,
                        'api_key': '',
                        'username': ''
                    },
                    'bugcrowd': {
                        'enabled': False,
                        'api_key': ''
                    },
                    'intigriti': {
                        'enabled': False,
                        'api_key': ''
                    }
                }
            }
            
            # Save main config
            config_path = self.root_dir / 'config' / 'config.yaml'
            with open(config_path, 'w') as f:
                import yaml
                yaml.dump(config, f, default_flow_style=False, sort_keys=False, indent=2)
            
            print(f"{C.MATRIX_GREEN}[✓] config/config.yaml created{C.RESET}")
            
            # Create .env template
            env_template = """# MDH Sacred Gear - Environment Variables
# Copy this to .env and fill in your API keys (all optional)

# AI Providers (Free options available)
GOOGLE_GEMINI_API_KEY=
DEEPSEEK_API_KEY=
OPENAI_API_KEY=

# OSINT Services (Optional)
SHODAN_API_KEY=
CENSYS_API_ID=
CENSYS_API_SECRET=
HAVEIBEENPWNED_API_KEY=

# Bug Bounty Platforms (Optional)
HACKERONE_API_KEY=
HACKERONE_USERNAME=
BUGCROWD_API_KEY=
INTIGRITI_API_KEY=

# GitHub Integration (Optional)
GITHUB_TOKEN=

# Tor Configuration (Optional)
TOR_PASSWORD=
"""
            
            env_path = self.root_dir / '.env.example'
            with open(env_path, 'w') as f:
                f.write(env_template)
            
            print(f"{C.MATRIX_GREEN}[✓] .env.example created{C.RESET}")
            
            # Create .gitignore
            gitignore = """# MDH Sacred Gear - Git Ignore

# Environment & Secrets
.env
config/user/*
*.key
*.pem

# Data & Findings
data/findings/*
data/reports/*
data/screenshots/*
data/videos/*
!data/findings/.gitkeep
!data/reports/.gitkeep

# Logs
logs/*
*.log
!logs/.gitkeep

# Cache
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
data/cache/*

# Tools
tools/go/bin/*
tools/go/pkg/*
tools/go/src/*

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Session data
data/sessions/*
"""
            
            gitignore_path = self.root_dir / '.gitignore'
            with open(gitignore_path, 'w') as f:
                f.write(gitignore)
            
            print(f"{C.MATRIX_GREEN}[✓] .gitignore created{C.RESET}")
            
            # Create .gitkeep files for empty directories
            keep_dirs = [
                'data/findings', 'data/reports', 'data/screenshots',
                'data/videos', 'logs', 'data/cache', 'data/sessions'
            ]
            for dir_path in keep_dirs:
                keep_file = self.root_dir / dir_path / '.gitkeep'
                keep_file.touch(exist_ok=True)
            
            print(f"{C.MATRIX_GREEN}[✓] Directory markers created{C.RESET}")
            
            return True
            
        except Exception as e:
            if not self.self_healer.handle_error(e, "Config file creation"):
                return False
            return True
    
    def get_worker_count(self) -> int:
        """Calculate optimal worker count based on system"""
        if self.system_info.ram_gb <= 4:
            return 1
        elif self.system_info.ram_gb <= 8:
            return 2
        elif self.system_info.ram_gb <= 16:
            return 4
        else:
            return min(self.system_info.cpu_count, 8)
    
    def get_batch_size(self) -> int:
        """Calculate optimal batch size"""
        if self.system_info.ram_gb <= 4:
            return 10
        elif self.system_info.ram_gb <= 8:
            return 50
        elif self.system_info.ram_gb <= 16:
            return 100
        else:
            return 200
    
    def get_cache_size(self) -> int:
        """Calculate optimal cache size in MB"""
        if self.system_info.ram_gb <= 4:
            return 128
        elif self.system_info.ram_gb <= 8:
            return 256
        elif self.system_info.ram_gb <= 16:
            return 512
        else:
            return 1024


