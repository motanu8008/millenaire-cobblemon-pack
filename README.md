# MillenaireCobblemon

Minecraft 1.21.1 · NeoForge 21.1.265 · packwiz

Pack URL: `https://raw.githubusercontent.com/motanu8008/millenaire-cobblemon-pack/main/pack.toml`

- **Server** (Pterodactyl, egg "NeoForge + packwiz"): set `PACKWIZ_URL` to the URL above. Mods sync on every start; client-only mods are skipped.
- **Players** (Prism Launcher): *Add Instance → Import* and paste
  `https://github.com/motanu8008/millenaire-cobblemon-pack/releases/latest/download/MillenaireCobblemon-Prism.zip`.
  Mods sync every time the game starts.
- **Players** (CurseForge App): download
  [MillenaireCobblemon-CurseForge.zip](https://github.com/motanu8008/millenaire-cobblemon-pack/releases/latest/download/MillenaireCobblemon-CurseForge.zip)
  and use *Create Custom Profile → Import*. No auto-update: re-import the new zip after a pack update
  (build it with `tools/export-curseforge.sh` and attach it to a new release).

## Updating the pack

```bash
packwiz update --all     # or: packwiz update <mod>
packwiz refresh
git commit -am "Update mods" && git push
```

Restart the server; players get the update next time they launch.

## Third-party files

`mods/create-otbwg-compat-1.0.jar` is "Create: Oh The Biomes We've Gone Compat" by Blizzor, MIT licensed,
bundled here because its CurseForge project blocks third-party downloads.
