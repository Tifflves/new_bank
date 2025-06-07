a = {
    "SAVING": [],
    "CHECKING": []
}


def accounts(value: tuple[str, int]):
    match value[0]:
        case "SAVING":
            print("saving")
            a["SAVING"].append(value[1])

        case "CHECKING":
            print("checking")
    return True

accounts(("SAVING", 1234_5678))
accounts(("SAVING", 1234_5678))
print(a)
print(a.values())
print(a["SAVING"])
