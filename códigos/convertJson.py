import subprocess
import json

# Define o intervalo de tempo em segundos
interval = 60

# Define a lista de arquivos a serem processados
filenames = [
    'monday.tcpdump',
    'tuesday.tcpdump',
    'wednesday.tcpdump',
    'thursday.tcpdump',
    'friday.tcpdump'
]

print("Iniciando a tradução doas arquivos tcpdump para Json.")

# Loop por cada arquivo
for filename in filenames:
    # Cria um dicionário vazio para armazenar os dados agrupados
    data = {}

    # Filename + caminho do arquivo
    path = f'./data/{filename}'

    # Executa o comando Tshark e processa a saída
    # frame.cap_len
    try:
        p = subprocess.Popen(['tshark', '-r', path, '-T', 'fields', '-e', 'frame.time_epoch', '-e', 'frame.len'],
                             stdout=subprocess.PIPE)

    except FileNotFoundError:
        print(f'O arquivo {filename} não foi encontrado.')
        break

    for line in iter(p.stdout.readline, b''):
        # Divide a linha em campos
        fields = line.decode().strip().split('\t')

        # Obtém o tempo da captura e arredonda para o intervalo de tempo definido
        timestamp = float(fields[0])
        interval_start = int(timestamp // interval * interval)

        # Obtém o comprimento do pacote
        packet_len = int(fields[1])

        # Adiciona os dados ao dicionário
        if interval_start not in data:
            data[interval_start] = {
                'count': 0,
                'total_len': 0
            }
        data[interval_start]['count'] += 1
        data[interval_start]['total_len'] += packet_len

    # Calcula a média do comprimento dos pacotes em cada intervalo
    for interval_start in data:
        count = data[interval_start]['count']
        total_len = data[interval_start]['total_len']
        if count > 0:
            data[interval_start]['avg_len'] = total_len / count

    # Grava o dicionário em um arquivo JSON
    output_filename = filename.replace('.tcpdump', '.json')
    with open(f'./json/{output_filename}', 'w') as f:
        json.dump(data, f)

    print(f'O arquivo {output_filename} foi gerado com sucesso.')

print("Iniciando a concatenação dos Json.")

# Cria um dicionário vazio para armazenar os dados de todos os Json
full_data = {}

# Lista de dias da semana
week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']

# Itera sobre cada arquivo Json
for day in week_days:
    with open(f'./json/{day}.json', 'r') as f:
        day_data = json.load(f)

    # Itera sobre cada timestamp do arquivo Json e adiciona ao dicionário completo
    for timestamp, data in day_data.items():
        if timestamp not in full_data:
            full_data[timestamp] = {"count": 0, "total_len": 0, "avg_len": 0}
        full_data[timestamp]["count"] += data["count"]
        full_data[timestamp]["total_len"] += data["total_len"]
        full_data[timestamp]["avg_len"] = full_data[timestamp]["total_len"] / \
            full_data[timestamp]["count"]

# Cria um novo arquivo Json com os dados de todos os outros Json concatenados
with open('fullData.json', 'w') as f:
    json.dump(full_data, f)

print("O arquivo fullData.json foi gerado com sucesso.")
