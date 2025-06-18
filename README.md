# Keyword Cipher

A simple and interactive implementation of the **Keyword Cipher**, a classical substitution cipher where a keyword determines the order of letters in the cipher alphabet.

---

## Description

The **Keyword Cipher** is a monoalphabetic cipher that builds a custom alphabet by starting with a keyword and then appending the rest of the unused letters of the standard alphabet. Each letter in the plaintext is replaced with its corresponding letter in the cipher alphabet.

This project allows encoding and decoding of text in **English or Russian** alphabets and supports interaction through a terminal interface using `prompt_toolkit`.

---

## Features

- 🔐 Encrypt or decrypt text using a keyword-based substitution cipher
- 🌐 Supports **English** and **Russian** alphabets
- 🔠 Preserves non-alphabet characters (e.g., spaces, punctuation)
- 🧠 Handles case-insensitive input
- 🧼 Prevents mixing alphabets (e.g., Russian keyword with English text)
- 💬 Simple command-line interface using `prompt_toolkit`

---

## Technologies Used

- **Python 3**
- **prompt_toolkit** (for clean CLI input)

---

## How the Keyword Cipher Works

### Step 1: Generate Cipher Alphabet

From a given keyword (e.g., `keyword`), remove any duplicate letters and append the remaining characters of the alphabet.

Example (English):
- **Keyword:** `keyword`
- **Base Alphabet:** `abcdefghijklmnopqrstuvwxyz`
- **Generated Cipher Alphabet:** `keywordabcfghijlmnpqstuvxz`

### Step 2: Encode Text

Each letter from the original text is substituted with the corresponding letter from the generated cipher alphabet.

Example:
- **Text:** `hello`
- **Cipher Alphabet:** `keywordabcfghijlmnpqstuvxz`
- **Encoded Text:** `jaddn`

### Step 3: Decode Text

To decrypt, reverse the substitution by mapping the cipher letters back to the original alphabet.

---

## Example Run

```bash
Choose mode (1 - encode, 2 - decode): 1

Choose alphabet (1 - eng, 2 - ru): 1

Input keyword: keyword

Input text: hello world

Keyword: keyword
Result: jaddn vnsdj
