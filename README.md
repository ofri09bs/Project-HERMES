# Steganography & Cryptography Framework

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Security](https://img.shields.io/badge/Encryption-AES--128-green.svg)
![Technique](https://img.shields.io/badge/Steganography-LSB-orange.svg)

> **⚠️ EDUCATIONAL USE ONLY**
>
> This tool was developed for cyber security research and learning purposes.
> It demonstrates data hiding techniques and binary manipulation.

---

## 📖 Overview

**Project HERMES** is a stealth communication tool that allows users to hide encrypted secret messages inside innocent-looking images.
Unlike standard encryption which creates suspicious "gibberish" files, HERMES uses **Steganography** to ensure that the existence of the message is known only to the sender and the receiver.

The tool modifies the **Least Significant Bits (LSB)** of the image pixels, making the alterations invisible to the human eye.

---

## ⚙️ Key Features

* **🖼️ LSB Steganography:** Injects binary data directly into the RGB channels of PNG images without altering their visual appearance.
* **🔐 Military-Grade Encryption:** Before embedding, messages are encrypted using **AES-128 (CBC/ECB)**. Even if the hidden bits are extracted, they cannot be read without the password.
* **🔑 Secure Key Derivation:** User passwords are hashed using **SHA-256** to generate secure encryption keys.
* **🛠️ Modular Design:** Built with separate modules for binary processing, crypto operations, and image manipulation.

---

## 🛠️ Technical Architecture

The project consists of four main modules:

```text
📦 Project HERMES
 ┣ 📜 main_hermes.py       # The Interface (CLI): Manages user input and flow.
 ┣ 📜 stego_engine.py      # The Engine: Handles Image I/O and LSB manipulation (Pillow).
 ┣ 📜 crypto_module.py     # The Vault: Handles AES encryption/decryption.
 ┗ 📜 text_processing.py   # The Translator: Converts Text <-> Binary strings.

```
---

## The Process (Pipeline)

**1. Input:** User provides a message ("Hello") and a Password ("1234").

**2. Encryption:** Message is encrypted via AES -> U2FsdGVkX1...

**3. Binary Conversion:** Encrypted string is converted to bits -> 010101...

**4. Embedding:** Bits are injected into the LSB of the image pixels.

**Output:** A new PNG image is generated. Visual difference: 0%.

---

## 🔜 Roadmap (Future Updates)
**[ ] Graphical User Interface (GUI):** A full visual interface using tkinter.

**[ ] Drag & Drop Support:** Easier file handling.

**[ ] Capacity Indicator:** Visual bar showing how much data can fit in the image.

**[ ] File Embedding:** Ability to hide full files (PDF/ZIP) inside images, not just text.
