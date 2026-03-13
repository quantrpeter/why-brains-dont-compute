#!/usr/bin/env bash
ROOT="/home/peter/workspace/why-brains-dont-compute"
MAX_JOBS=${1:-4}
LOGDIR="$ROOT/render_logs"
mkdir -p "$LOGDIR"

LESSONS=(
  "1:SolvingProblems"
  "2:ObjectiveSubjectiveReality"
  "3:AlgorithmsExplainer"
  "4:CodingExplainer"
  "5:NeuralNetworksExplainer"
  "6:ResurrectionExplainer"
  "7:LearningEmpiricallyExplainer"
  "8:WhatWePerceiveExplainer"
  "9:SpatialIntervalsExplainer"
  "10:AnglesExplainer"
  "11:LightnessDarknessExplainer"
  "12:EmpiricalRankingExplainer"
  "13:ColorExplainer"
  "14:ColorPsychophysicsExplainer"
  "15:MotionSpeedExplainer"
  "16:MotionDirectionExplainer"
  "17:ObjectSizeExplainer"
  "18:StereopsisExplainer"
  "19:StimuliAndBehaviorExplainer"
  "20:AssociationsExplainer"
  "21:MechanismsExplainer"
  "22:ReflexesExplainer"
  "23:FeatureDetectionExplainer"
  "24:StatisticalInferenceExplainer"
  "25:SummingUpExplainer"
)

render_one() {
  local n="${1%%:*}"
  local cls="${1##*:}"
  local dir="$ROOT/lesson $n/video"
  local log="$LOGDIR/lesson_${n}.log"
  local outfile="$dir/media/videos/scene/1080p60/${cls}.mp4"

  if [[ -f "$outfile" ]]; then
    echo "[lesson $n] SKIP — ${cls}.mp4 already exists"
    return 0
  fi

  echo "[lesson $n] START ${cls}"
  if (cd "$dir" && manim render -qh scene.py "$cls") > "$log" 2>&1; then
    local sz
    sz=$(du -h "$outfile" 2>/dev/null | cut -f1)
    echo "[lesson $n] DONE  ${cls} (${sz})"
  else
    echo "[lesson $n] FAIL  — check $log"
  fi
}

job_count=0
for entry in "${LESSONS[@]}"; do
  render_one "$entry" &
  ((job_count++))
  if (( job_count >= MAX_JOBS )); then
    wait -n 2>/dev/null || true
    ((job_count--))
  fi
done
wait

echo ""
echo "=== Render summary ==="
ok=0; fail=0; skip=0
for entry in "${LESSONS[@]}"; do
  n="${entry%%:*}"
  cls="${entry##*:}"
  f="$ROOT/lesson $n/video/media/videos/scene/1080p60/${cls}.mp4"
  if [[ -f "$f" ]]; then
    sz=$(du -h "$f" | cut -f1)
    echo "  lesson $n: $cls.mp4 ($sz)"
    ((ok++))
  else
    echo "  lesson $n: MISSING"
    ((fail++))
  fi
done
echo ""
echo "OK: $ok  FAIL: $fail"
