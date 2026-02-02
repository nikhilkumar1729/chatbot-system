from chatbot import ChatBot
from colorama import Fore, Style, init

# Initialize colors for the terminal
init(autoreset=True)

def main():
    bot = ChatBot()
    print(f"{Fore.CYAN}🤖 Chatbot initialized! Type 'exit' or 'quit' to stop.{Style.RESET_ALL}")
    
    while True:
        user_input = input(f"{Fore.GREEN}You: {Style.RESET_ALL}")
        
        if user_input.lower() in ["exit", "quit"]:
            print(f"{Fore.YELLOW}Goodbye!")
            break
            
        if not user_input.strip():
            continue

        response = bot.get_response(user_input)
        print(f"{Fore.MAGENTA}Bot: {Style.RESET_ALL}{response}\n")

if __name__ == "__main__":
    main()
