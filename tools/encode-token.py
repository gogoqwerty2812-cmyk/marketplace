# Encode a Telegram bot token into the split/obfuscated form used by config.js.
# Usage:  python tools/encode-token.py 1234567890:AA....your-token....
# Paste the printed two lines into SITE.telegram.tokenParts in assets/js/config.js.
import base64, sys

if len(sys.argv) < 2:
    print("Usage: python tools/encode-token.py <bot_token>")
    raise SystemExit(1)

tok = sys.argv[1].strip()
rev = base64.b64encode(tok.encode()).decode()[::-1]
half = len(rev) // 2
print("tokenParts: [")
print(f'  "{rev[:half]}",')
print(f'  "{rev[half:]}",')
print("],")
