#!/usr/bin/env python3
"""
This script processes a text file (200k.txt) by reading its contents,
multiplying the lines to increase the dataset, and then creating
multiple new files with varying numbers of randomly shuffled lines.

Specifically, it performs the following tasks:
1. Reads the contents of 200k.txt and multiplies the lines by 5.
2. Creates a new file (10k.txt) with the first 10,000 shuffled lines.
3. Creates a new file (100k.txt) with the first 100,000 shuffled lines.
4. Creates a new file (500k.txt) with the first 500,000 shuffled lines.
5. Creates a new file (1m.txt) with the first 1,000,000 shuffled lines.

Modules:
- pathlib: To handle file paths and writing text to files.
- random: To shuffle the lines randomly.

Usage:
Run the script in the same directory as 200k.txt.
The script will generate four new files: 10k.txt, 100k.txt, 500k.txt, and
1m.txt.
"""

from pathlib import Path
import random

# Open the original file and read all lines, multiplying by 5
# to increase the data
with open("200k.txt") as file_obj:
    lines = file_obj.readlines() * 5

    # Shuffle the lines randomly and write the first 10,000 lines to 10k.txt
    random.shuffle(lines)
    Path("speed_test/10k.txt").write_text("".join(lines[:10000]))

    # Shuffle the lines again and write the first 100,000 lines to 100k.txt
    random.shuffle(lines)
    Path("speed_test/100k.txt").write_text("".join(lines[:100000]))

    # Shuffle the lines again and write the first 500,000 lines to 500k.txt
    random.shuffle(lines)
    Path("speed_test/500k.txt").write_text("".join(lines[:500000]))

    # Shuffle the lines one more time and write the first 1,000,000 lines to
    # 1m.txt
    random.shuffle(lines)
    Path("speed_test/1m.txt").write_text("".join(lines[:1000000]))
