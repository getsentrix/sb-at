# AltStore Source for SceneBox

Custom AltStore / SideStore repository for [SceneBox](https://github.com/donbytyqi/scenebox), a media player for iPhone, iPad, Apple TV, and Mac that streams releases from Stremio-compatible sources, downloads for offline, and keeps your progress in sync.

<p align="center">
  <img src="LOGO.jpg" alt="SceneBox Logo" width="120" style="border-radius: 24px;" />
</p>

---

## 🔗 Repository URL

Copy and paste this URL into your sideloading app:

```text
https://getsentrix.github.io/sb-at/apps.json
```

*(Raw fallback URL: `https://raw.githubusercontent.com/getsentrix/sb-at/main/apps.json`)*

---

## 📲 How to Add

### SideStore / AltStore
1. Open **SideStore** or **AltStore**.
2. Navigate to the **Sources** tab.
3. Tap the **+** (Add) button in the top corner.
4. Paste the URL: `https://getsentrix.github.io/sb-at/apps.json`
5. Tap **Add**. SceneBox will now appear in your browse/source list with automatic update notifications!

### LiveContainer
1. Open **LiveContainer**.
2. Go to the **Sources** tab.
3. Tap **+** and paste: `https://getsentrix.github.io/sb-at/apps.json`
*(Or tap "Add to LiveContainer" directly from the [web page](https://getsentrix.github.io/sb-at/))*

### Feather / ESign / Scarlet
1. Open the app and go to **Sources / Repositories**.
2. Tap **Add Source**.
3. Paste `https://getsentrix.github.io/sb-at/apps.json` and confirm.

---

## ⚙️ How It Works

This repository automatically stays up to date with official releases:
- A GitHub Actions workflow runs every 12 hours (and can be triggered manually).
- It queries the official upstream repository ([donbytyqi/scenebox](https://github.com/donbytyqi/scenebox)) via GitHub API for new releases.
- When a new version with an iOS `.ipa` is published, it updates `apps.json` with the new version number, download link, release notes, and file size.

---

## 📜 Credits

- [donbytyqi/scenebox](https://github.com/donbytyqi/scenebox) - Developer of SceneBox
- [AltStore](https://altstore.io/) - Sideloading platform & source specifications
