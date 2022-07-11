#!/usr/bin/python3

# https://www.codewars.com/kata/52742f58faf5485cae000b9a/
def format_duration(seconds):  # can be compressed into a (very long) ternary oneliner if you want
    if not seconds:
        return "now"
    times = dict(year=seconds // 31536000,
                 day=(seconds % 31536000) // 86400,
                 hour=(seconds % 86400) // 3600,
                 minute=(seconds % 3600) // 60,
                 second=seconds % 60)
    return ", ".join([f"{v} {k + 's' if v > 1 else k}" for k, v in times.items() if v])[::-1].replace(" ,", " dna ", 1)[::-1]


def format_duration_oneliner(seconds):  # comme ça
    return "now" if not seconds else ", ".join([f"{v} {k + 's' if v > 1 else k}" for k, v in dict(year=seconds // 31536000, day=(seconds % 31536000) // 86400, hour=(seconds % 86400) // 3600, minute=(seconds % 3600) // 60, second=seconds % 60).items() if v])[::-1].replace(" ,", " dna ", 1)[::-1]
