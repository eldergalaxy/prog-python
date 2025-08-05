from pathlib import Path
h = Path.home()
#(h / 'spam').mkdir(exist_ok=True)

for i in range(5):
    with open(h / f'spam/fil{i}.txt', 'w', encoding='UTF-8') as file:
        file.write('Hello')