"""Write one office joke to /output/entry.txt.

Entry for make.fun's "Make the AI Judge Laugh: the Office Joke Open".
Stdlib only, no network, no dependencies.
"""

import os

JOKE = "The printer has been 'warming up' since Tuesday — same as my manager, who's been 'circling back' on my raise since March."


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
