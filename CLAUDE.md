@AGENTS.md

## Propre à Claude Code

Les consignes du dépôt sont dans `AGENTS.md` (importé ci-dessus) : modifie-les là, pas ici.

- Les règles de `.claude/rules/` se chargent seules quand tu ouvres un fichier qui correspond à leur en-tête `paths:` ; la table de `AGENTS.md` (« quel fichier lire selon ce que tu touches ») ne sert qu'aux autres agents.
- Les skills du projet (`.claude/skills/`) se lancent avec l'outil `Skill` (`montage`, `upload`, `radar`, `miniature-kai`). Les sous-agents et le pipeline Opus / Sonnet du skill `montage` sont ceux de Claude Code.
- Le skill `/youtube` réellement utilisé est celui de `~/.claude/skills/` ; `claude-youtube/` n'en est qu'une copie locale (voir `AGENTS.md`).
- La mémoire automatique de Claude (`~/.claude/projects/…/memory/`) ne suit pas le dépôt : ce qui doit survivre à un changement de machine ou d'agent se range dans `AGENTS.md` ou dans un skill.
