
internal class Program
{
    private static void Main(string[] args)
    {
        string[] names = ["Alice", "Bob", "Bob"];
        int[] heights = [155, 185, 150];

        Result.Solution result = new Result.Solution();

        foreach (var item in result.SortPeople(names, heights))
        {
            System.Console.WriteLine(item);
        }
    }
}



