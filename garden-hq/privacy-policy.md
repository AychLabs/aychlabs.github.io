---
layout: policy
app: Garden HQ
slug: garden-hq
doc: privacy-policy
effective: 2026-10-03
updated: 2026-10-03
contact: support@aychlabs.com
coppa: false
accent: "#3F6B3A"
---

Garden HQ is a plant-tracking and garden-care app developed by Aych Labs ("we", "us"). This policy explains what Garden HQ stores, why, where, who else handles it, and how to have it deleted. Using Garden HQ is also subject to the [Aych Labs Terms of Service](/legal/terms-of-service/).

> **The short version:** Garden HQ stores your gardens and plants so the app works across reinstalls and phones. No ads, no analytics, no tracking, and we never sell your data. Photos you take of your plants stay on your phone. Garden HQ has no AI features yet; if we add them, this policy will say what they send and where before they're turned on.

## Information We Collect

### Your account

When you first open Garden HQ, it creates an **anonymous account**: a random account ID, with no name, email address or phone number. It's what lets your gardens belong to you.

If you choose **Back up with Google** (or **Restore from Google**), your anonymous account is linked to your Google account. We then also store your **Google email address and display name**, received from Google when you sign in, so the app can show "Backed up as …" and so you can get your gardens back on a new phone. We don't get your Google password or access to anything else in your Google account.

### Your gardens (stored in the cloud)

Everything you enter about your gardens is stored in Google's Firebase Cloud Firestore database, in the United States (Google Cloud region us-east1, South Carolina):

- **Gardens:** the name you give each garden, its **ZIP code** if you enter one, its USDA hardiness zone, and which reminder types are on. The ZIP code is used only to look up the garden's hardiness zone, and is kept so the zone can be checked again if the hardiness zone map is updated. The lookup happens on your phone, from data built into the app. Entering a ZIP code is optional: you can pick a zone instead.
- **Plants in your gardens:** which plant it is, any nickname, planted date, location text (for example "Raised bed 2"), ground or pot, notes, its status (growing, harvested, removed, didn't make it) and its reminder settings.
- **Care history:** each time you mark a reminder done: which reminder, which plant, and the date.
- **Custom plants** you add that aren't in the built-in catalog: name, scientific name, category, whether it's edible, and notes.
- **Photo records:** for each photo, where the image file is kept on your phone, its caption, and when it was taken. **The photo itself is not uploaded.**

### Information collected automatically

When Garden HQ signs you in, Firebase Authentication receives your **IP address** and basic technical information (the Firebase SDK version and platform), which Google uses for security and to prevent abuse during sign-up and sign-in. See Third-Party Services below.

### On your phone only

- **Photos.** When you add a photo, Garden HQ saves a resized copy in its own private storage on your phone. The copy keeps the date the photo was taken but **removes everything else in the photo's metadata, including its location**.
- **Settings**, such as your daily reminder time and which garden is open.
- **Reminders.** Notifications are scheduled on your phone; we don't send them from a server.
- A copy of your garden data, so the app works offline.

### What we don't collect

Garden HQ doesn't use your phone's location (GPS), contacts, microphone or other apps. It uses the camera only when you tap **Take photo** (through your phone's camera app), and it sees only the photos you pick in your phone's photo picker. It has no advertising, analytics or crash-reporting services.

## How We Use Information

We use your information only to run Garden HQ for you:

- to show your gardens, plants and care history;
- to work out your reminders and schedule them on your phone;
- to look up your garden's hardiness zone from its ZIP code;
- to keep your data when you reinstall the app or change phones, if you've backed up with Google;
- to keep the service secure and prevent abuse (Firebase Authentication's use of your IP address);
- to answer you when you contact us, including deletion requests.

We don't use your information for advertising, and we don't build profiles of you.

## How We Share Information

**We never sell your data**, and we don't rent it or share it for advertising. Your data is handled only by the service providers listed under Third-Party Services, which process it on our behalf to run the app. We may disclose information if the law requires us to.

## Third-Party Services

Garden HQ uses these Google services. Each receives only what's listed here.

| Service | Provided by | What it receives |
|---|---|---|
| **Firebase Authentication** | Google | Your account ID; your **IP address**, which it collects for security and abuse prevention during sign-up and sign-in; technical information (Firebase SDK version, platform, and our app's Firebase ID); and, only if you back up with Google, the sign-in token from Google and your Google email address and display name. |
| **Cloud Firestore** (Firebase) | Google | The garden information listed above under "Your gardens", with your account ID, and technical information (Firebase SDK version and platform). Stored in us-east1, United States. |
| **Sign in with Google** (Android Credential Manager and Google Play services) | Google | Used only when you tap **Back up with Google** or **Restore from Google**: shows Google's account picker on your phone and gives Garden HQ a sign-in token, which the app passes only to Firebase Authentication. |

Firebase Authentication can also use Google's reCAPTCHA and Play Integrity services to protect sign-in from abuse; when it does, they receive information about your device and app to check that requests are genuine. Google's privacy policy: [policies.google.com/privacy](https://policies.google.com/privacy). Firebase's privacy and security information: [firebase.google.com/support/privacy](https://firebase.google.com/support/privacy).

Garden HQ's photo picker, camera, notifications, settings storage and built-in plant catalog run entirely on your phone and send nothing to anyone.

## Data Retention

- **Your account and garden data:** kept until you delete it or ask us to delete your account.
- **Database backups:** deleted data can remain in our database's automatic backups for up to **7 days**, then it's gone.
- **Deletion requests:** we delete your account, or the data you asked about, within **30 days** of your request. We keep a record of the request (its date and your account ID, none of your garden data) for **12 months** to show it was fulfilled.
- **Photos:** stay on your phone until you delete them in the app or uninstall Garden HQ.

If you never back up with Google and then uninstall the app, your anonymous account can't be opened again, but its data stays stored until you ask us to delete it. We can find it by its account ID (shown in **Settings → Request account deletion**).

## Data Security

Your data travels encrypted (HTTPS) and is stored by Google in Firebase. Our database's security rules let each account read and change only its own gardens. Photos are kept in Garden HQ's private storage on your phone.

**Android backup and photos:** Garden HQ keeps all of its data out of Android's cloud backup (to Google Drive), and photos aren't part of your Google backup in this version. The one exception: if you move to a new phone with Android's phone-to-phone transfer (by cable or directly between the phones), your photos can go with you; nothing else from Garden HQ does. Otherwise, if you uninstall the app or lose your phone, your photos are gone.

## Your Rights and Choices

- **See and change your data:** almost everything Garden HQ stores is shown in the app, and you can edit it there.
- **Delete photos:** open a photo in the app and tap **Delete**.
- **Delete your account or specific data:** in the app, go to **Settings → Request account deletion**, or follow the steps on our [account deletion page](/garden-hq/delete-account/). It explains what's deleted, what's kept, and how long it takes.
- **Back up with Google is optional.** Without it, Garden HQ works with an anonymous account only.
- **ZIP code is optional.** You can pick your garden's hardiness zone instead.
- **Notifications** can be turned off at any time in your phone's settings.

Depending on where you live, you may have the right to access, correct, export or delete your data. To ask about any of these, email **support@aychlabs.com**.

## Children's Privacy

Garden HQ is not directed to children under 13, and we don't knowingly collect personal information from children under 13. If you believe a child under 13 has given us personal information, email **support@aychlabs.com** and we'll delete it.

## Changes to This Policy

If we change this policy, we'll update the "updated" date on this page. Before a change that affects data you've already given us (for example, when photo backup or AI features arrive), we'll tell you in the app.

## Contact Us

Questions about this policy or your data: **support@aychlabs.com** (Aych Labs).
