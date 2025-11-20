from rich import print
from openai import OpenAI
import os
import subprocess
import sys
from pathlib import Path

USING_DOTENV = True

if USING_DOTENV:
    import dotenv
    dotenv.load_dotenv()
else:
    print("hard coded")
    os.environ["OPENAI_API_KEY"] = 'skh-asdfgsadgasdgasdga'  # replace with your API key

print(os.environ.get("OPENAI_API_KEY")[:10])

client = OpenAI()


def setup():
    repoRoot = Path(__file__).resolve().parent
    requirementsPath = repoRoot / "requirements.txt"

    if not requirementsPath.exists():
        printRed(f"requirements.txt not found at {requirementsPath}")
        return

    print(f"Installing packages from {requirementsPath} ...")

    try:
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", "-r", str(requirementsPath)]
        )
        printGreen("Package installation complete.")
    except subprocess.CalledProcessError as error:
        printRed(f"pip install failed with return code {error.returncode}")


def invoke(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


def printGreen(message):
    print(f"[green]{message}[/green]")


def printRed(message):
    print(f"[bold magenta]{message}[/bold magenta]")

