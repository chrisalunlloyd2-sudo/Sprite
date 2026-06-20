#!/usr/bin/env python3
"""
GENESIS RECOVERY ORCHESTRATOR (v1.0)
The 'One-Line' Restoration Script for the Matrix CE Ecosystem.
Usage: python3 genesis_restore.py
"""
import os
import subprocess
import sys

def run(cmd, desc):
    print(f"[*] {desc}...")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[-] Failed: {result.stderr}")
        return False
    print(f"[+] Success.")
    return True

def restore():
    print("🌌 STARTING MATRIX CE GENESIS RESTORE...")

    # 1. Environment Variables & Paths
    HOME = os.path.expanduser("~")
    KAI_ROOT = os.path.join(HOME, "KAI_9000")
    PROJECT_ROOT = os.path.join(KAI_ROOT, "projects/PocketMatrix")

    # 2. Kill existing processes
    run("pm2 delete all", "Clearing PM2 Process List")

    # 3. Start Core Services
    run(f"pm2 start {KAI_ROOT}/Sprite/scripts/qwen_pedagogy_server.py --name qwen_server --interpreter python3", "Starting Qwen Pedagogy Server")
    run(f"pm2 start {KAI_ROOT}/Sprite/scripts/hive_daemon.py --name hive_daemon --interpreter python3", "Starting Hive Daemon")

    # 4. Start GUI Bridge (The Matrix)
    run(f"pm2 start {PROJECT_ROOT}/PocketMatrix/system/gui_bridge.py --name matrix_gui --interpreter python3 --cwd {PROJECT_ROOT}", "Starting Matrix GUI Bridge")

    # 5. Verify Health
    run("pm2 status", "Verifying Service Status")

    print("\n✅ SYSTEM RESTORED TO GOLDEN STATE.")
    print("🌐 Matrix CE GUI: http://127.0.0.1:8081")

if __name__ == "__main__":
    restore()
