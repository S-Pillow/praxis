#!/usr/bin/env python3
"""Check opaque sRGB hex color pairs; not a rendered accessibility audit."""
import argparse
import json
import math
import re


def luminance(value):
    if not re.fullmatch(r'#[0-9a-fA-F]{6}', value):
        raise ValueError('Expected opaque #RRGGBB; resolve compositing first')
    channels = [int(value[i:i+2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return sum(c * w for c, w in zip(linear, (0.2126, 0.7152, 0.0722)))


def check(foreground, background, minimum=4.5):
    if not math.isfinite(minimum) or not 1 <= minimum <= 21:
        raise ValueError('Minimum contrast must be between 1 and 21')
    hi, lo = sorted((luminance(foreground), luminance(background)), reverse=True)
    ratio = (hi + 0.05) / (lo + 0.05)
    return dict(foreground=foreground, background=background, ratio=ratio,
                minimum=minimum, passed=ratio >= minimum)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('foreground')
    parser.add_argument('background')
    parser.add_argument('--minimum', type=float, default=4.5)
    args = parser.parse_args()
    try:
        result = check(args.foreground, args.background, args.minimum)
    except ValueError as exc:
        parser.error(str(exc))
    print(json.dumps(result))
    return 0 if result['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
