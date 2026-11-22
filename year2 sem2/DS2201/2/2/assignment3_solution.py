from math import inf


def calculate_asymmetric_cost(station_x, villages, w_west=3, w_east=1):
    """Total cable cost if we drop the station at one chosen village."""
    bill_total = 0
    for home_spot in villages:
        if home_spot < station_x:
            bill_total += w_west * (station_x - home_spot)
        else:
            bill_total += w_east * (home_spot - station_x)
    return bill_total


def solve_greedy(villages, w_west=3, w_east=1):
    """Pick the best single village for the station under the west/east weights."""
    if not villages:
        raise ValueError("need at least one village location")

    ordered_spots = sorted(villages)
    left_cut = w_east * len(ordered_spots) / (w_west + w_east)

    # Same weighted-median idea from the notes; for 3:1 it lands around ceil(N/4).
    for pos_idx, station_x in enumerate(ordered_spots, start=1):
        if pos_idx >= left_cut:
            return station_x, calculate_asymmetric_cost(
                station_x, ordered_spots, w_west=w_west, w_east=w_east
            )

    station_x = ordered_spots[-1]
    return station_x, calculate_asymmetric_cost(
        station_x, ordered_spots, w_west=w_west, w_east=w_east
    )


def block_quote(villages, start, end, w_west=3, w_east=1):
    """One-station cost for a contiguous slice of villages."""
    run = sorted(villages[start : end + 1])
    station_x, block_cost = solve_greedy(run, w_west=w_west, w_east=w_east)
    return station_x, block_cost


def solve_dp(villages, k, w_west=3, w_east=1):
    """DP version for the case where we are allowed to build several stations."""
    if k <= 0:
        raise ValueError("k must be a positive integer")
    if not villages:
        return 0, []

    villages = sorted(villages)
    village_count = len(villages)
    k = min(k, village_count)

    quote_cost = [[0] * village_count for _ in range(village_count)]
    picked_station = [[None] * village_count for _ in range(village_count)]
    for start in range(village_count):
        for end in range(start, village_count):
            picked_station[start][end], quote_cost[start][end] = block_quote(
                villages, start, end, w_west=w_west, w_east=w_east
            )

    best_tab = [[inf] * (village_count + 1) for _ in range(k + 1)]
    cut_at = [[None] * (village_count + 1) for _ in range(k + 1)]
    best_tab[0][0] = 0

    for stations_used in range(1, k + 1):
        best_tab[stations_used][0] = 0
        for served_upto in range(1, village_count + 1):
            for start in range(1, served_upto + 1):
                maybe_better = (
                    best_tab[stations_used - 1][start - 1]
                    + quote_cost[start - 1][served_upto - 1]
                )
                if maybe_better < best_tab[stations_used][served_upto]:
                    best_tab[stations_used][served_upto] = maybe_better
                    cut_at[stations_used][served_upto] = start - 1

    groups = []
    stations_used = k
    served_upto = village_count
    while stations_used > 0 and served_upto > 0:
        start = cut_at[stations_used][served_upto]
        groups.append(
            {
                "start_index": start,
                "end_index": served_upto - 1,
                "station_x": picked_station[start][served_upto - 1],
                "cost": quote_cost[start][served_upto - 1],
            }
        )
        served_upto = start
        stations_used -= 1

    groups.reverse()
    return best_tab[k][village_count], groups


contiguous_block_cost = block_quote


if __name__ == "__main__":
    coast_demo = [2, 5, 12, 18, 20]
    best_station, best_cost = solve_greedy(coast_demo)
    print("Question 1 sample run")
    print(f"Optimal station: {best_station}")
    print(f"Optimal cost: {best_cost}")
    print()

    small_case = [1, 2, 5, 6]
    total_cost, groups = solve_dp(small_case, 2)
    print("Question 2 sample run")
    print(f"Optimal total cost with 2 stations: {total_cost}")
    print("Blocks:")
    for group in groups:
        print(group)
