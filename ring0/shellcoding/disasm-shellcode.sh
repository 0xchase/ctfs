echo -ne $1 > temp
ndisasm -b64 temp
rm temp
