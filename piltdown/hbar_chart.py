"""Horizontal bar charts for Piltdown."""
import math
from typing import Dict, List
import piltdown.literals as lit
import piltdown.util as util


def hbar_line(
    length: float,
    eighths: Dict[int, str],
    eight_eighths: str,
) -> str:
    """Generate a single bar for a horizontal bar chart."""
    ret: str = ""
    rounded: float = round(length * 8) / 8 / 8
    ret += eight_eighths * math.floor(rounded)
    ret += eighths[int((rounded - math.floor(rounded)) * 8)]
    return ret


def hbar(
    data: List[float],
    labels: List[str] = lit.DEFAULT_LABELS,
    eighths: Dict[int, str] = lit.EIGHTHS,
    eight_eighths: str = lit.EIGHT_EIGHTHS,
    print_values: bool = True
) -> str:
    """Generate a horizontal bar chart."""
    if len(data) > len(labels):
        raise ValueError("Not enough labels")
    # Left-pad labels so they're all the same length
    label_max: int = max(map(len, labels))
    for i,item in enumerate(labels):
        labels[i]=item.rjust(label_max)
    # Produce chart
    ret: str = ""
    for line, label in zip(data, labels):
        ret += util.fullwidth(label) 
        ret += hbar_line(line, eighths, eight_eighths)
        if line == 0 and print_values:ret+=" "
        if print_values:ret+=str(line)
        ret += "\n"
    return ret
