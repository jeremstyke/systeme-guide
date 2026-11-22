# Articles du blog, par langue. Un article = un dict.
# body : HTML. [CTA] insere un encadre avec le bouton d'inscription (lien affilie).
# Regles : faits verifies sur systeme.io, aucun tiret long ni demi-cadratin, ecriture humaine.

BLOGTXT = {
    "en": dict(blog="Guides", read="Read", guides_h="Systeme.io guides", all="All guides", more="Keep reading",
               upd="Updated", cta_p="Try it yourself: the free plan has no time limit and needs no credit card.",
               blog_p="Practical guides to build your online business with Systeme.io."),
    "fr": dict(blog="Guides", read="Lire", guides_h="Guides Systeme.io", all="Tous les guides", more="À lire aussi",
               upd="Mis à jour le", cta_p="Testez par vous-même : l'offre gratuite n'a pas de limite de durée et ne demande pas de carte bancaire.",
               blog_p="Des guides concrets pour lancer et faire tourner votre business en ligne avec Systeme.io."),
}

ARTICLES = [
dict(lang="fr", slug="creer-tunnel-de-vente-gratuit", date="2026-11-22",
title="Créer un tunnel de vente gratuit avec Systeme.io (guide pas à pas)",
h1="Créer un tunnel de vente gratuit avec Systeme.io",
desc="Comment créer un tunnel de vente gratuitement avec Systeme.io : les pages à prévoir, les étapes dans l'outil, les limites de l'offre gratuite et les erreurs à éviter.",
body="""
<p>Oui, vous pouvez créer un tunnel de vente complet sans payer un centime : l'offre gratuite de Systeme.io permet de créer jusqu'à 3 tunnels, avec la page de capture, la page de vente, le paiement et la page de remerciement. Voici comment faire, dans l'ordre, et ce qu'il faut savoir avant de commencer.</p>

<h2>Un tunnel de vente, c'est quoi concrètement ?</h2>
<p>C'est une suite de pages qui emmène un visiteur jusqu'à l'achat. Au lieu d'un site avec dix menus où il se perd, chaque page n'a qu'un seul objectif et un seul bouton. Un tunnel classique ressemble à ça :</p>
<ol>
<li><strong>La page de capture</strong> : vous offrez quelque chose de gratuit (un guide, une checklist, une vidéo) contre une adresse email.</li>
<li><strong>La page de remerciement</strong> : elle confirme l'inscription et livre le cadeau.</li>
<li><strong>La page de vente</strong> : elle présente votre offre payante.</li>
<li><strong>Le bon de commande</strong> : le paiement, par carte via Stripe ou par PayPal.</li>
<li><strong>La page de confirmation</strong> : elle donne l'accès au produit acheté.</li>
</ol>
<p>Rien ne vous oblige à tout faire d'un coup. Beaucoup de gens commencent par un tunnel de deux pages, capture et remerciement, juste pour se constituer une liste d'emails.</p>

<h2>Ce que permet l'offre gratuite</h2>
<div class="tbl"><table>
<tr><th>Élément</th><th>Offre gratuite</th></tr>
<tr><td>Tunnels de vente</td><td>3</td></tr>
<tr><td>Contacts</td><td>2 000</td></tr>
<tr><td>Envoi d'emails</td><td>Illimité</td></tr>
<tr><td>Formations</td><td>1</td></tr>
<tr><td>Règles d'automatisation</td><td>1</td></tr>
<tr><td>Nom de domaine personnalisé</td><td>1</td></tr>
<tr><td>Frais sur vos ventes</td><td>0 %, vous payez seulement Stripe ou PayPal</td></tr>
</table></div>
<p>Pour un premier produit, c'est largement suffisant. La limite qui coince en premier, c'est souvent la règle d'automatisation unique : dès que vous voulez plusieurs scénarios d'emails, il faut passer à l'offre Startup (17 € par mois, 10 tunnels et 5 000 contacts).</p>

[CTA]

<h2>Créer votre tunnel, étape par étape</h2>
<h3>1. Créez votre compte et choisissez le type de tunnel</h3>
<p>Une fois inscrit, allez dans la partie Tunnels de votre tableau de bord et créez-en un nouveau. Systeme.io vous demande votre objectif : récolter des emails, vendre un produit, organiser un webinaire... Choisissez « récolter des emails » si vous n'avez encore rien à vendre. Les intitulés exacts peuvent changer un peu avec les mises à jour de l'outil, mais la logique reste la même.</p>

<h3>2. Partez d'un modèle</h3>
<p>Pour chaque page, Systeme.io propose des modèles prêts à l'emploi. Prenez-en un simple, changez les couleurs, le titre et l'image. L'éditeur fonctionne en glisser-déposer : on clique sur un bloc pour modifier le texte, on fait glisser un bloc pour l'ajouter. Aucune ligne de code.</p>
<p>Notre conseil : ne passez pas trois soirs sur le design. Une page sobre avec un titre clair convertit souvent mieux qu'une page chargée.</p>

<h3>3. Écrivez une page de capture qui donne envie</h3>
<p>Le titre doit dire ce que la personne obtient, pas ce que vous êtes. « La checklist pour préparer votre premier marché de Noël » parle plus que « Bienvenue sur mon site ». Ajoutez trois lignes sur ce que contient le cadeau, un champ email, un bouton. C'est tout.</p>

<h3>4. Branchez l'email de bienvenue</h3>
<p>Avec votre règle d'automatisation, déclenchez l'envoi d'un email dès qu'une personne s'inscrit sur la page de capture : il livre le cadeau et présente qui vous êtes. C'est le premier contact, soignez-le.</p>

<h3>5. Ajoutez la vente quand vous êtes prêt</h3>
<p>Pour vendre, ajoutez une page de vente et un bon de commande au tunnel, puis connectez votre compte Stripe ou PayPal dans les réglages de paiement. Systeme.io ne prend aucune commission sur vos ventes. Vous pouvez aussi ajouter plus tard une offre complémentaire juste après l'achat (un « upsell »), mais commencez sans.</p>

<h3>6. Testez avant de partager</h3>
<p>Inscrivez-vous vous-même avec une autre adresse email, vérifiez que l'email arrive, que les liens marchent et que la page s'affiche bien sur téléphone. La plupart des visiteurs arriveront depuis un mobile.</p>

<h2>Les erreurs qui font fuir les visiteurs</h2>
<ul>
<li><strong>Trop de choix sur une page.</strong> Un tunnel marche parce qu'il n'y a qu'une action possible. Retirez les liens vers vos réseaux sociaux de la page de capture.</li>
<li><strong>Un cadeau trop vague.</strong> « Mes conseils » n'attire personne. « 10 modèles d'emails pour relancer un client » attire.</li>
<li><strong>Oublier les mentions légales.</strong> Dès que vous collectez des emails ou vendez en France, il faut des mentions légales, une politique de confidentialité et, pour la vente, des conditions générales. Ajoutez-les en bas de chaque page.</li>
<li><strong>Attendre que tout soit parfait.</strong> Un tunnel en ligne et imparfait vous apprend plus qu'un tunnel parfait qui reste en brouillon.</li>
</ul>

<h2>Gratuit ou payant : quand passer à l'offre supérieure ?</h2>
<p>Restez sur l'offre gratuite tant que vous avez moins de 2 000 contacts et un seul scénario d'emails. Passez à Startup quand vous voulez plusieurs automatisations ou plus de 3 tunnels. L'offre Webinar (47 € par mois) n'est utile que si vous vendez avec des webinaires automatiques. Et en payant à l'année, vous gagnez 2 mois.</p>

<h2>Questions fréquentes</h2>
<h3>Faut-il un site internet pour créer un tunnel de vente ?</h3>
<p>Non. Systeme.io héberge vos pages. Vous pouvez utiliser l'adresse fournie, ou brancher votre propre nom de domaine (un domaine est inclus dans l'offre gratuite).</p>
<h3>Combien de temps faut-il pour créer son premier tunnel ?</h3>
<p>Pour un tunnel simple avec une page de capture et une page de remerciement à partir d'un modèle, comptez une soirée. Le plus long est d'écrire le texte et de préparer le cadeau.</p>
<h3>Peut-on vendre sans auto-entreprise ?</h3>
<p>Pour vendre régulièrement en France, il faut un statut, la micro-entreprise étant le plus simple. Renseignez-vous sur service-public.fr avant votre première vente.</p>
"""),
]
