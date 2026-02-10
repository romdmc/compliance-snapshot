# Compliance Snapshot

Site marketing, blog et page acquisition pour l'offre d'audit flash compliance, avec scoring interactif, CTA email/Stripe et script de calcul partageable.

## Contenu

- `site/`
  - `index.html` : landing principale
  - `blog/` : index + 3 articles
  - `acquisition/` : funnel orienté levée de fonds avec formulaire Netlify
  - `assets/js/scoring.js` : algorithme de calcul du score
  - `assets/css/styles.css` : système visuel
- `scripts/compliance_scoring.py` : CLI pour rejouer le scoring côté ops
- `netlify.toml` : configuration de déploiement (serveur statique)

## Développement local

```bash
cd compliance-snapshot
python3 -m http.server --directory site 4000
# ou
npx serve site
```

Le script de scoring peut être testé isolément :

```bash
python3 scripts/compliance_scoring.py --region eu --industry saas --customers 150 --incidents 1 --policies full
```

## Contact / CTA

- Bouton email → `ops@compliancesnapshot.studio`
- Bouton paiement → lien Stripe placeholder (test). Remplacer l'URL dans `site/index.html` et `site/acquisition/index.html` par votre Payment Link live.

## Déploiement

```
netlify deploy --dir=site        # preview
netlify deploy --dir=site --prod # production
```

Voir `OPERATIONS.md` pour la fiche d'exploitation complète (Netlify, contenu, scoring, analytics).
