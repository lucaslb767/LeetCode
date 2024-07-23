namespace Result;

public class Solution {
    public string[] SortPeople(string[] names, int[] heights) {
        
        Dictionary<int, string> solutionDictionary = new Dictionary<int, string>();

        for(int i = 0; i <= names.Length - 1; i ++)
        {
            solutionDictionary.Add(heights[i], names[i]);
        }

        string[] result = new string[names.Length];
        var ordered = solutionDictionary.OrderByDescending( x => x.Key).ToList();

        int index = 0;
        foreach(var item in ordered)
        {
            result[index] = item.Value;
            index++;
        }
        return result;
    }
    
}