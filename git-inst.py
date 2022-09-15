
class helper:
    def __init__(self):
        print("Hi, this a git helper, it will tell you with the steps to initialize git for your project")
        print("Start by using the command git init in the directory desire")
        siguiente = input("type next to continue with instructions\n")
        while siguiente:
            if siguiente == "next":
                print("great!, now if this is your first time using git configure your user email"
                    " with the following command git config --global user.email 'youremail@example'")
                break
            else:
                while siguiente != "next":
                    siguiente = input("type next to continue with instructions\n")


a=helper()

if __name__ == '__main__':
    a