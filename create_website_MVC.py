#!/usr/bin/python3

# ------------  ----------------- AJOUT IMPORT ------------------------------------
import os
import urllib.request

print()
print("=============================================================")
print("        Creation architecture de base d'un site web MVC")
print("=============================================================")
print()
print()

# ---------------------------- RECUPERATION DU CHEMIN DU SCRIPT -----------------
path = os.path.realpath(__file__)
path = os.getcwd()
directory = os.path.basename(path)

# ---------------------------- AFFICHAGE DU DOSSIER COURANT ---------------------
print("Le dossier courant est \"" + directory + "\", entrez le nom du site")

# ---------------------------- DEMANDE DU NOM DE DOSSIER ------------------------
root_website = input("Nom du site: ")
chemin = path + "/"

# ---------------------------- AJOUT URL CDN POUR INCORPORER A L'INDEX PHP ------
url_bootstrap_css = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
url_bootstrap_bundle_js = "https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/js/bootstrap.bundle.min.js"
url_jquery = "https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.min.js"
url_fontawesome = "https://use.fontawesome.com/releases/v5.15.1/css/all.css"

# ---------------------------- AJOUT DE TEMPLATE POUR LES PRINCIPAUX FICHIERS ---
template_Index = """<?php
session_start();
$root = str_replace('index.php', '', $_SERVER['SCRIPT_FILENAME']);
define('ROOT', $root);

include_once 'header.php';

if ($_GET['action']) {
	$params = explode('/', $_GET['action']);
	if ($params[0] != '') {
		$controller = $params[0];
		$action = '';
		if (isset($params[1])) {
			$action = $params[1];
		}

		require_once(ROOT . 'controllers/' . $controller . '.php');

		if (function_exists($action)) {
			if (isset($params[2]) && isset($params[3])) {
				$action($params[2], $params[3]);
			} elseif (isset($params[2])) {
				$action($params[2]);
			} else {
				$action();
			}
		}
	} else {
		echo 'page par défaut';
	}
} else {
	echo `<p class="text-center">Aucune action n'existe</p> <br>`;
}

include_once 'footer.php';
"""

template_Model_BDD = """<?php
function bdd()
{
    try {
        $bdd = new PDO(\"mysql:dbname= BDD; host= HOST\", \"USER\", \"PASS\");
        $bdd->exec('SET NAMES utf8');
    } catch (PDOException $e) {
        echo 'Connexion échouée: ' . $e->getMessage();
    }
    return $bdd;
}"""

template_Php = """<?php"""

template_Membre = """<?php"""

template_Js = """"""

template_Css = """* {
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
}"""

template_VarConf = """<?php"""

template_ConfPhp = """<?php"""

template_Models = """<?php
require_once "models/modelBDD.php";

"""

template_Views = """<?php

?>
<div>
	
</div>
"""

template_Header = """<!DOCTYPE html>
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
    <div class="container">"""

template_Footer = """   </div>
        <footer class="bg-secondary text-center text-lg-start">
            <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2)">
                © <?php echo (date('Y')) ?> Copyright: <a class="text-dark" href="https://dabou.best/~Franck">DabouLion</a>
            </div>
        </footer>
        <script src="framework/JQuery.slim.min.css"></script>
        <script src="framework/Bootstrap.bundle.min.js"></script>
        <script src="assets/js/main.js"></script>
    </body>

</html>"""

template_Controllers = """<?php
require_once "models/model";

"""

template_Htacces = """# permet de démarrer la réécriture d'URL
RewriteEngine on

# permet de définir une règle de réécriture d'URL et fonctionne comme suit
RewriteRule ^([A-Za-z0-9\-\_\/]*)$ index.php?action=$1
"""

template_Humans = """------------------------------Documentation utilisateur----------------------------------"""

# ---------------------------- AJOUT CHEMIN DOSSIERS/FICHIERS -------------------

# ---------------------------- EMPLACEMENTS DES DOSSIERS ------------------------
dossier_assets = root_website + "/assets"
dossier_assets_css = dossier_assets + "/css"
dossier_assets_css_images = "{0}/images".format(dossier_assets_css)
dossier_assets_js = dossier_assets + "/js"
dossier_assets_php = dossier_assets + "/php"
dossier_assets_sass = dossier_assets + "/sass"
dossier_assets_sass_libs = dossier_assets_sass + "/libs"
dossier_assets_webfonts = dossier_assets + "/webfonts"
dossier_framework = root_website + "/framework"
dossier_images = root_website + "/images"
dossier_models = root_website + "/models"
dossier_views = root_website + "/views"
dossier_controller = root_website + "/controllers"

# ---------------------------- EMPLACEMENTS DES FICHIERS ------------------------
fichier_index = root_website + "/index.php"
fichier_header_php = root_website + "/header.php"
fichier_footer_php = root_website + "/footer.php"
fichier_main_css = dossier_assets_css + "/main.css"
fichier_main_js = dossier_assets_js + "/main.js"
fichier_php_varconf = dossier_assets_php + "/Varconf.php"
fichier_php_confphp = dossier_assets_php + "/Confphp.php"
fichier_php_membre = dossier_assets_php + "/membres.php"
fichier_php_view = dossier_views + "/view.php"
fichier_php_model_bdd = dossier_models + "/modelBDD.php"
fichier_php_model = dossier_models + "/model.php"
fichier_php_controller = dossier_controller + "/controller.php"
fichier_human = root_website + "/humans.txt"
fichier_htaccess = root_website + "/.htaccess"

# ---------------------------- EMPLACEMENTS DES FICHIERS ------------------------
fichier_bootstrap_css = dossier_framework + "/Bootstrap.min.css"
fichier_bootstrap_bundle_js = dossier_framework + "/Bootstrap.bundle.min.js"
fichier_jquery = dossier_framework + "/JQuery.slim.min.js"
fichier_fontawesome = dossier_framework + "/Fontawesome.css"

# -------------------------------------------------------------------------------

# ---------------------------- CREATION DES FONCTIONS ---------------------------
def ajout_dossier(name):
    split = chemin.split("/")
    root_split = split[-1]
    if (root_split == name):
        if not os.path.exists(chemin):
            os.makedirs(chemin)
            print("Dossier " + name + " créer.")
        else:
            print("Le dossier " + name + " existe déjà.")
    else:
        if not os.path.exists(chemin + name):
            os.makedirs(chemin + name)
            print("Dossier " + name + " créer.")
        else:
            print("Le dossier " + name + " existe déjà.")


def ajout_fichier(name, template):
    if not os.path.exists(chemin + name):
        with open(chemin + name, "x") as fichier:
            fichier.write(template)
        print("Fichier " + name + " créer.")
    else:
        print("Le fichier " + name + " existe déjà.")


def ajout_framework(name, url_framework):
    if not os.path.exists(chemin + name):
        urllib.request.urlretrieve(url_framework, chemin + name)
        print("Fichier " + name + " téléchargé.")
    else:
        print("Le fichier " + name + " existe déjà.")

# ---------------------------- CREATION DES DOSSIERS ----------------------------
ajout_dossier(root_website)
ajout_dossier(dossier_assets)
ajout_dossier(dossier_assets_css)
ajout_dossier(dossier_assets_css_images)
ajout_dossier(dossier_assets_js)
ajout_dossier(dossier_assets_php)
ajout_dossier(dossier_assets_sass)
ajout_dossier(dossier_assets_sass_libs)
ajout_dossier(dossier_assets_webfonts)
ajout_dossier(dossier_framework)
ajout_dossier(dossier_images)
ajout_dossier(dossier_models)
ajout_dossier(dossier_views)
ajout_dossier(dossier_controller)

# ---------------------------- CREATION DES FICHIERS ----------------------------
ajout_fichier(fichier_index, template_Index)
ajout_fichier(fichier_header_php, template_Header)
ajout_fichier(fichier_footer_php, template_Footer)
ajout_fichier(fichier_main_css, template_Css)
ajout_fichier(fichier_main_js, template_Js)
ajout_fichier(fichier_php_model_bdd, template_Model_BDD)
ajout_fichier(fichier_php_varconf, template_VarConf)
ajout_fichier(fichier_php_confphp, template_ConfPhp)
ajout_fichier(fichier_php_membre, template_Membre)
ajout_fichier(fichier_php_model, template_Models)
ajout_fichier(fichier_php_view, template_Views)
ajout_fichier(fichier_php_controller, template_Controllers)
ajout_fichier(fichier_human, template_Humans)
ajout_fichier(fichier_htaccess, template_Htacces)

# ---------------------------- TELECHARGEMENT FRAMEWORK -------------------------
ajout_framework(fichier_bootstrap_css, url_bootstrap_css)
ajout_framework(fichier_bootstrap_bundle_js, url_bootstrap_bundle_js)
ajout_framework(fichier_jquery, url_jquery)
ajout_framework(fichier_fontawesome, url_fontawesome)
