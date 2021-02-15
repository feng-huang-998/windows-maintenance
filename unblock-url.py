from shutil import copyfile

src = "hosts.normal"
dst = "C:\\Windows\\System32\\drivers\\etc\\hosts"

copyfile(src, dst)
