# Projet Virtualisation

Thomas Saudemont - Yoann Hamel-Muller


## Description


Les conteneurs ```command_post```et ```radio_op1``` sont situés dans le même docker-compose sur une première machine (VM1). ```command_post``` envoie un ordre à ```radio_op1```. Ce dernier relaie ensuite le message à ```radio_op2``` situé sur une deuxième machine (VM2) qui transmet enfin le message à ```officer```. Tout comme pour la première machine ces deux conteneurs sont voisins au sein du même docker-compose). ```officer``` se charge d'exécuter les ordres.


```command_post``` envoie deux types d'ordres:

- spawn: génère une armée de processus zombie

- kill: tue le générateur (processus parent)


Tuer le processus parent est supposé tuer les zombies (enfants) par la même occasion. Or, il se trouve que ce n'est pas le cas ici contrairement à ce qui a été constaté dans la voie de la fourchette (voir logs du conteneur ```officer```). Les programmes C utilisés ici pour gérer les zombies sont des versions abrégées du programme de la voie de la fourchette. Se référer à la version complète pour la démonstration (```zombies.c```).


## Utilisation


Vis-à-vis de Proxmox, la VM2 (receveur) correspond à ```thomas```, et la VM1 (envoyeur) à ```noe```. Tous les mots de passe sont "ensibs". L'adresse IP de la VM2 se spécifie dans le fichier ```relay_to_radio_op2.py``` (```DEST_HOST=<IP>```) situé dans ```~/Desktop/VM1/radio_op1```. Cela est déjà fait. Les adresses IP ne devraient pas changer.


Dans l'ordre, lancer sur la VM2 les conteneurs:


- officer: ```sudo docker-compose build officer && sudo docker-compose up officer```

- radio_op2: ```sudo docker-compose build radio_op2 && sudo docker-compose up radio_op2```


Puis sur la VM1 les conteneurs:


- radio_op1: ```sudo docker-compose build radio_op1 && sudo docker-compose up radio_op1```

- command_post: ```sudo docker-compose build command_post && sudo docker-compose up command_post```


Chaque conteneur affiche des logs à toutes les étapes de la chaîne de commande. Il est possible de relancer le conteneur ```command_post``` plusieurs fois.


Une version du projet qui fonctionne dans un seul et même docker-compose est jointe (```command_chain_local```). Il s'utilise de la même manière.
