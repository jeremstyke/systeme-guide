# Versions longues (SEO) des pages Avis et Comparatifs, par langue.
# {AFF} = attributs du lien affilie ; {CTA} = texte du bouton. Pas de tiret cadratin.
# Chaque entree : dict(body=HTML, faq=[(q, r), ...])

def cta(txt):
    return f'<div class="cta-box"><p>{txt}</p><a class="btn" {{AFF}}>{{CTA}}</a></div>'

LONG = {}

# ---------------------------------------------------------------- FR : AVIS
LONG[("fr", "review")] = dict(body=f"""
<p>Systeme.io est un outil tout-en-un pour vendre en ligne : tunnels de vente, emailing, formations, blog, site web, automatisations et programme d'affiliation. Sa promesse est simple : remplacer cinq ou six abonnements par un seul, avec une offre gratuite qui n'expire jamais. Dans cet avis, on passe en revue ce que l'outil fait vraiment, ce que contient chaque offre, ses limites, et pour qui il vaut le coup.</p>
<h2>Systeme.io en bref</h2>
<ul>
<li><b>Type d'outil :</b> plateforme marketing tout-en-un (tunnels, emails, formations, site, blog, automatisations).</li>
<li><b>Prix :</b> offre gratuite à vie, puis Startup à 17 €, Webinar à 47 € et Unlimited à 97 € par mois.</li>
<li><b>Paiement annuel :</b> 2 mois offerts.</li>
<li><b>Frais sur vos ventes :</b> 0 % pris par Systeme.io (seuls les frais de votre prestataire de paiement s'appliquent).</li>
<li><b>Envois d'emails :</b> illimités sur toutes les offres.</li>
<li><b>Pour qui :</b> débutants, coachs, formateurs, créateurs et petites entreprises.</li>
</ul>
{cta("Testez l'offre gratuite : aucune carte bancaire demandée.")}
<h2>Ce que fait Systeme.io, fonction par fonction</h2>
<h3>1. Les tunnels de vente</h3>
<p>C'est le cœur de l'outil. Un tunnel est une suite de pages qui amène un visiteur jusqu'à l'achat : page de capture pour récupérer l'email, page de vente, bon de commande, page de remerciement. Systeme.io fournit un éditeur de pages par glisser-déposer et des modèles prêts à l'emploi. Vous pouvez ajouter sur le bon de commande un <b>order bump</b> (une offre complémentaire en un clic avant de payer) et, juste après le paiement, un <b>upsell en un clic</b> sans que le client ressaisisse sa carte. L'outil propose aussi les <b>tests A/B</b> pour comparer deux versions d'une page, les <b>codes promo</b> et les <b>tunnels à date limite</b> (deadline funnels) pour créer une vraie urgence.</p>
<h3>2. L'emailing</h3>
<p>Vous gérez votre liste de contacts, vous envoyez des newsletters et vous créez des campagnes, c'est-à-dire des séquences d'emails envoyés automatiquement les uns après les autres. Le gros point fort : <b>les envois sont illimités sur toutes les offres</b>, y compris l'offre gratuite. Chez beaucoup d'outils d'emailing, le prix grimpe avec le nombre d'emails envoyés ; ici, c'est le nombre de contacts qui compte.</p>
<h3>3. Les formations en ligne</h3>
<p>Systeme.io permet d'héberger vos formations avec un espace membre pour vos élèves. Vous pouvez vendre une formation en paiement unique, en abonnement ou en paiement en plusieurs fois, et la livrer automatiquement après l'achat. L'outil propose aussi des <b>communautés</b>, pour que vos élèves ou clients échangent entre eux et avec vous.</p>
<h3>4. Le site web et le blog</h3>
<p>Vous pouvez créer un site complet et un blog, et les publier sur votre propre nom de domaine. Pour un petit business, cela évite de payer un hébergement et un thème WordPress en plus.</p>
<h3>5. Les automatisations</h3>
<p>Les <b>règles d'automatisation</b> et les <b>workflows</b> déclenchent des actions toutes seules : quand quelqu'un s'inscrit, achète ou visite une page, Systeme.io peut lui ajouter un tag, l'inscrire à une formation ou lancer une séquence d'emails. C'est ce qui permet de faire tourner un business en pilote automatique.</p>
<h3>6. Votre propre programme d'affiliation</h3>
<p>Fonction rare à ce prix : vous pouvez créer votre propre programme d'affiliation, pour que d'autres personnes fassent la promotion de vos produits contre une commission. Systeme.io suit les ventes de chaque affilié pour vous.</p>
<h3>7. Agenda et réservations</h3>
<p>Systeme.io intègre un module d'événements et de réservations, pratique pour les coachs qui vendent des séances : vos clients réservent un créneau directement depuis votre page.</p>
<h3>8. Paiements</h3>
<p>Pour encaisser, vous connectez votre propre compte de paiement. Systeme.io est compatible avec <b>Stripe, Apple Pay, PayPal, Razorpay, Flutterwave, Mercado Pago, Xendit</b> et le paiement à la livraison. L'argent arrive directement chez vous, et Systeme.io ne prend aucun pourcentage.</p>
<h2>Les offres et les prix en détail</h2>
<div class="tbl"><table>
<thead><tr><th>Offre</th><th>Prix par mois</th><th>Contacts</th><th>Tunnels de vente</th><th>Formations</th></tr></thead>
<tbody>
<tr><td><b>Gratuit</b></td><td>0 €</td><td>2 000</td><td>3</td><td>1</td></tr>
<tr><td><b>Startup</b></td><td>17 €</td><td>5 000</td><td>10</td><td>5</td></tr>
<tr><td><b>Webinar</b></td><td>47 €</td><td>10 000</td><td>50</td><td>20</td></tr>
<tr><td><b>Unlimited</b></td><td>97 €</td><td>Illimités</td><td>Illimités</td><td>Illimitées</td></tr>
</tbody></table></div>
<p><b>Toutes les offres</b> incluent les envois d'emails illimités, le stockage de fichiers illimité, 0 % de frais de transaction, le programme d'affiliation, le support en ligne et les intégrations de paiement. Le paiement annuel vous offre 2 mois, et Systeme.io propose une <b>migration gratuite</b> si vous venez d'un autre outil.</p>
<h3>Que contient vraiment l'offre gratuite ?</h3>
<p>L'offre gratuite n'est pas un simple essai : elle n'expire jamais et ne demande pas de carte bancaire. Elle comprend jusqu'à 2 000 contacts, 3 tunnels de vente, 1 blog, 1 formation, 1 programme d'affiliation, 1 nom de domaine personnalisé, des envois d'emails illimités, 1 règle d'automatisation et 1 campagne email. C'est largement suffisant pour lancer un premier produit, construire sa liste et faire ses premières ventes.</p>
<h3>Quelle offre choisir ?</h3>
<ul>
<li><b>Gratuit :</b> pour tester l'outil et lancer un premier produit.</li>
<li><b>Startup (17 €) :</b> dès que vous dépassez 2 000 contacts ou que vous avez besoin de plus d'automatisations et de campagnes.</li>
<li><b>Webinar (47 €) :</b> si vous vendez avec des webinaires automatisés ou si vous avez plusieurs produits et jusqu'à 10 000 contacts.</li>
<li><b>Unlimited (97 €) :</b> au-delà de 10 000 contacts, ou si vous voulez tout en illimité.</li>
</ul>
{cta("Commencez gratuitement et passez à une offre payante seulement quand vous en avez besoin.")}
<h2>Les avantages</h2>
<ul class="pc good">
<li><b>Une vraie offre gratuite à vie</b>, sans carte bancaire, avec de quoi lancer un business.</li>
<li><b>Tout est au même endroit</b> : pas besoin de relier cinq outils entre eux.</li>
<li><b>Emails illimités</b> sur toutes les offres.</li>
<li><b>0 % de frais</b> pris par Systeme.io sur vos ventes.</li>
<li><b>Prix bas</b> : l'offre complète Unlimited coûte le même prix que l'offre d'entrée de ClickFunnels, et moins que l'offre de base de Kajabi.</li>
<li><b>Disponible en français</b> et dans de nombreuses autres langues.</li>
</ul>
<h2>Les inconvénients</h2>
<ul class="pc bad">
<li><b>L'offre gratuite a des limites</b> : 1 seule règle d'automatisation et 1 seule campagne email, ce qui oblige vite à passer à Startup si vous automatisez beaucoup.</li>
<li><b>Les limites montent par paliers</b> : au-delà de 10 000 contacts, il faut passer à l'offre à 97 €.</li>
<li><b>Moins de fonctions avancées que des outils spécialisés</b> : un outil d'emailing pur ou une plateforme de formation haut de gamme ira plus loin sur leur spécialité. Systeme.io mise sur la simplicité et le tout-en-un.</li>
</ul>
<h2>Pour qui Systeme.io est-il fait ?</h2>
<p><b>Les débutants</b> qui veulent lancer un business en ligne sans investir au départ. <b>Les coachs et formateurs</b> qui vendent des formations, des séances ou des accompagnements. <b>Les créateurs et infopreneurs</b> qui ont besoin d'une page de capture, d'une séquence d'emails et d'un bon de commande. <b>Les petites entreprises</b> qui veulent remplacer plusieurs abonnements par un seul.</p>
<p>En revanche, si vous avez déjà une très grosse liste, une équipe nombreuse ou des besoins très pointus sur un seul domaine, comparez d'abord avec des outils spécialisés.</p>
<h2>Comment démarrer en 5 étapes</h2>
<ol>
<li>Créez votre compte gratuit, sans carte bancaire.</li>
<li>Connectez votre moyen de paiement (Stripe ou PayPal par exemple).</li>
<li>Choisissez un modèle de tunnel et personnalisez votre page de capture et votre page de vente.</li>
<li>Créez une séquence d'emails de bienvenue pour vos nouveaux inscrits.</li>
<li>Publiez votre tunnel, partagez le lien et suivez vos statistiques.</li>
</ol>
<h2>Notre verdict</h2>
<div class="tip">Systeme.io est l'un des meilleurs rapports qualité-prix du marché pour lancer et faire grandir un business en ligne. L'offre gratuite permet de tout tester et même de faire ses premières ventes, et les offres payantes restent bien moins chères que celles de ClickFunnels ou Kajabi. Si vous débutez ou si vous voulez réduire vos abonnements, c'est le choix le plus logique.</div>
{cta("Créez votre compte Systeme.io gratuit en quelques secondes.")}
""", faq=[
 ("Systeme.io est-il vraiment gratuit ?", "Oui. L'offre gratuite n'expire jamais et ne demande pas de carte bancaire. Elle inclut 2 000 contacts, 3 tunnels de vente, 1 formation et des envois d'emails illimités."),
 ("Systeme.io prend-il une commission sur mes ventes ?", "Non. Systeme.io prend 0 % de frais de transaction. Seuls les frais de votre prestataire de paiement (Stripe, PayPal, etc.) s'appliquent."),
 ("Quels moyens de paiement sont acceptés ?", "Stripe, Apple Pay, PayPal, Razorpay, Flutterwave, Mercado Pago, Xendit et le paiement à la livraison."),
 ("Peut-on utiliser son propre nom de domaine ?", "Oui, même avec l'offre gratuite, qui inclut 1 nom de domaine personnalisé."),
 ("Systeme.io est-il disponible en français ?", "Oui. L'outil et son support sont disponibles en français."),
 ("Peut-on changer d'offre plus tard ?", "Oui. Vous pouvez commencer gratuitement et passer à Startup, Webinar ou Unlimited quand votre activité grandit. Le paiement annuel offre 2 mois."),
])

# ---------------------------------------------------------------- EN : REVIEW
LONG[("en", "review")] = dict(body=f"""
<p>Systeme.io is an all-in-one tool to sell online: sales funnels, email marketing, online courses, a blog, a website, automations and your own affiliate program. Its promise is simple: replace five or six subscriptions with one, with a free plan that never expires. In this review we look at what the tool really does, what each plan includes, where it falls short, and who it is worth it for.</p>
<h2>Systeme.io at a glance</h2>
<ul>
<li><b>Type of tool:</b> all-in-one marketing platform (funnels, emails, courses, website, blog, automations).</li>
<li><b>Price:</b> free plan forever, then Startup at $17, Webinar at $47 and Unlimited at $97 per month.</li>
<li><b>Yearly billing:</b> 2 months free.</li>
<li><b>Fees on your sales:</b> 0% taken by Systeme.io (only your payment provider's fees apply).</li>
<li><b>Email sends:</b> unlimited on every plan.</li>
<li><b>Best for:</b> beginners, coaches, course creators, creators and small businesses.</li>
</ul>
{cta("Try the free plan: no credit card required.")}
<h2>What Systeme.io does, feature by feature</h2>
<h3>1. Sales funnels</h3>
<p>This is the core of the tool. A funnel is a series of pages that takes a visitor to a purchase: an opt-in page to collect the email, a sales page, an order form and a thank-you page. Systeme.io gives you a drag-and-drop page editor and ready-made templates. On the order form you can add an <b>order bump</b> (a one-click extra offer before payment) and, right after payment, a <b>one-click upsell</b> without the customer typing their card again. You also get <b>A/B tests</b> to compare two versions of a page, <b>coupon codes</b> and <b>deadline funnels</b> to create real urgency.</p>
<h3>2. Email marketing</h3>
<p>You manage your contact list, send newsletters and build campaigns, which are sequences of emails sent automatically one after another. The big plus: <b>email sends are unlimited on every plan</b>, including the free one. With many email tools the price climbs with the number of emails you send; here only the number of contacts matters.</p>
<h3>3. Online courses</h3>
<p>Systeme.io hosts your courses with a members area for your students. You can sell a course as a one-time payment, a subscription or a payment plan, and deliver it automatically after purchase. There is also a <b>community</b> feature so your students or customers can talk to each other and to you.</p>
<h3>4. Website and blog</h3>
<p>You can build a full website and a blog and publish them on your own domain. For a small business, that saves paying for hosting and a WordPress theme on top.</p>
<h3>5. Automations</h3>
<p><b>Automation rules</b> and <b>workflows</b> trigger actions on their own: when someone signs up, buys or visits a page, Systeme.io can add a tag, enroll them in a course or start an email sequence. That is what lets you run your business on autopilot.</p>
<h3>6. Your own affiliate program</h3>
<p>A rare feature at this price: you can create your own affiliate program so other people promote your products for a commission. Systeme.io tracks every affiliate's sales for you.</p>
<h3>7. Events and bookings</h3>
<p>Systeme.io includes events and bookings, handy for coaches who sell sessions: clients book a slot straight from your page.</p>
<h3>8. Payments</h3>
<p>To get paid, you connect your own payment account. Systeme.io works with <b>Stripe, Apple Pay, PayPal, Razorpay, Flutterwave, Mercado Pago, Xendit</b> and cash on delivery. Money goes straight to you and Systeme.io takes no percentage.</p>
<h2>Plans and prices in detail</h2>
<div class="tbl"><table>
<thead><tr><th>Plan</th><th>Price per month</th><th>Contacts</th><th>Sales funnels</th><th>Courses</th></tr></thead>
<tbody>
<tr><td><b>Free</b></td><td>$0</td><td>2,000</td><td>3</td><td>1</td></tr>
<tr><td><b>Startup</b></td><td>$17</td><td>5,000</td><td>10</td><td>5</td></tr>
<tr><td><b>Webinar</b></td><td>$47</td><td>10,000</td><td>50</td><td>20</td></tr>
<tr><td><b>Unlimited</b></td><td>$97</td><td>Unlimited</td><td>Unlimited</td><td>Unlimited</td></tr>
</tbody></table></div>
<p><b>Every plan</b> includes unlimited email sends, unlimited file storage, 0% transaction fees, the affiliate program, online support and payment integrations. Yearly billing gives you 2 months free, and Systeme.io offers <b>free migration</b> if you come from another tool.</p>
<h3>What does the free plan really include?</h3>
<p>The free plan is not a trial: it never expires and needs no credit card. It includes up to 2,000 contacts, 3 sales funnels, 1 blog, 1 course, 1 affiliate program, 1 custom domain, unlimited email sends, 1 automation rule and 1 email campaign. That is enough to launch a first product, build your list and make your first sales.</p>
<h3>Which plan should you choose?</h3>
<ul>
<li><b>Free:</b> to test the tool and launch a first product.</li>
<li><b>Startup ($17):</b> once you pass 2,000 contacts or need more automations and campaigns.</li>
<li><b>Webinar ($47):</b> if you sell with automated webinars or have several products and up to 10,000 contacts.</li>
<li><b>Unlimited ($97):</b> beyond 10,000 contacts, or if you want everything unlimited.</li>
</ul>
{cta("Start for free and upgrade only when you need to.")}
<h2>Pros</h2>
<ul class="pc good">
<li><b>A real free plan forever</b>, with no credit card and enough to launch a business.</li>
<li><b>Everything in one place</b>: no need to connect five tools together.</li>
<li><b>Unlimited emails</b> on every plan.</li>
<li><b>0% fees</b> taken by Systeme.io on your sales.</li>
<li><b>Low prices</b>: the complete Unlimited plan costs the same as ClickFunnels' entry plan, and less than Kajabi's basic plan.</li>
<li><b>Available in many languages.</b></li>
</ul>
<h2>Cons</h2>
<ul class="pc bad">
<li><b>The free plan has limits</b>: only 1 automation rule and 1 email campaign, so heavy automation quickly means moving to Startup.</li>
<li><b>Limits rise in steps</b>: beyond 10,000 contacts you need the $97 plan.</li>
<li><b>Fewer advanced features than specialist tools</b>: a dedicated email tool or a high-end course platform will go further in its own niche. Systeme.io bets on simplicity and all-in-one.</li>
</ul>
<h2>Who is Systeme.io for?</h2>
<p><b>Beginners</b> who want to launch an online business without upfront costs. <b>Coaches and trainers</b> who sell courses, sessions or programs. <b>Creators</b> who need an opt-in page, an email sequence and an order form. <b>Small businesses</b> that want to replace several subscriptions with one.</p>
<p>On the other hand, if you already have a very large list, a big team or very specific needs in one area, compare it with specialist tools first.</p>
<h2>How to get started in 5 steps</h2>
<ol>
<li>Create your free account, no credit card needed.</li>
<li>Connect your payment method (Stripe or PayPal, for example).</li>
<li>Pick a funnel template and customize your opt-in page and sales page.</li>
<li>Write a welcome email sequence for new subscribers.</li>
<li>Publish your funnel, share the link and track your stats.</li>
</ol>
<h2>Our verdict</h2>
<div class="tip">Systeme.io is one of the best value tools on the market to launch and grow an online business. The free plan lets you test everything and even make your first sales, and the paid plans stay far cheaper than ClickFunnels or Kajabi. If you are starting out or want to cut your subscriptions, it is the most logical choice.</div>
{cta("Create your free Systeme.io account in seconds.")}
""", faq=[
 ("Is Systeme.io really free?", "Yes. The free plan never expires and needs no credit card. It includes 2,000 contacts, 3 sales funnels, 1 course and unlimited email sends."),
 ("Does Systeme.io take a commission on my sales?", "No. Systeme.io takes 0% transaction fees. Only your payment provider's fees (Stripe, PayPal, etc.) apply."),
 ("Which payment methods are supported?", "Stripe, Apple Pay, PayPal, Razorpay, Flutterwave, Mercado Pago, Xendit and cash on delivery."),
 ("Can I use my own domain name?", "Yes, even on the free plan, which includes 1 custom domain."),
 ("Can I change plans later?", "Yes. You can start for free and move to Startup, Webinar or Unlimited as your business grows. Yearly billing gives you 2 months free."),
])

# ---------------------------------------------------------------- FR : VS CLICKFUNNELS
LONG[("fr", "vs-clickfunnels")] = dict(body=f"""
<p>ClickFunnels est l'outil qui a popularisé les tunnels de vente. Systeme.io est arrivé ensuite avec une approche différente : tout-en-un, beaucoup moins cher, et une offre gratuite à vie. Les deux servent à créer des tunnels, envoyer des emails et vendre des formations, mais leurs prix et leurs limites n'ont rien à voir. Voici une comparaison détaillée, basée sur les pages de tarifs officielles des deux outils.</p>
<h2>Le résumé en 30 secondes</h2>
<ul>
<li><b>Prix d'entrée :</b> 0 € chez Systeme.io (offre gratuite à vie), 97 $ par mois chez ClickFunnels (81 $ en annuel).</li>
<li><b>Offre gratuite :</b> oui chez Systeme.io, non chez ClickFunnels (seulement un essai).</li>
<li><b>Frais sur les ventes :</b> aucun pourcentage dans les deux cas.</li>
<li><b>Limites de départ :</b> plus hautes chez ClickFunnels, mais pour un prix bien plus élevé.</li>
<li><b>Notre choix pour la plupart des gens :</b> Systeme.io.</li>
</ul>
{cta("Essayez Systeme.io gratuitement, sans carte bancaire.")}
<h2>Comparaison des prix</h2>
<h3>Les offres de Systeme.io</h3>
<div class="tbl"><table>
<thead><tr><th>Offre</th><th>Prix par mois</th><th>Contacts</th><th>Tunnels</th><th>Formations</th></tr></thead>
<tbody>
<tr><td>Gratuit</td><td>0 €</td><td>2 000</td><td>3</td><td>1</td></tr>
<tr><td>Startup</td><td>17 €</td><td>5 000</td><td>10</td><td>5</td></tr>
<tr><td>Webinar</td><td>47 €</td><td>10 000</td><td>50</td><td>20</td></tr>
<tr><td>Unlimited</td><td>97 €</td><td>Illimités</td><td>Illimités</td><td>Illimitées</td></tr>
</tbody></table></div>
<p>Emails illimités sur toutes les offres, 2 mois offerts en paiement annuel.</p>
<h3>Les offres de ClickFunnels</h3>
<div class="tbl"><table>
<thead><tr><th>Offre</th><th>Mensuel</th><th>Annuel (par mois)</th><th>Contacts</th><th>Emails par mois</th><th>Formations</th><th>Membres d'équipe</th></tr></thead>
<tbody>
<tr><td>Launch</td><td>97 $</td><td>81 $</td><td>10 000</td><td>50 000</td><td>3</td><td>2</td></tr>
<tr><td>Scale</td><td>197 $</td><td>164 $</td><td>75 000</td><td>300 000</td><td>6</td><td>5</td></tr>
<tr><td>Optimize</td><td>297 $</td><td>248 $</td><td>150 000</td><td>750 000</td><td>10</td><td>10</td></tr>
<tr><td>Dominate</td><td>-</td><td>5 997 $ par an</td><td>400 000</td><td>1 200 000</td><td>20</td><td>20</td></tr>
</tbody></table></div>
<p>Toutes les offres ClickFunnels incluent des tunnels, des pages et des visiteurs illimités, et un essai gratuit.</p>
<h3>Ce que ça donne sur une année</h3>
<p>Sur un an, l'offre la moins chère de ClickFunnels coûte au minimum <b>972 $</b> (81 $ x 12 en paiement annuel). Avec Systeme.io, vous pouvez rester sur l'offre gratuite tant que vous avez moins de 2 000 contacts, ou payer 17 € par mois sur Startup. Même l'offre Unlimited de Systeme.io, avec contacts, tunnels et formations illimités, coûte le prix de l'offre d'entrée de ClickFunnels.</p>
<h2>Comparaison fonction par fonction</h2>
<div class="tbl"><table>
<thead><tr><th>Critère</th><th>Systeme.io</th><th>ClickFunnels</th></tr></thead>
<tbody>
<tr><td>Offre gratuite</td><td class="win">Oui, à vie</td><td>Non (essai gratuit)</td></tr>
<tr><td>Prix de départ</td><td class="win">0 €, puis 17 €/mois</td><td>97 $/mois</td></tr>
<tr><td>Tunnels de vente</td><td>3 (gratuit) à illimités</td><td>Illimités</td></tr>
<tr><td>Envois d'emails</td><td class="win">Illimités</td><td>50 000 par mois sur Launch</td></tr>
<tr><td>Contacts sur l'offre d'entrée</td><td>2 000 (gratuit), 5 000 (17 €)</td><td>10 000</td></tr>
<tr><td>Formations</td><td>1 à illimitées selon l'offre</td><td>3 à 20 selon l'offre</td></tr>
<tr><td>Membres d'équipe</td><td>Comptes assistants disponibles</td><td>2 à 20 selon l'offre</td></tr>
<tr><td>Order bump et upsell en un clic</td><td>Oui</td><td>Oui</td></tr>
<tr><td>Frais sur vos ventes</td><td>0 %</td><td>Aucun pourcentage</td></tr>
</tbody></table></div>
<h2>Les points forts de Systeme.io face à ClickFunnels</h2>
<ul class="pc good">
<li><b>Le prix</b> : de 0 € à 97 € par mois, contre 97 $ à 297 $ par mois (et 5 997 $ par an pour Dominate).</li>
<li><b>Une offre gratuite à vie</b>, idéale pour démarrer sans risque.</li>
<li><b>Les emails illimités</b>, alors que ClickFunnels plafonne les envois mensuels selon l'offre.</li>
<li><b>Le programme d'affiliation intégré</b> dès l'offre gratuite.</li>
<li><b>La simplicité</b> : un outil pensé pour les débutants.</li>
</ul>
<h2>Les points forts de ClickFunnels face à Systeme.io</h2>
<ul class="pc good">
<li><b>Des limites de départ plus hautes</b> : 10 000 contacts et 2 membres d'équipe dès l'offre Launch.</li>
<li><b>Des tunnels illimités</b> sur toutes les offres.</li>
<li><b>Pensé pour les équipes</b> : jusqu'à 20 espaces de travail et 20 membres sur l'offre la plus haute.</li>
</ul>
<h2>Combien vous coûte chaque outil selon la taille de votre liste ?</h2>
<p>Le bon critère pour comparer, c'est votre nombre de contacts. Voici l'offre minimum à prendre dans chaque outil selon la taille de votre liste.</p>
<div class="tbl"><table>
<thead><tr><th>Nombre de contacts</th><th>Systeme.io</th><th>ClickFunnels</th></tr></thead>
<tbody>
<tr><td>Jusqu'à 2 000</td><td class="win">0 € (Gratuit)</td><td>97 $ (Launch)</td></tr>
<tr><td>Jusqu'à 5 000</td><td class="win">17 € (Startup)</td><td>97 $ (Launch)</td></tr>
<tr><td>Jusqu'à 10 000</td><td class="win">47 € (Webinar)</td><td>97 $ (Launch)</td></tr>
<tr><td>Jusqu'à 75 000</td><td class="win">97 € (Unlimited)</td><td>197 $ (Scale)</td></tr>
<tr><td>Jusqu'à 150 000</td><td class="win">97 € (Unlimited)</td><td>297 $ (Optimize)</td></tr>
</tbody></table></div>
<p>Quelle que soit la taille de votre liste, Systeme.io revient moins cher. L'écart est maximal au démarrage, quand vous avez peu de contacts : c'est justement le moment où chaque euro compte.</p>
<h2>Prise en main</h2>
<p>Systeme.io a été pensé pour les débutants : un seul tableau de bord, des modèles de tunnels prêts à l'emploi et un éditeur par glisser-déposer. Comme tout est intégré (emails, formations, paiements), vous n'avez pas à connecter plusieurs outils entre eux. ClickFunnels est aussi un éditeur visuel complet, mais son prix d'entrée le destine plutôt à des entrepreneurs qui ont déjà un produit qui se vend.</p>
<h2>Tunnels de vente</h2>
<p>Les deux outils couvrent l'essentiel : pages de capture, pages de vente, bons de commande, order bumps et upsells en un clic. Systeme.io ajoute les tests A/B, les codes promo et les tunnels à date limite. La différence se joue sur le nombre : ClickFunnels donne des tunnels illimités dès Launch, Systeme.io en donne 3 en gratuit, 10 sur Startup, 50 sur Webinar et un nombre illimité sur Unlimited. Pour la plupart des business, 10 tunnels suffisent largement.</p>
<h2>Emailing</h2>
<p>C'est l'un des gros avantages de Systeme.io : les envois d'emails sont <b>illimités sur toutes les offres</b>. Chez ClickFunnels, le nombre d'emails par mois dépend de l'offre (50 000 sur Launch). Si vous envoyez une newsletter par semaine à 10 000 contacts, vous atteignez déjà 40 000 emails par mois, sans compter vos séquences automatiques.</p>
<h2>Formations en ligne</h2>
<p>Les deux outils permettent d'héberger et de vendre des formations avec un espace membre. ClickFunnels limite le nombre de formations (3 sur Launch). Systeme.io en propose 1 en gratuit, 5 sur Startup, 20 sur Webinar et un nombre illimité sur Unlimited, avec en plus des communautés pour vos élèves.</p>
<h2>Paiements et migration</h2>
<p>Ni l'un ni l'autre ne prend de pourcentage sur vos ventes. Systeme.io se connecte à Stripe, Apple Pay, PayPal, Razorpay, Flutterwave, Mercado Pago, Xendit et au paiement à la livraison. Si vous êtes déjà sur ClickFunnels, Systeme.io met en avant une migration gratuite pour vous aider à transférer votre activité.</p>
<h2>Lequel choisir ?</h2>
<p><b>Choisissez Systeme.io si</b> vous débutez, si vous voulez tester une idée sans dépenser, si vous avez un petit ou moyen business, ou si vous voulez simplement payer moins. Pour la grande majorité des coachs, formateurs et créateurs, Systeme.io fait le travail pour une fraction du prix.</p>
<p><b>Choisissez ClickFunnels si</b> vous avez déjà un gros business, une équipe à faire travailler sur plusieurs espaces et un budget marketing confortable.</p>
<h2>Verdict</h2>
<div class="tip">Systeme.io gagne nettement sur le prix et sur l'accessibilité : vous démarrez gratuitement, vos emails sont illimités, et même son offre la plus complète coûte le prix de l'offre d'entrée de ClickFunnels. ClickFunnels reste une option pour les grosses structures, mais pour un débutant ou une petite entreprise, Systeme.io est le choix le plus malin.</div>
{cta("Lancez votre premier tunnel gratuitement avec Systeme.io.")}
""", faq=[
 ("Systeme.io est-il moins cher que ClickFunnels ?", "Oui. Systeme.io a une offre gratuite à vie et des offres payantes de 17 € à 97 € par mois. ClickFunnels démarre à 97 $ par mois (81 $ en annuel) et n'a pas d'offre gratuite."),
 ("ClickFunnels a-t-il une offre gratuite ?", "Non. ClickFunnels propose seulement un essai gratuit avant de passer à une offre payante."),
 ("Peut-on passer de ClickFunnels à Systeme.io ?", "Oui. Systeme.io met en avant une migration gratuite pour les nouveaux clients qui viennent d'un autre outil."),
 ("Lequel est le meilleur pour débuter ?", "Systeme.io, grâce à son offre gratuite, sa prise en main simple et ses emails illimités."),
])

LONG[("en", "vs-clickfunnels")] = dict(body=f"""
<p>ClickFunnels is the tool that made sales funnels popular. Systeme.io came later with a different approach: all-in-one, much cheaper, and a free plan forever. Both help you build funnels, send emails and sell courses, but their prices and limits are worlds apart. Here is a detailed comparison based on both tools' official pricing pages.</p>
<h2>The 30-second summary</h2>
<ul>
<li><b>Entry price:</b> $0 at Systeme.io (free plan forever), $97 per month at ClickFunnels ($81 billed yearly).</li>
<li><b>Free plan:</b> yes at Systeme.io, no at ClickFunnels (trial only).</li>
<li><b>Fees on sales:</b> no percentage on either.</li>
<li><b>Starting limits:</b> higher at ClickFunnels, but for a much higher price.</li>
<li><b>Our pick for most people:</b> Systeme.io.</li>
</ul>
{cta("Try Systeme.io for free, no credit card required.")}
<h2>Price comparison</h2>
<h3>Systeme.io plans</h3>
<div class="tbl"><table>
<thead><tr><th>Plan</th><th>Price per month</th><th>Contacts</th><th>Funnels</th><th>Courses</th></tr></thead>
<tbody>
<tr><td>Free</td><td>$0</td><td>2,000</td><td>3</td><td>1</td></tr>
<tr><td>Startup</td><td>$17</td><td>5,000</td><td>10</td><td>5</td></tr>
<tr><td>Webinar</td><td>$47</td><td>10,000</td><td>50</td><td>20</td></tr>
<tr><td>Unlimited</td><td>$97</td><td>Unlimited</td><td>Unlimited</td><td>Unlimited</td></tr>
</tbody></table></div>
<p>Unlimited emails on every plan, 2 months free with yearly billing.</p>
<h3>ClickFunnels plans</h3>
<div class="tbl"><table>
<thead><tr><th>Plan</th><th>Monthly</th><th>Yearly (per month)</th><th>Contacts</th><th>Emails per month</th><th>Courses</th><th>Team members</th></tr></thead>
<tbody>
<tr><td>Launch</td><td>$97</td><td>$81</td><td>10,000</td><td>50,000</td><td>3</td><td>2</td></tr>
<tr><td>Scale</td><td>$197</td><td>$164</td><td>75,000</td><td>300,000</td><td>6</td><td>5</td></tr>
<tr><td>Optimize</td><td>$297</td><td>$248</td><td>150,000</td><td>750,000</td><td>10</td><td>10</td></tr>
<tr><td>Dominate</td><td>-</td><td>$5,997 per year</td><td>400,000</td><td>1,200,000</td><td>20</td><td>20</td></tr>
</tbody></table></div>
<p>Every ClickFunnels plan includes unlimited funnels, pages and visitors, and a free trial.</p>
<h3>What it costs over a year</h3>
<p>Over a year, ClickFunnels' cheapest plan costs at least <b>$972</b> ($81 x 12 on yearly billing). With Systeme.io you can stay on the free plan while you have fewer than 2,000 contacts, or pay $17 per month on Startup. Even Systeme.io's Unlimited plan, with unlimited contacts, funnels and courses, costs the same as ClickFunnels' entry plan.</p>
<h2>Feature by feature</h2>
<div class="tbl"><table>
<thead><tr><th>Criteria</th><th>Systeme.io</th><th>ClickFunnels</th></tr></thead>
<tbody>
<tr><td>Free plan</td><td class="win">Yes, forever</td><td>No (free trial)</td></tr>
<tr><td>Starting price</td><td class="win">$0, then $17/month</td><td>$97/month</td></tr>
<tr><td>Sales funnels</td><td>3 (free) to unlimited</td><td>Unlimited</td></tr>
<tr><td>Email sends</td><td class="win">Unlimited</td><td>50,000 per month on Launch</td></tr>
<tr><td>Contacts on the entry plan</td><td>2,000 (free), 5,000 ($17)</td><td>10,000</td></tr>
<tr><td>Courses</td><td>1 to unlimited depending on plan</td><td>3 to 20 depending on plan</td></tr>
<tr><td>Team members</td><td>Assistant accounts available</td><td>2 to 20 depending on plan</td></tr>
<tr><td>Order bumps and one-click upsells</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Fees on your sales</td><td>0%</td><td>No percentage</td></tr>
</tbody></table></div>
<h2>Where Systeme.io beats ClickFunnels</h2>
<ul class="pc good">
<li><b>Price</b>: $0 to $97 per month, against $97 to $297 per month (and $5,997 per year for Dominate).</li>
<li><b>A free plan forever</b>, ideal to start with no risk.</li>
<li><b>Unlimited emails</b>, while ClickFunnels caps monthly sends by plan.</li>
<li><b>A built-in affiliate program</b> from the free plan.</li>
<li><b>Simplicity</b>: a tool designed for beginners.</li>
</ul>
<h2>Where ClickFunnels beats Systeme.io</h2>
<ul class="pc good">
<li><b>Higher starting limits</b>: 10,000 contacts and 2 team members from the Launch plan.</li>
<li><b>Unlimited funnels</b> on every plan.</li>
<li><b>Built for teams</b>: up to 20 workspaces and 20 members on the top plan.</li>
</ul>
<h2>What does each tool cost for your list size?</h2>
<p>The right way to compare is your number of contacts. Here is the minimum plan you need in each tool depending on the size of your list.</p>
<div class="tbl"><table>
<thead><tr><th>Number of contacts</th><th>Systeme.io</th><th>ClickFunnels</th></tr></thead>
<tbody>
<tr><td>Up to 2,000</td><td class="win">$0 (Free)</td><td>$97 (Launch)</td></tr>
<tr><td>Up to 5,000</td><td class="win">$17 (Startup)</td><td>$97 (Launch)</td></tr>
<tr><td>Up to 10,000</td><td class="win">$47 (Webinar)</td><td>$97 (Launch)</td></tr>
<tr><td>Up to 75,000</td><td class="win">$97 (Unlimited)</td><td>$197 (Scale)</td></tr>
<tr><td>Up to 150,000</td><td class="win">$97 (Unlimited)</td><td>$297 (Optimize)</td></tr>
</tbody></table></div>
<p>Whatever your list size, Systeme.io comes out cheaper. The gap is widest at the start, when you have few contacts: exactly when every dollar counts.</p>
<h2>Ease of use</h2>
<p>Systeme.io was designed for beginners: one dashboard, ready-made funnel templates and a drag-and-drop editor. Since everything is built in (emails, courses, payments), you do not have to connect several tools together. ClickFunnels is also a complete visual builder, but its entry price makes it better suited to entrepreneurs who already have a product that sells.</p>
<h2>Sales funnels</h2>
<p>Both tools cover the essentials: opt-in pages, sales pages, order forms, order bumps and one-click upsells. Systeme.io adds A/B tests, coupon codes and deadline funnels. The difference is the number: ClickFunnels gives unlimited funnels from Launch, Systeme.io gives 3 on Free, 10 on Startup, 50 on Webinar and unlimited on Unlimited. For most businesses, 10 funnels are more than enough.</p>
<h2>Email marketing</h2>
<p>This is one of Systeme.io's big advantages: email sends are <b>unlimited on every plan</b>. At ClickFunnels, the number of emails per month depends on the plan (50,000 on Launch). If you send one newsletter a week to 10,000 contacts, you already reach 40,000 emails a month, before counting your automated sequences.</p>
<h2>Online courses</h2>
<p>Both tools let you host and sell courses with a members area. ClickFunnels limits the number of courses (3 on Launch). Systeme.io offers 1 on Free, 5 on Startup, 20 on Webinar and unlimited on Unlimited, plus communities for your students.</p>
<h2>Payments and migration</h2>
<p>Neither takes a percentage of your sales. Systeme.io connects to Stripe, Apple Pay, PayPal, Razorpay, Flutterwave, Mercado Pago, Xendit and cash on delivery. If you are already on ClickFunnels, Systeme.io advertises free migration to help you move your business.</p>
<h2>Which one should you choose?</h2>
<p><b>Choose Systeme.io if</b> you are starting out, want to test an idea without spending, run a small or medium business, or simply want to pay less. For most coaches, trainers and creators, Systeme.io does the job for a fraction of the price.</p>
<p><b>Choose ClickFunnels if</b> you already run a large business, have a team working across several workspaces and a comfortable marketing budget.</p>
<h2>Verdict</h2>
<div class="tip">Systeme.io clearly wins on price and accessibility: you start for free, your emails are unlimited, and even its most complete plan costs the same as ClickFunnels' entry plan. ClickFunnels remains an option for large companies, but for a beginner or a small business, Systeme.io is the smarter choice.</div>
{cta("Launch your first funnel for free with Systeme.io.")}
""", faq=[
 ("Is Systeme.io cheaper than ClickFunnels?", "Yes. Systeme.io has a free plan forever and paid plans from $17 to $97 per month. ClickFunnels starts at $97 per month ($81 billed yearly) and has no free plan."),
 ("Does ClickFunnels have a free plan?", "No. ClickFunnels only offers a free trial before you move to a paid plan."),
 ("Can I move from ClickFunnels to Systeme.io?", "Yes. Systeme.io advertises free migration for new customers coming from another tool."),
 ("Which is better for beginners?", "Systeme.io, thanks to its free plan, its ease of use and its unlimited emails."),
])

# ---------------------------------------------------------------- FR : VS KAJABI
LONG[("fr", "vs-kajabi")] = dict(body=f"""
<p>Kajabi est une plateforme haut de gamme très connue des créateurs de formations et des coachs. Systeme.io couvre les mêmes besoins de base (formations, tunnels, emails, automatisations, site web), mais avec une offre gratuite et des prix beaucoup plus bas. Voici une comparaison détaillée basée sur les pages de tarifs officielles.</p>
<h2>Le résumé en 30 secondes</h2>
<ul>
<li><b>Prix d'entrée :</b> 0 € chez Systeme.io, 179 $ par mois chez Kajabi (143 $ en annuel).</li>
<li><b>Offre gratuite :</b> oui chez Systeme.io, non chez Kajabi (essai de 14 jours et garantie satisfait ou remboursé de 30 jours).</li>
<li><b>Frais :</b> 0 % chez Systeme.io ; chez Kajabi, frais de carte dès 2,9 % + 0,30 $ (États-Unis) avec Kajabi Payments, ou frais supplémentaires si vous utilisez un autre prestataire.</li>
<li><b>Notre choix pour la plupart des gens :</b> Systeme.io.</li>
</ul>
{cta("Essayez Systeme.io gratuitement, sans carte bancaire.")}
<h2>Comparaison des prix</h2>
<h3>Les offres de Kajabi</h3>
<div class="tbl"><table>
<thead><tr><th>Offre</th><th>Mensuel</th><th>Annuel (par mois)</th><th>Produits</th><th>Contacts</th><th>Sites</th><th>Admins</th></tr></thead>
<tbody>
<tr><td>Basic</td><td>179 $</td><td>143 $</td><td>5</td><td>2 500</td><td>1</td><td>2</td></tr>
<tr><td>Growth</td><td>249 $</td><td>199 $</td><td>50</td><td>25 000</td><td>1</td><td>11</td></tr>
<tr><td>Pro</td><td>499 $</td><td>399 $</td><td>Illimités</td><td>100 000</td><td>3</td><td>26</td></tr>
</tbody></table></div>
<p>Contacts supplémentaires chez Kajabi : 125 $ par mois par tranche de 25 000.</p>
<h3>Les offres de Systeme.io</h3>
<div class="tbl"><table>
<thead><tr><th>Offre</th><th>Prix par mois</th><th>Contacts</th><th>Tunnels</th><th>Formations</th></tr></thead>
<tbody>
<tr><td>Gratuit</td><td>0 €</td><td>2 000</td><td>3</td><td>1</td></tr>
<tr><td>Startup</td><td>17 €</td><td>5 000</td><td>10</td><td>5</td></tr>
<tr><td>Webinar</td><td>47 €</td><td>10 000</td><td>50</td><td>20</td></tr>
<tr><td>Unlimited</td><td>97 €</td><td>Illimités</td><td>Illimités</td><td>Illimitées</td></tr>
</tbody></table></div>
<h3>Ce que ça donne sur une année</h3>
<p>L'offre Basic de Kajabi coûte au minimum <b>1 716 $ par an</b>, pour 5 produits et 2 500 contacts. Avec Systeme.io, l'offre Startup à 17 € par mois vous donne 5 formations et 5 000 contacts, soit deux fois plus de contacts pour une fraction du prix. Et l'offre Unlimited de Systeme.io (97 € par mois, tout illimité) reste moins chère que l'offre la plus basse de Kajabi.</p>
<h2>Les frais sur vos ventes</h2>
<p>C'est une différence importante. <b>Systeme.io prend 0 %</b> : vous payez seulement les frais habituels de Stripe ou PayPal. <b>Kajabi ne prend pas de part de vos revenus</b>, mais ses frais de carte via Kajabi Payments vont de 2,9 % + 0,30 $ (Basic) à 2,7 % + 0,30 $ (Pro) aux États-Unis, et si vous passez par un autre prestataire de paiement, Kajabi ajoute 2 % (Basic), 1 % (Growth) ou 0,5 % (Pro).</p>
<h2>Comparaison fonction par fonction</h2>
<div class="tbl"><table>
<thead><tr><th>Critère</th><th>Systeme.io</th><th>Kajabi</th></tr></thead>
<tbody>
<tr><td>Offre gratuite</td><td class="win">Oui, à vie</td><td>Non (essai de 14 jours)</td></tr>
<tr><td>Prix de départ</td><td class="win">0 €, puis 17 €/mois</td><td>179 $/mois</td></tr>
<tr><td>Contacts sur l'offre d'entrée</td><td class="win">2 000 (gratuit), 5 000 (17 €)</td><td>2 500</td></tr>
<tr><td>Formations / produits</td><td>1 à illimitées</td><td>5 à illimités</td></tr>
<tr><td>Envois d'emails</td><td class="win">Illimités</td><td>Inclus</td></tr>
<tr><td>Tunnels de vente</td><td>Oui</td><td>Oui</td></tr>
<tr><td>Communauté</td><td>Oui</td><td>Oui</td></tr>
<tr><td>Frais sur les ventes</td><td class="win">0 %</td><td>Frais de carte ou frais si autre prestataire</td></tr>
<tr><td>Garantie</td><td>Offre gratuite pour tester</td><td>Satisfait ou remboursé 30 jours</td></tr>
</tbody></table></div>
<h2>Les points forts de Systeme.io face à Kajabi</h2>
<ul class="pc good">
<li><b>Un prix sans comparaison</b> : de 0 € à 97 € par mois, contre 179 $ à 499 $.</li>
<li><b>Une offre gratuite à vie</b> pour lancer sa première formation sans rien payer.</li>
<li><b>0 % de frais</b> sur vos ventes, quel que soit votre prestataire de paiement.</li>
<li><b>Plus de contacts</b> pour le prix sur les petites offres.</li>
</ul>
<h2>Les points forts de Kajabi face à Systeme.io</h2>
<ul class="pc good">
<li><b>Une plateforme premium</b> très orientée création de formations et de coaching.</li>
<li><b>Des limites élevées sur les grosses offres</b> : jusqu'à 100 000 contacts et 26 administrateurs.</li>
<li><b>Une garantie satisfait ou remboursé de 30 jours.</b></li>
</ul>
<h2>Combien vous coûte chaque outil selon la taille de votre liste ?</h2>
<p>Voici l'offre minimum à prendre dans chaque outil selon votre nombre de contacts, sans option de contacts supplémentaires.</p>
<div class="tbl"><table>
<thead><tr><th>Nombre de contacts</th><th>Systeme.io</th><th>Kajabi</th></tr></thead>
<tbody>
<tr><td>Jusqu'à 2 000</td><td class="win">0 € (Gratuit)</td><td>179 $ (Basic)</td></tr>
<tr><td>Jusqu'à 5 000</td><td class="win">17 € (Startup)</td><td>249 $ (Growth)</td></tr>
<tr><td>Jusqu'à 10 000</td><td class="win">47 € (Webinar)</td><td>249 $ (Growth)</td></tr>
<tr><td>Jusqu'à 25 000</td><td class="win">97 € (Unlimited)</td><td>249 $ (Growth)</td></tr>
<tr><td>Jusqu'à 100 000</td><td class="win">97 € (Unlimited)</td><td>499 $ (Pro)</td></tr>
</tbody></table></div>
<p>Avec 5 000 contacts, la différence dépasse 200 par mois. Sur un an, cela représente plusieurs milliers d'euros que vous pouvez réinvestir dans votre publicité ou votre contenu.</p>
<h2>Prise en main</h2>
<p>Les deux outils sont pensés pour des non-techniciens. Systeme.io mise sur la simplicité : un tableau de bord unique, des modèles et un éditeur par glisser-déposer. Kajabi propose une expérience très soignée, mais son prix en fait surtout un outil pour les créateurs déjà installés.</p>
<h2>Formations et communauté</h2>
<p>C'est le terrain de Kajabi, qui compte ses limites en « produits » : 5 sur Basic, 50 sur Growth, illimités sur Pro. Systeme.io compte en formations : 1 en gratuit, 5 sur Startup, 20 sur Webinar, illimitées sur Unlimited. Les deux proposent un espace membre et une communauté pour vos élèves, et permettent de vendre en paiement unique, en abonnement ou en plusieurs fois.</p>
<h2>Tunnels et emailing</h2>
<p>Systeme.io est né comme un outil de tunnels de vente : order bumps, upsells en un clic, tests A/B, codes promo et tunnels à date limite sont au cœur de l'outil. Côté emailing, les envois sont illimités sur toutes les offres de Systeme.io. Kajabi intègre aussi l'emailing et des pipelines de vente, mais compte ses limites en contacts, avec des contacts supplémentaires à 125 $ par mois par tranche de 25 000.</p>
<h2>Équipe</h2>
<p>Si vous travaillez avec beaucoup de collaborateurs, Kajabi a un avantage : 2 administrateurs sur Basic, 11 sur Growth et 26 sur Pro. Systeme.io propose des comptes assistants, suffisants pour un solo ou une petite équipe.</p>
<h2>Paiements et migration</h2>
<p>Systeme.io se connecte à Stripe, Apple Pay, PayPal, Razorpay, Flutterwave, Mercado Pago, Xendit et au paiement à la livraison, sans prendre de pourcentage. Si vous êtes déjà sur Kajabi, Systeme.io met en avant une migration gratuite.</p>
<h2>Lequel choisir ?</h2>
<p><b>Choisissez Systeme.io si</b> vous lancez votre première formation, si vous voulez garder vos coûts bas, ou si vous avez une petite ou moyenne audience. Vous aurez formations, tunnels, emails et automatisations pour une fraction du prix.</p>
<p><b>Choisissez Kajabi si</b> vous avez déjà une grosse activité, un budget confortable et besoin de nombreux administrateurs.</p>
<h2>Verdict</h2>
<div class="tip">Kajabi est une bonne plateforme, mais à 179 $ par mois minimum et sans offre gratuite, elle s'adresse surtout aux business déjà installés. Systeme.io couvre les mêmes bases dès 0 €, ne prend aucun pourcentage sur vos ventes et reste moins cher même sur son offre illimitée. Pour la grande majorité des créateurs de formations, Systeme.io est le meilleur choix.</div>
{cta("Créez votre première formation gratuitement avec Systeme.io.")}
""", faq=[
 ("Systeme.io est-il moins cher que Kajabi ?", "Oui, de loin. Systeme.io a une offre gratuite et des offres de 17 € à 97 € par mois. Kajabi démarre à 179 $ par mois (143 $ en annuel)."),
 ("Kajabi a-t-il une offre gratuite ?", "Non. Kajabi propose un essai gratuit de 14 jours et une garantie satisfait ou remboursé de 30 jours."),
 ("Kajabi prend-il une commission ?", "Kajabi ne prend pas de part de vos revenus, mais applique des frais de carte via Kajabi Payments, ou des frais supplémentaires si vous utilisez un autre prestataire de paiement."),
 ("Lequel est le meilleur pour vendre une formation ?", "Pour débuter ou garder des coûts bas, Systeme.io. Kajabi convient surtout aux gros business avec un budget confortable."),
])

LONG[("en", "vs-kajabi")] = dict(body=f"""
<p>Kajabi is a well-known premium platform for course creators and coaches. Systeme.io covers the same core needs (courses, funnels, emails, automations, website), but with a free plan and much lower prices. Here is a detailed comparison based on the official pricing pages.</p>
<h2>The 30-second summary</h2>
<ul>
<li><b>Entry price:</b> $0 at Systeme.io, $179 per month at Kajabi ($143 billed yearly).</li>
<li><b>Free plan:</b> yes at Systeme.io, no at Kajabi (14-day trial and 30-day money-back guarantee).</li>
<li><b>Fees:</b> 0% at Systeme.io; at Kajabi, card fees from 2.9% + 30¢ (US) with Kajabi Payments, or extra fees if you use another processor.</li>
<li><b>Our pick for most people:</b> Systeme.io.</li>
</ul>
{cta("Try Systeme.io for free, no credit card required.")}
<h2>Price comparison</h2>
<h3>Kajabi plans</h3>
<div class="tbl"><table>
<thead><tr><th>Plan</th><th>Monthly</th><th>Yearly (per month)</th><th>Products</th><th>Contacts</th><th>Websites</th><th>Admins</th></tr></thead>
<tbody>
<tr><td>Basic</td><td>$179</td><td>$143</td><td>5</td><td>2,500</td><td>1</td><td>2</td></tr>
<tr><td>Growth</td><td>$249</td><td>$199</td><td>50</td><td>25,000</td><td>1</td><td>11</td></tr>
<tr><td>Pro</td><td>$499</td><td>$399</td><td>Unlimited</td><td>100,000</td><td>3</td><td>26</td></tr>
</tbody></table></div>
<p>Extra contacts at Kajabi: $125 per month per block of 25,000.</p>
<h3>Systeme.io plans</h3>
<div class="tbl"><table>
<thead><tr><th>Plan</th><th>Price per month</th><th>Contacts</th><th>Funnels</th><th>Courses</th></tr></thead>
<tbody>
<tr><td>Free</td><td>$0</td><td>2,000</td><td>3</td><td>1</td></tr>
<tr><td>Startup</td><td>$17</td><td>5,000</td><td>10</td><td>5</td></tr>
<tr><td>Webinar</td><td>$47</td><td>10,000</td><td>50</td><td>20</td></tr>
<tr><td>Unlimited</td><td>$97</td><td>Unlimited</td><td>Unlimited</td><td>Unlimited</td></tr>
</tbody></table></div>
<h3>What it costs over a year</h3>
<p>Kajabi's Basic plan costs at least <b>$1,716 per year</b> for 5 products and 2,500 contacts. With Systeme.io, the $17 Startup plan gives you 5 courses and 5,000 contacts: twice the contacts for a fraction of the price. And Systeme.io's Unlimited plan ($97 per month, everything unlimited) is still cheaper than Kajabi's lowest plan.</p>
<h2>Fees on your sales</h2>
<p>This is a key difference. <b>Systeme.io takes 0%</b>: you only pay Stripe's or PayPal's usual fees. <b>Kajabi takes no revenue share</b>, but its card fees through Kajabi Payments range from 2.9% + 30¢ (Basic) to 2.7% + 30¢ (Pro) in the US, and if you use another payment processor Kajabi adds 2% (Basic), 1% (Growth) or 0.5% (Pro).</p>
<h2>Feature by feature</h2>
<div class="tbl"><table>
<thead><tr><th>Criteria</th><th>Systeme.io</th><th>Kajabi</th></tr></thead>
<tbody>
<tr><td>Free plan</td><td class="win">Yes, forever</td><td>No (14-day trial)</td></tr>
<tr><td>Starting price</td><td class="win">$0, then $17/month</td><td>$179/month</td></tr>
<tr><td>Contacts on the entry plan</td><td class="win">2,000 (free), 5,000 ($17)</td><td>2,500</td></tr>
<tr><td>Courses / products</td><td>1 to unlimited</td><td>5 to unlimited</td></tr>
<tr><td>Email sends</td><td class="win">Unlimited</td><td>Included</td></tr>
<tr><td>Sales funnels</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Community</td><td>Yes</td><td>Yes</td></tr>
<tr><td>Fees on sales</td><td class="win">0%</td><td>Card fees or extra fee with another processor</td></tr>
<tr><td>Guarantee</td><td>Free plan to test</td><td>30-day money-back</td></tr>
</tbody></table></div>
<h2>Where Systeme.io beats Kajabi</h2>
<ul class="pc good">
<li><b>Unbeatable price</b>: $0 to $97 per month, against $179 to $499.</li>
<li><b>A free plan forever</b> to launch your first course without paying anything.</li>
<li><b>0% fees</b> on your sales, whatever your payment provider.</li>
<li><b>More contacts for the money</b> on the smaller plans.</li>
</ul>
<h2>Where Kajabi beats Systeme.io</h2>
<ul class="pc good">
<li><b>A premium platform</b> focused on courses and coaching.</li>
<li><b>High limits on the bigger plans</b>: up to 100,000 contacts and 26 admins.</li>
<li><b>A 30-day money-back guarantee.</b></li>
</ul>
<h2>What does each tool cost for your list size?</h2>
<p>Here is the minimum plan you need in each tool depending on your number of contacts, without extra contact add-ons.</p>
<div class="tbl"><table>
<thead><tr><th>Number of contacts</th><th>Systeme.io</th><th>Kajabi</th></tr></thead>
<tbody>
<tr><td>Up to 2,000</td><td class="win">$0 (Free)</td><td>$179 (Basic)</td></tr>
<tr><td>Up to 5,000</td><td class="win">$17 (Startup)</td><td>$249 (Growth)</td></tr>
<tr><td>Up to 10,000</td><td class="win">$47 (Webinar)</td><td>$249 (Growth)</td></tr>
<tr><td>Up to 25,000</td><td class="win">$97 (Unlimited)</td><td>$249 (Growth)</td></tr>
<tr><td>Up to 100,000</td><td class="win">$97 (Unlimited)</td><td>$499 (Pro)</td></tr>
</tbody></table></div>
<p>With 5,000 contacts the difference is over $200 a month. Over a year, that is several thousand dollars you can put back into ads or content.</p>
<h2>Ease of use</h2>
<p>Both tools are built for non-technical people. Systeme.io bets on simplicity: one dashboard, templates and a drag-and-drop editor. Kajabi offers a very polished experience, but its price makes it mainly a tool for established creators.</p>
<h2>Courses and community</h2>
<p>This is Kajabi's home turf, which counts its limits in "products": 5 on Basic, 50 on Growth, unlimited on Pro. Systeme.io counts courses: 1 on Free, 5 on Startup, 20 on Webinar, unlimited on Unlimited. Both offer a members area and a community for your students, and let you sell with a one-time payment, a subscription or a payment plan.</p>
<h2>Funnels and email</h2>
<p>Systeme.io started as a sales funnel tool: order bumps, one-click upsells, A/B tests, coupon codes and deadline funnels are at its core. For email, sends are unlimited on every Systeme.io plan. Kajabi also includes email and sales pipelines, but counts its limits in contacts, with extra contacts at $125 per month per block of 25,000.</p>
<h2>Team</h2>
<p>If you work with many collaborators, Kajabi has an edge: 2 admins on Basic, 11 on Growth and 26 on Pro. Systeme.io offers assistant accounts, enough for a solo creator or a small team.</p>
<h2>Payments and migration</h2>
<p>Systeme.io connects to Stripe, Apple Pay, PayPal, Razorpay, Flutterwave, Mercado Pago, Xendit and cash on delivery, with no percentage taken. If you are already on Kajabi, Systeme.io advertises free migration.</p>
<h2>Which one should you choose?</h2>
<p><b>Choose Systeme.io if</b> you are launching your first course, want to keep costs low, or have a small or medium audience. You get courses, funnels, emails and automations for a fraction of the price.</p>
<p><b>Choose Kajabi if</b> you already run a large business, have a comfortable budget and need many admins.</p>
<h2>Verdict</h2>
<div class="tip">Kajabi is a good platform, but at $179 per month minimum and with no free plan, it is mainly for established businesses. Systeme.io covers the same basics from $0, takes no percentage of your sales and stays cheaper even on its unlimited plan. For most course creators, Systeme.io is the better choice.</div>
{cta("Create your first course for free with Systeme.io.")}
""", faq=[
 ("Is Systeme.io cheaper than Kajabi?", "Yes, by far. Systeme.io has a free plan and paid plans from $17 to $97 per month. Kajabi starts at $179 per month ($143 billed yearly)."),
 ("Does Kajabi have a free plan?", "No. Kajabi offers a 14-day free trial and a 30-day money-back guarantee."),
 ("Does Kajabi take a commission?", "Kajabi takes no revenue share, but charges card fees through Kajabi Payments, or extra fees if you use another payment processor."),
 ("Which is better to sell a course?", "To start out or keep costs low, Systeme.io. Kajabi mostly suits large businesses with a comfortable budget."),
])
