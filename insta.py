from ItsAGramLive import ItsAGramLive

# live = ItsAGramLive()

username=input("Enter your username:")
password=input("Enter your password:")

live = ItsAGramLive(
    username=username,
    password=password
)

live.start()
