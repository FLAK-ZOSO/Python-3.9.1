using System;

namespace EsQuickSort
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] num = { 1, 5, 8, 12 };
            int[] min = new int[num.Length];
            int[] max = new int[num.Length];
            int i = 0;
            x(num, min, max, i);
        }

        static int x(int[] arr, int[] min, int[] max, int i)
        {
            if (arr == null || arr.Length==1)
            {
                return 0;
            }
            else
            {
                int p = arr[0];
                if (p >= arr[i]){
                    max[i] = arr[i];
                    i++;
                }
                else {
                    min[i] = arr[i];
                    i++;
                }
                return 1;
            }
        }
    }
}