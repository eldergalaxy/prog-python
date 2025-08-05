from pathlib import Path
h = Path.home()

(h / 'spam/eggs').mkdir(exist_ok=True)
(h / 'spam/eggs/bacon').mkdir(exist_ok=True)
(h / 'spam/eggs/eggs2').mkdir(exist_ok=True)  
(h / 'spam/eggs/bacon/toast').mkdir(exist_ok=True)  



for f in ['spam/file1.txt', 'spam/eggs/file23.txt', 'spam/eggs/eggs2/file93.txt', 'spam/eggs/bacon/file33.txt', 'spam/eggs/bacon/toast/file69.txt']:
    with open(h / f, 'w', encoding='utf-8') as file:
        file.write('HelloSpam')