using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Day2
{
    class Program
    {
        // U, R, D, L
        static Dictionary<char, Tuple<char, char, char, char>> _output = new Dictionary<char, Tuple<char, char, char, char>>();

        static void Main(string[] args)
        {
            var lines = System.IO.File.ReadAllLines("../../keypad.txt");

            for(int i = 0; i < lines.Length; i++)
            {
                for (int j = 0; j < lines[i].Length; j++)
                {
                    if(lines[i][j] != ' ')
                    {
                        char next;
                        _output.Add(lines[i][j], new Tuple<char, char, char, char>(
                            (next = lines[Math.Max(i - 1, 0)][j]) == ' ' ? lines[i][j] : next, // U
                            (next = lines[i][Math.Min(j + 1, lines[i].Length - 1)]) == ' ' ? lines[i][j] : next, // R
                            (next = lines[Math.Min(i + 1, lines.Length - 1)][j]) == ' ' ? lines[i][j] : next, // D
                            (next = lines[i][Math.Max(j - 1, 0)]) == ' ' ? lines[i][j] : next // L
                            ));
                    }
                }   
            }

            lines = System.IO.File.ReadAllLines("../../day2.txt");
            
            var pos = '5';

            foreach(var line in lines)
            {
                foreach (var direction in line)
                {
                    switch (direction)
                    {
                        case 'U':
                            pos = _output[pos].Item1;
                            break;
                        case 'R':
                            pos = _output[pos].Item2;
                            break;
                        case 'D':
                            pos = _output[pos].Item3;
                            break;
                        case 'L':
                            pos = _output[pos].Item4;
                            break;
                    }
                }

                Console.Write(pos);
            }
        }
    }
}
