namespace Result;

public class Solution {
    public int[] FrequencySort(int[] nums) {

        Dictionary<int, int> numberDict = new Dictionary<int, int>();
        int[] result = new int[nums.Length];
        int index = 0;

        foreach(var number in nums)
        {
            if(numberDict.ContainsKey(number))
            {
                numberDict[number] += 1;
            }
            else
            {
                numberDict.Add(number, 1);
            }
        }

        foreach (var item in numberDict.OrderByDescending(x=> x.Key).OrderBy(x => x.Value).ToList())
        {

            for(var i =0; i< item.Value; i++)
            {
                result[index] = item.Key;
                index++;
            }
        }
        return result;
    }
}