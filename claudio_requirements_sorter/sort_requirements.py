from typing import List, Tuple


def sort_requirements(requirements: List[str]) -> List[str]:
    requirement_pieces = _get_requirements_pieces(requirements=requirements)
    new_requirements = [a + b for a, b in sorted(requirement_pieces, key=lambda x: x[0])]
    return new_requirements


def _get_requirements_pieces(requirements: List[str]) -> List[Tuple[str, str]]:
    requirement_pieces = []
    for requirement in requirements:
        if (sep := "==") in requirement:
            requirement_pieces.append(_split_requirement(requirement=requirement, sep=sep))
        elif (sep := ">=") in requirement:
            requirement_pieces.append(_split_requirement(requirement=requirement, sep=sep))
        elif (sep := "<=") in requirement:
            requirement_pieces.append(_split_requirement(requirement=requirement, sep=sep))
        else:
            raise ValueError(f"Invalid separator in: {requirement}")

    return requirement_pieces


def _split_requirement(requirement: str, sep: str) -> tuple:
    index = requirement.index(sep)
    return requirement[:index], requirement[index:]
