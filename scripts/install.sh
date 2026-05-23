#!/usr/bin/env bash
set -euo pipefail

force=0
codex_home="${CODEX_HOME:-$HOME/.codex}"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --force)
      force=1
      shift
      ;;
    --codex-home)
      codex_home="$2"
      shift 2
      ;;
    *)
      echo "Unknown option: $1" >&2
      echo "Usage: bash scripts/install.sh [--force] [--codex-home PATH]" >&2
      exit 64
      ;;
  esac
done

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(cd "$script_dir/.." && pwd)"
source_dir="$repo_root/skills/pdf-to-docx-humanize"
skills_root="$codex_home/skills"
dest_dir="$skills_root/pdf-to-docx-humanize"

if [[ ! -d "$source_dir" ]]; then
  echo "Skill source not found: $source_dir" >&2
  exit 1
fi

mkdir -p "$skills_root"

if [[ -e "$dest_dir" ]]; then
  if [[ "$force" -ne 1 ]]; then
    echo "Destination already exists: $dest_dir"
    echo "Run again with --force to replace it."
    exit 2
  fi
  rm -rf "$dest_dir"
fi

cp -R "$source_dir" "$dest_dir"

echo "Installed pdf-to-docx-humanize to:"
echo "  $dest_dir"

missing=()
for dep in humanize humanize-gen-plan humanize-refine-plan humanize-rlcr; do
  if [[ ! -d "$skills_root/$dep" ]]; then
    missing+=("$dep")
  fi
done

if [[ "${#missing[@]}" -gt 0 ]]; then
  echo
  echo "Warning: full RLCR workflow needs these missing skills:"
  printf '  - %s\n' "${missing[@]}"
  echo "Install the humanize skill family, then restart Codex."
else
  echo
  echo "Humanize dependency check passed."
fi

echo
echo 'Restart Codex, then invoke: $pdf-to-docx-humanize'
