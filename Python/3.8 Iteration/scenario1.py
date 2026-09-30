print("you walk inside a forest,")
print("but wait! you hear a sound...\n")

while True:
    choice = input("what do you do? ('run' OR 'fight') ").lower().strip()

    if choice == "run":
        print("you're a coward Smh")
        break
    elif choice == "fight":
        print("wow, you're brave!")
        break
    # w raise keyword
    else:
        err = "dude"
        raise Exception(err)  # noqa: TRY002

print("End of story!")