import json
import urllib.request
from datetime import datetime

REPO = "donbytyqi/scenebox"
SOURCE_NAME = "SceneBox Community Source"
SOURCE_ID = "com.community.scenebox-source"
BUNDLE_ID = "app.scenebox.SceneBox"

url = f"https://api.github.com/repos/{REPO}/releases/latest"
req = urllib.request.Request(url, headers={"User-Agent": "AltStore-Updater"})

with urllib.request.urlopen(req) as resp:
    data = json.loads(resp.read().decode("utf-8"))

version = data.get("tag_name", "").lstrip("v")
release_date = data.get("published_at", datetime.utcnow().isoformat())
body = data.get("body", "Latest release of SceneBox.")

# Locate the .ipa asset
# Filter specifically for the iOS build (matches *.ipa and excludes tvOS)
ipa_asset = next(
    (
        a for a in data.get("assets", [])
        if a["name"].lower().endswith(".ipa") and "tvos" not in a["name"].lower()
    ),
    None,
)

if not ipa_asset:
    raise SystemExit("No iOS IPA asset found in latest release.")if not ipa_asset:
    raise SystemExit("No IPA asset found in latest release.")

ipa_url = ipa_asset["browser_download_url"]
size = ipa_asset["size"]

source_data = {
    "name": SOURCE_NAME,
    "identifier": SOURCE_ID,
    "apps": [
        {
            "name": "SceneBox",
            "bundleIdentifier": BUNDLE_ID,
            "developerName": "Don Bytyqi",
            "subtitle": "Track movies, TV shows, and anime",
            "localizedDescription": "SceneBox is an app to track your favorite movies, series, and anime.",
            "iconURL": "https://raw.githubusercontent.com/donbytyqi/scenebox/main/assets/icon.png",
            "tintColor": "FF3366",
            "version": version,
            "versionDate": release_date,
            "versionDescription": body,
            "downloadURL": ipa_url,
            "size": size
        }
    ]
}

with open("apps.json", "w", encoding="utf-8") as f:
    json.dump(source_data, f, indent=2)
