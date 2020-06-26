#!/bin/bash
ls | grep -i .pdf &> list.txt
while IFS= read -r line;
do 
qpdf --password='' --decrypt --replace-input "$line"
echo "decrypted" "$line"
done < list.txt
