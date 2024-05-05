'''
  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

  DESCRIPTION:
An anagram is the result of rearranging the letters of a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given are anagrams of each other; return false otherwise.

Examples
"foefet" is an anagram of "toffee"

"Buckethead" is an anagram of "DeathCubeK”

'''
from check_anagram.brute_force import check_anagram_brute_force
from check_anagram.greedy import check_anagram_greedy
from check_anagram.dynamic_programming import check_anagram_dynamic
from check_anagram.min_max import check_anagram_min_max
import streamlit as st
import time
import matplotlib.pyplot as plt
import numpy as np
# pip install streamlit numpy matplotlib  
# pip3 freeze > requirements.txt  # Python3
# pip freeze > requirements.txt  # Python2
# Main function
def main():
  # print(check_anagram_brute_force("listen", "silent"))  # Output: True
  # print(check_anagram_greedy("listen", "silent"))  # Output: True
  # print(check_anagram_dynamic("listen", "silent"))  # Output: True
  # print(check_anagram_min_max("saxm", "mxas"))
  st.title("Anagram Check Simulation")

  num_simulations = st.number_input("Number of Simulations:", min_value=1, step=1)
  str1 = st.text_input("Input String 1:")
  str2 = st.text_input("Input String 2:")
  
  times_brute_force = []
  times_greedy = []
  times_dynamic = []
  times_min = []
  times_max = []
  if st.button("Run Simulation"):
    for _ in range(num_simulations):
      start_time = time.time_ns()
      check_anagram_brute_force(str1, str2)
      end_time = time.time_ns()
      times_brute_force.append(end_time - start_time)
      
      start_time = time.time_ns()
      check_anagram_greedy(str1, str2)
      end_time = time.time_ns()
      times_greedy.append(end_time - start_time)
      
      start_time = time.time_ns()
      check_anagram_dynamic(str1, str2)
      end_time = time.time_ns()
      times_dynamic.append(end_time - start_time)
      
      start_time = time.time_ns()
      check_anagram_min_max(str1, str2, min)
      end_time = time.time_ns()
      times_min.append(end_time - start_time)
      
      start_time = time.time_ns()
      check_anagram_min_max(str1, str2, max)
      end_time = time.time_ns()
      times_max.append(end_time - start_time)
    
    # st.write("Minimum Execution Time (Brute Force):", np.min(times_brute_force), "nanoseconds")
    st.write("Maximum Execution Time (Brute Force):", np.max(times_brute_force), "nanoseconds")
    
    # st.write("Minimum Execution Time (Greedy):", np.min(times_greedy), "nanoseconds")
    st.write("Maximum Execution Time (Greedy):", np.max(times_greedy), "nanoseconds")
    
    # st.write("Minimum Execution Time (Dynamic Programming):", np.min(times_dynamic), "nanoseconds")
    st.write("Maximum Execution Time (Dynamic Programming):", np.max(times_dynamic), "nanoseconds")

    # st.write("Minimum Execution Time (Min Method [Proposed]):", np.min(times_min), "nanoseconds")
    st.write("Maximum Execution Time (Min Method [Proposed]):", np.max(times_min), "nanoseconds")
    
    # st.write("Minimum Execution Time (Max Method [Proposed]):", np.min(times_max), "nanoseconds")
    st.write("Maximum Execution Time (Max Method [Proposed]):", np.max(times_max), "nanoseconds")
    
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, num_simulations+1), times_brute_force, label="Brute Force")
    plt.plot(range(1, num_simulations+1), times_greedy, label="Greedy")
    plt.plot(range(1, num_simulations+1), times_dynamic, label="Dynamic Programming")
    plt.plot(range(1, num_simulations+1), times_min, label="Min Method [Proposed]")
    plt.plot(range(1, num_simulations+1), times_max, label="Max Method [Proposed]")
    plt.xlabel("Simulation")
    plt.ylabel("Execution Time (nanoseconds)")
    plt.title("Execution Time Comparison")
    plt.legend()
    st.pyplot(plt)
  else:
    st.write("Click the 'Run Simulation' button to start the simulation.")
    st.write("Maximum Execution Time (Brute Force): xxx nanoseconds")
    st.write("Maximum Execution Time (Greedy): xxx nanoseconds")
    st.write("Maximum Execution Time (Dynamic Programming): xxx nanoseconds")
    st.write("Maximum Execution Time (Min Method [Proposed]): xxx nanoseconds")
    st.write("Maximum Execution Time (Max Method [Proposed]): xxx nanoseconds")
    
    plt.figure(figsize=(10, 6))
    plt.plot(0,0, label="Brute Force")
    plt.plot(0,0, label="Greedy")
    plt.plot(0,0, label="Dynamic Programming")
    plt.plot(0,0, label="Min Method [Proposed]")
    plt.plot(0,0, label="Max Method [Proposed]")
    plt.xlabel("Simulation")
    plt.ylabel("Execution Time (nanoseconds)")
    plt.title("Execution Time Comparison")
    plt.legend()
    st.pyplot(plt)

if __name__ == "__main__":
  main()

