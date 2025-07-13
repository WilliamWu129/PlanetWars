import sys
sys.path.insert(0, '../')
from planet_wars import issue_order




def spread_and_attack_if_possible(state):
    my_planets = sorted(state.my_planets(), key=lambda p: p.num_ships)

    # Prioritize neutral planets first
    targets = state.neutral_planets() + state.enemy_planets()
    targets = sorted(targets, key=lambda p: p.num_ships)

    for my_planet in my_planets:
        for target in targets:
            # Don’t send to planets we're already targeting
            if any(fleet.destination_planet == target.ID for fleet in state.my_fleets()):
                continue

            distance = state.distance(my_planet.ID, target.ID)
            required_ships = target.num_ships
            if target.owner == 2:  # enemy
                required_ships += target.growth_rate * distance
            required_ships += 1  # just to be safe

            if my_planet.num_ships > required_ships:
                return issue_order(state, my_planet.ID, target.ID, required_ships)

    return False  # Nothing launched

# def attack_weakest_enemy_planet(state):
#     # (1) If we currently have a fleet in flight, abort plan.
#     if len(state.my_fleets()) >= 1:
#         return False

#     # (2) Find my strongest planet.
#     strongest_planet = max(state.my_planets(), key=lambda t: t.num_ships, default=None)

#     # (3) Find the weakest enemy planet.
#     weakest_planet = min(state.enemy_planets(), key=lambda t: t.num_ships, default=None)

#     if not strongest_planet or not weakest_planet:
#         # No legal source or destination
#         return False
#     else:
#         # (4) Send half the ships from my strongest planet to the weakest enemy planet.
#         return issue_order(state, strongest_planet.ID, weakest_planet.ID, strongest_planet.num_ships / 2)


# def spread_to_weakest_neutral_planet(state):
#     # (1) If we currently have a fleet in flight, just do nothing.
#     if len(state.my_fleets()) >= 1:
#         return False

#     # (2) Find my strongest planet.
#     strongest_planet = max(state.my_planets(), key=lambda p: p.num_ships, default=None)

#     # (3) Find the weakest neutral planet.
#     weakest_planet = min(state.neutral_planets(), key=lambda p: p.num_ships, default=None)

#     if not strongest_planet or not weakest_planet:
#         # No legal source or destination
#         return False
#     else:
#         # (4) Send half the ships from my strongest planet to the weakest enemy planet.
#         return issue_order(state, strongest_planet.ID, weakest_planet.ID, strongest_planet.num_ships / 2)



