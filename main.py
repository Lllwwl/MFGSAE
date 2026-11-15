import argparse
import os

from mfgsae.model import run as run_ours
from mfgsae.simplification import prepare_graph
from mfgsae.visualization import plot_before_after_comparison
from mfgsae._shared import save_result_json, set_seed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--output_dir", default="results")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--target_ndr", type=float, default=0.145)
    parser.add_argument("--use_centroids", action="store_true")
    parser.add_argument("--preserve_closed_shapes", action="store_true")
    args = parser.parse_args()

    set_seed(args.seed)
    os.makedirs(args.output_dir, exist_ok=True)
    prepared = prepare_graph(
        args.dataset,
        seed=args.seed,
        use_centroids=(False if args.preserve_closed_shapes else args.use_centroids),
    )
    result = run_ours(prepared, seed=args.seed, target_ndr=args.target_ndr)

    fig_path = os.path.join(
        args.output_dir,
        f"{os.path.splitext(os.path.basename(args.dataset))[0]}_ours_comparison.png",
    )
    plot_before_after_comparison(
        prepared.graph,
        result["simplified_graph"],
        prepared.critical_labels,
        result["removed_nodes"],
        save_path=fig_path,
        scores=result.get("scores"),
        node_list=prepared.node_list,
        redundant_candidate_nodes=result.get("redundant_candidate_nodes"),
        title_prefix=f"ours on {os.path.basename(args.dataset)}",
    )
    result["comparison_figure"] = fig_path
    result.pop("simplified_graph", None)
    payload = {
        "dataset": os.path.basename(args.dataset),
        "osm_file": args.dataset,
        "seed": args.seed,
        "target_ndr": args.target_ndr,
        "use_centroids": bool(False if args.preserve_closed_shapes else args.use_centroids),
        "preserve_closed_shapes": bool(args.preserve_closed_shapes),
        "result": result,
    }
    save_path = os.path.join(
        args.output_dir,
        f"{os.path.splitext(os.path.basename(args.dataset))[0]}_ours_results.json",
    )
    save_result_json(save_path, payload)
    print(save_path)


if __name__ == "__main__":
    main()
