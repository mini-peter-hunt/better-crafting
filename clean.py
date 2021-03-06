from os.path import join
from os import remove, walk


def clean():
    func_path = join('better-crafting', 'data', 'better_crafting', 'functions')

    for path in [*walk(func_path)][0][2]:
        remove(join(func_path, path))

    recipe_path = join('better-crafting', 'data', 'minecraft', 'recipes')

    for path in [*walk(recipe_path)][0][2]:
        remove(join(recipe_path, path))

    with open(join(func_path, 'init.mcfunction'), 'w') as file:
        pass

    with open(join(func_path, 'tick.mcfunction'), 'w') as file:
        pass


if __name__ == '__main__':
    clean()
