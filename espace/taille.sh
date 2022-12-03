#!/bin/bash

if  [ -e /home/yoann/Documents/RandomFile.txt ]
then 
echo "Fichier deja existant, suppression en cours..."
rm RandomFile.txt
dd if=/dev/urandom of=RandomFile.txt bs=1M count=1024
echo "Fichier supprimé et re créé !"
else
echo "Creation du fichier..."
dd if=/dev/urandom of=RandomFile.txt bs=1M count=1024
echo "Fichier créé !"
fi

bytes=$(stat -c %B RandomFile.txt)
echo "le nombre de bytes necessaires par bloc est : $bytes"

bloc=$(stat -c %b RandomFile.txt)
echo "Nombre de blocs alloués : $bloc" 

espace=$(($bytes*$bloc))
echo "Espace theorique : $espace"

reelle=$(stat -c %s RandomFile.txt)
echo "La taille réelle du fichier est de : $reelle"
