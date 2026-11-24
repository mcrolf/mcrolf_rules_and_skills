#!/usr/bin/env bash
# Copy shared rules and the clean-code guide into each skill that bundles them,
# so every skill folder works on its own.
#   scripts/sync-skill-references.sh          copy sources over the bundled files
#   scripts/sync-skill-references.sh --check  exit 1 if any bundled file is out of date
set -euo pipefail
cd "$(dirname "$0")/.."

# source -> bundled copy
copies=(
  "rules/domain-language.md      skills/clean-code/domain-language.md"
  "rules/domain-language.md      skills/knowledge-bank/references/domain-language.md"
  "rules/domain-language.md      skills/pull-request/references/domain-language.md"
  "rules/domain-language.md      skills/react-best-practices/references/domain-language.md"
  "rules/domain-language.md      skills/tough-critic/references/domain-language.md"
  "rules/writing.md              skills/knowledge-bank/references/writing.md"
  "rules/writing.md              skills/pull-request/references/writing.md"
  "rules/token-efficiency.md     skills/knowledge-bank/references/token-efficiency.md"
  "rules/ongoing-development.md  skills/pull-request/references/ongoing-development.md"
  "skills/clean-code/SKILL.md    skills/react-best-practices/references/clean-code.md"
  "skills/clean-code/heuristics.md skills/react-best-practices/references/heuristics.md"
  "skills/clean-code/SKILL.md    skills/tough-critic/references/clean-code.md"
  "skills/clean-code/heuristics.md skills/tough-critic/references/heuristics.md"
)

stale=0
for pair in "${copies[@]}"; do
  read -r source copy <<<"$pair"
  if [[ "${1:-}" == "--check" ]]; then
    if ! cmp -s "$source" "$copy"; then
      echo "out of date: $copy (source: $source)"
      stale=1
    fi
  else
    mkdir -p "$(dirname "$copy")"
    cp "$source" "$copy"
  fi
done
exit "$stale"
