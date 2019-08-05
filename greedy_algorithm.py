def greedy_algorithm(states_needed: set, stations: dict)-> set:
    final_station = set()
    best_station = None
    while states_needed != set():
        best_station = get_best_station(states_needed, stations, final_station)
        if best_station is None:
            return None
        states_needed = states_needed - stations[best_station]
        final_station.add(best_station)
    return final_station


def get_best_station(states_needed: set, stations: dict, final_station: set) -> str:
    best_station = None
    count_states = 0
    for k, v in stations.items():
        if len(v.intersection(states_needed)) > count_states and k not in final_station:
            best_station = k
            count_states = len(v.intersection(states_needed))
    return best_station
        

states_needed = {'mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'}
stations = {'kone': {'id', 'nv', 'ut'},
            'ktwo': {'wa', 'id', 'mt'},
            'kthree': {'or', 'nv', 'ca'},
            'kfour': {'nv', 'ut'},
            'kfive': {'ca', 'az'}}

print(greedy_algorithm(states_needed, stations))
