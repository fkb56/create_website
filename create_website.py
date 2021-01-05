#!/usr/bin/python3

# ----------------------------- AJOUT IMPORT ------------------------------------
import os
import urllib.request

print()
print("===================================================")
print("        Creation architecture de base du site")
print("===================================================")
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
            © <?php echo (date('Y')) ?> Copyright: <a class="text-dark" href="https://dabou.best/~Franck">DabouLion</a>
        </div>
        </footer>
        <script src="framework/JQuery.slim.min.css"></script>
        <script src="framework/Bootstrap.bundle.min.js"></script>
        <script src="assets/js/main.js"></script>
    </body>
</html>"""

template_Php = """<?php

"""

template_Bdd = """<?php
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

template_Membre = """<?php"""

template_Js = """"""

template_Css = """"""

template_VarConf = """<?php"""

template_ConfPhp = """<?php"""

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

# ---------------------------- EMPLACEMENTS DES FICHIERS ------------------------
fichier_index = root_website + "/index.php"
fichier_main_css = dossier_assets_css + "/main.css"
fichier_main_js = dossier_assets_js + "/main.js"
fichier_php_bdd = dossier_assets_php + "/bdd.php"
fichier_php_varconf = dossier_assets_php + "/Varconf.php"
fichier_php_confphp = dossier_assets_php + "/Confphp.php"
fichier_php_membre = dossier_assets_php + "/membres.php"
fichier_human = root_website + "/humans.txt"

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
            print("Dossier " + name + " crée.")
        else:
            print("Le dossier " + name + " existe déjà.")
    else:
        if not os.path.exists(chemin + name):
            os.makedirs(chemin + name)
            print("Dossier " + name + " crée.")
        else:
            print("Le dossier " + name + " existe déjà.")


def ajout_fichier(name, template):
    if not os.path.exists(chemin + name):
        with open(chemin + name, "x") as fichier:
            fichier.write(template)
        print("Fichier " + name + " crée.")
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

# ---------------------------- CREATION DES FICHIERS ----------------------------
ajout_fichier(fichier_index, template_Index)
ajout_fichier(fichier_main_css, template_Css)
ajout_fichier(fichier_main_js, template_Js)
ajout_fichier(fichier_php_bdd, template_Bdd)
ajout_fichier(fichier_php_varconf, template_VarConf)
ajout_fichier(fichier_php_confphp, template_ConfPhp)
ajout_fichier(fichier_php_membre, template_Membre)
ajout_fichier(fichier_human, template_Humans)

# ---------------------------- TELECHARGEMENT FRAMEWORK -------------------------
ajout_framework(fichier_bootstrap_css, url_bootstrap_css)
ajout_framework(fichier_bootstrap_bundle_js, url_bootstrap_bundle_js)
ajout_framework(fichier_jquery, url_jquery)
ajout_framework(fichier_fontawesome, url_fontawesome)
