import os

from coding_agent import Agent


def main():

    workspace = os.getcwd()

    print("================================")
    print("       CODING AGENT")
    print("================================")
    print()
    print(f"Workspace: {workspace}")
    print()
    print("Type your request.")
    print("Type 'exit' to quit.")
    print()

    agent = Agent(workspace)

    while True:

        try:
            prompt = input("> ")

        except KeyboardInterrupt:
            print("\nExiting...")
            break

        if not prompt.strip():
            continue

        if prompt.lower() in {"exit", "quit"}:
            print("Goodbye.")
            break

        print("\nAgent working...\n")

        try:
            result = agent.run(prompt)
            print("\n")
            print(result)
            print()

        except Exception as e:
            print(f"\nAgent error: {e}\n")


if __name__ == "__main__":
    main()