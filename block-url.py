from shutil import copyfile

src = "hosts.block"
dst = "C:\\Windows\\System32\\drivers\\etc\\hosts"

copyfile(src, dst)
