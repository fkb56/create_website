# create_website

### Pré-requis

Il y a juste a intaller python pour pouvoir faire fonctionner le script.

## Création d'un script pour réaliser une achitecture pour un site web

Il y a 2 script l'un sert a créer une architecture [normal](#create_website-1) et le deuxième sert a créer une architecture [MVC](#create_website_mvc)

### create_website

Va créer une architecture web en php

* Création du dossier assets
<small>(Avec les fichiers ci-dessous à l'intérieur)</small>
  * Création du dossier **css**
  * Création du dossier **js**
  * Création du dossier **php**
  * Création du dossier **sass**
  * Création du dossier **webfonts**

* Création du dossier framework et téléchargement des frameworks
  * Téléchargement du fichier **Bootstrap.bundle.js**
  * Téléchargement du fichier **Bootstrap.css**
  * Téléchargement du fichier **Fontawesome**
  * Téléchargement du fichier **JQuery**

* Création du dossier images 

* Des templates sont directement intégré au différent fichier créer
  * **index.php**

	```php
	<?php
	require_once "assets/php/bdd.php";

	?>
	<!DOCTYPE html>
	<html lang="fr">

		<head>
			<meta charset="utf-8">
			<meta http-equiv="X-UA-Compatible" content="IE=edge">
			<meta name="viewport" content="width=device-width, initial-scale=1, user-scalable=no">
			<title>Titre</title>
			<link rel="stylesheet" href="assets/css/main.css">
			<link rel="stylesheet" href="framework/Bootstrap.min.css">
			<link rel="stylesheet" href="framework/Fontawesome.css">
		</head>

		<body>
			<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
				<div class="container-fluid">
					<a class="navbar-brand" href="#">Navbar</a>
					<button class="navbar-toggler" type="button">
						<span class="navbar-toggler-icon"></span>
					</button>
					<div class="collapse navbar-collapse" id="navbarSupportedContent">
						<ul class="navbar-nav me-auto mb-2 mb-lg-0 p-2">
							<li class="nav-item">
								<a class="nav-link active" aria-current="page" href="#">Home</a>
							</li>
							<li class="nav-item">
								<a class="nav-link" href="#">Link</a>
							</li>
							<li class="nav-item">
								<a class="nav-link" href="#" tabindex="-1">Disabled</a>
							</li>
						</ul>
						<form class="d-flex">
							<input class="form-control me-2" type="search" placeholder="Search">
							<button class="btn btn-orange" type="submit">Search</button>
						</form>
					</div>
				</div>
			</nav>

			<footer class="bg-secondary text-center text-lg-start">
			<div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2)">
				© <?php echo (date('Y')) ?> Copyright: <a class="text-dark" href="#">Place name here</a>
			</div>
			</footer>
			<script src="framework/JQuery.slim.min.css"></script>
			<script src="framework/Bootstrap.bundle.min.js"></script>
			<script src="assets/js/main.js"></script>
		</body>
	</html>```

  * **humans.txt**
	```
	------------------------------Documentation utilisateur----------------------------------
	```

  * **main.css**
	```css
	* {
		margin: 0;
		padding: 0;
	}

	nav>div>a:hover, nav>div>div>ul>li>a:hover{
		color:rgb(248, 117, 9) !important;
		font-weight:bold;
	}

	.btn-orange{
		color:rgb(248, 117, 9) !important;
		border-color: rgb(248, 117, 9) !important;
	}

	.btn-orange:hover{
		background-color:rgb(248, 117, 9) !important;
			color: black !important;
	}

	footer {
		position: absolute !important;
		bottom: 0 !important;
		width: 100%;
	}
	```

  * **bdd.php**

	```php
	<?php
	function bdd()
	{
		try {
			$bdd = new PDO("mysql:dbname= BDD; host= HOST", "USER", "PASS");
			$bdd->exec('SET NAMES utf8');
		} catch (PDOException $e) {
			echo 'Connexion échouée: ' . $e->getMessage();
		}
		return $bdd;
	}
	```

  * **main.js** est vide

  * **Conf.php** est vide

  * **membres.php** est vide

  * **Varconf.php** est vide


**********************************************************************************************

### create_website_MVC

# EN COURS
