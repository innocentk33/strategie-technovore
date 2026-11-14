// Chronomètre des tests à partir des sessions de Pi (~/.pi/agent/sessions).
// Usage : node chrono.mjs            → toutes les sessions de D:\strata-demo\*
//         node chrono.mjs jeu        → seulement les dossiers qui contiennent « jeu »
// Pi note l'heure de chaque message et la durée de chaque réponse du modèle :
// début = ta demande envoyée, fin = la dernière réponse du modèle.
import fs from "node:fs";
import os from "node:os";
import path from "node:path";

const root = path.join(os.homedir(), ".pi", "agent", "sessions");
const filtre = (process.argv[2] || "").toLowerCase();
const heure = (ms) => new Date(ms).toLocaleTimeString("fr-FR");
const duree = (ms) => {
  const s = Math.round(ms / 1000);
  return `${Math.floor(s / 60)} min ${String(s % 60).padStart(2, "0")} s`;
};
const n = (x) => x.toLocaleString("fr-FR");

const dossiers = fs.readdirSync(root).filter((d) => d.includes("strata-demo") && d.toLowerCase().includes(filtre));
if (!dossiers.length) console.log("Aucune session trouvée dans", root);

for (const d of dossiers) {
  for (const f of fs.readdirSync(path.join(root, d)).filter((x) => x.endsWith(".jsonl")).sort()) {
    const lignes = fs.readFileSync(path.join(root, d, f), "utf8").trim().split("\n").map((l) => JSON.parse(l));
    const cwd = lignes.find((e) => e.type === "session")?.cwd ?? d;
    const msgs = lignes.filter((e) => e.type === "message").map((e) => ({ ...e.message, t: Date.parse(e.timestamp) }));

    // Une « manche » par demande que tu tapes : la première, puis chaque relance.
    const manches = [];
    for (const m of msgs) {
      if (m.role === "user") manches.push({ debut: m.t, rep: [], tous: [] });
      else if (manches.length) {
        manches.at(-1).tous.push(m);
        if (m.role === "assistant") manches.at(-1).rep.push(m);
      }
    }
    // Temps perdu sur un outil qui ne rend pas la main : plus de 3 min entre un appel du modèle et son résultat
    // (souvent un navigateur que le modèle a lancé pour se tester). Ce n'est pas du travail du modèle.
    for (const s of manches) {
      s.bloque = 0;
      s.tous.forEach((m, k) => {
        const av = s.tous[k - 1];
        if (av?.role === "assistant" && m.role === "toolResult" && m.t - av.t > 180000) s.bloque += m.t - av.t;
      });
    }

    console.log(`\n${cwd}  (${f.slice(0, 19)})`);
    manches.forEach((s, i) => {
      if (!s.rep.length) return console.log(`  ${i ? `relance ${i}` : "demande"} : pas de réponse`);
      const fin = Math.max(...s.rep.map((r) => r.t));
      const tModele = s.rep.reduce((a, r) => a + (r.durationMs || 0), 0);
      const sortie = s.rep.reduce((a, r) => a + (r.usage?.output || 0), 0);
      const lus = s.rep.reduce((a, r) => a + (r.usage?.input || 0), 0);
      const repris = s.rep.reduce((a, r) => a + (r.usage?.cacheRead || 0), 0);
      const dernier = s.rep.at(-1);
      // Fichiers vraiment écrits ou modifiés (outils write/edit de Pi), pas ceux que le modèle dit avoir écrits.
      const ecrits = s.rep.flatMap((r) => (Array.isArray(r.content) ? r.content : []))
        .filter((p) => p.type === "toolCall" && (p.name === "write" || p.name === "edit"))
        .map((p) => `${p.name} ${path.basename(p.arguments?.path ?? "?")}`);
      console.log(
        `  ${i ? `relance ${i}` : "demande"} : ${heure(s.debut)} → ${heure(fin)}  =  ${duree(fin - s.debut)}` +
          `  |  ${s.rep.length} requêtes, ${n(sortie)} tokens écrits (≈ ${(sortie / (tModele / 1000)).toFixed(1)} tok/s, lecture comprise)` +
          `  |  ${n(lus)} tokens lus, ${n(repris)} repris du cache` +
          `  |  fin : ${dernier.stopReason}${dernier.stopReason === "stop" ? "" : "  ⚠️ pas terminé normalement"}` +
          `\n             fichiers : ${ecrits.length ? ecrits.join(", ") : "⚠️ aucun fichier écrit"}` +
          (s.bloque ? `\n             ⏸ bloqué ${duree(s.bloque)} sur un outil qui ne rendait pas la main (compris dans la durée)` : "")
      );
    });
    const faites = manches.filter((s) => s.rep.length);
    if (faites.length > 1) {
      const fin = Math.max(...faites.flatMap((s) => s.rep.map((r) => r.t)));
      const tModele = faites.reduce((a, s) => a + s.rep.reduce((b, r) => b + (r.durationMs || 0), 0), 0);
      const sortie = faites.reduce((a, s) => a + s.rep.reduce((b, r) => b + (r.usage?.output || 0), 0), 0);
      const bloque = faites.reduce((a, s) => a + s.bloque, 0);
      console.log(
        `  TOTAL : ${heure(faites[0].debut)} → ${heure(fin)}  =  ${duree(fin - faites[0].debut)} à l'horloge` +
          ` (dont ${duree(tModele)} de travail du modèle${bloque ? `, ${duree(bloque)} bloqué sur un outil` : ""})  |  ${n(sortie)} tokens écrits`
      );
    }
  }
}
