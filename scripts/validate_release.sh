#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

export PYTHONDONTWRITEBYTECODE=1
trap 'find . -type d -name __pycache__ -prune -exec rm -rf {} + 2>/dev/null || true' EXIT

python -m unittest discover -s tests -p "test_*.py"
python scripts/check_showcase.py

if [[ "${1:-}" == "--release" ]]; then
  python scripts/check_release_candidate.py --release
else
  python scripts/check_release_candidate.py
fi

echo "GymFlow local release validation completed successfully."
