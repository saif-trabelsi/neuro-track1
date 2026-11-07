# 🏎️ Neuro-Track : Conduite Autonome par Neuroévolution

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![Pygame](https://img.shields.io/badge/Pygame-2.6-green?logo=gamepad)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Academic](https://img.shields.io/badge/Projet-Ingénierie%20Logiciel%20(3ème%20Année)-orange)

> **Projet d'Intelligence Artificielle & Algorithmique Avancée**  
> **Binôme :** Saifeddine TRABELSI & Achref TLILI  
> **Encadrante :** Madame Bouhajeb  

---

## 📌 Présentation du Projet

**Neuro-Track** est une simulation interactive en 2D où une flotte de véhicules apprend de façon totalement autonome à piloter sur un circuit fermé sans trajectoire préprogrammée.

Le système repose sur la **Neuroévolution** (couplage Réseau de Neurones + Algorithme Génétique) :
1. **Perception (Radars) :** Chaque voiture projette 5 faisceaux de détection (raycasting) mesurant en temps réel la distance aux bordures de la piste.
2. **Décision (Cerveau MLP) :** Un Perceptron Multicouche (5 entrées $\to$ 8 neurones cachés $\to$ 1 sortie de braquage) décide de la direction du véhicule.
3. **Apprentissage (AG) :** L'Algorithme Génétique remplace la descente de gradient par sélection naturelle (Élitisme, Tournoi, Croisement, Mutation) pour optimiser les poids synaptiques de génération en génération.

---

## ✨ Fonctionnalités & Valeur Ajoutée

* 🧠 **Visualiseur Neuronal en Direct :** Moniteur synaptique dans l'UI affichant en temps réel les neurones actifs et les synapses colorées du leader.
* 📈 **Courbe d'Apprentissage Temps Réel :** Graphique vectoriel dynamique intégré traçant l'évolution du Fitness maximal et moyen.
* 📄 **Rapport Intégré (Touche `F1`) :** Fenêtre modale académique en 4 onglets détaillant la théorie mathématique et exportable en **HTML/PDF**.
* ⚡ **Accélération Temporelle :** Possibilité de multiplier la vitesse de simulation jusqu'à **$16\times$** pour observer 10 générations en 15 secondes.
* 🏆 **Mode Champion Pré-entraîné :** Injection instantanée d'un modèle élite (`best_brain.json`) capable d'enchaîner plusieurs tours sans crash.

---

## 🚀 Installation & Lancement

```bash
# 1. Cloner le dépôt
git clone https://github.com/saif-trabelsi/neuro-track1.git
cd neuro-track1

# 2. Installer les dépendances
pip install pygame numpy matplotlib

# 3. Lancer la simulation interactive
python main.py
```

---

## 🎮 Commandes Interactives (Souris & Clavier)

L'ensemble des actions est cliquable directement dans le panneau latéral ou accessible via le clavier :

| Raccourci | Action | Rôle lors de la présentation |
| :--- | :--- | :--- |
| **`F1` / Clic [Rapport]** | **Ouvrir le Rapport** | Présenter les équations et la théorie à l'examinateur |
| **`ESPACE` / Clic [Pause]** | **Pause / Reprendre** | Figer l'écran pour analyser les décisions dans un virage |
| **`FLECHE HAUT` / `+`** | **Accélérer ($2\times$ à $16\times$)** | Démontrer la convergence rapide de l'algorithme |
| **`R` / Clic [Radars]** | **Mode Radars** | Masquer / Leader uniquement / Toute la flotte |
| **`L` / Clic [Charger Best]** | **Démonstration Champion** | Lancer immédiatement un parcours parfait sans risque de crash |
| **`S` / Clic [Sauver ADN]** | **Sauvegarder l'élite** | Exporter les poids dans `best_brain.json` |

---

## 🧬 Modélisation Mathématique de l'AG

| Composant | Modélisation dans le projet |
| :--- | :--- |
| **Individu** | Une instance de véhicule avec son propre cerveau artificiel. |
| **Chromosome (ADN)** | Vecteur 1D de **57 gènes réels** regroupant tous les poids et biais : $(5 \times 8) + 8 + (8 \times 1) + 1$. |
| **Fitness** | $\text{Score} = (\text{Checkpoints\_Validés} \times 1000) + \text{Progression\_vers\_le\_prochain}$. Détection anti-boucle (3s max). |
| **Élitisme** | Les **10%** meilleurs individus (4 champions) sont clonés sans mutation pour garantir la monotonie croissante du record. |
| **Sélection** | **Par Tournoi ($k=3$)** sur la moitié supérieure de la population. |
| **Croisement** | **Uniform Crossover ($P_c = 0.85$)** : chaque gène a 50% de chance d'hériter du parent A ou B. |
| **Mutation** | **Gaussienne ($P_m = 0.12$)** : perturbation stochastique $\Delta \sim \mathcal{N}(0, 0.35^2)$. |

---

## 👥 Auteurs

Projet réalisé dans le cadre du module d'IA / Algorithmique Avancée :
* **Saifeddine TRABELSI**
* **Achref TLILI**  
*Sous la supervision de **Madame Bouhajeb***.
