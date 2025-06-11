# 🔐 Modular Caesar Cipher

This project implements a **modular Caesar cipher** for encoding and decoding English alphabetic messages. It's structured in a clean, maintainable folder-based architecture using Python functions and modules.

---

## 📁 Project Structure

```
CaesarCipherProject/
├── main.py                         # Main runner script
├── Variables/
│   └── main.py                     # Contains shared constants (alphabets, delimiter)
├── Tokenizer/
│   └── main.py                     # Contains the Transfomer function
├── encoder/
│   └── encoder.py                  # Encoding logic
├── decoder/
    └── decoder.py                  # Decoding logic
```

---

## 🚀 How It Works

### 🔁 `Transfomer(input_sentence)`

* Breaks sentence into individual characters
* Converts characters into index positions in the alphabet
* Passes characters to `Encode_Message()` and indices to `Decoded_Message()`

### 🔐 `Encode_Message(each_letter)`

* Shifts each letter back by 3 positions in the alphabet
* Returns the encoded message as a string

### 🔓 `Decoded_Message(word_index_in_alphabet)`

* Adjusts negative indices (replaces them with -1, which maps to 'z')
* Reconstructs the original sentence (note: 'z' used as space)

---

## 💬 Example

```python
input_sentence = 'we are going home today'

# Output:
Encoded Message: tb xob dlfkd eljb qlabv
Decoded Message: we are going home today
```

(Note: In this version, 'z' is temporarily used to indicate spaces)

---

## 🔧 Future Improvements (Phase 2+)

* Fix space handling more cleanly without using 'z'
* Support upper/lower case properly
* Handle non-alphabetic characters
* Create CLI or GUI wrapper
* Write unit tests for encoding/decoding logic

---

## 📦 Requirements

* Python 3+

---

## ⚖️ License

MIT License — free to use and modify.

---

## 👤 Author

* GitHub: obirikan

> "Encryption teaches us the power of shifting perspective—literally and logically."
