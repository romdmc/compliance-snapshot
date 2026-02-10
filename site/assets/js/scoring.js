const scoreForm = document.getElementById('scoreForm');

const weightTable = {
  region: { eu: 0, us: -5, multi: -8 },
  industry: { saas: 0, fintech: -6, health: -4, other: -2 },
  policies: { full: 8, partial: -4, light: -10 }
};

function scoreIncidents(count) {
  if (count === 0) return 6;
  if (count === 1) return 0;
  if (count <= 3) return -8;
  return -15;
}

function scoreCustomers(count) {
  if (count < 50) return 6;
  if (count < 200) return 2;
  if (count < 1000) return -4;
  return -10;
}

function computeScore(data) {
  let base = 80;
  base += weightTable.region[data.region] || 0;
  base += weightTable.industry[data.industry] || 0;
  base += weightTable.policies[data.policies] || 0;
  base += scoreIncidents(Number(data.incidents));
  base += scoreCustomers(Number(data.customers));
  return Math.max(5, Math.min(99, Math.round(base)));
}

function statusLabel(score) {
  if (score >= 85) return 'Ready pour Series B';
  if (score >= 70) return 'Maturité contrôlée';
  if (score >= 55) return 'Risque moyen, chantiers à lancer';
  return 'Zone critique, plan d’urgence requis';
}

if (scoreForm) {
  scoreForm.addEventListener('submit', (event) => {
    event.preventDefault();
    const formData = new FormData(scoreForm);
    const data = Object.fromEntries(formData.entries());
    const score = computeScore(data);
    document.getElementById('scoreValue').textContent = score;
    document.getElementById('scoreStatus').textContent = statusLabel(score);
  });
}

if (typeof module !== 'undefined') {
  module.exports = { computeScore, statusLabel };
}
