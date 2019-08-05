def greedy_algorithm(states_needed: set, stations: dict) -> (set, None):
    """Принимает множество штатов и словарь станций с обхватом этих штатов.
    На выходе множество станций, для обхвата всех штатов жадным алгоритмом"""
    final_station = set()
    while states_needed != set():  # пока все штаты без покрытия станций
        best_station = get_best_station(states_needed, stations, final_station)
        if best_station is None:  # если лучшей станции нет
            return
        states_needed = states_needed - stations[best_station]  # убираем штаты станции из начального списка
        final_station.add(best_station)  # добавляем станцию в результирующий сеттер
    return final_station


def get_best_station(states_needed: set, stations: dict, final_station: set) -> (str, None):
    """Вывод лучшей станции из ещё непросмотренных"""
    best_station = None
    count_states = 0
    for k, v in stations.items():
        # если пересечение по штатам наибольшее и станция не просмотренна
        if len(v & states_needed) > count_states and k not in final_station:
            best_station = k
            count_states = len(v.intersection(states_needed))
    return best_station
        

states = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
stations_s = {'k_one': {'id', 'nv', 'ut'},
              'k_two': {'wa', 'id', 'mt'},
              'k_three': {'or', 'nv', 'ca'},
              'k_four': {'nv', 'ut'},
              'k_five': {'ca', 'az'}}

print(greedy_algorithm(states, stations_s))
