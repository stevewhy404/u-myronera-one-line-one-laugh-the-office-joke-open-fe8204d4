import os

LINE = "I asked IT for a second monitor and got a mirror, a sticky note saying 'reflect on your priorities', and a ticket closed as resolved."

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
