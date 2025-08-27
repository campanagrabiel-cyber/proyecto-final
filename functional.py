"""
Módulo de utilidades con enfoque de programación funcional.
Evita estado compartido y efectos colaterales.
"""
from functools import reduce
from typing import Iterable, Callable, Any, Dict, List, Tuple

def fmap(fn: Callable[[Any], Any], xs: Iterable[Any]) -> list:
    "Aplica una función a cada elemento. Devuelve lista nueva."
    return list(map(fn, xs))

def ffilter(pred: Callable[[Any], bool], xs: Iterable[Any]) -> list:
    "Filtra elementos según un predicado. Devuelve lista nueva."
    return list(filter(pred, xs))

def freduce(fn: Callable[[Any, Any], Any], xs: Iterable[Any], initial: Any) -> Any:
    "Agrega/combina elementos (fold-left)."
    return reduce(fn, xs, initial)

def compose(*fns: Callable[[Any], Any]) -> Callable[[Any], Any]:
    "Composición de funciones: compose(f,g,h)(x) == f(g(h(x)))."
    def composed(x):
        for fn in reversed(fns):
            x = fn(x)
        return x
    return composed

def group_by(key_fn: Callable[[Any], Any], xs: Iterable[Any]) -> Dict[Any, list]:
    "Agrupa por clave derivada de cada elemento."
    res: Dict[Any, list] = {}
    for x in xs:
        k = key_fn(x)
        res.setdefault(k, []).append(x)
    return res

def moving_average(window: int, series: Iterable[float]) -> List[float]:
    "Promedio móvil simple."
    s = list(series)
    if window <= 0 or window > len(s):
        raise ValueError("window inválido")
    out = []
    for i in range(window-1, len(s)):
        out.append(sum(s[i-window+1:i+1]) / window)
    return out
