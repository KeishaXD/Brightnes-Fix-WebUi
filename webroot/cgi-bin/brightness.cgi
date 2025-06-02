#!/system/bin/sh
echo "Content-type: text/plain"
echo ""

# Ambil nilai dari URL query, misalnya value=87
PERCENT=$(echo "$QUERY_STRING" | sed -n 's/^value=//p')

# Validasi angka 1–100
if ! echo "$PERCENT" | grep -qE '^[0-9]+$' || [ "$PERCENT" -lt 1 ] || [ "$PERCENT" -gt 100 ]; then
  echo "Invalid input"
  exit 1
fi

# Array mapping dari 1–100
VALUES=(
  "" 41 82 123 164 205 246 287 328 369 410
  451 491 532 573 614 655 696 737 778 819
  860 901 942 983 1024 1065 1106 1147 1188 1229
  1270 1311 1352 1393 1434 1475 1516 1557 1598 1638
  1679 1720 1761 1802 1843 1884 1925 1966 2007 2048
  2089 2130 2171 2212 2253 2294 2335 2376 2417 2457
  2498 2539 2580 2621 2662 2703 2744 2785 2826 2867
  2908 2949 2990 3031 3072 3113 3154 3195 3236 3276
  3317 3358 3399 3440 3481 3522 3563 3604 3645 3686
  3727 3768 3809 3850 3891 3932 3973 4014 4055 4095
)

BRIGHTNESS=${VALUES[$PERCENT]}

# Tulis nilai brightness (perlu root permission!)
echo "$BRIGHTNESS" > /sys/class/backlight/sprd_backlight/brightness 2>/dev/null && echo "OK" || echo "FAIL"