import zipfile, json, sys
raw, orig_manifest, out = sys.argv[1:4]
restore = {1261726, 976014, 1395542, 1285600, 959184}
orig = json.load(open(orig_manifest))
zin = zipfile.ZipFile(raw)
m = json.loads(zin.read("manifest.json"))
have = {f["projectID"] for f in m["files"]}
m["files"] += [f for f in orig["files"] if f["projectID"] in restore and f["projectID"] not in have]
m["author"] = "motanu8008"
with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
    for item in zin.infolist():
        if item.filename.startswith("overrides/mods/") or item.filename == "manifest.json":
            continue
        zout.writestr(item, zin.read(item.filename))
    zout.writestr("manifest.json", json.dumps(m, indent=2))
a = {(f["projectID"], f["fileID"]) for f in m["files"]}
b = {(f["projectID"], f["fileID"]) for f in orig["files"]}
print(len(m["files"]), "files; identical to original manifest:", a == b, "| missing:", b - a, "| extra:", a - b)
