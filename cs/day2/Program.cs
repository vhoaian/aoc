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

    static long calPoint_v1(char op, char you)
    {
        long p = 0;
        switch (you)
        {
            case 'X':
                p += 1;
                if (op == 'A')
                {
                    p += 3;
                }
                else if (op == 'C')
                {
                    p += 6;
                }
                break;
            case 'Y':
                p += 2;
                if (op == 'A')

                {
                    p += 6;
                }
                else if (op == 'B')
                {
                    p += 3;
                }
                break;
            case 'Z':
                p += 3;
                if (op == 'B')
                {
                    p += 6;
                }
                else if (op == 'C')
                {
                    p += 3;
                }
                break;
        }
        return p;
    }

    static long calPoint_v2(char op, char you)
    {
        long p = 0;
        switch (you)
        {
            case 'X':
                if (op == 'A')
                {
                    p += 3;
                }
                else if (op == 'B')
                {
                    p += 1;
                }
                else
                {
                    p += 2;
                }
                break;
            case 'Y':
                p += 3;
                if (op == 'A')
                {
                    p += 1;
                }
                else if (op == 'B')
                {
                    p += 2;
                }
                else
                {
                    p += 3;
                }
                break;
            case 'Z':
                p += 6;
                if (op == 'A')
                {
                    p += 2;
                }
                else if (op == 'B')
                {
                    p += 3;
                }
                else
                {
                    p += 1;
                }
                break;
        }
        return p;
    }

    static long calPoints_v1(string[] input)
    {
        long sum = 0;
        foreach (string line in input)
        {
            var _line = line.Trim();
            var splitted = _line.Split(" ");
            var a = splitted[0];
            var b = splitted[1];
            var point = calPoint_v1(a[0], b[0]);
            sum += point;
        }

        return sum;
    }

    static long calPoints_v2(string[] input)
    {
        long sum = 0;
        foreach (string line in input)
        {
            var _line = line.Trim();
            var splitted = _line.Split(" ");
            var a = splitted[0];
            var b = splitted[1];
            var point = calPoint_v2(a[0], b[0]);
            sum += point;
        }

        return sum;
    }

    static void solvePart1()
    {
        var input = getInput("1_2.inp");
        var sum = calPoints_v1(input);
        Console.WriteLine(sum);
    }

    static void solvePart2()
    {
        var input = getInput("1_2.inp");
        var sum = calPoints_v2(input);
        Console.WriteLine(sum);
    }

    static void Main(string[] args)
    {
        solvePart2();
    }
}
