Set wshShell = CreateObject("WScript.shell")
wshShell.run "mfgtool2.exe -c ""Linux"" -l ""AllToEmmcRootfsTar_RX_MRS"" -s ""board=imx6sxea-com"" -s ""dtb=kit"" -s ""mmc=2"" -s ""rootfs=ea-image-base"" "
Set wshShell = Nothing
