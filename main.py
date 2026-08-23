from coding_agent import Agent
import os

def main():

    agent = Agent(os.getcwd())

    while True:

        prompt = input("> ")

        if prompt.lower() in {"exit", "quit"}:
            break

        print(agent.run(prompt))

if __name__ == "__main__":
    main()