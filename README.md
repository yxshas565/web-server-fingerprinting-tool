# 🌐 Web Server Fingerprinting Tool

### 🔐 Secure Multi-Client Banner Grabbing using Socket Programming

---

## 📖 Project Overview

This project implements a **Web Server Fingerprinting Tool** to identify server type and version by analyzing service banners using socket communication.

It uses **secure SSL/TLS-based client-server communication**, performs **HTTP/HTTPS banner grabbing**, and extracts server details such as protocol, port, server type, and version.

---

## 🎯 Problem Statement

Develop a tool to identify web server type and version by analyzing service banners using socket communication.

---

## 🚀 Key Functionalities

* HTTP/HTTPS banner grabbing
* Service identification (server type & version)
* Multi-server testing
* SSL/TLS secure communication
* Accuracy evaluation

---

## 🏗️ Architecture

```
Client(s) → SSL → Server → Banner Grabbing → Service Detection → Response
```

---

## ⚙️ Technologies Used

* Python
* Socket Programming
* SSL/TLS
* Multithreading

---

## 🚀 Features

* Secure communication using SSL/TLS
* Multi-client support
* HTTP/HTTPS detection
* Banner extraction
* Version detection

---

## 📂 Files

* `server.py`
* `client.py`
* `cert.pem`
* `key.pem`

---

## ▶️ How to Run

```bash
To run the tool, open a terminal in the project folder. First, start the server by running python server.py. Then open another terminal and run python client.py. In the client program, enter the target website name when prompted (for example, google.com). The tool will connect to the server and display the detected web server type and version.
```

---

## 👥 Team Details

**Team No:** 10
**Project No:** 7

### Members:

**Yashas Sadananda**
SRN: PES2UG24CS610
Github : yxshas565
Email: [yxshas565@gmail.com](mailto:yxshas565@gmail.com)

---

**Vishwas H**
SRN: PES2UG24CS596
GitHub: Vishwas-H-sys
Email: [Vishwashosamath47@gmail.com](mailto:Vishwashosamath47@gmail.com)

---

**Thejaswi S**
SRN: PES2UG24CS562
GitHub: RockingThej
Email: [thejubhat2006@gmail.com](mailto:thejubhat2006@gmail.com)

---

## 🧠 Contributions

### Yashas Sadananda

* System architecture design
* SSL/TLS server implementation
* Multi-threaded client handling
* Core socket programming

### Vishwas H

* Client-side implementation
* Input handling and communication logic
* Testing and debugging

### Thejaswi S

* Banner grabbing logic
* Server & version detection
* Performance testing and error handling

---

## 📌 Conclusion

This project demonstrates secure socket communication, concurrency, and real-world server fingerprinting using low-level networking concepts.

---
