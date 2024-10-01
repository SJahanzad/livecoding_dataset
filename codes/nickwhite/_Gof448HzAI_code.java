class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> output_arr = new ArrayList<>();
        for (int i=1; fizz=0, buzz=0; i<=n; i++) {
            fizz++;
            buzz++;
            if (fizz == 3 && buzz == 5) {
                output_arr.add("FizzBuzz");
                fizz = 0;
                buzz = 0;
            } else if (fizz == 3) {
                output_arr.add("Fizz");
                fizz = 0;
            } else if (buzz == 5) {
                output_arr.add("Buzz");
                buzz = 0;
            } else {
                output_arr.add(Integer.toString(i));
            }
        }
        return output_arr;
    }
}
