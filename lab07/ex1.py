import argparse
import sympy as sp

def newton(fn: str, x: float, s: float, n: int, p: float):
    
    symbol = sp.Symbol("x")
    f = sp.sympify(fn)
    df = f.diff(symbol)

    for _ in range(n):
        if df.subs(symbol, x) == 0:
            raise ValueError("Derivative of the given function is zero")

        xnext = x - s * f.subs(symbol, x) / df.subs(symbol, x)

        if abs(xnext - x) < p:
            print(f"Found a zero at {xnext} with precision {p}")
            return
        
        x = xnext
    
    print(f"Could not find a zero in {n} steps")

parser = argparse.ArgumentParser(description="Newton's method for finding zeros")
parser.add_argument("fn", type=str, help="Considered function with x as a variable")
parser.add_argument("-x", type=float, help="Starting point", default=0.0)
parser.add_argument("-s", type=float, help="Step length", default=1.0)
parser.add_argument("-n", type=int, help="Number of steps", default=100)
parser.add_argument("-p", type=float, help="Set precission", default=1e-6)

args = parser.parse_args()

newton(args.fn, args.x, args.s, args.n, args.p)
