# Compliance Snapshot · Doc d'exploitation

## 1. Pitch produit
- Audit flash (72 h) couvrant gouvernance, privacy, sécurité, juridique.
- Livrable : score, matrice risques, backlog d'actions, Q&A room 30 jours.
- CTA : email vers partner + paiement direct Stripe (12 k€ HT par défaut).

## 2. Architecture
- Site statique (HTML/CSS/JS) hébergé sur Netlify (`publish = site`).
- Formulaire acquisition Netlify (`data-netlify="true"`). Les leads arrivent dans l'onglet « Forms » de Netlify + notif email si activée.
- Blog statique (3 articles initiaux), liens vers ressources Notion (placeholder).
- Script de scoring partagé :
  - Front : `site/assets/js/scoring.js` (export CommonJS pour ré-usage Node).
  - Ops : `scripts/compliance_scoring.py` (CLI).

## 3. Contenu dynamique à maintenir
- Mentions CTA : `ops@compliancesnapshot.studio` + lien Stripe. Chercher `buy.stripe.com` dans le repo pour remplacer par votre lien live.
- Blog : éditer les fichiers HTML sous `site/blog/`. Ajoutez un nouvel article via `cp site/blog/template.html site/blog/slug.html` puis liez-le depuis `site/blog/index.html`.
- Acquisition : formulaire Netlify prêt à connecter à Zapier/HubSpot via Webhooks.

## 4. Netlify
- `netlify init` dans `compliance-snapshot/` si le dossier n'est pas encore lié.
- Commandes :
  - `netlify deploy --dir=site` → URL preview
  - `netlify deploy --dir=site --prod` → mise en prod
- Variables d'env possibles :
  - `FORMS_NOTIFICATION_EMAIL` si vous utilisez un service tiers (sinon Netlify par défaut).
  - `STRIPE_PAYMENT_URL` si vous décidez de templatiser le bouton (ajouter script pour remplacement au build).

## 5. Tracking & SEO
- Balises `meta` prêtes pour description.
- Ajouter votre snippet analytics (Plausible, Fathom…) dans `site/index.html` juste avant `</body>`.
- Fichiers supplémentaires possibles : `robots.txt`, `sitemap.xml` (non nécessaire pour MVP).

## 6. Roadmap future
- Ajouter un mode sombre/clair automatique (actuellement dark par défaut).
- Injecter des témoignages dynamiques via JSON.
- Connecter le scoring à Airtable/Notion pour historiser les instantanés envoyés aux prospects.

## 7. Support
- Owner contenu : Mr DOMEC
- Owner technique : Orion (AI consigliere)
- SLA mise à jour : 24h
