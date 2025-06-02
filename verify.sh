#!/system/bin/sh
# Check if busybox httpd is available
if ! command -v busybox >/dev/null; then
  ui_print "BusyBox not found. WebUI will not work."
fi
