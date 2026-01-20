#!/bin/bash

# Parameters
EXECUTABLE=${2:-"./matrix_mult_openmp"}
MATRIX_SIZE=${1:-500}
NUM_RUNS=10

# Check if the executable exists
if [ ! -f "$EXECUTABLE" ]; then
    echo "Executable '$EXECUTABLE' not found."
    exit 1
fi


echo "Threads | Avg Wall Time (ms) | Standard Error (ms) | Speedup Factor | Speedup SE | Efficiency | Efficiency SE"
echo "--------+-------------------+------------------+----------------+-------------+------------+----------------"

# Compute the baseline time
output=$(OMP_NUM_THREADS=1 $EXECUTABLE $MATRIX_SIZE 1)
baseline_time=$(echo "$output" | awk '{print $(NF-1)}')
baseline_time_error=0

# Vary the number of threads from 1 to 8
for NUM_THREADS in {1..8}; do
    # Run the matrix multiplication program, calculate the average wall time, and accumulate squared differences
    total_time=0
    times=()
    for i in $(seq 1 $NUM_RUNS); do
        output=$($EXECUTABLE $MATRIX_SIZE $NUM_THREADS)
        time_ms=$(echo "$output" | awk '{print $(NF-1)}')
        total_time=$(echo "scale=7; $total_time + $time_ms" | bc -l)
        times+=($time_ms)
    done

    average_time=$(echo "scale=7; $total_time / $NUM_RUNS" | bc -l)

    # Calculate the standard error
    squared_diff_sum=0
    for time in "${times[@]}"; do
        diff=$(echo "scale=7; $time - $average_time" | bc -l)
        squared_diff=$(echo "scale=7; $diff * $diff" | bc -l)
        squared_diff_sum=$(echo "scale=7; $squared_diff_sum + $squared_diff" | bc -l)
    done

    variance=$(echo "scale=7; $squared_diff_sum / ($NUM_RUNS - 1)" | bc -l)
    standard_deviation=$(echo "scale=7; sqrt($variance)" | bc -l)
    standard_error=$(echo "scale=7; $standard_deviation / sqrt($NUM_RUNS)" | bc -l)

    # Calculate the speedup factor relative to the single-threaded case and its standard error
    if [[ "$NUM_THREADS" -eq 1 ]]; then
        speedup_factor="1.00"
        speedup_error="0.00"
        baseline_time=$average_time
        baseline_time_error=$standard_error
    else
        speedup_factor=$(echo "scale=7; $baseline_time / $average_time" | bc -l)
        speedup_error=$(echo "scale=7; $speedup_factor * sqrt((($standard_error / $average_time) ^ 2) + (($baseline_time_error / $baseline_time) ^ 2))" | bc -l)
    fi

    # Calculate the efficiency and its standard error
    if [[ "$NUM_THREADS" -eq 1 ]]; then
        efficiency="1.00"
        efficiency_error="0.00"
    else
        efficiency=$(echo "scale=7; $speedup_factor / $NUM_THREADS" | bc -l)
        efficiency_error=$(echo "scale=7; $speedup_error / $NUM_THREADS" | bc -l)
    fi

    printf "%-8d| %-18.2f| %-18.2f| %-15.3f | %-11.3f | %-10.3f | %-12.3f\n" "$NUM_THREADS" "$average_time" "$standard_error" "$speedup_factor" "$speedup_error" "$efficiency" "$efficiency_error"
done
