# MillenaireCobblemon

Minecraft 1.21.1 · NeoForge 21.1.265 · packwiz

Pack URL: `https://raw.githubusercontent.com/motanu8008/millenaire-cobblemon-pack/main/pack.toml`

- **Server** (Pterodactyl, egg "NeoForge + packwiz"): set `PACKWIZ_URL` to the URL above. Mods sync on every start; client-only mods are skipped.
- **Players** (Prism Launcher): import the `MillenaireCobblemon-Prism.zip` instance. Mods sync every time the game starts.

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
