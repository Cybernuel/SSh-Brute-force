
# 🔓 SSH Brute Forcer – BlackVault-SSHForce

A Python-based SSH brute-force tool designed to simulate password-guessing attacks on SSH-enabled systems for educational and ethical hacking purposes.

> ⚠️ For educational use only. Do **not** use this tool on systems you don’t own or have explicit permission to test.

---

## 💡 Features

- Multi-attempt SSH login using username:password combinations
- Logs successful credentials to a file
- Handles timeouts, bad auth, and SSH connection errors
- Clean CLI interface
- Supports custom wordlists
- Easy to extend with threading or `argparse` options

---

## 📸 Screenshots

![demo.gif](demo.gif) <!-- Replace with your own GIF if needed -->
![Screenshot 2025-07-04 041556](https://github.com/user-attachments/assets/2a336f0d-4ae9-4a4d-914d-d982d5a04218)
![Screenshot 2025-07-04 042021](https://github.com/user-attachments/assets/514804f9-3844-4bf7-8eff-76c060aab69b)
![Screenshot 2025-07-04 041755](https://github.com/user-attachments/assets/714f27e6-7b95-4f39-88fa-c6cb24e029f3)

---

## 🛠️ Usage

### 1. Clone the repo

```bash
git clone https://github.com/your-username/BlackVault-SSHForce.git
cd BlackVault-SSHForce
````

### 2. Install dependencies

```bash
pip install paramiko
```

### 3. Prepare your `wordlist.txt`

Format:

```
username:password
admin:123456
root:toor
```

You can generate combo lists using `combine_users_passwords.py`.

### 4. Run the script

```bash
python ssh_force.py
```

Enter the target IP when prompted, and let it run.

---

## 🧪 Testing Environment

* TryHackMe / Hack The Box VM (with SSH enabled)
* Local VM or server with known credentials for ethical testing

---

## 🧠 Educational Goals

This project helps understand:

* How brute-force attacks are carried out
* SSH security configurations and risks
* Why rate limiting, key-based auth, and strong passwords are essential

---

## 📁 File Structure

```
SSHForce/
├── ssh_force.py              # Main brute force script
├── wordlist.txt              # Username:password combos
├── combine_users_passwords.py  # Optional combo generator
├── successful_logins.txt     # Auto-created if a login is successful
```

---

## 🚧 Future Improvements

* Threaded brute-forcing for speed
* `argparse` for CLI options
* Rich terminal UI with progress bar


---

## 📚 Disclaimer

This tool is intended for **educational and authorized penetration testing only**.
The developer is **not responsible for misuse**. Always obtain written permission before testing any system.

---

## ✍️ Author

**Cybernuel**
[LinkedIn](https://www.linkedin.com/in) • [GitHub](https://github.com/Cybernuel)
 #Cybersecurity | #PythonHacks

---

## 🔗 License

MIT License – Free to use and modify with proper credit.

```

