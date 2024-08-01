import wikipedia

def process_command(command):
    try:
        if 'what ' in command:
            info = wikipedia.summary(command, sentences=2)
            print(info)  
        else:
            print("Please rephrase the question.")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Multiple results found: {e.options}")
    except wikipedia.exceptions.PageError:
        print("No page found for the given query.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    while True:
        command = input("what is your question: ")
        if command.lower() in ["exit", "quit"]:
            break
        print()
        process_command(command)
        print()
        

if _name_ == "_main_":
    main()
