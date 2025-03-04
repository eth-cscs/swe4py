import textwrap
import rich
import rich.console


def hello_world():
    rich.console.Console().print(
        textwrap.dedent(
            """
            Hello, World!
            """
        ),
        style="reverse",
    )


if __name__ == "__main__":
    hello_world()
