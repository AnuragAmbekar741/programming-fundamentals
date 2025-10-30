# Group Anagrams

## Problem Statement

Given an array of strings `strs`, group the **anagrams** together. You can return the answer in **any order**.

An **anagram** is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Constraints:

- `1 ≤ strs.length ≤ 10^4`
- `0 ≤ strs[i].length ≤ 100`
- `strs[i]` consists of lowercase English letters only

### Input:

- `strs`: An array of strings (list of words)

### Output:

- Return a list of lists, where each inner list contains strings that are anagrams of each other

---

## Examples

### Example 1:

**Input:**

### strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

### [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
