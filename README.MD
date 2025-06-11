# 🔐 Simple Caesar Cipher Encoder/Decoder (Python)

This is a **basic Caesar cipher project (Phase 1)** that demonstrates a simple letter-shifting encryption and decryption algorithm using Python.

---

## 🧠 How It Works

* A lowercase English alphabet string is defined.
* A word (`text`) is encoded by shifting each character **backward by 3 positions**.
* The encoded message is then decoded by **shifting forward by 3 positions**, reversing the encryption.

---

## 🧪 Sample Input & Output

```python
text = 'hello'
# Encoded: 'ebiil'
# Decoded: 'hello'
```

---

## 📁 Files

* `caesar_cipher.ipynb`: Main script for encoding and decoding

---

## 🧱 Core Logic (Phase 1)

* `alphabets = 'abcdefghijklmnopqrstuvwxyz'`
* `indexes = [alphabets.find(x) - 3 for x in text]`
* `encoded_text = [alphabets[x] for x in indexes]`
* `decoded_text = [alphabets[alphabets.find(x) + 3] for x in encoded_text]`

---

## 🚀 Planned Improvements (Phase 2+)

* Handle uppercase letters
* Wrap around alphabet for boundary letters (e.g., 'a' → 'x')
* Include punctuation and whitespace handling
* Add user input functionality (CLI or GUI)
* Write unit tests

---

## 🧩 Dependencies

* Python 3 (no external libraries required)

---

## ⚖️ License

This project is MIT licensed and open for learning, modification, and contribution.

---

## 🤝 Contributions

Feel free to fork, improve, and submit pull requests. Let’s build this into a full-featured crypto learning tool!

---

## 👤 Author

* GitHub: \[your\_username]

> "Encryption begins with the simplest ideas. This is one of them."
