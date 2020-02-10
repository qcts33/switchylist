def main():
    head = []
    body = []
    with open("OmegaRules.sorl", "r") as fp:
        for url in fp:
            if url.startswith("*"):
                body.append(url.strip())
            else:
                head.append(url.strip())
    with open("arange.sorl", "w") as fp:
        for line in head:
            print(line, file=fp)
        for line in sorted(set(body)):
            print(line, file=fp)


if __name__ == "__main__":
    main()
