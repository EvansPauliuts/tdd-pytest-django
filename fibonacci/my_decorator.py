from typing import Tuple, Callable


def get_list_of_kwargs_for_func(
    identifiers: str, values: list[Tuple[int, int]]
) -> list[dict[str, str]]:
    print(f"getting list of kwargs for function, \n{identifiers=}, {values=}")
    parsed_identifiers = identifiers.split(",")
    list_of_kwargs_for_func = []

    for tuple_value in values:
        kw_for_func = {}
        for i, keyword in enumerate(parsed_identifiers):
            kw_for_func[keyword] = tuple_value[i]

        list_of_kwargs_for_func.append(kw_for_func)

    print(f"{list_of_kwargs_for_func=}")
    return list_of_kwargs_for_func


def my_parametrized(identifiers: str, values: list[Tuple[int, int]]) -> Callable:
    def parametrized_decorator(func: Callable) -> Callable:
        def func_parametrized() -> None:
            list_of_kwargs_for_func = get_list_of_kwargs_for_func(
                identifiers=identifiers, values=values
            )

            for kw_for_func in list_of_kwargs_for_func:
                print(f"calling function {func.__name__} with {kw_for_func}")
                func(**kw_for_func)

        return func_parametrized

    return parametrized_decorator
