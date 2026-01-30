import csv
import pickle
import json
import os


# TXT
def write_txt(file_path: str, data: str):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(data)


def read_txt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def readlines_txt(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as f:
        return f.readlines()
    
def append_txt(file_path: str, data: str):
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(data)


# CSV
def write_csv(file_path: str, rows: list):
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def read_csv(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        return list(reader)

def append_csv(file_path: str, rows: list):
    with open(file_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


# BIN
def write_bin(file_path: str, data):
    with open(file_path, "wb") as f:
        pickle.dump(data, f)


def read_bin(file_path: str):
    with open(file_path, "rb") as f:
        return pickle.load(f)
    
#JSON
def write_json(file_path: str, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f)

def read_json(file_path: str):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)


#SOME COMMON NECESSARY FUNCTIONS

def exists(file_path: str) -> bool:
    return os.path.exists(file_path)

def delete(file_path: str):
    os.remove(file_path)

def file_size(file_path: str)  -> int:
    return os.path.getsize(file_path)

def get_extension(file_path: str) -> str:
    return os.path.splitext(file_path)[1].lower()