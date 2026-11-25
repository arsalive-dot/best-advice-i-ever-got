#!/usr/bin/env python3
"""Write the one-sentence advice for the make.fun bounty
'The Best Advice I Ever Got'.

The advice: a grandmother's test for a partner - soup when you are
sick, not flowers when you are well. One sentence, a real voice
recalling a real person, specific and true beyond the moment.
Gate: 1-200 characters, one sentence; this entry is 112 characters,
tight enough to read in a single breath.
"""

import os

ENTRY = "My grandmother told me to marry the man who brings you soup when you're sick, not flowers when you're well."


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    tmp_path = os.path.join(out_dir, ".entry.txt.tmp")
    final_path = os.path.join(out_dir, "entry.txt")
    with open(tmp_path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    os.replace(tmp_path, final_path)
    os.chmod(final_path, 0o644)


if __name__ == "__main__":
    main()
