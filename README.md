Ce projet a été réalisé par **Martin Timeo** et **Braz Arno** depuis le **9/10/2025**.
Ci-contre le ***github*** du projet : https://github.com/timeomartin2601-byte/TP4/tree/V4 
***Casse-Brique***: Le joueur contrôle une raquette pour faire rebondir une balle et détruire tous les blocs présents à l'écran, tout en gérant son score, son temps et ses vies.

# 📜 Règles du Jeu
L'objectif du Casse-Brique est de détruire tous les blocs affichés en haut de l'écran à l'aide d'une balle.

## Contrôles :

    Utilisez les flèches directionnelles Gauche (<Left>) et Droite (<Right>) pour déplacer la raquette (le "palet") horizontalement en bas de l'écran.

    Le mouvement de la raquette s'arrête lorsque vous relâchez la touche.

## Objectif :

    Vous devez faire rebondir la balle sur votre raquette pour l'envoyer sur les blocs en haut de l'écran.
    La partie est gagnée lorsque tous les blocs ont été détruits.

## Mécaniques de Jeu :

    Vies : Vous commencez avec un nombre de vies défini dans le menu (de 1 à 5). Vous perdez une vie si la balle tombe sous votre raquette et touche le bas de l'écran.

    Game Over : La partie est perdue lorsque vous n'avez plus de vies.

    Blocs : Selon le niveau de difficulté (de 1 à 3), les blocs peuvent nécessiter plusieurs coups pour être détruits. Leur couleur change pour indiquer leur état (bleu, orange puis rouge) avant de disparaître.

    Angle de Rebond : L'endroit où la balle frappe la raquette influe sur l'angle de rebond. Frapper la balle avec le centre de la raquette la renvoie plus verticalement, tandis que les bords la renvoient avec un angle plus aigu. Attention cela affecte également la vitesse, il faut donc être réactif !

    Score : Votre score augmente en cassant des blocs. Il diminue si vous perdez une vie. Le temps (chrono) est également pris en compte dans le calcul du score final (plus vous êtes rapide, meilleur est le score).