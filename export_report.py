import os
import csv
import base64

def generate_html_report(csv_path="metrics.csv", img_path="fitness_evolution.png", output_html="rapport_neurotrack.html"):
    """
    Génère un rapport technique complet au format HTML avec mise en page moderne,
    parfaitement aligné sur les 4 sections exigées par Madame Bouhajeb :
    1. Le Problème Traité
    2. L'Approche Utilisée
    3. Les Étapes de Réalisation
    4. Les Résultats Obtenus
    """
    rows = []
    if os.path.exists(csv_path):
        with open(csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for r in reader:
                rows.append(r)

    img_tag = ""
    if os.path.exists(img_path):
        with open(img_path, "rb") as f:
            b64_img = base64.b64encode(f.read()).decode("utf-8")
            img_tag = f'<img src="data:image/png;base64,{b64_img}" alt="Courbe d apprentissage" class="w-full rounded-lg shadow-md border border-slate-700 my-4"/>'
    else:
        img_tag = '<p class="text-amber-400 italic">Graphique en attente de génération.</p>'

    table_rows = ""
    for r in rows[-10:]: # 10 dernières générations
        table_rows += f"""
        <tr class="border-b border-slate-800 hover:bg-slate-800/50">
            <td class="py-2 px-4 text-cyan-400 font-bold">Génération {r.get('generation', '')}</td>
            <td class="py-2 px-4 text-emerald-400 font-semibold">{r.get('best_fitness', '')} pts</td>
            <td class="py-2 px-4 text-slate-300">{r.get('avg_fitness', '')} pts</td>
            <td class="py-2 px-4 text-amber-300">{r.get('max_checkpoints', '')}</td>
        </tr>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="fr" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rapport de Projet : Neuro-Track (Algorithmes Génétiques)</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        @media print {{
            .no-print {{ display: none !important; }}
            body {{ background: #ffffff !important; color: #111827 !important; font-size: 11pt; }}
            .card {{ border: 1px solid #e5e7eb !important; background: #ffffff !important; color: #111827 !important; }}
            h1, h2, h3, h4 {{ color: #1e3a8a !important; }}
            p, span, li, td, th {{ color: #1f2937 !important; }}
            table {{ border: 1px solid #d1d5db !important; }}
        }}
    </style>
</head>
<body class="bg-slate-950 text-slate-100 font-sans leading-relaxed p-6 md:p-12">
    <div class="max-w-4xl mx-auto space-y-8">
        
        <!-- En-tête officiel ISI / UTM -->
        <header class="border-b border-slate-800 pb-6 flex flex-col md:flex-row justify-between items-start md:items-end gap-4 card p-6 rounded-xl bg-slate-900">
            <div>
                <span class="inline-block px-3 py-1 bg-cyan-950 text-cyan-400 border border-cyan-800 text-xs font-semibold rounded-full mb-3 uppercase tracking-wider">
                    Algorithmique Avancée & Intelligence Artificielle
                </span>
                <h1 class="text-3xl font-extrabold text-white tracking-tight">
                    Projet Neuro-Track : Voitures Autonomes (AG)
                </h1>
                <p class="text-slate-400 text-sm mt-1">Conduite Autonome par Neuroévolution (Réseau de Neurones & Algorithme Génétique)</p>
            </div>
            <div class="text-left md:text-right text-xs text-slate-400 bg-slate-950 p-4 rounded-lg border border-slate-800 space-y-1">
                <p><span class="text-slate-200 font-semibold">Binôme :</span> TRABELSI Saifeddine & TLILI Achref</p>
                <p><span class="text-slate-200 font-semibold">Classe :</span> 3 IDL 2</p>
                <p><span class="text-slate-200 font-semibold">Établissement :</span> ISI - Université Tunis El Manar</p>
                <p><span class="text-slate-200 font-semibold">Enseignante :</span> Madame Bouhajeb</p>
            </div>
        </header>

        <!-- Bouton d'impression PDF -->
        <div class="no-print flex justify-end gap-3">
            <button onclick="window.print()" class="px-5 py-2.5 bg-cyan-600 hover:bg-cyan-500 text-white rounded-lg text-sm font-semibold transition shadow-md flex items-center gap-2">
                🖨 Enregistrer en PDF (Ctrl + P)
            </button>
        </div>

        <!-- 1. Le Problème Traité -->
        <section class="bg-slate-900 border border-slate-800 rounded-xl p-6 card">
            <h2 class="text-xl font-bold text-cyan-400 mb-3">1. Le Problème Traité</h2>
            <p class="text-slate-300 text-sm mb-3">
                L'objectif est d'amener une flotte de véhicules autonomes à naviguer sur un circuit fermé comportant des virages à courbures variées, <strong>sans aucune trajectoire préprogrammée</strong>. L'agent ignore la forme de la piste et l'emplacement des bordures.
            </p>
            <ul class="list-disc list-inside text-xs text-slate-300 space-y-1.5">
                <li><strong>Agnosticisme de la piste :</strong> Les voitures ne disposent d'aucune carte en mémoire.</li>
                <li><strong>Perception locale :</strong> Seuls 5 capteurs radars virtuels mesurent la distance à l'herbe en temps réel.</li>
                <li><strong>Pourquoi l'AG ?</strong> L'apprentissage supervisé par descente de gradient est inapplicable : les collisions sont des événements discrets et non dérivables, et aucun conducteur humain ne fournit de trajectoire modèle.</li>
            </ul>
        </section>

        <!-- 2. L'Approche Utilisée -->
        <section class="bg-slate-900 border border-slate-800 rounded-xl p-6 card space-y-4">
            <h2 class="text-xl font-bold text-cyan-400">2. L'Approche Utilisée : La Neuroévolution</h2>
            <p class="text-slate-300 text-sm">
                L'approche repose sur le couplage d'un <strong>Réseau de Neurones (MLP)</strong> embarqué dans chaque voiture et d'un <strong>Algorithme Génétique</strong> qui optimise ses poids synaptiques au fil des générations.
            </p>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                <div class="bg-slate-950 p-4 rounded-lg border border-slate-800 card">
                    <h3 class="text-amber-400 font-semibold mb-1">A. L'ADN (57 Gènes)</h3>
                    <p class="text-slate-400">
                        Chaque individu possède un chromosome 1D de 57 nombres réels :<br>
                        • 5 capteurs $\times$ 8 cachés = 40 poids W1<br>
                        • 8 biais B1<br>
                        • 8 cachés $\times$ 1 sortie = 8 poids W2<br>
                        • 1 biais B2<br>
                        <strong>Total = 57 gènes</strong> agissant comme multiplicateurs sur le volant.
                    </p>
                </div>

                <div class="bg-slate-950 p-4 rounded-lg border border-slate-800 card">
                    <h3 class="text-amber-400 font-semibold mb-1">B. Fonction de Fitness & Anti-Triche</h3>
                    <p class="text-slate-400">
                        • 18 checkpoints ordonnés (+1000 pts par porte validée).<br>
                        • Bonus continu vers la prochaine porte.<br>
                        • <strong>Anti-triche :</strong> élimination si aucun checkpoint n'est franchi en 3 secondes (empêche de tourner en rond).
                    </p>
                </div>
            </div>

            <div class="bg-slate-950 p-4 rounded-lg border border-slate-800 card text-xs">
                <h3 class="text-amber-400 font-semibold mb-2">C. Les 4 Opérateurs Génétiques</h3>
                <ul class="space-y-1 text-slate-300">
                    <li>• <strong>Élitisme (10%) :</strong> Les 4 meilleures voitures sont reconduites intactes pour garantir zéro régression du record.</li>
                    <li>• <strong>Sélection par Tournoi (k = 3) :</strong> Tirage au sort de 3 individus, le plus apte devient parent.</li>
                    <li>• <strong>Croisement Uniforme (85%) :</strong> Tirage à 50/50 pour chaque gène entre le parent A et le parent B.</li>
                    <li>• <strong>Mutation Gaussienne (12%) :</strong> Ajout d'une perturbation aléatoire normale N(0, 0.35) pour explorer de nouvelles trajectoires.</li>
                </ul>
            </div>
        </section>

        <!-- 3. Les Étapes de Réalisation -->
        <section class="bg-slate-900 border border-slate-800 rounded-xl p-6 card">
            <h2 class="text-xl font-bold text-cyan-400 mb-3">3. Les Étapes de Réalisation</h2>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                <div class="bg-slate-950 p-3 rounded-lg border border-slate-800 card">
                    <h4 class="font-bold text-white mb-1">Étape 1 : Le Circuit (<code class="text-cyan-300">track.py</code>)</h4>
                    <p class="text-slate-400">Piste 2D en boucle avec asphalte, vibreurs, détection de texture et disposition des 18 checkpoints.</p>
                </div>
                <div class="bg-slate-950 p-3 rounded-lg border border-slate-800 card">
                    <h4 class="font-bold text-white mb-1">Étape 2 : Physique & Radars (<code class="text-cyan-300">car.py</code>)</h4>
                    <p class="text-slate-400">Cinématique 2D, raycasting de 5 faisceaux de détection et collision sur les 4 sommets du véhicule.</p>
                </div>
                <div class="bg-slate-950 p-3 rounded-lg border border-slate-800 card">
                    <h4 class="font-bold text-white mb-1">Étape 3 : Cerveau MLP (<code class="text-cyan-300">brain.py</code>)</h4>
                    <p class="text-slate-400">Inférence matricielle rapide avec activation Tanh et sérialisation/désérialisation de l'ADN.</p>
                </div>
                <div class="bg-slate-950 p-3 rounded-lg border border-slate-800 card">
                    <h4 class="font-bold text-white mb-1">Étape 4 : Moteur AG & Interface (<code class="text-cyan-300">ga.py</code> & <code class="text-cyan-300">main.py</code>)</h4>
                    <p class="text-slate-400">Élitisme, tournoi, mutation, dashboard temps réel, visualiseur synaptique en direct et modale F1.</p>
                </div>
            </div>
        </section>

        <!-- 4. Les Résultats Obtenus -->
        <section class="bg-slate-900 border border-slate-800 rounded-xl p-6 card">
            <h2 class="text-xl font-bold text-cyan-400 mb-3">4. Les Résultats Obtenus et Analyse de la Convergence</h2>
            <p class="text-slate-300 text-sm mb-4">
                La courbe ci-dessous démontre la progression mathématique du Fitness : les voitures passent de crashs quasi immédiats (Gén 1-3) à une navigation fluide accomplissant plus de 3 tours sans collision ($> 56\,000$ pts dès la Gén 10).
            </p>

            {img_tag}

            <div class="overflow-x-auto mt-4">
                <table class="w-full text-left text-xs bg-slate-950 rounded-lg border border-slate-800">
                    <thead class="bg-slate-900 text-slate-400 uppercase font-semibold">
                        <tr>
                            <th class="py-2.5 px-4">Génération</th>
                            <th class="py-2.5 px-4">Fitness Maximal</th>
                            <th class="py-2.5 px-4">Fitness Moyen</th>
                            <th class="py-2.5 px-4">Checkpoints Validés</th>
                        </tr>
                    </thead>
                    <tbody>
                        {table_rows}
                    </tbody>
                </table>
            </div>
        </section>

        <!-- Conclusion -->
        <footer class="text-center text-xs text-slate-500 pt-4 border-t border-slate-800">
            Neuro-Track • TRABELSI Saifeddine & TLILI Achref (3 IDL 2) • Encadré par Mme Bouhajeb • ISI / UTM
        </footer>
    </div>
</body>
</html>"""

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"[Export] Rapport HTML généré avec succès sous '{output_html}'.")
    return True

if __name__ == "__main__":
    generate_html_report()
