import argparse
import yaml


def main():
    parser = argparse.ArgumentParser(description="Train diabetic retinopathy screening models.")
    parser.add_argument("--config", type=str, required=True, help="Path to YAML config file.")
    args = parser.parse_args()

    with open(args.config, "r") as f:
        config = yaml.safe_load(f)

    print("Loaded config:")
    print(config)
    print("\nTraining pipeline placeholder.")
    print("Add dataset paths, model initialization, training loop, and checkpoint saving here.")


if __name__ == "__main__":
    main()
