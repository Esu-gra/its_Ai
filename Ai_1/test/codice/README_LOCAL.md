# Lavorare senza inizializzare un repository Git

Questo progetto è configurato per non mostrare prompt di Git in VS Code. Le modifiche rimarranno locali finché non esegui comandi Git espliciti (ad esempio `git init`, `git add`, `git commit` o `git push`).

Cosa ho fatto:
- Ho disabilitato l'estensione Git in VS Code creando `.vscode/settings.json` con `git.enabled: false`.

Opzioni e passi consigliati (in italiano):

1) Lavorare senza Git (nessuna inizializzazione)

- Modifica i file normalmente e salvali: le modifiche rimangono nel filesystem locale.
- Fai backup manuali se vuoi sicurezza (esempio: copia dell'intera cartella di progetto):

```bash
# crea una copia di backup timestamped
cp -r . "../backup_$(date +%Y%m%d_%H%M%S)"
```

2) Se vuoi usare Git ma SOLO in locale (nessun remote)

- Puoi inizializzare un repository locale (opzionale) e non aggiungere remote. I commit rimarranno locali finché non imposti un remote e non esegui `git push`.

```bash
# inizializza repo locale
git init
git add .
git commit -m "Salvataggio locale"
# non aggiungere remote (o non eseguire git push)
```

3) Se vuoi rimuovere completamente ogni traccia di Git (rimuovere la cartella .git)

Attenzione: questa operazione elimina la cronologia del repository. Eseguire un backup prima se necessario.

```bash
# rimuove la cartella .git (irreversibile senza backup)
rm -rf .git
```

4) Come ripristinare il comportamento precedente di VS Code

- Per abilitare di nuovo Git in VS Code rimuovi o modifica `.vscode/settings.json` e imposta `git.enabled` su `true` oppure elimina il file.

File aggiunto in questa cartella:
- `.vscode/settings.json` — disabilita l'estensione Git di VS Code per evitare suggerimenti di inizializzazione.

Se vuoi che applichi altre modifiche (ad esempio rimuovere `.git` dal progetto o creare uno script di backup), dimmi quale opzione preferisci e la applico. Non eseguirò comandi Git o push verso remoti senza il tuo esplicito consenso.

---
Piccole note di sicurezza: non condividerò né eseguirò operazioni che inviino i tuoi file a servizi esterni senza permesso esplicito.
