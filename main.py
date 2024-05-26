'''
  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

  DESCRIPTION:
  An anagram is the result of rearranging the letters of a word to produce a new word.

  Note: anagrams are case insensitive

  Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

  Examples
  "foefet" is an anagram of "toffee"

  "Buckethead" is an anagram of "DeathCubeK”

'''
from check_anagram.brute_force import check_anagram_brute_force
from check_anagram.bubble_sort import check_anagram_bubble_sort
from check_anagram.frequency_table import check_anagram_frequency_table
from check_anagram.hash_map import check_anagram_hash_map
from check_anagram.min_max import check_anagram_min_max
from check_anagram.min_max_explain import check_anagram_min_max_explain
import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def measure_execution_time(algorithm, *args):
  start_time = time.perf_counter_ns()
  algorithm(*args)
  end_time = time.perf_counter_ns()
  return end_time - start_time

def plot_execution_times(times_dict, num_simulations):
  plt.figure(figsize=(10, 6))
  for algo, times in times_dict.items():
      plt.plot(range(1, num_simulations+1), times, label=algo)
  plt.xlabel("Simulation")
  plt.ylabel("Execution Time (nanoseconds)")
  plt.title("Execution Time Comparison")
  plt.legend()
  st.pyplot(plt)

def run_simulation(num_simulations, str1, str2):
    times_dict = {
        "Brute Force": [],
        "Bubble Sort": [],
        "Frequency Table": [],
        "Hash Map": [],
        "Min Method [Proposed]": [],
        "Max Method [Proposed]": []
    }

    for _ in range(num_simulations):
        times_dict["Brute Force"].append(measure_execution_time(check_anagram_brute_force, str1, str2))
        times_dict["Bubble Sort"].append(measure_execution_time(check_anagram_bubble_sort, str1, str2))
        times_dict["Frequency Table"].append(measure_execution_time(check_anagram_frequency_table, str1, str2))
        times_dict["Hash Map"].append(measure_execution_time(check_anagram_hash_map, str1, str2))
        times_dict["Min Method [Proposed]"].append(measure_execution_time(check_anagram_min_max, str1, str2, min))
        times_dict["Max Method [Proposed]"].append(measure_execution_time(check_anagram_min_max, str1, str2, max))

    df = pd.DataFrame(times_dict)

    summary = df.describe().transpose()
    summary["Difference (nanoseconds)"] = summary["max"] - summary["min"]
    
    # Check if standard deviation is available and replace <NA> with 0 if there's only one data point
    if "std" in summary.columns and pd.isna(summary["std"]).any():
        summary["std"].fillna(0, inplace=True)
    
    # Round the values and convert to string with formatting
    summary = summary.round(4).astype(str)
    summary["Mean"] = summary["mean"].apply(lambda x: f"{float(x):,.4f}".rstrip('0').rstrip('.'))
    summary["Standard Deviation"] = summary["std"].apply(lambda x: f"{float(x):,.4f}".rstrip('0').rstrip('.'))
    summary["Minimum"] = summary["min"].apply(lambda x: f"{float(x):,.4f}".rstrip('0').rstrip('.'))
    summary["Q1"] = summary["25%"].apply(lambda x: f"{float(x):,.4f}".rstrip('0').rstrip('.'))
    summary["Median"] = summary["50%"].apply(lambda x: f"{float(x):,.4f}".rstrip('0').rstrip('.'))
    summary["Q3"] = summary["75%"].apply(lambda x: f"{float(x):,.4f}".rstrip('0').rstrip('.'))
    summary["Maximum"] = summary["max"].apply(lambda x: f"{float(x):,.4f}".rstrip('0').rstrip('.'))
    summary["Difference (nanoseconds)"] = summary["Difference (nanoseconds)"].apply(lambda x: f"{float(x):,.4f}".rstrip('0').rstrip('.'))
    
    summary.rename(columns={"Mean": "Mean (nanoseconds)", "Standard Deviation": "Standard Deviation (nanoseconds)", "Minimum": "Minimum (nanoseconds)", "Q1": "Q1 (nanoseconds)", "Median": "Median (nanoseconds)", "Q3": "Q3 (nanoseconds)", "Maximum": "Maximum (nanoseconds)"}, inplace=True)
    summary.index.name = "Algorithm"
    
    summary.drop(["mean", "std", "min", "25%", "50%", "75%", "max"], axis=1, inplace=True)
    summary = summary.sort_values(by="Mean (nanoseconds)", ascending=False)

    st.write("### Execution Time Statistics")
    st.table(summary)

    plot_execution_times(times_dict, num_simulations)

def main():
    st.title("Anagram Check Simulation")
    num_simulations = st.number_input("Number of Simulations:", min_value=1, step=1, value=1000)
    str1 = st.text_input("Input String 1:", value="heksakosioiheksekontaheksafobia")
    str2 = st.text_input("Input String 2:", value="heksakosioiheksekontaheksafobia")
    run_simulation_button = st.button("Run Simulation")

    if not str1.strip() or not str2.strip():
        st.warning("String inputs must not be empty!")
        return
    elif run_simulation_button:
        with st.spinner("Running Simulation..."):
            start_time = time.perf_counter_ns()
            run_simulation(num_simulations, str1, str2)
            end_time = time.perf_counter_ns()
            st.success(f"Simulation completed in {(end_time - start_time) / 1e9:.2f} seconds")

            # show divider
            st.title("Detailed Explanation of the Min Proposed Method")
            check_anagram_min_max_explain(str1, str2)
            st.title("Detailed Explanation of the Max Proposed Method")
            check_anagram_min_max_explain(str1, str2, max)
    else:
      st.write("CLick on Run Simulation Button to check the anagram of the given strings.")
      
    # show source link
    st.write("[Source: Documents](https://docs.google.com/document/d/1-92EFhkl2M-OFx2cyj6ZFaoME4IZRWbbN_l553kCTis/edit?usp=sharing)")


if __name__ == "__main__":
  main()