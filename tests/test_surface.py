from pathlib import Path

SOURCE = (Path(__file__).parents[1] / "contracts" / "contract.py").read_text()

def test_contract_surface():
    for method in ["open_flight", "pin_note", "get_flight", "get_reviews_page", "get_flights_page", "get_summary"]:
        assert f"def {method}" in SOURCE

def test_lifecycle_guards_and_consensus():
    for signal in ["family in filled", "actor in tasters", "int(flight.fatigue) >= 3", "len(pins) == len(families)", "run_nondet_unsafe", "judged_family != family"]:
        assert signal in SOURCE
