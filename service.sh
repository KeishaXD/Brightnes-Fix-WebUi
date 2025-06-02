#!/system/bin/sh
MODDIR=${0%/*}
# Start web server on port 8080
busybox httpd -f -p 8080 -h "$MODDIR/webroot"
