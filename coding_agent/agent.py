import json

from coding_agent.model import client, MODEL

from coding_agent.prompt import SYSTEM_PROMPT

from coding_agent.tools import (
    TOOLS,
    execute_tool,
    set_workspace
)

class Agent:

    def __init__(self, workspace: str):

        self.workspace = workspace

        set_workspace(workspace)

    def run(self, prompt: str):

        set_workspace(self.workspace)

        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]

        max_iterations = 10

        for _ in range(max_iterations):

            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                tools=TOOLS,
                tool_choice="auto",
                temperature=0,
                max_tokens=3000
            )

            message = response.choices[0].message

            messages.append(message)

            if not message.tool_calls:
                return message.content

            for tool_call in message.tool_calls:

                tool_name = (
                    tool_call.function.name
                )

                arguments = json.loads(
                    tool_call.function.arguments
                )

                print(
                    f"\n[TOOL] {tool_name}"
                )

                print(
                    f"[ARGS] {arguments}"
                )

                try:

                    result = execute_tool(
                        tool_name,
                        arguments
                    )

                except Exception as e:

                    result = (
                        f"ERROR executing "
                        f"{tool_name}: {e}"
                    )

                print(
                    f"[RESULT] {result}"
                )

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id":
                            tool_call.id,
                        "content": json.dumps(
                            result,
                            default=str
                        )
                    }
                )

        return "Maximum iterations reached."