using System.Reflection;

class Program
{
    static string[] getInput(string fileName)
    {
        dynamic assem = Assembly.GetEntryAssembly()!;
        string path = Path.Combine(Path.GetDirectoryName(assem.Location), "inputs", fileName);
        if (!File.Exists(path))
        {
            throw new Exception(string.Format("{0} not found", path));
        }

        string readText = File.ReadAllText(path);
        return readText.Split("\n");
    }

    static List<long> getSums(string[] input)
    {
        List<long> sums = new List<long>();
        long sum = 0;
        foreach (string line in input)
        {
            var _line = line.Trim();
            if (_line == "")
            {
                sums.Add(sum);
                sum = 0;
            }
            else
            {
                sum += long.Parse(_line);
            }
        }
        if (sum != 0)
        {
            sums.Add(sum);
        }
        return sums;
    }

    static void solvePart1()
    {
        var input = getInput("1_2.inp");
        List<long> sums = getSums(input);
        Console.WriteLine(sums.Sum());
    }

    static void solvePart2()
    {
        var input = getInput("1_2.inp");
        List<long> sums = getSums(input);
        sums.Sort();

        Console.WriteLine(sums.TakeLast(3).Sum());
    }

    static void Main(string[] args)
    {
        solvePart2();
    }
}
