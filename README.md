# 📁 Simple File Utils

A lightweight Python library for simplified file handling operations.
It provides easy-to-use functions for working with text, CSV, JSON, and binary files.

### ✨ Features

- Read / Write / Append TXT files
- Read / Write / Append CSV files
- Read / Write JSON files
- Binary file support using pickle
- Utility helpers:
    - `exists()`
    - `delete()`
    - `file_size()`
    - `get_extension()`

---

### 📦 Installation

```bash
pip install simple-file-utils
```


### 🚀 Quickstart
```bash
import simple_file_utils as sfu
```
---

## 📄 TXT FILE FUNCTIONS

`write_txt(file_path, data)`

Writes text to a file (overwrites if it exists).

```bash
sfu.write_txt("example.txt", "Hello World")
```
---

`read_txt(file_path)`

Reads entire file content as a string.

```bash
content = sfu.read_txt("example.txt")
print(content)
```
---

`readlines_txt(file_path)`

Returns file content as a list of lines.

```bash
lines = sfu.readlines_txt("example.txt")
print(lines)
```
---

`append_txt(file_path, data)`

Appends text to an existing file.

```bash
sfu.append_txt("example.txt", "\nNew line added")
```
---

## 📊 CSV FILE FUNCTIONS
`write_csv(file_path, rows)`

Writes a list of rows to a CSV file.

```bash
rows = [
    ["Name", "Age"],
    ["John",18]
]
```

sfu.write_csv("data.csv", rows)
---

`read_csv(file_path)`

Reads CSV file and returns list of rows.

```bash
data = sfu.read_csv("data.csv")
print(data)
```
---

`append_csv(file_path, rows)`

Appends rows to an existing CSV file.

```bash
sfu.append_csv("data.csv", [["Alex", 22]])
```
---

## 🧾 JSON Functions
`write_json(file_path, data)`

Writes a dictionary or list to a JSON file.

```bash
user = {
    "name": "John",
    "age": 18
}

sfu.write_json("user.json", user)
```
---

`read_json(file_path)`

Reads JSON file and returns Python object.

```bash
data = sfu.read_json("user.json")
print(data)
```
---

## 💾 Binary Functions
`write_bin(file_path, data)`

Saves a Python object to a binary file.

```bash
numbers = [1, 2, 3, 4]
sfu.write_bin("numbers.bin", numbers)
```

`read_bin(file_path)`

Loads a Python object from a binary file.

```bash
numbers = sfu.read_bin("numbers.bin")
print(numbers)
```
---

## 🛠 Utility Functions
`exists(file_path)`

Checks if file exists.

```bash
print(sfu.exists("example.txt"))
```
---

`delete(file_path)`

Deletes a file.

```bash
sfu.delete("example.txt")
```
---

`file_size(file_path)`

Returns file size in bytes.

```bash
size = sfu.file_size("data.csv")
print(size)
```
---

`get_extension(file_path)`

Returns file extension in lowercase.

```bash
print(sfu.get_extension("data.csv"))   # .csv
```
---
## 🎯 Why Use This Library?

- Reduces repetitive file-handling boilerplate
- Beginner-friendly and easy to understand
- Clean and readable function names
- Great for small scripts and learning projects