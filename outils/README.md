# outils

## tableau_coaches.html

Le tableau de bord de lecture des coachés, publié aussi en artefact.
Il est autonome : les données du tableau SUIVI FINAL y sont figées dans
le fichier, il n'appelle rien de l'extérieur.

Ce qu'il montre, coaché par coaché : dernière saisie et état du dossier,
poids, calories déclarées, adhérence et récupération, progression par
exercice sur la série la plus lourde de chaque semaine, et toutes les
notes et bilans écrits.

### Le remettre à jour

Les données viennent de l'export XLSX du Sheet, jamais de la lecture
directe : la lecture directe tronque autour de 226 lignes par onglet et
fait croire qu'un client n'a rien noté.

1. Exporter `SUIVI FINAL !` en xlsx.
2. Relancer l'extraction (openpyxl) pour régénérer `clients.json`.
3. Réinjecter le JSON dans le fichier, à la place du `const DATA = {...}`.

### Ce que le tableau calcule

- La tendance compare la série la plus lourde de la dernière semaine
  saisie à celle d'il y a trois semaines. Pas au tout début, sinon un
  changement de salle passe pour une progression.
- Les graphiques gardent un empan minimal (3 kg, 400 kcal) pour que le
  bruit du matin ne ressemble pas à une tendance.
- Une série au-dessus de 40 répétitions est signalée comme saisie
  douteuse : les kg et les reps ont sans doute été inversés.
