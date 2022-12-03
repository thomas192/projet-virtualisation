#!/bin/bash

if [ -e /home/yoann/Documents/sature ]
then
	echo "Dossier déjà existant, suppression en cours..."
	rm -vrf sature
	echo "Création du dossier..."
	mkdir sature
	echo "Dossier créé."
else
	echo "Dossier en cours de création..."
	mkdir sature
	echo "Dossier créé."
fi

cd sature
count=0

while true 
do
	echo 0 > $count.txt
	let count++
done
