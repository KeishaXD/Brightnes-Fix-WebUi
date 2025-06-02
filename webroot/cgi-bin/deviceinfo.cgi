#!/system/bin/sh
echo "Content-type: text/plain"
echo ""

echo "DEVICE         : $(getprop ro.build.product)"
echo "MODEL          : $(getprop ro.product.model)"
echo "MANUFACTURER   : $(getprop ro.product.manufacturer)"
echo "PROCESSOR      : $(getprop ro.product.board)"
echo "CPU            : $(getprop ro.hardware)"
echo "ANDROID VERSION: $(getprop ro.build.version.release)"
echo "KERNEL VERSION : $(uname -r)"
echo "RAM            : $(free -h | grep Mem | awk '{print $2}')"