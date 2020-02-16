import copy

import fire


def build_from(file_name: str):
    head, body = load_sorl(file_name)
    wirte_sorl(head, body)


def load_sorl(file_name: str):
    head = []
    body = []
    with open(file_name) as fp:
        for url in fp:
            if url.startswith("*"):
                body.append(url.strip())
            else:
                head.append(url.strip())
    return head, body


def wirte_sorl(head, body):
    with open("arrange.sorl", "w") as fp:
        for line in head:
            print(line, file=fp)
        for line in sorted(set(body)):
            print(line, file=fp)


def merge(file_name: str):
    head, body = load_sorl("arrange.sorl")
    with open(file_name) as fp:
        new = [x.split()[0] for x in fp]
    wirte_sorl(head, body + new)


def optimize():
    head, body = load_sorl("arrange.sorl")
    copyed = copy.copy(body)
    body = list(b[1:] for b in body)
    filtered = []
    for outer, orig in zip(body, copyed):
        for inner in body:
            if outer.endswith(inner) and outer != inner:
                break
        else:
            filtered.append(orig)
    wirte_sorl(head, filtered)


if __name__ == "__main__":
    fire.Fire({"buildfrom": build_from, "merge": merge, "optimize": optimize})
