# Hash a new admin password into the SHA-256 form used by config.js.
# Usage:  python tools/hash-password.py "MyNewPassword"
# Paste the printed hash into SITE.adminPasswordHash in assets/js/config.js.
import hashlib, sys

if len(sys.argv) < 2:
    print('Usage: python tools/hash-password.py "newPassword"')
    raise SystemExit(1)

pw = sys.argv[1]
print(hashlib.sha256(pw.encode()).hexdigest())
