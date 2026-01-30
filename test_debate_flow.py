"""
Quick debate flow smoke test.
Runs the AutoGen debate loop with 4 agents in decentralized mode.
"""

from main import MADSystem


def main():
    system = MADSystem(config_path="./config/config.yaml")
    system.initialize()

    components = ["Pt", "Pd", "Ni", "Fe", "Co"]
    result = system.run_debate(components=components, reaction_type="OER", save_result=False)

    print("\n=== Debate Result (Summary) ===")
    print(f"Consensus: {result.get('consensus_reached')}")
    print(f"Products: {result.get('final_products')}")
    print(f"Performance: {result.get('final_performance')}")


if __name__ == "__main__":
    main()
